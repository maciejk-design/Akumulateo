/**
 * Akumulateo – Google Analytics 4 (GA4) Service
 * Tracks phone call conversion events (phone_call_click), traffic acquisition channels,
 * district performance, and 24h night emergency call volume.
 */

import { GoogleAuthService, GOOGLE_AUTH_SCOPES } from './google-auth';
import { WARSAW_DISTRICTS } from '../seo/districts-data';

export interface GA4DateRange {
  startDate: string; // YYYY-MM-DD or '30daysAgo'
  endDate: string;   // YYYY-MM-DD or 'today'
}

export interface GA4Dimension {
  name: string;
}

export interface GA4Metric {
  name: string;
}

export interface GA4StringFilter {
  matchType?: 'EXACT' | 'BEGINS_WITH' | 'ENDS_WITH' | 'CONTAINS' | 'FULL_REGEXP';
  value: string;
  caseSensitive?: boolean;
}

export interface GA4Filter {
  fieldName: string;
  stringFilter?: GA4StringFilter;
}

export interface GA4FilterExpression {
  filter?: GA4Filter;
  andGroup?: { expressions: GA4FilterExpression[] };
  orGroup?: { expressions: GA4FilterExpression[] };
  notExpression?: GA4FilterExpression;
}

export interface GA4RunReportRequest {
  dateRanges: GA4DateRange[];
  dimensions?: GA4Dimension[];
  metrics: GA4Metric[];
  dimensionFilter?: GA4FilterExpression;
  metricFilter?: GA4FilterExpression;
  limit?: number;
}

export interface GA4DimensionValue {
  value?: string;
}

export interface GA4MetricValue {
  value?: string;
}

export interface GA4Row {
  dimensionValues?: GA4DimensionValue[];
  metricValues?: GA4MetricValue[];
}

export interface GA4RunReportResponse {
  rows?: GA4Row[];
  rowCount?: number;
}

export interface ChannelPerformance {
  channel: string;
  sessions: number;
  phoneCalls: number;
  conversionRate: number; // in percent (e.g. 12.5%)
  estimatedGrossProfitPln: number; // based on MIN_ACCEPTABLE_PROFIT_PLN (180 PLN)
}

export interface PhoneConversionSummary {
  periodDays: number;
  totalSessions: number;
  totalPhoneCalls: number;
  overallConversionRate: number;
  estimatedTotalProfitPln: number;
  channels: ChannelPerformance[];
}

export interface DistrictConversionMetric {
  districtName: string;
  slug: string;
  pagePath: string;
  sessions: number;
  phoneCalls: number;
  conversionRate: number;
}

export interface HourlyCallMetric {
  hour: number;
  phoneCalls: number;
  isNightSlot: boolean; // 22:00 to 06:00
}

export interface HourlyDistributionReport {
  daytimeCalls: number; // 06:00 - 21:59
  nighttimeCalls: number; // 22:00 - 05:59
  nightCallsSharePercent: number;
  potentialNightSurchargeGainPln: number; // night calls * 80 PLN
  hourlyBreakdown: HourlyCallMetric[];
}

export class GA4Service {
  private authService: GoogleAuthService;
  private propertyId: string;
  private fetchImpl: typeof fetch;

  constructor(
    authService?: GoogleAuthService,
    propertyId?: string,
    fetchImpl: typeof fetch = fetch
  ) {
    this.authService = authService || new GoogleAuthService();
    this.propertyId = propertyId || process.env.GA4_PROPERTY_ID || '';
    this.fetchImpl = fetchImpl;
  }

  /**
   * Runs an arbitrary report against GA4 Data API v1beta.
   */
  public async runReport(request: GA4RunReportRequest): Promise<GA4RunReportResponse> {
    if (!this.propertyId) {
      throw new Error(
        'GA4_PROPERTY_ID is not configured. Set GA4_PROPERTY_ID in .env or pass it to constructor.'
      );
    }

    const token = await this.authService.getAccessToken(
      [GOOGLE_AUTH_SCOPES.ANALYTICS_READONLY],
      this.fetchImpl
    );

    const endpoint = `https://analyticsdata.googleapis.com/v1beta/properties/${this.propertyId}:runReport`;

    const response = await this.fetchImpl(endpoint, {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(request),
    });

    if (!response.ok) {
      const errText = await response.text();
      throw new Error(`GA4 runReport failed [${response.status}]: ${errText}`);
    }

    return (await response.json()) as GA4RunReportResponse;
  }

  /**
   * Evaluates overall phone call conversions (phone_call_click) broken down by traffic channel.
   * Direct answer to: "Is Google Ads driving calls or burning cash vs SEO?"
   */
  public async getPhoneConversionSummary(daysAgo: number = 30): Promise<PhoneConversionSummary> {
    const report = await this.runReport({
      dateRanges: [{ startDate: `${daysAgo}daysAgo`, endDate: 'today' }],
      dimensions: [{ name: 'sessionDefaultChannelGroup' }],
      metrics: [
        { name: 'sessions' },
        { name: 'eventCount' }, // We'll count specific events via dimensionFilter or total sessions
      ],
    });

    // Also fetch phone call clicks specifically
    const phoneCallsReport = await this.runReport({
      dateRanges: [{ startDate: `${daysAgo}daysAgo`, endDate: 'today' }],
      dimensions: [{ name: 'sessionDefaultChannelGroup' }],
      metrics: [{ name: 'eventCount' }],
      dimensionFilter: {
        filter: {
          fieldName: 'eventName',
          stringFilter: {
            matchType: 'EXACT',
            value: 'phone_call_click',
          },
        },
      },
    });

    const callsByChannel: Record<string, number> = {};
    for (const row of phoneCallsReport.rows || []) {
      const channel = row.dimensionValues?.[0]?.value || 'Unassigned';
      const count = parseInt(row.metricValues?.[0]?.value || '0', 10);
      callsByChannel[channel] = count;
    }

    let totalSessions = 0;
    let totalPhoneCalls = 0;
    const channels: ChannelPerformance[] = [];

    const minProfitPerJob = parseInt(process.env.MIN_ACCEPTABLE_PROFIT_PLN || '180', 10);

    for (const row of report.rows || []) {
      const channel = row.dimensionValues?.[0]?.value || 'Unassigned';
      const sessions = parseInt(row.metricValues?.[0]?.value || '0', 10);
      const phoneCalls = callsByChannel[channel] || 0;

      totalSessions += sessions;
      totalPhoneCalls += phoneCalls;

      const conversionRate = sessions > 0 ? Number(((phoneCalls / sessions) * 100).toFixed(2)) : 0;
      const estimatedGrossProfitPln = phoneCalls * minProfitPerJob;

      channels.push({
        channel,
        sessions,
        phoneCalls,
        conversionRate,
        estimatedGrossProfitPln,
      });
    }

    channels.sort((a, b) => b.phoneCalls - a.phoneCalls || b.sessions - a.sessions);

    const overallConversionRate =
      totalSessions > 0 ? Number(((totalPhoneCalls / totalSessions) * 100).toFixed(2)) : 0;

    return {
      periodDays: daysAgo,
      totalSessions,
      totalPhoneCalls,
      overallConversionRate,
      estimatedTotalProfitPln: totalPhoneCalls * minProfitPerJob,
      channels,
    };
  }

  /**
   * Maps landing page performance directly to Warsaw districts.
   * Pinpoints which district pages are successfully converting drivers into telephone calls.
   */
  public async getDistrictConversions(daysAgo: number = 30): Promise<DistrictConversionMetric[]> {
    const report = await this.runReport({
      dateRanges: [{ startDate: `${daysAgo}daysAgo`, endDate: 'today' }],
      dimensions: [{ name: 'pagePath' }, { name: 'eventName' }],
      metrics: [{ name: 'eventCount' }],
    });

    const sessionsByPath: Record<string, number> = {};
    const callsByPath: Record<string, number> = {};

    for (const row of report.rows || []) {
      const path = (row.dimensionValues?.[0]?.value || '').toLowerCase();
      const eventName = row.dimensionValues?.[1]?.value || '';
      const count = parseInt(row.metricValues?.[0]?.value || '0', 10);

      if (eventName === 'session_start' || eventName === 'page_view') {
        sessionsByPath[path] = (sessionsByPath[path] || 0) + count;
      } else if (eventName === 'phone_call_click') {
        callsByPath[path] = (callsByPath[path] || 0) + count;
      }
    }

    const results: DistrictConversionMetric[] = [];

    for (const district of WARSAW_DISTRICTS) {
      // Look for paths containing district slug
      let districtSessions = 0;
      let districtCalls = 0;
      let matchedPath = `/${district.slug}`;

      for (const [path, sess] of Object.entries(sessionsByPath)) {
        if (path.includes(district.slug)) {
          districtSessions += sess;
          matchedPath = path;
        }
      }

      for (const [path, calls] of Object.entries(callsByPath)) {
        if (path.includes(district.slug)) {
          districtCalls += calls;
        }
      }

      const cr =
        districtSessions > 0
          ? Number(((districtCalls / districtSessions) * 100).toFixed(2))
          : 0;

      results.push({
        districtName: district.name,
        slug: district.slug,
        pagePath: matchedPath,
        sessions: districtSessions,
        phoneCalls: districtCalls,
        conversionRate: cr,
      });
    }

    results.sort((a, b) => b.phoneCalls - a.phoneCalls || b.sessions - a.sessions);
    return results;
  }

  /**
   * Analyzes 24h distribution of phone clicks to evaluate night emergency demand (22:00 - 06:00).
   * Night jobs include an extra +80 PLN surcharge.
   */
  public async getHourlyCallDistribution(daysAgo: number = 30): Promise<HourlyDistributionReport> {
    const report = await this.runReport({
      dateRanges: [{ startDate: `${daysAgo}daysAgo`, endDate: 'today' }],
      dimensions: [{ name: 'hour' }],
      metrics: [{ name: 'eventCount' }],
      dimensionFilter: {
        filter: {
          fieldName: 'eventName',
          stringFilter: {
            matchType: 'EXACT',
            value: 'phone_call_click',
          },
        },
      },
    });

    const hourlyMap: Record<number, number> = {};
    for (let h = 0; h < 24; h++) {
      hourlyMap[h] = 0;
    }

    for (const row of report.rows || []) {
      const hourStr = row.dimensionValues?.[0]?.value || '0';
      const hour = parseInt(hourStr, 10);
      const count = parseInt(row.metricValues?.[0]?.value || '0', 10);
      hourlyMap[hour] = count;
    }

    let daytimeCalls = 0;
    let nighttimeCalls = 0;
    const hourlyBreakdown: HourlyCallMetric[] = [];

    const nightSurcharge = parseInt(process.env.NIGHT_SURCHARGE_PLN || '80', 10);

    for (let h = 0; h < 24; h++) {
      const calls = hourlyMap[h] || 0;
      const isNightSlot = h >= 22 || h < 6;

      if (isNightSlot) {
        nighttimeCalls += calls;
      } else {
        daytimeCalls += calls;
      }

      hourlyBreakdown.push({
        hour: h,
        phoneCalls: calls,
        isNightSlot,
      });
    }

    const totalCalls = daytimeCalls + nighttimeCalls;
    const nightCallsSharePercent =
      totalCalls > 0 ? Number(((nighttimeCalls / totalCalls) * 100).toFixed(1)) : 0;

    return {
      daytimeCalls,
      nighttimeCalls,
      nightCallsSharePercent,
      potentialNightSurchargeGainPln: nighttimeCalls * nightSurcharge,
      hourlyBreakdown,
    };
  }
}
