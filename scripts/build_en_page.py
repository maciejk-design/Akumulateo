#!/usr/bin/env python3
"""
Generator dla dedykowanej podstrony angielskiej Akumulateo:
URL: /car-battery-replacement-warsaw
Zgodność z Brandbook v2.2 i Single Source of Truth.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "snippets", "squarespace", "compiled-tailwind.min.css"), "r", encoding="utf-8") as f:
    TAILWIND_CSS = f.read().strip()

with open(os.path.join(BASE_DIR, "src", "config", "business-profile.json"), "r", encoding="utf-8") as f:
    PROFILE = json.load(f)

rating_val = PROFILE["rating"]["value"]
reviews_cnt = str(PROFILE["reviews"]["schemaCount"])

html_content = f"""<!-- ========================================================
     AKUMULATEO – ENGLISH LANDING PAGE (SQUARESPACE 7.1)
     URL Slug: /car-battery-replacement-warsaw
     Title: Mobile Car Battery Replacement Warsaw 24/7 | Fast Delivery & Installation – Akumulateo
     Meta Description: Dead car battery in Warsaw? 24/7 mobile battery replacement & jump start service delivered in 20-30 min to your location, hotel or underground garage. Call: +48 696 556 446.
     ======================================================== -->

<!-- 1. SCHEMA.ORG EMERGENCY SERVICE JSON-LD (ENGLISH) -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "EmergencyService",
  "name": "Akumulateo – 24/7 Mobile Car Battery Replacement Warsaw",
  "url": "https://www.akumulateo.pl/car-battery-replacement-warsaw",
  "telephone": "+48696556446",
  "inLanguage": "en",
  "priceRange": "$$",
  "image": "https://images.squarespace-cdn.com/content/v1/685d174157b18362d5b7b0f3/7c219de6-f0cf-4151-a1a4-eac82a1de5d2/akumulateo-hero-pagespeed.jpg",
  "areaServed": {{
    "@type": "City",
    "name": "Warsaw, Poland"
  }},
  "description": "Dead car battery in Warsaw? 24/7 mobile battery replacement & jump start service delivered in 20-30 min to your location, hotel or underground garage. Call: +48 696 556 446.",
  "openingHoursSpecification": {{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": [
      "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ],
    "opens": "00:00",
    "closes": "23:59"
  }},
  "aggregateRating": {{
    "@type": "AggregateRating",
    "ratingValue": "{rating_val}",
    "bestRating": "5.0",
    "worstRating": "1.0",
    "ratingCount": "{reviews_cnt}",
    "reviewCount": "{reviews_cnt}"
  }}
}}
</script>

<!-- 2. COMPILED TAILWIND CSS -->
<style id="akumulateo-optimized-tailwind">
{TAILWIND_CSS}
</style>

<!-- 3. ISOLATION & BRAND STYLES -->
<style id="akumulateo-en-custom-styles">
body {{
  background-color: #020617 !important;
}}

body #header,
body footer.sections,
body #footer-sections,
body section.page-section,
body .sqs-layout:not(.akumulateo-en-injected *),
body article:not(.akumulateo-en-injected *) {{
  display: none !important;
}}

.akumulateo-pulse-dot {{
  box-shadow: 0 0 0 0 rgba(2, 6, 23, 0.7);
  animation: akPulse 2s infinite;
}}

@keyframes akPulse {{
  0% {{
    box-shadow: 0 0 0 0 rgba(2, 6, 23, 0.7);
  }}
  70% {{
    box-shadow: 0 0 0 6px rgba(2, 6, 23, 0);
  }}
  100% {{
    box-shadow: 0 0 0 0 rgba(2, 6, 23, 0);
  }}
}}

.ak-mobile-menu {{
  transition: opacity 0.2s ease-in-out, visibility 0.2s ease-in-out;
}}
</style>

<!-- 4. MAIN EN LANDING PAGE CONTENT -->
<div class="akumulateo-root akumulateo-en-injected bg-slate-950 text-slate-100 font-sans antialiased min-h-screen flex flex-col justify-between" style="display:flex!important; visibility:visible!important; opacity:1!important; position:relative!important; z-index:100!important;">

  <!-- TOP EMERGENCY BAR -->
  <div class="bg-gradient-to-r from-amber-500 via-amber-400 to-amber-500 text-slate-950 px-3.5 sm:px-4 py-1.5 sm:py-2 text-[11px] sm:text-xs font-black tracking-wide">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-x-2.5 gap-y-1">
      <div class="flex items-center gap-1.5 flex-shrink-0">
        <span class="w-2 h-2 rounded-full bg-slate-950 akumulateo-pulse-dot flex-shrink-0"></span>
        <span class="uppercase font-black tracking-wider">24/7 Mobile Dispatch</span>
        <span class="hidden sm:inline font-bold text-slate-900">• Rapid 20–30 min arrival across Warsaw & airports</span>
      </div>
      <div class="flex items-center gap-2.5 flex-shrink-0 text-[11px] font-bold">
        <span class="inline-flex items-center gap-1 font-extrabold text-slate-950 bg-amber-300/90 px-1.5 py-0.5 rounded text-[10px]" title="English speaking support 24/7">🇬🇧 English Support</span>
        <a href="https://g.page/r/CXjN9llopHR_EBM/" target="_blank" rel="noopener noreferrer" class="hover:text-slate-800 hover:underline flex items-center gap-1 transition cursor-pointer" title="Verified Google Maps reviews">
          <span>⭐ <span data-ak-cfg="ratingValue">{rating_val}</span> on Google (<span data-ak-cfg="reviewsCount">{reviews_cnt}+</span> reviews) ↗</span>
        </a>
      </div>
    </div>
  </div>

  <!-- STICKY HEADER -->
  <header class="bg-slate-900/95 backdrop-filter backdrop-blur-md sticky top-0 z-40 border-b border-slate-800 px-2 sm:px-4 py-2 sm:py-3.5">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-1 sm:gap-4">
      
      <!-- LOGO: ACTIVE LINK TO HOME -->
      <a href="/" class="flex items-center gap-1.5 sm:gap-2 group text-decoration-none min-w-0 cursor-pointer flex-shrink-0" aria-label="Akumulateo – Home">
        <div class="w-7 h-7 sm:w-9 sm:h-9 rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center p-1 shadow-md group-hover:border-amber-500 transition" style="width:28px;height:28px;min-width:28px;min-height:28px;max-width:36px;max-height:36px;flex-shrink:0;">
          <svg viewBox="0 0 68 68" style="width:100%;height:100%;display:block;" fill="none">
            <rect x="14" y="6" width="10" height="7" rx="2" fill="#94A3B8" />
            <rect x="44" y="6" width="10" height="7" rx="2" fill="#EF4444" />
            <rect x="6" y="12" width="56" height="52" rx="10" fill="#0F172A" stroke="#475569" stroke-width="2" />
            <path d="M37 17L22 38h9l-5 19 19-24h-10l7-16z" fill="#F59E0B" />
            <circle cx="53" cy="56" r="3" fill="#10B981" />
          </svg>
        </div>
        <div class="leading-none">
          <div class="text-sm sm:text-lg md:text-xl font-black tracking-wide sm:tracking-wider text-white whitespace-nowrap">
            AKUMULAT<span class="text-amber-500">E</span>O
          </div>
          <div class="text-[9px] sm:text-[10px] text-slate-400 font-semibold tracking-wider uppercase hidden sm:block">
            Mobile Roadside Service 24/7
          </div>
        </div>
      </a>

      <!-- CTA BUTTON & MENU -->
      <div class="flex items-center gap-1.5 sm:gap-3 flex-shrink-0">
        <a href="/" class="hidden md:inline-flex items-center gap-1 text-xs font-bold text-slate-300 hover:text-amber-400 px-2 py-1 transition">
          🇵🇱 Wersja PL
        </a>
        <a href="tel:+48696556446" class="inline-flex items-center gap-1 sm:gap-2 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black px-2 py-1.5 sm:px-3.5 sm:py-2 rounded-lg sm:rounded-xl shadow-lg shadow-amber-500/20 active:scale-95 transition text-[11px] sm:text-sm whitespace-nowrap flex-shrink-0" title="Call Emergency Battery Service">
          <svg class="w-3.5 h-3.5 sm:w-4 sm:h-4 animate-bounce" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="width:14px;height:14px;">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
          </svg>
          <span class="font-extrabold">696 556 446</span>
        </a>
        
        <button id="ak-menu-toggle" class="ak-mobile-menu-btn flex items-center justify-center gap-1.5 px-2.5 py-1.5 rounded-lg border-2 border-amber-500 bg-slate-800 text-amber-400 font-black text-xs uppercase shadow-md shadow-amber-500/25 active:scale-95 transition cursor-pointer flex-shrink-0" aria-label="Open Navigation Menu">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="width:16px;height:16px;">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
          <span id="ak-menu-btn-text" class="tracking-wider">MENU</span>
        </button>
      </div>

    </div>
  </header>

  <!-- MOBILE MENU DRAWER -->
  <nav id="ak-mobile-menu" class="ak-mobile-menu hidden bg-slate-900 border-b border-slate-800 px-4 py-3 shadow-xl">
    <div class="max-w-7xl mx-auto flex flex-col gap-2">
      <a href="/" class="text-slate-200 hover:text-amber-400 font-bold py-2 border-b border-slate-800/80">🏠 Home (Wersja Polska)</a>
      <a href="/obszar-dzialania-warszawa-i-okolice" class="text-slate-200 hover:text-amber-400 font-bold py-2 border-b border-slate-800/80">📍 Service Coverage (Warsaw & Metro)</a>
      <a href="/awaryjne-odpalanie-samochodu-warszawa" class="text-slate-200 hover:text-amber-400 font-bold py-2 border-b border-slate-800/80">⚡ Jump Start Service (12V/24V)</a>
      <a href="tel:+48696556446" class="text-amber-400 font-black py-2">📞 Emergency Dispatch: +48 696 556 446</a>
    </div>
  </nav>

  <!-- MAIN HERO SECTION -->
  <main class="flex-grow">
    <section class="relative pt-6 sm:pt-10 pb-12 sm:pb-16 px-4 overflow-hidden border-b border-slate-800">
      <div class="max-w-4xl mx-auto text-center">
        
        <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs sm:text-sm font-extrabold mb-4 sm:mb-6 uppercase tracking-wider">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          24/7 Mobile Car Battery Service • Warsaw & Suburbs
        </div>

        <h1 class="text-3xl sm:text-5xl md:text-6xl font-black text-white tracking-tight mb-4 sm:mb-6 leading-tight">
          Mobile Car Battery Replacement in Warsaw <span class="text-amber-400">24/7</span>
        </h1>

        <p class="text-base sm:text-lg md:text-xl text-slate-300 font-normal mb-8 max-w-3xl mx-auto leading-relaxed">
          Stranded with a flat battery in Warsaw? Our mobile technicians arrive at your location in <strong class="text-white">20–30 minutes</strong> — whether you are at home, office, hotel, or stuck in a tight underground garage. We deliver, test, install premium OEM batteries (<strong class="text-amber-400">Varta, Yuasa, Bosch</strong>), and perform computer BMS coding on the spot.
        </p>

        <!-- CTA SECTION -->
        <div class="flex flex-col sm:flex-row items-center justify-center gap-3 sm:gap-4 mb-8">
          <a href="tel:+48696556446" class="w-full sm:w-auto inline-flex items-center justify-center gap-3 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black text-lg sm:text-xl px-6 py-4 rounded-xl shadow-xl shadow-amber-500/25 active:scale-95 transition cursor-pointer text-decoration-none">
            <svg class="w-6 h-6 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="width:24px;height:24px;">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
            </svg>
            <span>Call English Support: 696 556 446</span>
          </a>
        </div>

        <div class="flex flex-wrap items-center justify-center gap-4 text-xs sm:text-sm font-semibold text-slate-400">
          <span class="flex items-center gap-1.5"><span class="text-emerald-400">✓</span> Fast 20–30 min ETA</span>
          <span class="flex items-center gap-1.5"><span class="text-emerald-400">✓</span> Card & BLIK payments</span>
          <span class="flex items-center gap-1.5"><span class="text-emerald-400">✓</span> Underground garages access</span>
          <span class="flex items-center gap-1.5"><span class="text-emerald-400">✓</span> Up to 3-year warranty</span>
        </div>

      </div>
    </section>

    <!-- PRE-QUALIFICATION NOTICE BANNER -->
    <section class="max-w-4xl mx-auto px-4 py-6">
      <div class="p-4 sm:p-5 rounded-2xl bg-amber-500/10 border-2 border-amber-500/30 flex flex-col sm:flex-row items-start sm:items-center gap-3.5">
        <div class="w-10 h-10 rounded-xl bg-amber-500 text-slate-950 flex items-center justify-center font-black text-xl flex-shrink-0">
          ℹ️
        </div>
        <div>
          <h2 class="text-base sm:text-lg font-black text-amber-400 uppercase tracking-wide mb-1">
            100% On-Site Mobile Service with Direct Delivery
          </h2>
          <p class="text-sm sm:text-base text-slate-200 leading-relaxed m-0">
            We operate exclusively as a <strong>24/7 mobile assistance service</strong>. We do <strong>NOT</strong> have a walk-in storefront or self-pickup depot. Our technician arrives directly to your vehicle with a brand-new battery, performs diagnostic checks, installs it safely, and takes care of the old battery.
          </p>
        </div>
      </div>
    </section>

    <!-- KEY SERVICES GRID -->
    <section class="max-w-4xl mx-auto px-4 py-8">
      <h2 class="text-2xl sm:text-3xl font-black text-white text-center mb-8">
        Our Professional Services in Warsaw
      </h2>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <!-- SERVICE 1 -->
        <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 flex flex-col justify-between hover:border-amber-500/50 transition">
          <div>
            <div class="w-12 h-12 rounded-xl bg-amber-500/10 text-amber-400 flex items-center justify-center text-2xl font-black mb-4">
              🔋
            </div>
            <h3 class="text-lg font-black text-white mb-2">Mobile Battery Replacement</h3>
            <p class="text-sm text-slate-300 leading-relaxed mb-4">
              Complete on-site delivery and professional installation of brand-new OEM batteries from <strong class="text-white">Varta, Yuasa, and Bosch</strong>. Full manufacturer warranty up to 3 years.
            </p>
          </div>
          <div class="text-xs text-amber-400 font-bold border-t border-slate-800 pt-3">
            Includes alternator & charging test
          </div>
        </div>

        <!-- SERVICE 2 -->
        <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 flex flex-col justify-between hover:border-amber-500/50 transition">
          <div>
            <div class="w-12 h-12 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center text-2xl font-black mb-4">
              ⚡
            </div>
            <h3 class="text-lg font-black text-white mb-2">Emergency Jump Start</h3>
            <p class="text-sm text-slate-300 leading-relaxed mb-4">
              Safe vehicle startup using heavy-duty 3000A microprocessor boosters (12V / 24V). Complete surge protection for ECU, hybrid systems, and sensitive vehicle electronics.
            </p>
          </div>
          <div class="text-xs text-emerald-400 font-bold border-t border-slate-800 pt-3">
            Safe for Hybrid & EV 12V auxiliary
          </div>
        </div>

        <!-- SERVICE 3 -->
        <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 flex flex-col justify-between hover:border-amber-500/50 transition">
          <div>
            <div class="w-12 h-12 rounded-xl bg-blue-500/20 text-blue-400 flex items-center justify-center text-2xl font-black mb-4">
              💻
            </div>
            <h3 class="text-lg font-black text-white mb-2">BMS Coding & Diagnostics</h3>
            <p class="text-sm text-slate-300 leading-relaxed mb-4">
              Battery Management System (BMS) registration via OBD2 for Start-Stop, AGM and EFB batteries. Memory saving unit preserves all radio, clock, and steering adaptations.
            </p>
          </div>
          <div class="text-xs text-blue-400 font-bold border-t border-slate-800 pt-3">
            Essential for BMW, Audi, Mercedes, VW
          </div>
        </div>

      </div>
    </section>

    <!-- WHY CHOOSE US & UNDERGROUND ACCESS -->
    <section class="max-w-4xl mx-auto px-4 py-8">
      <div class="bg-gradient-to-b from-slate-900 to-slate-950 border border-slate-800 rounded-2xl p-6 sm:p-8">
        <h2 class="text-xl sm:text-2xl font-black text-white mb-6">
          Why Drivers & Expats in Warsaw Trust Akumulateo
        </h2>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div class="flex items-start gap-3.5">
            <span class="text-amber-400 font-black text-lg">🏢</span>
            <div>
              <h3 class="text-base font-bold text-white mb-1">Underground Parking Specialists</h3>
              <p class="text-sm text-slate-300 leading-relaxed">
                Our compact service vehicles and portable trolley boosters easily enter tight underground parking garages (levels -1, -2, -3) with clearances below 1.9m.
              </p>
            </div>
          </div>

          <div class="flex items-start gap-3.5">
            <span class="text-amber-400 font-black text-lg">💳</span>
            <div>
              <h3 class="text-base font-bold text-white mb-1">Card, Contactless & BLIK Accepted</h3>
              <p class="text-sm text-slate-300 leading-relaxed">
                Pay conveniently on the spot using Visa, Mastercard, Apple Pay, Google Pay, BLIK or cash. Official 23% VAT invoice issued immediately.
              </p>
            </div>
          </div>

          <div class="flex items-start gap-3.5">
            <span class="text-amber-400 font-black text-lg">♻️</span>
            <div>
              <h3 class="text-base font-bold text-white mb-1">Free Old Battery Recycling</h3>
              <p class="text-sm text-slate-300 leading-relaxed">
                We take away your old dead battery for certified eco-friendly recycling, eliminating the standard 30 PLN legal deposit surcharge.
              </p>
            </div>
          </div>

          <div class="flex items-start gap-3.5">
            <span class="text-amber-400 font-black text-lg">🗣️</span>
            <div>
              <h3 class="text-base font-bold text-white mb-1">Fluent English Speaking Support</h3>
              <p class="text-sm text-slate-300 leading-relaxed">
                No language barriers. Communicate your location, vehicle model, and situation clearly with our English-speaking dispatchers and technicians.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- COVERAGE AREA -->
    <section class="max-w-4xl mx-auto px-4 py-8">
      <h2 class="text-xl sm:text-2xl font-black text-white text-center mb-4">
        Serving All 18 Warsaw Districts & Warsaw Airports
      </h2>
      <p class="text-sm sm:text-base text-slate-400 text-center max-w-2xl mx-auto mb-6">
        Rapid roadside dispatch across the entire Warsaw metropolitan area (20–30 min average arrival):
      </p>

      <div class="bg-slate-900/60 border border-slate-800 rounded-xl p-5 text-center text-xs sm:text-sm text-slate-300 leading-relaxed">
        <strong>Śródmieście (City Centre)</strong> • <strong>Mokotów</strong> • <strong>Wola</strong> • <strong>Wilanów</strong> • <strong>Ochota</strong> • <strong>Ursynów</strong> • <strong>Bielany</strong> • <strong>Bemowo</strong> • <strong>Białołęka</strong> • <strong>Targówek</strong> • <strong>Praga-Północ</strong> • <strong>Praga-Południe</strong> • <strong>Włochy</strong> • <strong>Ursus</strong> • <strong>Żoliborz</strong> • <strong>Wawer</strong> • <strong>Wesoła</strong> • <strong>Rembertów</strong><br><br>
        <span class="text-amber-400 font-semibold">✈️ Chopin Airport (WAW) & Modlin Airport (WMI) parking lots covered 24/7.</span>
      </div>
    </section>

    <!-- FAQ SECTION -->
    <section class="max-w-4xl mx-auto px-4 py-8 mb-12">
      <h2 class="text-2xl sm:text-3xl font-black text-white text-center mb-8">
        Frequently Asked Questions (FAQ)
      </h2>

      <div class="space-y-4">
        <div class="bg-slate-900 border border-slate-800 rounded-xl p-5">
          <h3 class="text-base font-bold text-amber-400 mb-2">Can you enter low-clearance underground garages?</h3>
          <p class="text-sm text-slate-300 leading-relaxed m-0">
            Yes. Our service fleet consists of low-clearance vehicles and fully portable battery testers and 3000A jump starters. We easily access parking decks on levels -1, -2, and -3 in residential buildings, hotels, and business centres.
          </p>
        </div>

        <div class="bg-slate-900 border border-slate-800 rounded-xl p-5">
          <h3 class="text-base font-bold text-amber-400 mb-2">What payment methods are accepted?</h3>
          <p class="text-sm text-slate-300 leading-relaxed m-0">
            Every technician carries a mobile payment terminal. We accept chip & contactless cards (Visa, Mastercard), mobile wallets (Apple Pay, Google Pay), BLIK, and cash. We can issue a Polish VAT 23% invoice immediately.
          </p>
        </div>

        <div class="bg-slate-900 border border-slate-800 rounded-xl p-5">
          <h3 class="text-base font-bold text-amber-400 mb-2">What battery brands do you carry?</h3>
          <p class="text-sm text-slate-300 leading-relaxed m-0">
            We exclusively install brand-new, factory-fresh batteries from globally recognized premium manufacturers: <strong>Varta, Yuasa, and Bosch</strong>. Every unit comes with up to 3 years manufacturer warranty.
          </p>
        </div>

        <div class="bg-slate-900 border border-slate-800 rounded-xl p-5">
          <h3 class="text-base font-bold text-amber-400 mb-2">How fast can a technician arrive?</h3>
          <p class="text-sm text-slate-300 leading-relaxed m-0">
            Our average arrival time in Warsaw is between 20 and 30 minutes from your phone call, depending on traffic and your district.
          </p>
        </div>
      </div>
    </section>

    <!-- FINAL CALL TO ACTION -->
    <section class="max-w-4xl mx-auto px-4 pb-16">
      <div class="bg-gradient-to-r from-amber-500 via-amber-400 to-amber-500 rounded-3xl p-8 sm:p-10 text-center text-slate-950 shadow-2xl">
        <h2 class="text-2xl sm:text-4xl font-black mb-3">
          Need Immediate Battery Assistance in Warsaw?
        </h2>
        <p class="text-base sm:text-lg font-bold text-slate-900 mb-6 max-w-2xl mx-auto">
          Speak directly with our English-speaking dispatcher. Describe your vehicle and location — a certified technician is dispatched immediately.
        </p>
        <a href="tel:+48696556446" class="inline-flex items-center justify-center gap-3 bg-slate-950 hover:bg-slate-900 text-amber-400 hover:text-amber-300 font-black text-xl sm:text-2xl px-8 py-5 rounded-2xl shadow-xl active:scale-95 transition text-decoration-none">
          <span>📞 Call: +48 696 556 446</span>
        </a>
      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="bg-slate-950 border-t border-slate-800/80 px-4 py-8 text-center text-xs text-slate-400">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
      <div>
        © 2026 Akumulateo. 24/7 Mobile Car Battery Replacement Warsaw. All rights reserved.
      </div>
      <div class="flex items-center gap-4 font-bold text-slate-300">
        <a href="/" class="hover:text-amber-400 transition">Strona Główna (PL)</a>
        <span>•</span>
        <a href="/obszar-dzialania-warszawa-i-okolice" class="hover:text-amber-400 transition">Obszar Działania</a>
        <span>•</span>
        <a href="tel:+48696556446" class="hover:text-amber-400 transition">+48 696 556 446</a>
      </div>
    </div>
  </footer>

</div>

<!-- 5. MOBILE MENU INTERACTION SCRIPT -->
<script>
(function() {{
  var btn = document.getElementById('ak-menu-toggle');
  var menu = document.getElementById('ak-mobile-menu');
  var txt = document.getElementById('ak-menu-btn-text');
  if (btn && menu && txt) {{
    btn.addEventListener('click', function(e) {{
      e.stopPropagation();
      var isClosed = menu.classList.contains('hidden');
      if (isClosed) {{
        menu.classList.remove('hidden');
        txt.textContent = 'CLOSE';
      }} else {{
        menu.classList.add('hidden');
        txt.textContent = 'MENU';
      }}
    }});
    menu.querySelectorAll('a').forEach(function(a) {{
      a.addEventListener('click', function() {{
        menu.classList.add('hidden');
        txt.textContent = 'MENU';
      }});
    }});
  }}
}})();
</script>
"""

out_snippet = os.path.join(BASE_DIR, "snippets", "squarespace", "car-battery-replacement-warsaw-page-header-injection.html")
out_page = os.path.join(BASE_DIR, "src", "seo", "generated-pages", "car-battery-replacement-warsaw.html")

with open(out_snippet, "w", encoding="utf-8") as f:
    f.write(html_content)

with open(out_page, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ Generated EN snippet: {len(html_content)} chars -> {out_snippet}")
print(f"✅ Generated EN page: {len(html_content)} chars -> {out_page}")
