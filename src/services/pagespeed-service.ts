/**
 * Akumulateo – Google PageSpeed Insights (PSI) Service
 * Audits mobile & desktop performance and Core Web Vitals.
 * Evaluates impact on Google Ads Quality Score and emergency driver call conversion.
 */

export type PageSpeedStrategy = 'mobile' | 'desktop';

export interface CoreWebVitalsMetrics {
  largestContentfulPaintMs: number; // LCP (Key CWV)
  firstContentfulPaintMs: number;   // FCP
  cumulativeLayoutShift: number;    // CLS
  totalBlockingTimeMs: number;      // TBT
  speedIndexMs: number;             // Speed Index
}

export interface AuditOpportunity {
  id: string;
  title: string;
  displayValue?: string;
  description?: string;
  wastedMs?: number;
  wastedBytes?: number;
}

export type ReadinessStatus = 'EXCELLENT' | 'ACCEPTABLE' | 'CRITICAL_RISK';

export interface EmergencyCallReadiness {
  status: ReadinessStatus;
  headlinePl: string;
  driverImpactPl: string;
  googleAdsImpactPl: string;
  recommendedActionPl: string;
}

export interface PageSpeedAuditResult {
  url: string;
  strategy: PageSpeedStrategy;
  performanceScore: number; // 0 - 100
  seoScore?: number;        // 0 - 100
  metrics: CoreWebVitalsMetrics;
  emergencyReadiness: EmergencyCallReadiness;
  opportunities: AuditOpportunity[];
  timestamp: string;
}

export interface LighthouseAuditRaw {
  numericValue?: number;
  score?: number | null;
  title?: string;
  displayValue?: string;
  description?: string;
  details?: {
    overallSavingsMs?: number;
    overallSavingsBytes?: number;
  };
}

export interface LighthouseResponseRaw {
  lighthouseResult?: {
    categories?: {
      performance?: { score?: number | null };
      seo?: { score?: number | null };
    };
    audits?: Record<string, LighthouseAuditRaw | undefined>;
  };
}

export interface PageSpeedServiceOptions {
  apiKey?: string;
  defaultUrl?: string;
  fetchImpl?: typeof fetch;
}

export class PageSpeedService {
  private apiKey?: string;
  private defaultUrl: string;
  private fetchImpl: typeof fetch;

  constructor(options?: PageSpeedServiceOptions) {
    this.apiKey = options?.apiKey || process.env.GOOGLE_PAGESPEED_API_KEY;
    this.defaultUrl = options?.defaultUrl || process.env.PAGESPEED_TARGET_URL || 'https://www.akumulateo.pl/';
    this.fetchImpl = options?.fetchImpl || fetch;
  }

  /**
   * Evaluates page speed from the perspective of an emergency battery replacement customer.
   * A stranded driver on the road has low patience and high urgency (85%+ mobile).
   */
  public static evaluateEmergencyReadiness(
    score: number,
    lcpMs: number,
    tbtMs: number
  ): EmergencyCallReadiness {
    if (lcpMs <= 2500 && score >= 80) {
      return {
        status: 'EXCELLENT',
        headlinePl: 'Błyskawiczna gotowość alarmowa (Wzorowa)',
        driverImpactPl: 'Kierowca widzi numer telefonu 696 556 446 w mniej niż 2.5s. Minimalne ryzyko odrzucenia.',
        googleAdsImpactPl: 'Wysoki Wynik Jakości (Quality Score). Najniższy możliwy koszt kliknięcia (CPC) w Google Ads.',
        recommendedActionPl: 'Utrzymywać lekki kod widgetów i unikać ciężkich bibliotek zewnętrznych w Squarespace.',
      };
    }

    if (lcpMs <= 4000 && score >= 50) {
      return {
        status: 'ACCEPTABLE',
        headlinePl: 'Wydajność akceptowalna, lecz wymaga poprawy',
        driverImpactPl: 'Kierowca czeka 2.5–4.0s na załadowanie paska kontaktowego. Część niecierpliwych użytkowników może wrócić do Google.',
        googleAdsImpactPl: 'Średni Wynik Jakości. Możliwe nieznaczne zawyżenie stawek CPC za kliknięcia reklamowe.',
        recommendedActionPl: 'Zoptymalizować wagę zdjęć tła w Squarespace i opóźnić ładowanie skryptów analitycznych poza priorytetem LCP.',
      };
    }

    return {
      status: 'CRITICAL_RISK',
      headlinePl: 'Krytyczne ryzyko utraty zapytań telefonicznych',
      driverImpactPl: 'Strona ładuje się zbyt wolno (>4.0s). Kierowca w stresie prawdopodobnie zamknie kartę i zadzwoni do konkurenta z Map Google.',
      googleAdsImpactPl: 'Niski Wynik Jakości (Landing Page Experience). Google Ads zawyża koszt kliknięcia i ogranicza wyświetlanie reklam.',
      recommendedActionPl: 'Pilnie odchudzić stronę: usunąć nieużywany kod CSS/JS w Squarespace Code Injection i włączyć priorytet ładowania dla paska połączenia.',
    };
  }

  /**
   * Executes a PageSpeed Insights audit for the specified URL and strategy.
   */
  public async audit(
    url: string = this.defaultUrl,
    strategy: PageSpeedStrategy = 'mobile'
  ): Promise<PageSpeedAuditResult> {
    const endpoint = new URL('https://www.googleapis.com/pagespeedonline/v5/runPagespeed');
    endpoint.searchParams.set('url', url);
    endpoint.searchParams.set('strategy', strategy);
    endpoint.searchParams.append('category', 'performance');
    endpoint.searchParams.append('category', 'seo');

    if (this.apiKey) {
      endpoint.searchParams.set('key', this.apiKey);
    }

    const response = await this.fetchImpl(endpoint.toString(), {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      },
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(`PageSpeed API failed [${response.status}]: ${errorText}`);
    }

    const data = (await response.json()) as LighthouseResponseRaw;
    return this.parseAuditResponse(url, strategy, data);
  }

  /**
   * Parses raw Lighthouse response into structured business metrics.
   */
  public parseAuditResponse(
    url: string,
    strategy: PageSpeedStrategy,
    data: LighthouseResponseRaw
  ): PageSpeedAuditResult {
    const lighthouse = data.lighthouseResult || {};
    const categories = lighthouse.categories || {};
    const audits = lighthouse.audits || {};

    const perfScoreRaw = categories.performance?.score;
    const performanceScore = typeof perfScoreRaw === 'number' ? Math.round(perfScoreRaw * 100) : 0;

    const seoScoreRaw = categories.seo?.score;
    const seoScore = typeof seoScoreRaw === 'number' ? Math.round(seoScoreRaw * 100) : undefined;

    const lcpMs = Math.round(audits['largest-contentful-paint']?.numericValue || 0);
    const fcpMs = Math.round(audits['first-contentful-paint']?.numericValue || 0);
    const cls = Number((audits['cumulative-layout-shift']?.numericValue || 0).toFixed(3));
    const tbtMs = Math.round(audits['total-blocking-time']?.numericValue || 0);
    const speedIndexMs = Math.round(audits['speed-index']?.numericValue || 0);

    const metrics: CoreWebVitalsMetrics = {
      largestContentfulPaintMs: lcpMs,
      firstContentfulPaintMs: fcpMs,
      cumulativeLayoutShift: cls,
      totalBlockingTimeMs: tbtMs,
      speedIndexMs,
    };

    const emergencyReadiness = PageSpeedService.evaluateEmergencyReadiness(
      performanceScore,
      lcpMs,
      tbtMs
    );

    const opportunities: AuditOpportunity[] = [];
    const candidateAuditKeys = [
      'render-blocking-resources',
      'unused-javascript',
      'unused-css-rules',
      'modern-image-formats',
      'uses-optimized-images',
      'unminified-javascript',
      'unminified-css',
    ];

    for (const key of candidateAuditKeys) {
      const audit = audits[key];
      if (audit && (audit.score === null || (audit.score !== undefined && audit.score < 0.9))) {
        const wastedMs = audit.details?.overallSavingsMs;
        const wastedBytes = audit.details?.overallSavingsBytes;
        if (wastedMs || wastedBytes || audit.displayValue) {
          opportunities.push({
            id: key,
            title: audit.title || key,
            displayValue: audit.displayValue,
            description: audit.description,
            wastedMs: wastedMs ? Math.round(wastedMs) : undefined,
            wastedBytes: wastedBytes ? Math.round(wastedBytes) : undefined,
          });
        }
      }
    }

    return {
      url,
      strategy,
      performanceScore,
      seoScore,
      metrics,
      emergencyReadiness,
      opportunities,
      timestamp: new Date().toISOString(),
    };
  }
}
