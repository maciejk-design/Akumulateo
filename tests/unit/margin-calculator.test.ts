import { describe, it, expect } from 'vitest';
import { MarginCalculator, JobQuoteInput } from '../../src/core/margin-calculator.js';

describe('MarginCalculator Unit Tests', () => {
  it('oblicza poprawny zysk dla standardowej wymiany akumulatora w dzień (Zone 1)', () => {
    const jobInput: JobQuoteInput = {
      serviceType: 'REPLACEMENT_WITH_BATTERY',
      batteryCapacityAh: 70,
      batteryWholesaleCostPln: 350,
      customerBatteryPricePln: 520,
      timeSlot: 'DAY_STANDARD',
      districtZone: 'ZONE_1_CENTRAL',
      requiresBmsCoding: false,
      oldBatteryWeightKg: 19,
      scrapPricePerKgPln: 3.50
    };

    const result = MarginCalculator.calculateJob(jobInput);

    // Cena dla klienta: 520 (bateria) + 120 (usługa standardowa) = 640 PLN
    expect(result.customerTotalQuotePln).toBe(640);
    // Marża na baterii: 520 - 350 = 170 PLN
    expect(result.batteryMarginPln).toBe(170);
    // Opłata za usługę: 120 PLN
    expect(result.serviceFeePln).toBe(120);
    // Złom: 19 kg * 3.5 = 66.5 -> 67 PLN
    expect(result.scrapLeadProfitPln).toBe(67);
    // Łączny zysk: 170 + 120 + 67 = 357 PLN
    expect(result.totalNetProfitPln).toBe(357);
    expect(result.isProfitable).toBe(true);
  });

  it('uwzględnia dopłatę nocną i kodowanie BMS dla auta klasy premium w strefie podmiejskiej (Zone 3)', () => {
    const jobInput: JobQuoteInput = {
      serviceType: 'REPLACEMENT_WITH_BATTERY',
      batteryTechnology: 'AGM',
      batteryCapacityAh: 95,
      batteryWholesaleCostPln: 650,
      customerBatteryPricePln: 950,
      timeSlot: 'NIGHT_24H',
      districtZone: 'ZONE_3_SUBURBS', // Piaseczno / Pruszków
      requiresBmsCoding: true,        // Wymagane kodowanie BMS
      oldBatteryWeightKg: 24,
      scrapPricePerKgPln: 3.50
    };

    const result = MarginCalculator.calculateJob(jobInput);

    // Usługa: 120 (baza) + 80 (noc 24h) + 60 (strefa 3) + 60 (kodowanie) = 320 PLN
    expect(result.serviceFeePln).toBe(320);
    // Klient płaci: 950 + 320 = 1270 PLN
    expect(result.customerTotalQuotePln).toBe(1270);
    // Marża na baterii: 950 - 650 = 300 PLN
    expect(result.batteryMarginPln).toBe(300);
    // Złom: 24 * 3.50 = 84 PLN
    expect(result.scrapLeadProfitPln).toBe(84);
    // Łączny zysk: 300 + 320 + 84 = 704 PLN
    expect(result.totalNetProfitPln).toBe(704);
    expect(result.profitMarginPercent).toBeGreaterThan(50);
  });

  it('prawidłowo wycenia awaryjny rozruch boosterem (Jump Start Only)', () => {
    const jobInput: JobQuoteInput = {
      serviceType: 'JUMP_START_ONLY',
      timeSlot: 'DAY_STANDARD',
      districtZone: 'ZONE_1_CENTRAL'
    };

    const result = MarginCalculator.calculateJob(jobInput);

    expect(result.customerTotalQuotePln).toBe(150);
    expect(result.batteryMarginPln).toBe(0);
    expect(result.scrapLeadProfitPln).toBe(0);
    expect(result.totalNetProfitPln).toBe(150);
  });
});
