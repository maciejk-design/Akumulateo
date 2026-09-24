/**
 * Akumulateo – Google Search Console (GSC) Service
 * Tracks organic search queries, rankings, and clicks for Warsaw districts.
 * Detects stationary store queries to prevent misaligned traffic and brand dilution.
 */

import { GoogleAuthService, GOOGLE_AUTH_SCOPES } from './google-auth';

export type GSCDimension = 'query' | 'page' | 'device' | 'country' | 'date';

export interface GSCFilter {
  dimension: GSCDimension;
  operator: 'contains' | 'equals' | 'notContains' | 'notEquals';
  expression: string;
}

export interface GSCFilterGroup {
  filters: GSCFilter[];
}

export interface GSCQueryOptions {
  startDate: string; // YYYY-MM-DD
  endDate: string;   // YYYY-MM-DD
  dimensions?: GSCDimension[];
  rowLimit?: number;
  startRow?: number;
  dimensionFilterGroups?: GSCFilterGroup[];
}

export interface GSCRowData {
  keys: string[];
  clicks: number;
  impressions: number;
  ctr: number;
  position: number;
}

export interface GSCApiResponse {
  rows?: GSCRowData[];
  responseAggregationType?: string;
}

export interface DistrictPerformanceResult {
  districtName: string;
  slug: string;
  clicks: number;
  impressions: number;
  ctr: number;
  averagePosition: number;
  topQueries: Array<{
    query: string;
    clicks: number;
    impressions: number;
    position: number;
  }>;
}

export type NegativeCategory = 'STATIONARY_SHOP' | 'FREE_ASSISTANCE' | 'WORKSHOP_TIRES' | 'OTHER';

export interface NegativeQueryAlert {
  query: string;
  clicks: number;
  impressions: number;
  category: NegativeCategory;
  explanationPl: string;
}

export interface NegativeKeywordDetectionResult {
  wasteRiskScore: 'LOW' | 'MEDIUM' | 'HIGH';
  totalWastedImpressions: number;
  totalWastedClicks: number;
  detectedQueries: NegativeQueryAlert[];
  actionAdvicePl: string;
}

export interface EmergencyQueriesResult {
  queries: Array<{
    query: string;
    clicks: number;
    impressions: number;
    ctr: number;
    position: number;
  }>;
  totalClicks: number;
  totalImpressions: number;
}

export class SearchConsoleService {
  private authService: GoogleAuthService;
  private siteUrl: string;
  private fetchImpl: typeof fetch;

  constructor(
    authService?: GoogleAuthService,
    siteUrl?: string,
    fetchImpl: typeof fetch = fetch
  ) {
    this.authService = authService || new GoogleAuthService();
    this.siteUrl =
      siteUrl ||
      process.env.GOOGLE_SEARCH_CONSOLE_SITE_URL ||
      'https://www.akumulateo.pl/';
    this.fetchImpl = fetchImpl;
  }

  /**
   * Helper generating a date string in YYYY-MM-DD format N days ago.
   */
  public static getDateDaysAgo(daysAgo: number): string {
    const d = new Date();
    d.setDate(d.getDate() - daysAgo);
    return d.toISOString().split('T')[0];
  }

  /**
   * Executes a searchAnalytics query against Google Search Console API v1.
   */
  public async querySearchAnalytics(options: GSCQueryOptions): Promise<GSCRowData[]> {
    const token = await this.authService.getAccessToken(
      [GOOGLE_AUTH_SCOPES.SEARCH_CONSOLE_READONLY],
      this.fetchImpl
    );

    const encodedSite = encodeURIComponent(this.siteUrl);
    const endpoint = `https://searchconsole.googleapis.com/v1/sites/${encodedSite}/searchAnalytics/query`;

    const requestBody = {
      startDate: options.startDate,
      endDate: options.endDate,
      dimensions: options.dimensions || ['query'],
      rowLimit: options.rowLimit ?? 100,
      startRow: options.startRow ?? 0,
      dimensionFilterGroups: options.dimensionFilterGroups,
    };

    const response = await this.fetchImpl(endpoint, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestBody),
    });

    if (!response.ok) {
      const errText = await response.text();
      throw new Error(`Search Console API failed [${response.status}]: ${errText}`);
    }

    const data = (await response.json()) as GSCApiResponse;
    return data.rows || [];
  }

  /**
   * Evaluates organic performance for a specific Warsaw district landing page.
   */
  public async getDistrictPerformance(
    districtSlug: string,
    districtName: string,
    daysAgo: number = 28
  ): Promise<DistrictPerformanceResult> {
    const startDate = SearchConsoleService.getDateDaysAgo(daysAgo);
    const endDate = SearchConsoleService.getDateDaysAgo(1);

    const rows = await this.querySearchAnalytics({
      startDate,
      endDate,
      dimensions: ['query', 'page'],
      dimensionFilterGroups: [
        {
          filters: [
            {
              dimension: 'page',
              operator: 'contains',
              expression: districtSlug,
            },
          ],
        },
      ],
      rowLimit: 200,
    });

    let totalClicks = 0;
    let totalImpressions = 0;
    let weightedPositionSum = 0;

    const topQueries: DistrictPerformanceResult['topQueries'] = [];

    for (const r of rows) {
      totalClicks += r.clicks;
      totalImpressions += r.impressions;
      weightedPositionSum += r.position * r.impressions;

      const queryName = r.keys[0] || '';
      topQueries.push({
        query: queryName,
        clicks: r.clicks,
        impressions: r.impressions,
        position: Number(r.position.toFixed(1)),
      });
    }

    topQueries.sort((a, b) => b.clicks - a.clicks || b.impressions - a.impressions);

    const avgCtr = totalImpressions > 0 ? Number(((totalClicks / totalImpressions) * 100).toFixed(2)) : 0;
    const avgPos = totalImpressions > 0 ? Number((weightedPositionSum / totalImpressions).toFixed(1)) : 0;

    return {
      districtName,
      slug: districtSlug,
      clicks: totalClicks,
      impressions: totalImpressions,
      ctr: avgCtr,
      averagePosition: avgPos,
      topQueries: topQueries.slice(0, 10),
    };
  }

  /**
   * Scans organic queries to detect dangerous mismatches:
   * e.g. searches for stationary shops, free insurance assistance, or mechanics.
   * Akumulateo ONLY operates as a 24h mobile emergency battery service.
   */
  public async detectNegativeKeywords(daysAgo: number = 28): Promise<NegativeKeywordDetectionResult> {
    const startDate = SearchConsoleService.getDateDaysAgo(daysAgo);
    const endDate = SearchConsoleService.getDateDaysAgo(1);

    const rows = await this.querySearchAnalytics({
      startDate,
      endDate,
      dimensions: ['query'],
      rowLimit: 500,
    });

    const detected: NegativeQueryAlert[] = [];
    let wastedImpressions = 0;
    let wastedClicks = 0;

    const stationaryPatterns = ['sklep', 'sklepy', 'stacjonarny', 'odbiór osobisty', 'hurtownia'];
    const assistancePatterns = ['darmowe', 'ubezpieczenie', 'pzu', 'warta', 'allianz', 'assistance za darmo'];
    const workshopPatterns = ['warsztat', 'mechanik', 'wulkanizacja', 'opony', 'wymiana opon', 'klimatyzacja'];

    for (const r of rows) {
      const q = (r.keys[0] || '').toLowerCase();
      let matchedCategory: NegativeCategory | null = null;
      let explanation = '';

      if (stationaryPatterns.some((pattern) => q.includes(pattern))) {
        matchedCategory = 'STATIONARY_SHOP';
        explanation = 'Zapytanie o sklep stacjonarny lub odbiór osobisty (Akumulateo działa wyłącznie mobilnie z dojazdem!).';
      } else if (assistancePatterns.some((pattern) => q.includes(pattern))) {
        matchedCategory = 'FREE_ASSISTANCE';
        explanation = 'Kierowca oczekuje darmowej pomocy z polisy ubezpieczeniowej (spala czas dyspozytora).';
      } else if (workshopPatterns.some((pattern) => q.includes(pattern))) {
        matchedCategory = 'WORKSHOP_TIRES';
        explanation = 'Zapytanie o warsztat lub serwis opon (poza profilem działalności pogotowia akumulatorowego).';
      }

      if (matchedCategory) {
        detected.push({
          query: r.keys[0] || '',
          clicks: r.clicks,
          impressions: r.impressions,
          category: matchedCategory,
          explanationPl: explanation,
        });
        wastedImpressions += r.impressions;
        wastedClicks += r.clicks;
      }
    }

    detected.sort((a, b) => b.clicks - a.clicks || b.impressions - a.impressions);

    let wasteRiskScore: 'LOW' | 'MEDIUM' | 'HIGH' = 'LOW';
    if (wastedClicks > 20 || wastedImpressions > 300) {
      wasteRiskScore = 'HIGH';
    } else if (wastedClicks > 5 || wastedImpressions > 50) {
      wasteRiskScore = 'MEDIUM';
    }

    const actionAdvicePl =
      wasteRiskScore === 'HIGH'
        ? 'Pilnie wzmocnij komunikat „Wyłącznie mobilnie 24h z dojazdem – brak sklepu stacjonarnego” na stronie głównej oraz dodaj wykluczenia w kampaniach Google Ads!'
        : wasteRiskScore === 'MEDIUM'
        ? 'Upewnij się, że w nagłówkach i meta tagach wyraźnie akcentowana jest usługa z dojazdem.'
        : 'Ruch organiczny jest czysty i dobrze dopasowany do profilu mobilnego pogotowia.';

    return {
      wasteRiskScore,
      totalWastedImpressions: wastedImpressions,
      totalWastedClicks: wastedClicks,
      detectedQueries: detected,
      actionAdvicePl,
    };
  }

  /**
   * Fetches top emergency battery-related keywords with strong purchase intent.
   */
  public async getTopEmergencyQueries(
    daysAgo: number = 28,
    limit: number = 15
  ): Promise<EmergencyQueriesResult> {
    const startDate = SearchConsoleService.getDateDaysAgo(daysAgo);
    const endDate = SearchConsoleService.getDateDaysAgo(1);

    const rows = await this.querySearchAnalytics({
      startDate,
      endDate,
      dimensions: ['query'],
      rowLimit: 250,
    });

    const emergencyKeywords = [
      'akumulator',
      'wymiana akumulatora',
      'pogotowie akumulatorowe',
      'odpalanie',
      'kable',
      'dojazd',
      '24h',
      'rozładowany',
      'warszawa',
    ];

    const filtered = rows.filter((r) => {
      const q = (r.keys[0] || '').toLowerCase();
      return emergencyKeywords.some((kw) => q.includes(kw));
    });

    filtered.sort((a, b) => b.clicks - a.clicks || b.impressions - a.impressions);

    let totalClicks = 0;
    let totalImpressions = 0;
    const queries = filtered.slice(0, limit).map((r) => {
      totalClicks += r.clicks;
      totalImpressions += r.impressions;
      return {
        query: r.keys[0] || '',
        clicks: r.clicks,
        impressions: r.impressions,
        ctr: Number((r.ctr * 100).toFixed(2)),
        position: Number(r.position.toFixed(1)),
      };
    });

    return {
      queries,
      totalClicks,
      totalImpressions,
    };
  }
}
