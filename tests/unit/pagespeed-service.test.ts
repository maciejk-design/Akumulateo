import { describe, it, expect } from 'vitest';
import {
  PageSpeedService,
  LighthouseResponseRaw,
} from '../../src/services/pagespeed-service';

describe('PageSpeedService', () => {
  const mockLighthouseData: LighthouseResponseRaw = {
    lighthouseResult: {
      categories: {
        performance: { score: 0.88 },
        seo: { score: 0.95 },
      },
      audits: {
        'largest-contentful-paint': { numericValue: 2100 },
        'first-contentful-paint': { numericValue: 1200 },
        'cumulative-layout-shift': { numericValue: 0.04 },
        'total-blocking-time': { numericValue: 150 },
        'speed-index': { numericValue: 2400 },
        'unused-javascript': {
          score: 0.4,
          title: 'Zmniejsz ilość nieużywanego kodu JavaScript',
          displayValue: 'Potencjalna oszczędność 140 ms',
          details: { overallSavingsMs: 140, overallSavingsBytes: 45000 },
        },
      },
    },
  };

  it('correctly parses raw Lighthouse data into structured Core Web Vitals', () => {
    const service = new PageSpeedService();
    const result = service.parseAuditResponse(
      'https://www.akumulateo.pl/',
      'mobile',
      mockLighthouseData
    );

    expect(result.performanceScore).toBe(88);
    expect(result.seoScore).toBe(95);
    expect(result.metrics.largestContentfulPaintMs).toBe(2100);
    expect(result.metrics.firstContentfulPaintMs).toBe(1200);
    expect(result.metrics.cumulativeLayoutShift).toBe(0.04);
    expect(result.metrics.totalBlockingTimeMs).toBe(150);
    expect(result.metrics.speedIndexMs).toBe(2400);

    expect(result.opportunities.length).toBeGreaterThan(0);
    expect(result.opportunities[0].id).toBe('unused-javascript');
    expect(result.opportunities[0].wastedMs).toBe(140);
  });

  describe('evaluateEmergencyReadiness', () => {
    it('rates performance as EXCELLENT when LCP <= 2.5s and score >= 80', () => {
      const evaluation = PageSpeedService.evaluateEmergencyReadiness(85, 2200, 100);
      expect(evaluation.status).toBe('EXCELLENT');
      expect(evaluation.headlinePl).toContain('Wzorowa');
      expect(evaluation.driverImpactPl).toContain('696 556 446');
    });

    it('rates performance as ACCEPTABLE when LCP is between 2.5s and 4.0s', () => {
      const evaluation = PageSpeedService.evaluateEmergencyReadiness(65, 3200, 250);
      expect(evaluation.status).toBe('ACCEPTABLE');
      expect(evaluation.headlinePl).toContain('akceptowalna');
    });

    it('flags CRITICAL_RISK when LCP > 4.0s', () => {
      const evaluation = PageSpeedService.evaluateEmergencyReadiness(45, 5200, 600);
      expect(evaluation.status).toBe('CRITICAL_RISK');
      expect(evaluation.headlinePl).toContain('Krytyczne ryzyko');
      expect(evaluation.recommendedActionPl).toContain('odchudzić');
    });
  });

  it('performs mock audit using custom fetch implementation', async () => {
    const mockFetch = async () => ({
      ok: true,
      json: async () => mockLighthouseData,
      text: async () => '',
    }) as unknown as typeof fetch;

    const service = new PageSpeedService({ fetchImpl: mockFetch });
    const result = await service.audit('https://www.akumulateo.pl/', 'mobile');

    expect(result.performanceScore).toBe(88);
    expect(result.emergencyReadiness.status).toBe('EXCELLENT');
  });

  it('throws an informative error when API call fails', async () => {
    const failingFetch = async () => ({
      ok: false,
      status: 429,
      text: async () => 'Quota exceeded',
    }) as unknown as typeof fetch;

    const service = new PageSpeedService({ fetchImpl: failingFetch });
    await expect(service.audit('https://www.akumulateo.pl/')).rejects.toThrow(
      'PageSpeed API failed [429]: Quota exceeded'
    );
  });
});
