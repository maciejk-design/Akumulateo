#!/usr/bin/env tsx
/**
 * Akumulateo – Zintegrowany Raport Biznesowy (PSI + GSC + GA4)
 * Uruchomienie: npx tsx scripts/analytics-report.ts
 */

import * as fs from 'node:fs';
import * as path from 'node:path';
import { PageSpeedService } from '../src/services/pagespeed-service';
import { SearchConsoleService } from '../src/services/search-console-service';
import { GA4Service } from '../src/services/ga4-service';

// Basic .env loader (without requiring external dotenv package)
function loadEnv(): void {
  const envPath = path.resolve(process.cwd(), '.env');
  if (fs.existsSync(envPath)) {
    const lines = fs.readFileSync(envPath, 'utf8').split('\n');
    for (const line of lines) {
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith('#')) continue;
      const eqIdx = trimmed.indexOf('=');
      if (eqIdx !== -1) {
        const key = trimmed.slice(0, eqIdx).trim();
        let val = trimmed.slice(eqIdx + 1).trim();
        if (val.startsWith('"') && val.endsWith('"')) {
          val = val.slice(1, -1);
        } else if (val.startsWith("'") && val.endsWith("'")) {
          val = val.slice(1, -1);
        }
        if (!process.env[key]) {
          process.env[key] = val;
        }
      }
    }
  }
}

loadEnv();

async function runIntegratedReport(): Promise<void> {
  console.log('================================================================');
  console.log('   AKUMULATEO – ZINTEGROWANY RAPORT BIZNESOWY (PSI + GSC + GA4)');
  console.log('================================================================');

  const targetUrl = process.env.PAGESPEED_TARGET_URL || 'https://www.akumulateo.pl/';
  console.log(`\n1. [PageSpeed Insights] Audyt wydajności mobilnej dla ${targetUrl}...`);

  try {
    const psi = new PageSpeedService();
    const psiResult = await psi.audit(targetUrl, 'mobile');
    console.log(`   • Wynik Performance: ${psiResult.performanceScore}/100`);
    console.log(`   • LCP (czas do wyrenderowania telefonu): ${psiResult.metrics.largestContentfulPaintMs} ms`);
    console.log(`   • Status gotowości alarmowej: ${psiResult.emergencyReadiness.status}`);
    console.log(`   • Komunikat: ${psiResult.emergencyReadiness.headlinePl}`);
  } catch (err) {
    console.log(`   ⚠️ PageSpeed Insights: ${String(err)}`);
  }

  console.log('\n2. [Google Search Console] Pozycje lokalne i weryfikacja fraz negatywnych...');
  try {
    const gsc = new SearchConsoleService();
    const negativeCheck = await gsc.detectNegativeKeywords(28);
    console.log(`   • Ryzyko niepożądanego ruchu (sklepy stacjonarne/warsztaty): ${negativeCheck.wasteRiskScore}`);
    console.log(`   • Zmarnowane kliknięcia na zapytania stacjonarne: ${negativeCheck.totalWastedClicks}`);
    console.log(`   • Zalecenie biznesowe: ${negativeCheck.actionAdvicePl}`);

    const emergency = await gsc.getTopEmergencyQueries(28, 5);
    console.log(`   • Łącznie kliknięć w kluczowe frazy ratunkowe: ${emergency.totalClicks}`);
    if (emergency.queries.length > 0) {
      console.log('   • TOP 3 frazy ratunkowe:');
      for (const q of emergency.queries.slice(0, 3)) {
        console.log(`     - "${q.query}": ${q.clicks} kliknięć, śr. poz. ${q.position}`);
      }
    }
  } catch (err) {
    console.log(`   ℹ️ GSC: Wymaga skonfigurowania Service Account w .env (${String(err)})`);
  }

  console.log('\n3. [Google Analytics 4] Konwersje telefoniczne (phone_call_click) i zgłoszenia 24h...');
  try {
    const ga4 = new GA4Service();
    const calls = await ga4.getPhoneConversionSummary(30);
    console.log(`   • Łącznie kliknięć "Zadzwoń" (ostatnie 30 dni): ${calls.totalPhoneCalls}`);
    console.log(`   • Średni współczynnik konwersji ze strony na telefon: ${calls.overallConversionRate}%`);
    console.log(`   • Szacowany obrót/zysk minimalny z telefonów: ${calls.estimatedTotalProfitPln} PLN`);

    const hourly = await ga4.getHourlyCallDistribution(30);
    console.log(`   • Udział zgłoszeń nocnych 24h (22:00-06:00): ${hourly.nightCallsSharePercent}% (${hourly.nighttimeCalls} połączeń)`);
    console.log(`   • Potencjał dopłaty nocnej (+80 PLN): +${hourly.potentialNightSurchargeGainPln} PLN`);
  } catch (err) {
    console.log(`   ℹ️ GA4: Wymaga skonfigurowania GA4_PROPERTY_ID i Service Account w .env (${String(err)})`);
  }

  console.log('\n================================================================');
  console.log('   RAPORT ZAKOŃCZONY – AKUMULATEO 24H WARSZAWA');
  console.log('================================================================\n');
}

runIntegratedReport().catch((err) => {
  console.error('Błąd wykonania raportu:', err);
  process.exit(1);
});
