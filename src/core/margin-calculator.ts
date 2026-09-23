/**
 * Akumulateo – Core Margin & Pricing Engine
 * Narzędzie do kalkulacji rentowności zleceń pogotowia akumulatorowego 24h.
 * Uwzględnia marżę handlową, opłatę serwisową, dopłaty nocne/strefowe oraz zysk ze złomu.
 */

export type BatteryTechnology = 'CONVENTIONAL' | 'EFB' | 'AGM' | 'GEL';

export type TimeSlot = 'DAY_STANDARD' | 'NIGHT_24H' | 'HOLIDAY_WEEKEND';

export type DistrictZone =
  | 'ZONE_1_CENTRAL'   // Mokotów, Wola, Śródmieście, Ochota, Żoliborz, Praga Płd/Płn
  | 'ZONE_2_OUTER'     // Białołęka, Wawer, Ursus, Rembertów, Wesoła, Bielany, Bemowo, Wilanów
  | 'ZONE_3_SUBURBS';  // Piaseczno, Pruszków, Legionowo, Marki, Otwock, Łomianki, Ząbki, Wołomin

export type ServiceType =
  | 'REPLACEMENT_WITH_BATTERY' // Pełna usługa: dowóz + montaż + stary aku
  | 'JUMP_START_ONLY'          // Awaryjny rozruch boosterem 12V/24V
  | 'DIAGNOSTIC_ONLY';         // Test akumulatora, ładowania, upływności prądu

export interface JobQuoteInput {
  serviceType: ServiceType;
  batteryTechnology?: BatteryTechnology;
  batteryCapacityAh?: number;
  batteryWholesaleCostPln?: number; // Koszt zakupu akumulatora w hurtowni (brutto)
  customerBatteryPricePln?: number; // Sugerowana cena detaliczna akumulatora dla klienta
  timeSlot: TimeSlot;
  districtZone: DistrictZone;
  requiresBmsCoding?: boolean;      // Czy auto wymaga kodowania/adaptacji w komputerze BMS
  oldBatteryWeightKg?: number;      // Waga starego akumulatora oddawanego przez klienta
  scrapPricePerKgPln?: number;      // Cena skupu złomu ołowianego (domyślnie 3.50 PLN/kg)
}

export interface JobProfitabilityResult {
  customerTotalQuotePln: number;    // Łączna kwota dla klienta (akumulator + usługa)
  wholesaleCostPln: number;         // Bezpośredni koszt zakupu części
  batteryMarginPln: number;         // Zysk handlowy na samym akumulatorze
  serviceFeePln: number;            // Wynagrodzenie za dojazd, montaż i diagnostykę
  scrapLeadProfitPln: number;       // Czysty zysk ze sprzedaży starego akumulatora do skupu
  totalNetProfitPln: number;        // ŁĄCZNY ZYSK NETTO NA ZLECENIU
  profitMarginPercent: number;      // Rentowność procentowa zlecenia
  isProfitable: boolean;            // Czy zlecenie spełnia minimalny próg opłacalności
}

export const MIN_ACCEPTABLE_PROFIT_PLN = 180; // Minimalny zysk zlecenia uzasadniający wyjazd w trasę
export const DEFAULT_SCRAP_PRICE_PER_KG = 3.50; // Średnia cena złomu ołowianego w Warszawie (PLN/kg)

export class MarginCalculator {
  /**
   * Szacuje wagę starego akumulatora na podstawie pojemności Ah
   */
  public static estimateScrapWeight(capacityAh: number): number {
    if (capacityAh <= 50) return 12;
    if (capacityAh <= 65) return 15;
    if (capacityAh <= 80) return 19;
    if (capacityAh <= 100) return 24;
    return 28;
  }

  /**
   * Oblicza opłatę za dojazd i usługę w zależności od pory i strefy
   */
  public static calculateBaseServiceFee(
    serviceType: ServiceType,
    timeSlot: TimeSlot,
    zone: DistrictZone,
    requiresBmsCoding: boolean = false
  ): number {
    let baseFee = 0;

    switch (serviceType) {
      case 'JUMP_START_ONLY':
        baseFee = 150;
        break;
      case 'DIAGNOSTIC_ONLY':
        baseFee = 130;
        break;
      case 'REPLACEMENT_WITH_BATTERY':
        baseFee = 120; // Przy zakupie akumulatora opłata montażowa jest preferencyjna
        break;
    }

    // Dopłata za porę nocną / weekend
    if (timeSlot === 'NIGHT_24H') {
      baseFee += 80;
    } else if (timeSlot === 'HOLIDAY_WEEKEND') {
      baseFee += 40;
    }

    // Dopłata strefowa za dojazd
    if (zone === 'ZONE_2_OUTER') {
      baseFee += 30;
    } else if (zone === 'ZONE_3_SUBURBS') {
      baseFee += 60;
    }

    // Dopłata za procedurę kodowania BMS testerem diagnostycznym
    if (requiresBmsCoding) {
      baseFee += 60;
    }

    return baseFee;
  }

  /**
   * Główna metoda kalkulująca zysk i rentowność zlecenia
   */
  public static calculateJob(input: JobQuoteInput): JobProfitabilityResult {
    const scrapPricePerKg = input.scrapPricePerKgPln ?? DEFAULT_SCRAP_PRICE_PER_KG;
    const serviceFee = this.calculateBaseServiceFee(
      input.serviceType,
      input.timeSlot,
      input.districtZone,
      input.requiresBmsCoding
    );

    let wholesaleCost = 0;
    let customerBatteryPrice = 0;
    let batteryMargin = 0;
    let scrapProfit = 0;

    if (input.serviceType === 'REPLACEMENT_WITH_BATTERY') {
      wholesaleCost = input.batteryWholesaleCostPln ?? 0;
      customerBatteryPrice = input.customerBatteryPricePln ?? wholesaleCost * 1.35;
      batteryMargin = Math.max(0, customerBatteryPrice - wholesaleCost);

      const weightKg = input.oldBatteryWeightKg ?? 
        (input.batteryCapacityAh ? this.estimateScrapWeight(input.batteryCapacityAh) : 16);
      
      scrapProfit = Math.round(weightKg * scrapPricePerKg);
    }

    const customerTotalQuote = customerBatteryPrice + serviceFee;
    const totalProfit = batteryMargin + serviceFee + scrapProfit;
    const profitMarginPercent = customerTotalQuote > 0 
      ? Math.round((totalProfit / customerTotalQuote) * 100) 
      : 100;

    return {
      customerTotalQuotePln: Math.round(customerTotalQuote),
      wholesaleCostPln: Math.round(wholesaleCost),
      batteryMarginPln: Math.round(batteryMargin),
      serviceFeePln: Math.round(serviceFee),
      scrapLeadProfitPln: scrapProfit,
      totalNetProfitPln: Math.round(totalProfit),
      profitMarginPercent,
      isProfitable: totalProfit >= MIN_ACCEPTABLE_PROFIT_PLN
    };
  }
}
