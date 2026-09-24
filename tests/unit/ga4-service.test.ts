import { describe, it, expect, vi } from 'vitest';
import { GA4Service, GA4RunReportResponse } from '../../src/services/ga4-service';
import { GoogleAuthService } from '../../src/services/google-auth';

describe('GA4Service', () => {
  function createMockAuthService(): GoogleAuthService {
    const auth = new GoogleAuthService();
    vi.spyOn(auth, 'getAccessToken').mockResolvedValue('mock-ga4-token');
    return auth;
  }

  it('aggregates phone conversions and calculates gross profit by traffic channel', async () => {
    // 1st call: total sessions by channel
    const mockSessionsResponse: GA4RunReportResponse = {
      rows: [
        {
          dimensionValues: [{ value: 'Paid Search' }],
          metricValues: [{ value: '400' }],
        },
        {
          dimensionValues: [{ value: 'Organic Search' }],
          metricValues: [{ value: '300' }],
        },
      ],
    };

    // 2nd call: phone_call_click events by channel
    const mockCallsResponse: GA4RunReportResponse = {
      rows: [
        {
          dimensionValues: [{ value: 'Paid Search' }],
          metricValues: [{ value: '48' }],
        },
        {
          dimensionValues: [{ value: 'Organic Search' }],
          metricValues: [{ value: '42' }],
        },
      ],
    };

    let callCount = 0;
    const mockFetch = async () => {
      callCount++;
      const body = callCount === 1 ? mockSessionsResponse : mockCallsResponse;
      return {
        ok: true,
        json: async () => body,
        text: async () => '',
      } as unknown as typeof fetch;
    };

    const auth = createMockAuthService();
    const service = new GA4Service(auth, '123456789', mockFetch as unknown as typeof fetch);

    const summary = await service.getPhoneConversionSummary(30);

    expect(summary.totalSessions).toBe(700);
    expect(summary.totalPhoneCalls).toBe(90);
    expect(summary.overallConversionRate).toBe(12.86);
    expect(summary.estimatedTotalProfitPln).toBe(90 * 180); // 16,200 PLN

    expect(summary.channels.length).toBe(2);
    const paid = summary.channels.find((c) => c.channel === 'Paid Search');
    expect(paid).toBeDefined();
    expect(paid?.phoneCalls).toBe(48);
    expect(paid?.conversionRate).toBe(12);
  });

  it('evaluates 24h day vs night emergency call distribution and surcharge potential', async () => {
    // Mock 24 hours of call data
    const rows = [
      { dimensionValues: [{ value: '02' }], metricValues: [{ value: '5' }] }, // Night
      { dimensionValues: [{ value: '03' }], metricValues: [{ value: '3' }] }, // Night
      { dimensionValues: [{ value: '14' }], metricValues: [{ value: '12' }] }, // Day
      { dimensionValues: [{ value: '23' }], metricValues: [{ value: '7' }] }, // Night
    ];

    const mockFetch = async () => ({
      ok: true,
      json: async () => ({ rows }),
      text: async () => '',
    }) as unknown as typeof fetch;

    const auth = createMockAuthService();
    const service = new GA4Service(auth, '123456789', mockFetch);

    const report = await service.getHourlyCallDistribution(30);

    expect(report.nighttimeCalls).toBe(15); // 5 + 3 + 7
    expect(report.daytimeCalls).toBe(12);   // 12
    expect(report.potentialNightSurchargeGainPln).toBe(15 * 80); // 1200 PLN
    expect(report.hourlyBreakdown.length).toBe(24);
  });

  it('maps district landings and measures phone call conversion rates', async () => {
    const rows = [
      // Mokotów
      { dimensionValues: [{ value: '/warszawa-mokotow' }, { value: 'page_view' }], metricValues: [{ value: '200' }] },
      { dimensionValues: [{ value: '/warszawa-mokotow' }, { value: 'phone_call_click' }], metricValues: [{ value: '25' }] },
      // Ursynów
      { dimensionValues: [{ value: '/ursynow' }, { value: 'page_view' }], metricValues: [{ value: '150' }] },
      { dimensionValues: [{ value: '/ursynow' }, { value: 'phone_call_click' }], metricValues: [{ value: '18' }] },
    ];

    const mockFetch = async () => ({
      ok: true,
      json: async () => ({ rows }),
      text: async () => '',
    }) as unknown as typeof fetch;

    const auth = createMockAuthService();
    const service = new GA4Service(auth, '123456789', mockFetch);

    const districts = await service.getDistrictConversions(30);

    const mokotow = districts.find((d) => d.slug === 'mokotow');
    expect(mokotow).toBeDefined();
    expect(mokotow?.sessions).toBe(200);
    expect(mokotow?.phoneCalls).toBe(25);
    expect(mokotow?.conversionRate).toBe(12.5);
  });
});
