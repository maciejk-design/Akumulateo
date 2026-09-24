import { describe, it, expect, vi } from 'vitest';
import {
  SearchConsoleService,
  GSCRowData,
} from '../../src/services/search-console-service';
import { GoogleAuthService } from '../../src/services/google-auth';

describe('SearchConsoleService', () => {
  const mockRows: GSCRowData[] = [
    {
      keys: ['wymiana akumulatora mokotów'],
      clicks: 45,
      impressions: 420,
      ctr: 0.107,
      position: 2.1,
    },
    {
      keys: ['pogotowie akumulatorowe warszawa 24h'],
      clicks: 80,
      impressions: 600,
      ctr: 0.133,
      position: 1.8,
    },
    {
      keys: ['sklep z akumulatorami wola odbiór osobisty'],
      clicks: 12,
      impressions: 110,
      ctr: 0.109,
      position: 3.4,
    },
    {
      keys: ['pzu assistance darmowe odpalenie'],
      clicks: 6,
      impressions: 55,
      ctr: 0.109,
      position: 4.2,
    },
    {
      keys: ['warsztat wymiana opon wulkanizacja'],
      clicks: 4,
      impressions: 40,
      ctr: 0.1,
      position: 6.5,
    },
  ];

  function createMockAuthService(): GoogleAuthService {
    const auth = new GoogleAuthService();
    vi.spyOn(auth, 'getAccessToken').mockResolvedValue('mock-test-token');
    return auth;
  }

  it('detects negative and stationary keywords threatening unit economics', async () => {
    const mockFetch = async () => ({
      ok: true,
      json: async () => ({ rows: mockRows }),
      text: async () => '',
    }) as unknown as typeof fetch;

    const auth = createMockAuthService();
    const service = new SearchConsoleService(auth, 'https://www.akumulateo.pl/', mockFetch);

    const result = await service.detectNegativeKeywords(28);

    expect(result.detectedQueries.length).toBe(3);

    const categories = result.detectedQueries.map((q) => q.category);
    expect(categories).toContain('STATIONARY_SHOP');
    expect(categories).toContain('FREE_ASSISTANCE');
    expect(categories).toContain('WORKSHOP_TIRES');

    expect(result.totalWastedClicks).toBe(22); // 12 + 6 + 4
    expect(result.wasteRiskScore).toBe('HIGH'); // > 20 wasted clicks
    expect(result.actionAdvicePl).toContain('brak sklepu stacjonarnego');
  });

  it('aggregates top emergency high-intent battery queries', async () => {
    const mockFetch = async () => ({
      ok: true,
      json: async () => ({ rows: mockRows }),
      text: async () => '',
    }) as unknown as typeof fetch;

    const auth = createMockAuthService();
    const service = new SearchConsoleService(auth, 'https://www.akumulateo.pl/', mockFetch);

    const result = await service.getTopEmergencyQueries(28, 5);

    expect(result.queries.length).toBeGreaterThan(0);
    expect(result.queries[0].query).toBe('pogotowie akumulatorowe warszawa 24h');
    expect(result.queries[0].clicks).toBe(80);
    expect(result.totalClicks).toBeGreaterThanOrEqual(125);
  });

  it('calculates district performance accurately', async () => {
    const districtRows: GSCRowData[] = [
      {
        keys: ['wymiana akumulatora mokotów', '/warszawa-mokotow'],
        clicks: 30,
        impressions: 200,
        ctr: 0.15,
        position: 2.0,
      },
      {
        keys: ['akumulator mordor domaniewska', '/warszawa-mokotow'],
        clicks: 15,
        impressions: 100,
        ctr: 0.15,
        position: 3.0,
      },
    ];

    const mockFetch = async () => ({
      ok: true,
      json: async () => ({ rows: districtRows }),
      text: async () => '',
    }) as unknown as typeof fetch;

    const auth = createMockAuthService();
    const service = new SearchConsoleService(auth, 'https://www.akumulateo.pl/', mockFetch);

    const report = await service.getDistrictPerformance('mokotow', 'Mokotów', 28);

    expect(report.districtName).toBe('Mokotów');
    expect(report.slug).toBe('mokotow');
    expect(report.clicks).toBe(45);
    expect(report.impressions).toBe(300);
    expect(report.ctr).toBe(15);
    expect(report.averagePosition).toBe(2.3);
    expect(report.topQueries.length).toBe(2);
  });
});
