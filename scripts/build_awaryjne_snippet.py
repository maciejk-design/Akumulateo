#!/usr/bin/env python3
"""
Generator dedykowanego pakietu Page Header Code Injection dla podstrony:
https://www.akumulateo.pl/awaryjne-uruchomienie-auta-warszawa
Zgodny z Brandbook v2.2, Dark Mode (#020617), zero wycieków CSS,
kompaktowy nagłówek mobilny <= 320px (Logo 24px + Tel 11px + MENU),
brak ucinania H1 (text-xl sm:text-4xl), pełna koegzystencja banera ciasteczek
oraz mikrodane EmergencyService JSON-LD.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPETS_DIR = os.path.join(BASE_DIR, "snippets", "squarespace")

COLLECTION_ID = "collection-6a8c91070972152cc2fde180"

# Odczytujemy bazowy CSS Tailwind z szablonu Mokotowa
mokotow_path = os.path.join(SNIPPETS_DIR, "mokotow-page-header-injection.html")
with open(mokotow_path, "r", encoding="utf-8") as f:
    mokotow_raw = f.read()

tw_css_match = re.search(r'(<style id="akumulateo-optimized-tailwind">.*?</style>)', mokotow_raw, re.DOTALL)
if not tw_css_match:
    raise ValueError("Nie znaleziono stylu Tailwind w mokotow-page-header-injection.html")
TAILWIND_STYLE_TAG = tw_css_match.group(1)

HTML_CONTENT = f"""<!-- ========================================================
     AKUMULATEO – AWARYJNE URUCHOMIENIE AUTA WARSZAWA 24/7
     Dedykowany dla: /awaryjne-uruchomienie-auta-warszawa ({COLLECTION_ID})
     Zgodność: Brandbook v2.2, Core Web Vitals, Schema.org EmergencyService
     ======================================================== -->

<!-- 1. SCHEMA.ORG EMERGENCY SERVICE JSON-LD -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "EmergencyService",
  "name": "Akumulateo – Awaryjne Uruchomienie Auta Warszawa 24/7",
  "url": "https://www.akumulateo.pl/awaryjne-uruchomienie-auta-warszawa",
  "telephone": "+48696556446",
  "priceRange": "$$",
  "image": "https://images.squarespace-cdn.com/content/v1/685d174157b18362d5b7b0f3/7c219de6-f0cf-4151-a1a4-eac82a1de5d2/akumulateo-hero-pagespeed.jpg",
  "areaServed": [
    {{
      "@type": "AdministrativeArea",
      "name": "Warszawa"
    }},
    {{
      "@type": "AdministrativeArea",
      "name": "Aglomeracja Warszawska"
    }}
  ],
  "description": "Auto nie odpala? Całodobowe awaryjne uruchamianie auta w Warszawie i okolicach. Dojazd w 20-30 min, bezpieczny rozruch boosterem 12V/24V ze stabilizacją napięcia, diagnostyka alternatora pod obciążeniem oraz opcja natychmiastowej wymiany baterii pod domem. Zadzwoń: 696 556 446!",
  "openingHoursSpecification": {{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ],
    "opens": "00:00",
    "closes": "23:59"
  }},
  "aggregateRating": {{
    "@type": "AggregateRating",
    "ratingValue": "5.0",
    "bestRating": "5.0",
    "worstRating": "1.0",
    "ratingCount": "160",
    "reviewCount": "160"
  }}
}}
</script>

<!-- 2. ZOPTYMALIZOWANY WEWNĘTRZNY TAILWIND CSS -->
{TAILWIND_STYLE_TAG}

<!-- 3. STYLE IZOLUJĄCE I UKRYWAJĄCE SZABLON SQUARESPACE -->
<style id="akumulateo-awaryjne-custom-styles">
#{COLLECTION_ID} {{
  background-color: #020617 !important;
}}

#{COLLECTION_ID} #header,
#{COLLECTION_ID} footer.sections,
#{COLLECTION_ID} #footer-sections,
#{COLLECTION_ID} section[data-section-id="6a8c912f5849182127a62d59"],
#{COLLECTION_ID} section[data-section-id="6aa6dea4020991289c72c2d9"],
#{COLLECTION_ID} section[data-section-id="685d17bd78d1f26a9c224ebe"],
#{COLLECTION_ID} main > article > section,
#{COLLECTION_ID} #sections > section:not(#akumulateo-awaryjne-wrapper section) {{
  display: none !important;
}}

#{COLLECTION_ID} #siteWrapper {{
  min-height: 0 !important;
  height: auto !important;
  padding: 0 !important;
  margin: 0 !important;
  background-color: #020617 !important;
}}

#{COLLECTION_ID} #page,
#{COLLECTION_ID} #page-regions,
#{COLLECTION_ID} section.region,
#{COLLECTION_ID} main#page {{
  padding: 0 !important;
  margin: 0 !important;
}}

@keyframes akumulateo-pulse {{
  0% {{ transform: scale(0.95); opacity: 0.85; }}
  50% {{ transform: scale(1.15); opacity: 1; }}
  100% {{ transform: scale(0.95); opacity: 0.85; }}
}}
.akumulateo-pulse-dot {{
  animation: akumulateo-pulse 2s infinite ease-in-out;
}}

/* Mobilny Przycisk Menu – Kompaktowy Budżet <= 320px */
.ak-mobile-menu-btn {{
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 2px !important;
  background-color: #1e293b !important;
  border: 2px solid #f59e0b !important;
  border-radius: 8px !important;
  padding: 3px 5px !important;
  min-height: 28px !important;
  color: #fbbf24 !important;
  cursor: pointer !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4), 0 0 6px rgba(245, 158, 11, 0.25) !important;
  transition: all 0.15s ease !important;
  user-select: none !important;
  flex-shrink: 0 !important;
  -webkit-tap-highlight-color: transparent !important;
}}

@media (min-width: 640px) {{
  .ak-mobile-menu-btn {{
    gap: 5px !important;
    border-radius: 12px !important;
    padding: 6px 10px !important;
    min-height: 38px !important;
  }}
}}

@media (min-width: 1024px) {{
  .ak-mobile-menu-btn {{
    display: none !important;
  }}
}}

/* Przycisk telefonu w nagłówku – gwarancja budżetu na 320px */
.ak-header-phone-btn {{
  font-size: 11px !important;
  padding: 4px 6px !important;
  line-height: 1 !important;
}}
@media (min-width: 640px) {{
  .ak-header-phone-btn {{
    font-size: 14px !important;
    padding: 8px 12px !important;
  }}
}}

.ak-mobile-menu-btn:hover,
.ak-mobile-menu-btn:focus-visible {{
  background-color: #334155 !important;
  border-color: #fbbf24 !important;
  box-shadow: 0 4px 16px rgba(245, 158, 11, 0.4) !important;
}}

.ak-mobile-menu-btn:active {{
  transform: scale(0.96) !important;
}}

.ak-mobile-menu-btn .ak-menu-text {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  font-size: 9.5px !important;
  font-weight: 900 !important;
  letter-spacing: 0.05em !important;
  text-transform: uppercase !important;
  color: #fbbf24 !important;
  line-height: 1 !important;
}}

@media (min-width: 640px) {{
  .ak-mobile-menu-btn .ak-menu-text {{
    font-size: 11px !important;
    letter-spacing: 0.08em !important;
  }}
}}

.ak-mobile-menu-btn svg {{
  width: 13px !important;
  height: 13px !important;
  stroke: #fbbf24 !important;
  stroke-width: 2.5px !important;
  display: block !important;
  flex-shrink: 0 !important;
}}

@media (min-width: 640px) {{
  .ak-mobile-menu-btn svg {{
    width: 17px !important;
    height: 17px !important;
  }}
}}

/* Koegzystencja banera ciasteczek Squarespace */
.gdpr-cookie-banner, .cookie-banner-mount-point, .sqs-cookie-banner-v2 {{
  z-index: 10000005 !important;
}}

body:has(.gdpr-cookie-banner) #akumulateo-sticky-call-bar,
body:has(.sqs-cookie-banner-v2) #akumulateo-sticky-call-bar,
body:has(.cookie-banner-mount-point:not(:empty)) #akumulateo-sticky-call-bar {{
  display: none !important;
}}

/* FAQ Accordion Styling */
details.ak-faq-item summary::-webkit-details-marker {{
  display: none;
}}
details.ak-faq-item[open] summary svg {{
  transform: rotate(180deg);
}}
details.ak-faq-item summary svg {{
  transition: transform 0.2s ease-in-out;
}}
</style>

<!-- 4. TEMPLATE AWARYJNEGO URUCHOMIENIA -->
<template id="akumulateo-awaryjne-template">

<div class="akumulateo-root bg-slate-950 text-slate-100 font-sans antialiased overflow-hidden">
  
  <!-- 1. PASEK AWARYJNY DYŻURU (TOP NOTIFICATION BAR) -->
  <div class="bg-gradient-to-r from-amber-500 via-amber-400 to-amber-500 text-slate-950 px-2 sm:px-4 py-1.5 sm:py-2 text-[11px] sm:text-xs font-black tracking-wide">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-x-2 gap-y-1">
      <div class="flex items-center gap-1.5 flex-shrink-0">
        <span class="w-2 h-2 rounded-full bg-slate-950 akumulateo-pulse-dot flex-shrink-0"></span>
        <span class="uppercase font-black tracking-wider">Dyżur Pogotowia 24h/7</span>
        <span class="hidden sm:inline font-bold text-slate-900">• Dojazd 20–30 min w Warszawie i aglomeracji</span>
      </div>
      <div class="flex items-center gap-2 flex-shrink-0 text-[11px] font-bold">
        <span class="hidden md:inline-flex items-center gap-1 font-extrabold text-slate-950 bg-amber-300/90 px-1.5 py-0.5 rounded text-[10px]" title="We speak English – call us directly">🇬🇧 We speak English</span>
        <a href="https://g.page/r/CXjN9llopHR_EBM/" target="_blank" rel="noopener noreferrer" class="hover:text-slate-800 hover:underline flex items-center gap-1 transition cursor-pointer" title="Zobacz opinie Akumulateo w Google Maps">
          <span>⭐ <span>5.0</span> w Google (160+ opinii) ↗</span>
        </a>
      </div>
    </div>
  </div>

  <!-- 2. PASEK NAWIGACJI (STICKY HEADER - BUDŻET <= 320px) -->
  <header class="bg-slate-900/95 backdrop-filter backdrop-blur-md sticky top-0 z-40 border-b border-slate-800 px-1.5 sm:px-4 py-1.5 sm:py-3">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-1 sm:gap-3">
      
      <!-- LOGO: ZAWSZE KLIKALNY LINK NA STRONĘ GŁÓWNĄ -->
      <a href="/" class="flex items-center gap-1 sm:gap-2 group text-decoration-none min-w-0 cursor-pointer flex-shrink-0" aria-label="Akumulateo – Strona główna">
        <div class="rounded-lg bg-slate-800 border border-slate-700 flex items-center justify-center p-0.5 sm:p-1 shadow-md group-hover:border-amber-500 transition flex-shrink-0" style="width:24px;height:24px;min-width:24px;min-height:24px;">
          <svg viewBox="0 0 68 68" style="width:100%;height:100%;display:block;" fill="none">
            <rect x="14" y="6" width="10" height="7" rx="2" fill="#94A3B8" />
            <rect x="44" y="6" width="10" height="7" rx="2" fill="#EF4444" />
            <rect x="6" y="12" width="56" height="52" rx="10" fill="#0F172A" stroke="#475569" stroke-width="2" />
            <path d="M37 17L22 38h9l-5 19 19-24h-10l7-16z" fill="#F59E0B" />
            <circle cx="53" cy="56" r="3" fill="#10B981" />
          </svg>
        </div>
        <div class="leading-none">
          <div class="text-[13px] sm:text-lg md:text-xl font-black tracking-tight sm:tracking-wider text-white whitespace-nowrap">
            AKUMULAT<span class="text-amber-500">E</span>O
          </div>
          <div class="hidden sm:flex text-[8px] sm:text-[9px] font-black uppercase tracking-[0.16em] text-slate-400 mt-0.5 items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
            Pogotowie 24h
          </div>
        </div>
      </a>

      <!-- MENU DESKTOP -->
      <nav class="hidden lg:flex items-center gap-6 text-sm font-semibold text-slate-300">
        <a href="/#uslugi" class="hover:text-amber-400 transition font-bold">Usługi mobilne</a>
        <a href="/awaryjne-uruchomienie-auta-warszawa" class="text-amber-400 font-bold">Awaryjny rozruch</a>
        <a href="/wymiana-akumulatora-warszawa-mokotow" class="hover:text-amber-400 transition font-bold">Wymiana akumulatora</a>
        <a href="/#cennik" class="hover:text-amber-400 transition font-bold">Cennik</a>
        <a href="/obszar-dzialania-warszawa-i-okolice" class="hover:text-amber-400 transition font-bold">Warszawa & Aglomeracja</a>
        <a href="/#faq" class="hover:text-amber-400 transition font-bold">FAQ</a>
      </nav>

      <!-- PRAWA STRONA: PRZYCISK TELEFONU + MENU MOBILNE -->
      <div class="flex items-center gap-1 sm:gap-2 flex-shrink-0">
        <a href="tel:+48696556446" class="ak-header-phone-btn flex items-center gap-1 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black rounded-lg sm:rounded-xl shadow-md transition transform active:scale-95 whitespace-nowrap">
          <span class="text-xs">📞</span>
          <span class="tracking-tight sm:tracking-wide font-black">696 556 446</span>
        </a>
        <button id="akAwaryjneMenuBtn" onclick="var m=document.getElementById('akAwaryjneMobileDrawer');if(m){{var isHidden=m.classList.toggle('hidden');this.setAttribute('aria-expanded',!isHidden);var icon=this.querySelector('.ak-menu-icon');var closeIcon=this.querySelector('.ak-close-icon');var label=this.querySelector('.ak-menu-text');if(icon&&closeIcon){{icon.classList.toggle('hidden',!isHidden);closeIcon.classList.toggle('hidden',isHidden);}}if(label){{label.textContent=isHidden?'MENU':'ZAMKNIJ';}}}}" aria-label="Menu nawigacji" aria-expanded="false" class="ak-mobile-menu-btn lg:hidden">
          <span class="ak-menu-icon flex items-center">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"></path></svg>
          </span>
          <span class="ak-close-icon hidden flex items-center">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"></path></svg>
          </span>
          <span class="ak-menu-text">MENU</span>
        </button>
      </div>

    </div>
  </header>

  <!-- MOBILNE MENU ROZWIJANE (DRAWER) -->
  <div id="akAwaryjneMobileDrawer" class="hidden lg:hidden bg-slate-900 border-b border-slate-800 px-4 py-4 space-y-3 text-slate-200 text-sm font-bold shadow-2xl">
    <a href="/#uslugi" class="block py-2 px-3 rounded-lg hover:bg-slate-800 transition">Usługi mobilne 24h</a>
    <a href="/awaryjne-uruchomienie-auta-warszawa" class="block py-2 px-3 rounded-lg bg-amber-500/10 text-amber-400 font-extrabold transition">Awaryjne uruchomienie 24h</a>
    <a href="/wymiana-akumulatora-warszawa-mokotow" class="block py-2 px-3 rounded-lg hover:bg-slate-800 transition">Wymiana akumulatora z dojazdem</a>
    <a href="/#cennik" class="block py-2 px-3 rounded-lg hover:bg-slate-800 transition">Cennik interwencji</a>
    <a href="/obszar-dzialania-warszawa-i-okolice" class="block py-2 px-3 rounded-lg hover:bg-slate-800 transition">Obszar działania (18 dzielnic & miasta)</a>
    <a href="/#faq" class="block py-2 px-3 rounded-lg hover:bg-slate-800 transition">Częste pytania (FAQ)</a>
    <div class="pt-2">
      <a href="tel:+48696556446" class="flex items-center justify-center gap-2 bg-amber-500 text-slate-950 font-black py-3 rounded-xl text-center shadow-lg">
        <span>📞 Zadzwoń: 696 556 446</span>
      </a>
    </div>
  </div>

  <!-- 3. HERO SECTION DLA AWARYJNEGO URUCHOMIENIA -->
  <section class="relative pt-6 sm:pt-12 pb-10 sm:pb-16 px-4 sm:px-6 max-w-7xl mx-auto">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-10 items-center">
      
      <!-- LEWA KOLUMNA: COPY PERSWAZYJNE -->
      <div class="lg:col-span-7 space-y-4 sm:space-y-6">
        
        <!-- PIGUŁKA STATUSOWA -->
        <div class="inline-flex items-center gap-2 bg-slate-900 border border-amber-500/30 px-3 py-1 rounded-full text-xs font-bold text-amber-400 shadow-sm">
          <span class="w-2 h-2 rounded-full bg-emerald-400 akumulateo-pulse-dot"></span>
          <span>Warszawa i Aglomeracja • Dojazd w 20–30 minut</span>
        </div>

        <h1 class="text-xl sm:text-4xl lg:text-5xl font-black text-white tracking-tight leading-tight">
          Awaryjne Uruchomienie Auta <span class="text-transparent bg-clip-text bg-gradient-to-r from-amber-400 to-amber-500">Warszawa 24h/7</span>
        </h1>

        <p class="text-slate-300 text-[15.5px] sm:text-lg leading-relaxed font-normal">
          Rozładowany akumulator pod blokiem, na parkingu podziemnym lub w trasie? Nie ryzykuj spalenia komputera pokładowego tanimi kablami od sąsiada. Dojeżdżamy profesjonalnym sprzętem rozruchowym ze stabilizacją napięcia (Anti-Spike), bezpiecznym dla silników benzynowych, diesla oraz hybryd.
        </p>

        <!-- PIGUŁKI ZAUFANIA -->
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5 pt-1 text-xs">
          <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 flex items-center gap-2 text-slate-200">
            <span class="text-amber-400 text-base">⏱️</span>
            <div><strong class="block text-white">20–30 min</strong>Średni czas dojazdu</div>
          </div>
          <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 flex items-center gap-2 text-slate-200">
            <span class="text-amber-400 text-base">🛡️</span>
            <div><strong class="block text-white">Ochrona ECU</strong>Bezpieczny booster</div>
          </div>
          <div class="col-span-2 sm:col-span-1 bg-slate-900/90 border border-slate-800 rounded-xl p-2.5 flex items-center gap-2 text-slate-200">
            <span class="text-amber-400 text-base">🅿️</span>
            <div><strong class="block text-white">Garaże -1/-2</strong>Wjazd pod ziemię</div>
          </div>
        </div>

        <!-- PRZYCISKI CTA -->
        <div class="flex flex-col sm:flex-row gap-3 pt-2">
          <a href="tel:+48696556446" class="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black text-base px-6 py-3.5 rounded-xl shadow-xl shadow-amber-500/25 active:scale-95 transition">
            <span>📞 Wezwij Pomoc: 696 556 446</span>
          </a>
          <a href="#dlaczego-booster" class="inline-flex items-center justify-center gap-2 bg-slate-800 hover:bg-slate-700 text-white font-bold text-sm px-5 py-3.5 rounded-xl border border-slate-700 transition">
            <span>⚡ Dlaczego profesjonalny booster?</span>
          </a>
        </div>

        <!-- OCENA GOOGLE -->
        <div class="flex items-center gap-3 pt-1 text-xs text-slate-400">
          <div class="flex text-amber-400 text-sm">★★★★★</div>
          <span class="font-bold text-slate-200">5.0 / 5.0 w Google Maps</span>
          <span>•</span>
          <span>Ponad 160 zweryfikowanych opinii</span>
        </div>

      </div>

      <!-- PRAWA KOLUMNA: WIZYTÓWKA DYŻURU I GWARANCJI -->
      <div class="lg:col-span-5 bg-gradient-to-b from-slate-900 to-slate-950 border border-slate-800 rounded-2xl p-5 sm:p-6 shadow-2xl relative">
        <div class="absolute -top-3 right-4 bg-amber-500 text-slate-950 text-[10px] font-black uppercase px-3 py-1 rounded-full shadow-md">
          Dyżur Całodobowy
        </div>

        <h3 class="text-lg font-bold text-white mb-3 flex items-center gap-2">
          <span>🚨</span> Pogotowie Rozruchowe 24/7
        </h3>

        <div class="space-y-3 text-xs text-slate-300">
          <div class="flex items-start gap-2.5 p-2.5 rounded-xl bg-slate-800/60 border border-slate-800">
            <span class="text-emerald-400 text-sm font-bold">✓</span>
            <div>
              <strong class="text-white block">Bezpieczeństwo elektroniki pokładowej</strong>
              Stabilizowany prąd rozruchowy bez niebezpiecznych skoków napięcia palących moduły BCM/ECU.
            </div>
          </div>

          <div class="flex items-start gap-2.5 p-2.5 rounded-xl bg-slate-800/60 border border-slate-800">
            <span class="text-emerald-400 text-sm font-bold">✓</span>
            <div>
              <strong class="text-white block">Cyfrowy test alternatora w cenie</strong>
              Po uruchomieniu silnika mierzymy napięcie ładowania pod obciążeniem (światła, dmuchawa).
            </div>
          </div>

          <div class="flex items-start gap-2.5 p-2.5 rounded-xl bg-slate-800/60 border border-slate-800">
            <span class="text-amber-400 text-sm font-bold">★</span>
            <div>
              <strong class="text-amber-400 block">Plan Awaryjny: Nowa bateria w busie</strong>
              Jeśli akumulator ma zwarcie cel lub jest zużyty – montujemy nową baterię (Varta, Yuasa, Bosch) na miejscu, a koszt rozruchu odliczamy!
            </div>
          </div>
        </div>

        <div class="mt-5 pt-4 border-t border-slate-800/80 flex items-center justify-between">
          <div>
            <div class="text-[11px] text-slate-400">Numer alarmowy dyspozytora:</div>
            <div class="text-base font-black text-amber-400">696 556 446</div>
          </div>
          <a href="tel:+48696556446" class="bg-amber-500 hover:bg-amber-400 text-slate-950 font-black px-4 py-2 rounded-xl text-xs transition">
            Zadzwoń ➔
          </a>
        </div>
      </div>

    </div>
  </section>

  <!-- 4. SEKCJA: DLACZEGO PROFESJONALNY BOOSTER ZAMIAST KABLI? -->
  <section id="dlaczego-booster" class="py-12 px-4 sm:px-6 max-w-7xl mx-auto border-t border-slate-900">
    <div class="text-center max-w-3xl mx-auto mb-10">
      <h2 class="text-xl sm:text-3xl font-black text-white tracking-tight mb-3">
        Dlaczego profesjonalny booster, a nie przypadkowe kable od sąsiada?
      </h2>
      <p class="text-slate-400 text-sm sm:text-base">
        Współczesne samochody wyposażone w magistrale CAN i wrażliwą elektronikę wymagają ochrony przed impulsami przepięciowymi. Sprawdź, dlaczego warto wezwać specjalistów.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      
      <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 relative">
        <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-400 flex items-center justify-center text-xl mb-4">
          🛡️
        </div>
        <h3 class="text-base font-bold text-white mb-2">Zabezpieczenie Anti-Spike</h3>
        <p class="text-slate-300 text-sm leading-relaxed">
          Tanie kable marketowe przy odpinaniu generują szpilki napięciowe (voltage spikes) sięgające kilkudziesięciu woltów. Nasze akumulatorowe stacje rozruchowe posiadają wbudowane tłumiki przepięć, chroniąc sterownik silnika i moduły komfortu.
        </p>
      </div>

      <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 relative">
        <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-400 flex items-center justify-center text-xl mb-4">
          🅿️
        </div>
        <h3 class="text-base font-bold text-white mb-2">Wjazd do garaży podziemnych</h3>
        <p class="text-slate-300 text-sm leading-relaxed">
          Auto stoi przodem do ściany na poziomie -2 i żaden samochód nie jest w stanie podjechać przodem? Nasz technik przemieszcza się pieszo z mobilnym boosterem o prądzie udarowym do 3000A, uruchamiając pojazd w każdym ciasnym miejscu.
        </p>
      </div>

      <div class="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 relative">
        <div class="w-10 h-10 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-400 flex items-center justify-center text-xl mb-4">
          ⚡
        </div>
        <h3 class="text-base font-bold text-white mb-2">Test ładowania alternatora</h3>
        <p class="text-slate-300 text-sm leading-relaxed">
          Sam rozruch to dopiero połowa sukcesu. Technik bada cyfrowym multimetrem i testerem oporowym, czy alternator podaje prawidłowe napięcie pod obciążeniem oraz czy akumulator nadaje się do dalszej eksploatacji.
        </p>
      </div>

    </div>
  </section>

  <!-- 5. SEKCJA: 4 KROKI RATUNKOWE (JAK POMAGAMY) -->
  <section class="py-12 px-4 sm:px-6 max-w-7xl mx-auto border-t border-slate-900">
    <div class="text-center max-w-2xl mx-auto mb-10">
      <span class="text-amber-400 text-xs font-bold uppercase tracking-wider">Szybka Procedura</span>
      <h2 class="text-xl sm:text-3xl font-black text-white tracking-tight mt-1">
        Jak wygląda awaryjne uruchomienie w 4 krokach?
      </h2>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
      
      <div class="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-5 relative">
        <span class="text-amber-500 font-black text-2xl mb-2 block">01</span>
        <h3 class="text-base font-bold text-white mb-1.5">Kontakt i lokalizacja</h3>
        <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
          Dzwonisz pod numer 696 556 446. Podajesz dzielnicę lub miejscowość, markę i model pojazdu oraz okoliczności awarii.
        </p>
      </div>

      <div class="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-5 relative">
        <span class="text-amber-500 font-black text-2xl mb-2 block">02</span>
        <h3 class="text-base font-bold text-white mb-1.5">Dojazd w 20–30 min</h3>
        <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
          Dyspozytor od razu potwierdza czas dotarcia technika oraz przejrzysty koszt usługi. Żadnych niespodzianek na miejscu.
        </p>
      </div>

      <div class="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-5 relative">
        <span class="text-amber-500 font-black text-2xl mb-2 block">03</span>
        <h3 class="text-base font-bold text-white mb-1.5">Bezpieczny rozruch</h3>
        <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
          Technik podłącza stację rozruchową 12V/24V, weryfikuje biegunowość i bezpiecznie uruchamia silnik.
        </p>
      </div>

      <div class="bg-slate-900/60 border border-slate-800/80 rounded-2xl p-5 relative">
        <span class="text-amber-500 font-black text-2xl mb-2 block">04</span>
        <h3 class="text-base font-bold text-white mb-1.5">Pomiar i rekomendacje</h3>
        <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
          Testujemy alternator i kondycję baterii. Wiesz dokładnie, czy możesz bezpiecznie kontynuować podróż.
        </p>
      </div>

    </div>
  </section>

  <!-- 6. SEKCJA: CO JEŚLI SAM ROZRUCH NIE POMÓŻE? (UPSELL & UNIT ECONOMICS) -->
  <section class="py-10 px-4 sm:px-6 max-w-7xl mx-auto">
    <div class="bg-gradient-to-r from-amber-500/10 via-slate-900 to-slate-900 border-2 border-amber-500/40 rounded-2xl p-6 sm:p-8">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
        
        <div class="lg:col-span-8 space-y-3">
          <div class="inline-flex items-center gap-2 bg-amber-500 text-slate-950 text-xs font-black uppercase px-3 py-1 rounded-full">
            Plan Awaryjny Akumulateo
          </div>
          <h2 class="text-xl sm:text-3xl font-black text-white tracking-tight">
            Sam rozruch nie zawsze rozwiązuje problem. Co jeśli bateria jest martwa?
          </h2>
          <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
            Jeżeli akumulator ma wewnętrzne zwarcie w celi lub jest trwale zasiarczony, samochód zgaśnie na najbliższym skrzyżowaniu lub nie odpali pod biurem. Technik Akumulateo zawsze posiada w samochodzie serwisowym <strong>nowe, markowe akumulatory (Varta, Yuasa, Bosch, 4Max)</strong> dobrane pod Twój model.
          </p>
          <div class="bg-slate-950/60 border border-amber-500/20 rounded-xl p-3.5 text-xs sm:text-sm text-amber-300 font-medium">
            💡 <strong>Gwarancja Uczciwości:</strong> Jeśli po diagnozie zdecydujesz się na montaż nowego akumulatora na miejscu, <strong>anulujemy opłatę za awaryjny rozruch</strong>. Płacisz wyłącznie za nową baterię i usługę montażu z kodowaniem BMS!
          </div>
        </div>

        <div class="lg:col-span-4 flex flex-col gap-3 text-center sm:text-left">
          <div class="bg-slate-950/80 border border-slate-800 rounded-xl p-4">
            <div class="text-xs text-slate-400">Oficjalny asortyment w busie:</div>
            <div class="font-bold text-white text-sm mt-1">Yuasa • Varta • Bosch • 4Max</div>
            <div class="text-[11px] text-emerald-400 font-semibold mt-1">AGM, EFB, Standard • 24 mies. gwarancji</div>
          </div>
          <a href="tel:+48696556446" class="inline-flex items-center justify-center gap-2 bg-amber-500 hover:bg-amber-400 text-slate-950 font-black px-6 py-3.5 rounded-xl shadow-lg text-sm transition">
            <span>📞 Zadzwoń: 696 556 446</span>
          </a>
        </div>

      </div>
    </div>
  </section>

  <!-- 7. SEKCJA: CENNIK I PAKIETY USŁUG -->
  <section id="cennik" class="py-12 px-4 sm:px-6 max-w-7xl mx-auto border-t border-slate-900">
    <div class="text-center max-w-2xl mx-auto mb-10">
      <span class="text-amber-400 text-xs font-bold uppercase tracking-wider">Przejrzyste Warunki</span>
      <h2 class="text-xl sm:text-3xl font-black text-white tracking-tight mt-1">
        Cennik awaryjnego uruchomienia w Warszawie
      </h2>
      <p class="text-slate-400 text-xs sm:text-sm mt-2">
        Brak ukrytych kosztów. Cenę potwierdzamy telefonicznie przed wyruszeniem technika.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 items-stretch">
      
      <!-- PAKIET 1: STANDARD -->
      <div class="bg-slate-900/70 border border-slate-800 rounded-2xl p-6 flex flex-col justify-between">
        <div>
          <div class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">Pakiet Podstawowy</div>
          <h3 class="text-lg font-bold text-white mb-2">Awaryjny Rozruch 24h</h3>
          <div class="text-2xl font-black text-amber-400 mb-4">od 180 zł</div>
          <ul class="space-y-2.5 text-xs sm:text-sm text-slate-300">
            <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> Dojazd technika w 20–30 min</li>
            <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> Podłączenie stacji rozruchowej 12V/24V</li>
            <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> Bezpieczny rozruch ze stabilizacją</li>
            <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> Podstawowa kontrola ładowania</li>
          </ul>
        </div>
        <div class="mt-6 pt-4 border-t border-slate-800">
          <a href="tel:+48696556446" class="block w-full bg-slate-800 hover:bg-slate-700 text-white font-bold py-2.5 rounded-xl text-center text-xs transition">
            Zamów rozruch ➔
          </a>
        </div>
      </div>

      <!-- PAKIET 2: WYRÓŻNIONY (NAJCZĘŚCIEJ WYBIERANY) -->
      <div class="bg-gradient-to-b from-slate-900 to-slate-950 border-2 border-amber-500 rounded-2xl p-6 flex flex-col justify-between shadow-xl shadow-amber-500/10 relative">
        <div class="absolute -top-3 left-1/2 -translate-x-1/2 bg-amber-500 text-slate-950 font-black text-xs uppercase px-3.5 py-1 rounded-full shadow-md whitespace-nowrap">
          Najczęściej Wybierany
        </div>
        <div>
          <div class="text-xs font-bold text-amber-400 uppercase tracking-wider mb-2 pt-1">Pakiet Bezpieczeństwo</div>
          <h3 class="text-lg font-bold text-white mb-2">Rozruch + Pełna Diagnostyka</h3>
          <div class="text-2xl font-black text-amber-400 mb-4">od 220 zł</div>
          <ul class="space-y-2.5 text-xs sm:text-sm text-slate-200">
            <li class="flex items-center gap-2"><span class="text-amber-400">★</span> <strong>Wszystko z pakietu podstawowego</strong></li>
            <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> Pomiar sprawności akumulatora pod obciążeniem</li>
            <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> Badanie prądu upływu na postoju (czy coś kradnie prąd)</li>
            <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> Test diod i regulatora alternatora</li>
            <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> Rekomendacja dalszej eksploatacji</li>
          </ul>
        </div>
        <div class="mt-6 pt-4 border-t border-slate-800">
          <a href="tel:+48696556446" class="block w-full bg-amber-500 hover:bg-amber-400 text-slate-950 font-black py-3 rounded-xl text-center text-sm shadow-md transition">
            Wybierz Pakiet Diagnostyka ➔
          </a>
        </div>
      </div>

      <!-- PAKIET 3: WYMIANA Z DOSTAWĄ -->
      <div class="bg-slate-900/70 border border-slate-800 rounded-2xl p-6 flex flex-col justify-between">
        <div>
          <div class="text-xs font-bold text-slate-400 uppercase tracking-wider mb-2">Pełne Rozwiązanie</div>
          <h3 class="text-lg font-bold text-white mb-2">Rozruch z Wymianą Baterii</h3>
          <div class="text-2xl font-black text-amber-400 mb-4">Cena baterii + montaż</div>
          <ul class="space-y-2.5 text-xs sm:text-sm text-slate-300">
            <li class="flex items-center gap-2"><span class="text-amber-400 font-bold">GRATIS</span> Rozruch odliczony od usługi</li>
            <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> Nowy akumulator Varta / Yuasa / Bosch</li>
            <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> Montaż z podtrzymaniem napięcia sterowników</li>
            <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> Kodowanie BMS / adaptacja Start-Stop</li>
            <li class="flex items-center gap-2"><span class="text-emerald-400">✓</span> Darmowy recykling starej baterii</li>
          </ul>
        </div>
        <div class="mt-6 pt-4 border-t border-slate-800">
          <a href="tel:+48696556446" class="block w-full bg-slate-800 hover:bg-slate-700 text-white font-bold py-2.5 rounded-xl text-center text-xs transition">
            Wymień na miejscu ➔
          </a>
        </div>
      </div>

    </div>
  </section>

  <!-- 8. SEKCJA: NAJCZĘSTSZE PYTANIA (FAQ ACCORDION) -->
  <section id="faq" class="py-12 px-4 sm:px-6 max-w-4xl mx-auto border-t border-slate-900">
    <div class="text-center mb-10">
      <span class="text-amber-400 text-xs font-bold uppercase tracking-wider">Baza Wiedzy</span>
      <h2 class="text-xl sm:text-3xl font-black text-white tracking-tight mt-1">
        Najczęstsze pytania przed wezwaniem pomocy
      </h2>
    </div>

    <div class="space-y-3">
      
      <details class="ak-faq-item bg-slate-900/80 border border-slate-800 rounded-xl p-4 cursor-pointer group">
        <summary class="font-bold text-white text-sm sm:text-base flex items-center justify-between gap-3 list-none">
          <span>Czy awaryjny rozruch boosterem jest bezpieczny dla elektroniki mojego auta?</span>
          <svg class="w-5 h-5 text-amber-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
          </svg>
        </summary>
        <div class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed pt-2 border-t border-slate-800/60">
          Tak, w 100%. Używamy profesjonalnych stacji rozruchowych z filtrami przeciwprzepięciowymi, które całkowicie eliminują skoki napięcia mogące uszkodzić komputer pokładowy (ECU), moduł komfortu czy systemy multimedialne. Jest to metoda o wiele bezpieczniejsza niż tradycyjne odpalanie na kable od innego samochodu.
        </div>
      </details>

      <details class="ak-faq-item bg-slate-900/80 border border-slate-800 rounded-xl p-4 cursor-pointer group">
        <summary class="font-bold text-white text-sm sm:text-base flex items-center justify-between gap-3 list-none">
          <span>Co jeśli auto nie odpali mimo podłączenia boostera?</span>
          <svg class="w-5 h-5 text-amber-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
          </svg>
        </summary>
        <div class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed pt-2 border-t border-slate-800/60">
          Brak reakcji na podanie zasilania rozruchowego może świadczyć o uszkodzeniu rozrusznika, braku masy, usterce immobilizera lub braku paliwa. Na miejscu sprawdzimy podstawowe parametry elektryczne i wskażemy przyczynę problemu, abyś wiedział, jakie kroki należy podjąć.
        </div>
      </details>

      <details class="ak-faq-item bg-slate-900/80 border border-slate-800 rounded-xl p-4 cursor-pointer group">
        <summary class="font-bold text-white text-sm sm:text-base flex items-center justify-between gap-3 list-none">
          <span>Czy dojedziecie do garażu podziemnego o niskim stropie?</span>
          <svg class="w-5 h-5 text-amber-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
          </svg>
        </summary>
        <div class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed pt-2 border-t border-slate-800/60">
          Tak! Nasz sprzęt jest w pełni przenośny. Technik może zjechać windą lub wejść pieszo na poziomy -1, -2 czy -3 z kompaktową walizką rozruchową o ogromnej mocy. Nie ma potrzeby wjeżdżania drugim pojazdem ani wypychania auta na zewnątrz.
        </div>
      </details>

      <details class="ak-faq-item bg-slate-900/80 border border-slate-800 rounded-xl p-4 cursor-pointer group">
        <summary class="font-bold text-white text-sm sm:text-base flex items-center justify-between gap-3 list-none">
          <span>Jak długo powinienem jeździć po awaryjnym odpaleniu, aby naładować akumulator?</span>
          <svg class="w-5 h-5 text-amber-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
          </svg>
        </summary>
        <div class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed pt-2 border-t border-slate-800/60">
          Zalecamy ciągłą jazdę przez minimum 30–45 minut ze średnimi obrotami silnika (najlepiej trasą szybkiego ruchu). Postój na biegu jałowym dostarcza niewielki prąd ładowania i przy włączonych światłach czy nawiewie może nie wystarczyć do uzupełnienia energii na kolejny start.
        </div>
      </details>

      <details class="ak-faq-item bg-slate-900/80 border border-slate-800 rounded-xl p-4 cursor-pointer group">
        <summary class="font-bold text-white text-sm sm:text-base flex items-center justify-between gap-3 list-none">
          <span>Czy technik może od razu zamontować nowy akumulator?</span>
          <svg class="w-5 h-5 text-amber-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
          </svg>
        </summary>
        <div class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed pt-2 border-t border-slate-800/60">
          Oczywiście. Samochody serwisowe Akumulateo są mobilnymi punktami serwisowymi – wozimy ze sobą najpopularniejsze modele markowych baterii Yuasa, Varta i Bosch w technologiach AGM, EFB i tradycyjnych kwasowo-ołowiowych. Jeśli zdecydujesz się na wymianę, odliczamy koszt rozruchu!
        </div>
      </details>

      <details class="ak-faq-item bg-slate-900/80 border border-slate-800 rounded-xl p-4 cursor-pointer group">
        <summary class="font-bold text-white text-sm sm:text-base flex items-center justify-between gap-3 list-none">
          <span>Jakie formy płatności są akceptowane na miejscu?</span>
          <svg class="w-5 h-5 text-amber-400 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
          </svg>
        </summary>
        <div class="mt-3 text-xs sm:text-sm text-slate-300 leading-relaxed pt-2 border-t border-slate-800/60">
          Przyjmujemy płatności kartą płatniczą (technik posiada terminal płatniczy), BLIK-iem oraz gotówką. Na życzenie natychmiast wystawiamy fakturę VAT.
        </div>
      </details>

    </div>
  </section>

  <!-- 9. SEKCJA LINKUJĄCA OBSZAR DZIAŁANIA -->
  <section class="py-10 px-4 sm:px-6 max-w-7xl mx-auto border-t border-slate-900 text-center">
    <h3 class="text-lg font-bold text-white mb-2">Obsługiwany obszar – cała Warszawa i aglomeracja</h3>
    <p class="text-slate-400 text-xs sm:text-sm max-w-2xl mx-auto mb-4">
      Dyżurujemy we wszystkich 18 dzielnicach Warszawy oraz okolicznych miastach (m.in. Piaseczno, Pruszków, Otwock, Marki, Legionowo, Łomianki, Grodzisk Mazowiecki).
    </p>
    <a href="/obszar-dzialania-warszawa-i-okolice" class="inline-flex items-center gap-1.5 text-xs text-amber-400 hover:text-amber-300 font-bold underline">
      <span>Zobacz mapę i pełny wykaz 33 lokalizacji</span>
      <span>➔</span>
    </a>
  </section>

  <!-- 10. STOPKA AKUMULATEO -->
  <footer class="bg-slate-900/90 border-t border-slate-800 pt-10 pb-20 sm:pb-12 px-4 sm:px-6">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8 mb-8 text-xs text-slate-300">
      
      <div class="space-y-3">
        <div class="flex items-center gap-2">
          <div class="w-6 h-6 rounded bg-amber-500 flex items-center justify-center font-black text-slate-950 text-xs">⚡</div>
          <span class="font-black text-white text-base tracking-wider">AKUMULATEO</span>
        </div>
        <p class="text-slate-400 leading-relaxed">
          Całodobowe pogotowie akumulatorowe Warszawa i aglomeracja. Awaryjny rozruch 12V/24V, mobilna wymiana akumulatorów, diagnostyka alternatora i kodowanie BMS pod domem klienta.
        </p>
      </div>

      <div class="space-y-2">
        <div class="text-white font-bold mb-3">Usługi Mobilne 24h</div>
        <div><a href="/awaryjne-uruchomienie-auta-warszawa" class="text-amber-400 font-bold hover:underline">Awaryjny rozruch boosterem</a></div>
        <div><a href="/wymiana-akumulatora-warszawa-mokotow" class="hover:text-amber-400 transition">Wymiana akumulatora z dojazdem</a></div>
        <div><a href="/#uslugi" class="hover:text-amber-400 transition">Kodowanie i adaptacja BMS</a></div>
        <div><a href="/#uslugi" class="hover:text-amber-400 transition">Test alternatora i prądu upływu</a></div>
      </div>

      <div class="space-y-2">
        <div class="text-white font-bold mb-3">Oficjalne Marki</div>
        <div><span class="text-slate-300">Akumulatory Yuasa (YBX Series)</span></div>
        <div><span class="text-slate-300">Akumulatory Varta (AGM / EFB)</span></div>
        <div><span class="text-slate-300">Akumulatory Bosch (S4 / S5)</span></div>
        <div><span class="text-slate-300">Akumulatory 4Max & Eco-Force</span></div>
      </div>

      <div class="space-y-3">
        <div class="text-white font-bold mb-2">Telefon Alarmowy 24h</div>
        <a href="tel:+48696556446" class="inline-flex items-center gap-2 bg-amber-500 text-slate-950 font-black px-4 py-2.5 rounded-xl shadow-lg text-sm">
          <span>📞 696 556 446</span>
        </a>
        <div class="text-xs text-slate-400">Dyżur dyspozytora 7 dni w tygodniu 24h</div>
      </div>

    </div>

    <div class="max-w-7xl mx-auto pt-6 border-t border-slate-900 flex flex-col sm:flex-row items-center justify-between gap-3 text-[11px] text-slate-400">
      <div>© 2026 Akumulateo. Wszystkie prawa zastrzeżone. Mobilny serwis akumulatorów.</div>
      <div class="flex items-center gap-4">
        <span class="text-emerald-400 font-semibold">Eko Recykling BDO</span>
        <a href="/" class="hover:text-white transition">Strona Główna</a>
        <a href="/obszar-dzialania-warszawa-i-okolice" class="hover:text-white transition">Obszar Działania</a>
      </div>
    </div>
  </footer>

</div>

</template>

<!-- 5. SKRYPT MONTAŻU I LOGIKI INTERAKTYWNEJ -->
<script>
(function() {{
  function mountAkumulateoAwaryjne() {{
    if (document.getElementById('akumulateo-awaryjne-wrapper')) return true;
    
    var tpl = document.getElementById('akumulateo-awaryjne-template');
    if (!tpl) return false;
    
    var targetSection = document.querySelector('section[data-section-id="6a8c912f5849182127a62d59"]');
    var parent = targetSection ? targetSection.parentNode : 
                 (document.querySelector('#sections') || 
                  document.querySelector('main#page') || 
                  document.querySelector('#page') || 
                  document.body);
    if (!parent) return false;
    
    var wrapper = document.createElement('div');
    wrapper.id = 'akumulateo-awaryjne-wrapper';
    wrapper.appendChild(tpl.content.cloneNode(true));
    
    if (targetSection) {{
      parent.insertBefore(wrapper, targetSection);
    }} else if (parent.firstChild) {{
      parent.insertBefore(wrapper, parent.firstChild);
    }} else {{
      parent.appendChild(wrapper);
    }}

    return true;
  }}

  // Synchronizacja Sticky Call Bar z banerem cookies
  function syncCookieBannerWithStickyBar() {{
    var banner = document.querySelector('.gdpr-cookie-banner, .sqs-cookie-banner-v2, .cookie-banner-mount-point');
    var bar = document.getElementById('akumulateo-sticky-call-bar');
    if (!bar) return;
    var hasBanner = banner && banner.offsetHeight > 0 && window.getComputedStyle(banner).display !== 'none';
    if (hasBanner) {{
      bar.style.setProperty('display', 'none', 'important');
    }} else {{
      bar.style.display = '';
    }}
  }}

  if (!mountAkumulateoAwaryjne()) {{
    if (window.MutationObserver) {{
      var obs = new MutationObserver(function() {{
        if (mountAkumulateoAwaryjne()) {{
          obs.disconnect();
        }}
      }});
      obs.observe(document.documentElement, {{ childList: true, subtree: true }});
    }}
    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', mountAkumulateoAwaryjne);
    }}
    window.addEventListener('load', mountAkumulateoAwaryjne);
  }}

  setInterval(syncCookieBannerWithStickyBar, 300);
}})();
</script>
"""

out_path = os.path.join(SNIPPETS_DIR, "awaryjne-uruchomienie-page-header-injection.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"✅ Zaktualizowano pakiet wstrzyknięcia dla awaryjnego uruchomienia:")
print(f"   Ścieżka: {out_path}")
print(f"   Rozmiar: {len(HTML_CONTENT)} znaków")
