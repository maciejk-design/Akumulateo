#!/usr/bin/env python3
"""
Generator kompletnych, bezbłędnych wstrzyknięć Header Injection dla:
1. /obszar-dzialania-warszawa-i-okolice (collection-6a8c92622180ae5dca0135cf)
2. /wymiana-akumulatora-warszawa-mokotow (collection-6ab4470b50295a294b3a4066)

Wdraża standard Brandbook v2.2:
- Pełny wewnętrzny Tailwind CSS (compiled-tailwind.min.css)
- Ukrycie domyślnego nagłówka i stopki Squarespace (brak kolizji i dublowania)
- Brandowy Sticky Header z Logo i bezpośrednim przyciskiem połączenia 696 556 446
- Wyeliminowanie błędów 404 (kafelki łączą bezpośrednio z telefonem lub aktywnymi podstronami)
- Zaktualizowany czas reakcji 20–30 minut
- Schema.org EmergencyService JSON-LD 5.0★
"""

import os
import json
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "snippets", "squarespace", "compiled-tailwind.min.css"), "r", encoding="utf-8") as f:
    TAILWIND_CSS = f.read().strip()

NAV_HEADER_HTML = """
  <!-- 1. PASEK AWARYJNY DYŻURU (TOP NOTIFICATION BAR) -->
  <div class="bg-gradient-to-r from-amber-500 via-amber-400 to-amber-500 text-slate-950 px-3.5 sm:px-4 py-1.5 sm:py-2 text-[11px] sm:text-xs font-black tracking-wide">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-x-2.5 gap-y-1">
      <div class="flex items-center gap-1.5 flex-shrink-0">
        <span class="w-2 h-2 rounded-full bg-slate-950 akumulateo-pulse-dot flex-shrink-0"></span>
        <span class="uppercase font-black tracking-wider">Dyżur Pogotowia 24h/7</span>
        <span class="hidden sm:inline font-bold text-slate-900">• Dojazd 20–30 min w Warszawie i aglomeracji</span>
      </div>
      <div class="flex items-center gap-2.5 flex-shrink-0 text-[11px] font-bold">
        <span class="hidden md:inline-flex items-center gap-1 font-extrabold text-slate-950 bg-amber-300/90 px-1.5 py-0.5 rounded text-[10px]" title="We speak English – call us directly">🇬🇧 We speak English</span>
        <a href="https://g.page/r/CXjN9llopHR_EBM/" target="_blank" rel="noopener noreferrer" class="hover:text-slate-800 hover:underline flex items-center gap-1 transition cursor-pointer" title="Zobacz opinie Akumulateo w Google Maps">
          <span>⭐ <span data-ak-cfg="ratingValue">5.0</span> w Google (<span data-ak-cfg="reviewsCount">100+</span> opinii) ↗</span>
        </a>
      </div>
    </div>
  </div>

  <!-- 2. PASEK NAWIGACJI (STICKY HEADER) -->
  <header class="bg-slate-900/95 backdrop-filter backdrop-blur-md sticky top-0 z-40 border-b border-slate-800 px-2 sm:px-4 py-2 sm:py-3.5">
    <div class="max-w-7xl mx-auto flex items-center justify-between gap-1 sm:gap-4">
      
      <!-- Logo: zawsze klikalny link na stronę główną -->
      <a href="/" class="flex items-center gap-1.5 sm:gap-2 group text-decoration-none min-w-0 cursor-pointer flex-shrink-0" aria-label="Akumulateo – Strona główna">
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
          <div class="hidden sm:flex text-[8px] sm:text-[9px] font-black uppercase tracking-[0.16em] text-slate-400 mt-0.5 items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
            Pogotowie 24h
          </div>
        </div>
      </a>

      <!-- Menu Desktop -->
      <nav class="hidden lg:flex items-center gap-6 text-sm font-semibold text-slate-300">
        <a href="/#uslugi" class="hover:text-amber-400 transition font-bold">Usługi mobilne</a>
        <a href="/#cennik" class="hover:text-amber-400 transition font-bold">Cennik</a>
        <a href="/#marki" class="hover:text-amber-400 transition font-bold">Oficjalne Marki</a>
        <a href="/obszar-dzialania-warszawa-i-okolice" class="text-amber-400 font-bold">Warszawa & Aglomeracja</a>
        <a href="/#opinie" class="hover:text-amber-400 transition font-bold">Opinie Google</a>
        <a href="/#faq" class="hover:text-amber-400 transition font-bold">FAQ</a>
      </nav>

      <!-- Prawa strona: Telefon & Przycisk Menu -->
      <div class="flex items-center gap-1 sm:gap-2.5 flex-shrink-0">
        <a href="tel:+48696556446" class="flex items-center gap-1 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black px-2 sm:px-3.5 py-1.5 sm:py-2.5 rounded-xl shadow-lg shadow-amber-500/20 transition transform active:scale-95 text-[11px] sm:text-sm whitespace-nowrap">
          <span class="text-xs sm:text-base">📞</span>
          <span class="tracking-tight sm:tracking-wide font-black">696 556 446</span>
        </a>
        <button id="akMobileMenuBtn" onclick="var m=document.getElementById('akSubpageMobileDrawer')||document.getElementById('akMobileDrawer');if(m){var isHidden=m.classList.toggle('hidden');this.setAttribute('aria-expanded',!isHidden);var icon=this.querySelector('.ak-menu-icon');var closeIcon=this.querySelector('.ak-close-icon');var label=this.querySelector('.ak-menu-text');if(icon&&closeIcon){icon.classList.toggle('hidden',!isHidden);closeIcon.classList.toggle('hidden',isHidden);}if(label){label.textContent=isHidden?'MENU':'ZAMKNIJ';}}" aria-label="Menu nawigacji" aria-expanded="false" class="ak-mobile-menu-btn lg:hidden">
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

    <!-- Mobilny Drawer -->
    <div id="akSubpageMobileDrawer" class="hidden pt-4 pb-3 border-t border-slate-800 mt-3 space-y-2">
      <a href="/#uslugi" onclick="var m=document.getElementById('akSubpageMobileDrawer');if(m)m.classList.add('hidden');" class="block px-4 py-3 rounded-xl bg-slate-800/90 font-bold text-slate-100 hover:text-amber-400">⚡ Usługi mobilne</a>
      <a href="/#cennik" onclick="var m=document.getElementById('akSubpageMobileDrawer');if(m)m.classList.add('hidden');" class="block px-4 py-3 rounded-xl bg-slate-800/90 font-bold text-slate-100 hover:text-amber-400">💰 Cennik usług</a>
      <a href="/#marki" onclick="var m=document.getElementById('akSubpageMobileDrawer');if(m)m.classList.add('hidden');" class="block px-4 py-3 rounded-xl bg-slate-800/90 font-bold text-slate-100 hover:text-amber-400">🔋 Oficjalne marki (Varta, Yuasa, Bosch)</a>
      <a href="/obszar-dzialania-warszawa-i-okolice" onclick="var m=document.getElementById('akSubpageMobileDrawer');if(m)m.classList.add('hidden');" class="block px-4 py-3 rounded-xl bg-slate-800/90 font-bold text-amber-400">📍 Obszar działania (Warszawa & Aglomeracja)</a>
      <a href="/#opinie" onclick="var m=document.getElementById('akSubpageMobileDrawer');if(m)m.classList.add('hidden');" class="block px-4 py-3 rounded-xl bg-slate-800/90 font-bold text-slate-100 hover:text-amber-400">⭐ Opinie klientów (5.0 w Google Maps)</a>
      <a href="/#faq" onclick="var m=document.getElementById('akSubpageMobileDrawer');if(m)m.classList.add('hidden');" class="block px-4 py-3 rounded-xl bg-slate-800/90 font-bold text-slate-100 hover:text-amber-400">❓ FAQ – Pytania i Odpowiedzi</a>
      <a href="tel:+48696556446" class="block w-full text-center bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black py-3.5 px-4 rounded-xl text-base shadow-xl mt-2">📞 Zadzwoń: 696 556 446 (Pomoc 24h)</a>
    </div>
  </header>
"""

UNIFIED_FOOTER_HTML = """
  <!-- STOPKA STRONY -->
  <footer class="bg-slate-950 border-t border-slate-800 px-4 py-12 text-slate-300 text-sm">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8 mb-10">
      
      <div class="space-y-3">
        <div class="text-xl font-black text-white">AKUMULAT<span class="text-amber-500">E</span>O</div>
        <p class="text-slate-400 text-xs leading-relaxed">
          Mobilny serwis i pogotowie akumulatorowe 24h na terenie Warszawy oraz aglomeracji podwarszawskiej. Wymiana, diagnostyka i awaryjny rozruch pod domem klienta.
        </p>
        <div class="text-xs text-amber-400 font-bold">⭐ <span data-ak-cfg="ratingValue">5.0</span> w Google (<span data-ak-cfg="reviewsCount">100+</span> recenzji)</div>
      </div>

      <div class="space-y-2">
        <div class="text-white font-bold mb-3">Usługi 24h</div>
        <div><a href="/#uslugi" class="hover:text-amber-400 transition text-xs">Wymiana akumulatora z dojazdem</a></div>
        <div><a href="/#uslugi" class="hover:text-amber-400 transition text-xs">Awaryjny rozruch boosterem 12V/24V</a></div>
        <div><a href="/#uslugi" class="hover:text-amber-400 transition text-xs">Kodowanie i adaptacja BMS Start-Stop</a></div>
        <div><a href="/#uslugi" class="hover:text-amber-400 transition text-xs">Diagnostyka alternatora i upływu prądu</a></div>
      </div>

      <div class="space-y-2">
        <div class="text-white font-bold mb-3">Oficjalne Marki</div>
        <div><a href="/#marki" class="hover:text-amber-400 transition text-xs">Akumulatory Varta (AGM / EFB / Silver)</a></div>
        <div><a href="/#marki" class="hover:text-amber-400 transition text-xs">Akumulatory Yuasa (YBX Series)</a></div>
        <div><a href="/#marki" class="hover:text-amber-400 transition text-xs">Akumulatory Bosch (S4 / S5)</a></div>
        <div><a href="/#marki" class="hover:text-amber-400 transition text-xs">Akumulatory 4Max & Eco-Force</a></div>
      </div>

      <div class="space-y-3">
        <div class="text-white font-bold mb-2">Telefon Alarmowy 24h</div>
        <a href="tel:+48696556446" class="inline-flex items-center gap-2 bg-amber-500 text-slate-950 font-black px-4 py-2.5 rounded-xl shadow-lg text-sm">
          <span>📞 696 556 446</span>
        </a>
        <div class="text-xs text-slate-400">Dyżur dyspozytora 7 dni w tygodniu</div>
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
"""

def build_hub_page_injection():
    import importlib.util
    spec = importlib.util.spec_from_file_location("gen_module", os.path.join(BASE_DIR, "scripts", "generate-all-seo-pages.py"))
    gen_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gen_mod)

    districts = gen_mod.WARSAW_DISTRICTS
    suburbs = gen_mod.AGGLOMERATION_SUBURBS

    area_served_list = [{"@type": "AdministrativeArea", "name": f"{d['name']}, Warszawa"} for d in districts]
    for s in suburbs:
        area_served_list.append({"@type": "AdministrativeArea", "name": s['name']})

    schema = {
        "@context": "https://schema.org",
        "@type": "EmergencyService",
        "name": "Akumulateo – Pogotowie Akumulatorowe Warszawa i Aglomeracja 24h",
        "url": "https://www.akumulateo.pl/obszar-dzialania-warszawa-i-okolice",
        "telephone": "+48696556446",
        "priceRange": "$$",
        "image": "https://images.squarespace-cdn.com/content/v1/685d174157b18362d5b7b0f3/7c219de6-f0cf-4151-a1a4-eac82a1de5d2/akumulateo-hero-pagespeed.jpg",
        "areaServed": area_served_list,
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00",
            "closes": "23:59"
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "5.0",
            "bestRating": "5.0",
            "worstRating": "1.0",
            "ratingCount": "100",
            "reviewCount": "100"
        },
        "description": "Obszar działania mobilnego pogotowia akumulatorowego Akumulateo. Całodobowy dojazd w 20-30 min we wszystkich 18 dzielnicach Warszawy oraz szybki dojazd trasami ekspresowymi do miejscowości aglomeracji podwarszawskiej. Tel: 696 556 446."
    }
    schema_str = json.dumps(schema, ensure_ascii=False, indent=2)

    districts_cards_html = ""
    for d in districts:
        is_mokotow = d['slug'] == 'mokotow'
        more_link_html = f'<a href="/{d["url_slug"]}" class="text-xs text-slate-400 hover:text-amber-400 underline">Szczegóły dojazdu ➔</a>' if is_mokotow else f'<span class="text-[11px] text-emerald-400 font-bold flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span> Dyżur w rejonie</span>'
        
        districts_cards_html += f"""
        <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 flex flex-col justify-between hover:border-amber-500/60 transition shadow-lg group">
          <div>
            <div class="flex items-center justify-between mb-2">
              <span class="text-white font-extrabold text-lg group-hover:text-amber-400 transition">{d['name']}</span>
              <span class="bg-emerald-500/10 text-emerald-400 font-bold text-xs px-2.5 py-1 rounded-full border border-emerald-500/20">{d['eta']}</span>
            </div>
            <p class="text-slate-400 text-xs leading-relaxed mb-4">
              {d['areas'].split(',')[0].strip()}, {d['areas'].split(',')[1].strip() if len(d['areas'].split(',')) > 1 else ''}
            </p>
          </div>
          <div class="space-y-2 pt-2 border-t border-slate-800/80">
            <a href="tel:+48696556446" class="flex items-center justify-center gap-1.5 w-full bg-amber-500/10 hover:bg-amber-500 text-amber-400 hover:text-slate-950 border border-amber-500/30 font-bold text-xs py-2 rounded-xl transition">
              <span>📞 Wezwij: 696 556 446</span>
            </a>
            <div class="text-center">
              {more_link_html}
            </div>
          </div>
        </div>"""

    suburbs_cards_html = ""
    for s in suburbs:
        is_piaseczno = s['slug'] == 'piaseczno'
        first_area = s['areas'].split(',')[0].strip()
        second_area = s['areas'].split(',')[1].strip() if len(s['areas'].split(',')) > 1 else ''
        more_link_html = f'<a href="/{s["url_slug"]}" class="text-xs text-slate-400 hover:text-amber-400 underline">Szczegóły dojazdu ➔</a>' if is_piaseczno else f'<span class="text-[11px] text-emerald-400 font-bold flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span> Trasa ekspresowa</span>'

        suburbs_cards_html += f"""
        <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 flex flex-col justify-between hover:border-amber-500/60 transition shadow-lg group">
          <div>
            <div class="flex items-center justify-between mb-2">
              <span class="text-white font-extrabold text-lg group-hover:text-amber-400 transition">{s['name']}</span>
              <span class="bg-emerald-500/10 text-emerald-400 font-bold text-xs px-2.5 py-1 rounded-full border border-emerald-500/20">{s['eta']}</span>
            </div>
            <p class="text-slate-400 text-xs leading-relaxed mb-4">
              {first_area}{', ' + second_area if second_area else ''}
            </p>
          </div>
          <div class="space-y-2 pt-2 border-t border-slate-800/80">
            <a href="tel:+48696556446" class="flex items-center justify-center gap-1.5 w-full bg-amber-500/10 hover:bg-amber-500 text-amber-400 hover:text-slate-950 border border-amber-500/30 font-bold text-xs py-2 rounded-xl transition">
              <span>📞 Wezwij: 696 556 446</span>
            </a>
            <div class="text-center">
              {more_link_html}
            </div>
          </div>
        </div>"""

    content_html = f"""
<div class="akumulateo-root bg-slate-950 text-slate-100 font-sans antialiased overflow-hidden">
  
  {NAV_HEADER_HTML}

  <!-- SEKCJA GŁÓWNA HERO -->
  <section class="relative px-4 py-12 md:py-16 bg-gradient-to-b from-slate-900 via-slate-900 to-slate-950 border-b border-slate-800 text-center">
    <div class="max-w-4xl mx-auto">
      <div class="inline-flex items-center gap-2 bg-amber-500/10 border border-amber-500/30 text-amber-400 px-3.5 py-1.5 rounded-full text-xs font-black uppercase tracking-wider mb-5">
        <span>⚡ Mobilny Serwis z Dojazdem 24h</span>
      </div>
      <h1 class="text-3xl sm:text-5xl font-black text-white tracking-tight leading-tight mb-5">
        Obszar Działania Pogotowia Akumulatorowego
      </h1>
      <p class="text-slate-300 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed mb-8">
        Całodobowa wymiana akumulatora, awaryjny rozruch 12V/24V i kodowanie BMS z dojazdem pod Twój dom, biuro lub parking. Obsługujemy <strong>wszystkie 18 dzielnic Warszawy</strong> oraz <strong>aglomerację do 40 km</strong>.
      </p>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-3">
        <a href="tel:+48696556446" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black px-6 py-4 rounded-xl shadow-xl shadow-amber-500/25 transition transform active:scale-95 text-base sm:text-lg">
          <span>📞 Zadzwoń: 696 556 446</span>
        </a>
      </div>
      <div class="mt-3 text-xs text-slate-400 font-semibold">
        ⏱️ Średni czas dojazdu w Warszawie: <span class="text-emerald-400 font-bold">20–30 minut</span>
      </div>
    </div>
  </section>

  <!-- BANNER PREKWALIFIKACJI MOBILNEJ -->
  <section class="max-w-7xl mx-auto px-4 py-6">
    <div class="bg-amber-500/10 border border-amber-500/30 rounded-2xl p-5 text-center">
      <div class="text-amber-400 font-black text-xs uppercase tracking-wider mb-2">
        ℹ️ Usługa w 100% Mobilna z Dojazdem pod Auto
      </div>
      <p class="text-slate-200 text-sm sm:text-base leading-relaxed max-w-3xl mx-auto">
        Nie trać czasu na szukanie stacjonarnego sklepu ani holowanie auta. Akumulateo to <strong>mobilne pogotowie techniczne</strong> – nie prowadzimy sklepu stacjonarnego ani punktu odbioru. Serwisant przyjeżdża bezpośrednio pod Twoje auto z fabrycznie nową baterią i montuje ją na miejscu.
      </p>
    </div>
  </section>

  <!-- SEKCJA 1: 18 DZIELNIC WARSZAWY -->
  <section class="max-w-7xl mx-auto px-4 py-8">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-6">
      <div>
        <h2 class="text-2xl sm:text-3xl font-black text-white">Dzielnice Warszawy (18 dzielnic)</h2>
        <p class="text-slate-400 text-sm mt-1">Dojazd pogotowia w <strong>20–30 minut</strong> pod wskazany adres:</p>
      </div>
      <div class="self-start sm:self-auto bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs font-bold px-3 py-1.5 rounded-full">
        18 Dzielnic Stolicy
      </div>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
      {districts_cards_html}
    </div>
  </section>

  <!-- SEKCJA 2: AGLOMERACJA PODWARSZAWSKA -->
  <section class="max-w-7xl mx-auto px-4 py-8">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-6">
      <div>
        <h2 class="text-2xl sm:text-3xl font-black text-white">Miejscowości Aglomeracji</h2>
        <p class="text-slate-400 text-sm mt-1">Szybki dojazd trasami ekspresowymi S2, S7, S8, S17 oraz autostradą A2:</p>
      </div>
      <div class="self-start sm:self-auto bg-amber-500/10 border border-amber-500/30 text-amber-400 text-xs font-bold px-3 py-1.5 rounded-full">
        15 Miejscowości & Okolice
      </div>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
      {suburbs_cards_html}
    </div>
  </section>

  <!-- SEKCJA 3: GWARANCJE I STANDARD OBSŁUGI -->
  <section class="max-w-7xl mx-auto px-4 py-10">
    <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-10">
      <h3 class="text-2xl font-black text-white text-center mb-8">Standard mobilnego serwisu Akumulateo</h3>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        
        <div class="bg-slate-950 border border-slate-800 rounded-2xl p-5">
          <div class="text-3xl mb-3">⚡</div>
          <div class="text-white font-extrabold text-base mb-2">Dojazd & Diagnoza 24h</div>
          <p class="text-slate-400 text-xs leading-relaxed">
            Tester obciążeniowy akumulatora oraz precyzyjny test alternatora i poboru prądu na postoju.
          </p>
        </div>

        <div class="bg-slate-950 border border-slate-800 rounded-2xl p-5">
          <div class="text-3xl mb-3">🔋</div>
          <div class="text-white font-extrabold text-base mb-2">Markowe Baterie OEM</div>
          <p class="text-slate-400 text-xs leading-relaxed">
            Akumulatory <strong>Varta, Yuasa, Bosch, 4Max</strong>. Gwarancja fabryczna producenta do 3 lat.
          </p>
        </div>

        <div class="bg-slate-950 border border-slate-800 rounded-2xl p-5">
          <div class="text-3xl mb-3">💻</div>
          <div class="text-white font-extrabold text-base mb-2">Kodowanie BMS & OBD</div>
          <p class="text-slate-400 text-xs leading-relaxed">
            Podtrzymanie pamięci sterowników i rejestracja nowej baterii w systemie Start-Stop.
          </p>
        </div>

        <div class="bg-slate-950 border border-slate-800 rounded-2xl p-5">
          <div class="text-3xl mb-3">♻️</div>
          <div class="text-white font-extrabold text-base mb-2">Darmowy Recykling BDO</div>
          <p class="text-slate-400 text-xs leading-relaxed">
            Bezpłatny odbiór zużytej baterii – oszczędzasz 30 zł ustawowej kaucji depozytowej.
          </p>
        </div>

      </div>
    </div>
  </section>

  <!-- DOLNY CTA -->
  <section class="max-w-4xl mx-auto px-4 py-8 text-center">
    <div class="bg-gradient-to-r from-slate-900 to-slate-950 border border-slate-800 rounded-3xl p-8 sm:p-12 shadow-2xl">
      <h3 class="text-2xl sm:text-3xl font-black text-white mb-4">Potrzebujesz pomocy z akumulatorem?</h3>
      <p class="text-slate-300 text-base max-w-xl mx-auto mb-6 leading-relaxed">
        Zadzwoń do dyspozytora. Podaj markę, model auta oraz lokalizację – technik wyrusza natychmiast z dopasowanym akumulatorem.
      </p>
      <a href="tel:+48696556446" class="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black px-8 py-4 rounded-xl shadow-xl shadow-amber-500/30 text-lg transition transform active:scale-95">
        <span>📞 Zadzwoń: 696 556 446</span>
      </a>
    </div>
  </section>

  {UNIFIED_FOOTER_HTML}

</div>
"""

    template_code = """<!-- ========================================================
     AKUMULATEO – OBSZAR DZIAŁANIA PAGE HEADER INJECTION (SQUARESPACE 7.1)
     Dedykowany dla: /obszar-dzialania-warszawa-i-okolice (collection-6a8c92622180ae5dca0135cf)
     ======================================================== -->

<!-- 1. SCHEMA.ORG EMERGENCY SERVICE JSON-LD -->
<script type="application/ld+json">
__REPLACE_SCHEMA__
</script>

<!-- 2. ZOPTYMALIZOWANY WEWNĘTRZNY TAILWIND CSS -->
<style id="akumulateo-optimized-tailwind">
__REPLACE_TAILWIND__
</style>

<!-- 3. STYLE IZOLUJĄCE I UKRYWAJĄCE SZABLON SQUARESPACE -->
<style id="akumulateo-obszar-custom-styles">
#collection-6a8c92622180ae5dca0135cf {
  background-color: #020617 !important;
}

#collection-6a8c92622180ae5dca0135cf #header,
#collection-6a8c92622180ae5dca0135cf footer.sections,
#collection-6a8c92622180ae5dca0135cf #footer-sections,
#collection-6a8c92622180ae5dca0135cf section[data-section-id="6a8c9270e600463300572a53"],
#collection-6a8c92622180ae5dca0135cf .fe-6a8c9270c7617d7cc5094ae8 {
  display: none !important;
}

#collection-6a8c92622180ae5dca0135cf #siteWrapper {
  min-height: 0 !important;
  height: auto !important;
  padding: 0 !important;
  margin: 0 !important;
}

#collection-6a8c92622180ae5dca0135cf #page,
#collection-6a8c92622180ae5dca0135cf #page-regions,
#collection-6a8c92622180ae5dca0135cf section.region,
#collection-6a8c92622180ae5dca0135cf main#page {
  padding: 0 !important;
  margin: 0 !important;
}

@keyframes akumulateo-pulse {
  0% { transform: scale(0.95); opacity: 0.85; }
  50% { transform: scale(1.15); opacity: 1; }
  100% { transform: scale(0.95); opacity: 0.85; }
}
.akumulateo-pulse-dot {
  animation: akumulateo-pulse 2s infinite ease-in-out;
}

/* Mobilny Przycisk Menu – Wysoki Kontrast */
.ak-mobile-menu-btn {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 4px !important;
  background-color: #1e293b !important;
  border: 2px solid #f59e0b !important;
  border-radius: 10px !important;
  padding: 5px 8px !important;
  min-height: 34px !important;
  color: #fbbf24 !important;
  cursor: pointer !important;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4), 0 0 8px rgba(245, 158, 11, 0.25) !important;
  transition: all 0.15s ease !important;
  user-select: none !important;
  flex-shrink: 0 !important;
  -webkit-tap-highlight-color: transparent !important;
}

@media (min-width: 640px) {
  .ak-mobile-menu-btn {
    gap: 5px !important;
    border-radius: 12px !important;
    padding: 6px 10px !important;
    min-height: 38px !important;
  }
}

.ak-mobile-menu-btn:hover,
.ak-mobile-menu-btn:focus-visible {
  background-color: #334155 !important;
  border-color: #fbbf24 !important;
  box-shadow: 0 4px 16px rgba(245, 158, 11, 0.4) !important;
}

.ak-mobile-menu-btn:active {
  transform: scale(0.96) !important;
}

.ak-mobile-menu-btn .ak-menu-text {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  font-size: 10.5px !important;
  font-weight: 900 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: #fbbf24 !important;
  line-height: 1 !important;
}

@media (min-width: 640px) {
  .ak-mobile-menu-btn .ak-menu-text {
    font-size: 11px !important;
    letter-spacing: 0.08em !important;
  }
}

.ak-mobile-menu-btn svg {
  width: 15px !important;
  height: 15px !important;
  stroke: #fbbf24 !important;
  stroke-width: 2.5px !important;
  display: block !important;
  flex-shrink: 0 !important;
}

@media (min-width: 640px) {
  .ak-mobile-menu-btn svg {
    width: 17px !important;
    height: 17px !important;
  }
}
</style>

<!-- 4. TEMPLATE OBSZARU DZIAŁANIA -->
<template id="akumulateo-obszar-template">
__REPLACE_CONTENT__
</template>

<!-- 5. NATYCHMIASTOWY SKRYPT MONTAŻU (HIGH SPEED SSR EMULATION) -->
<script>
(function() {
  function mountAkumulateoObszar() {
    if (document.getElementById('akumulateo-obszar-wrapper')) return true;
    
    var tpl = document.getElementById('akumulateo-obszar-template');
    if (!tpl) return false;
    
    var targetSection = document.querySelector('section[data-section-id="6a8c9270e600463300572a53"]');
    var parent = targetSection ? targetSection.parentNode : 
                 (document.querySelector('#sections') || 
                  document.querySelector('main#page') || 
                  document.querySelector('#page') || 
                  document.body);
    if (!parent) return false;
    
    var wrapper = document.createElement('div');
    wrapper.id = 'akumulateo-obszar-wrapper';
    wrapper.appendChild(tpl.content.cloneNode(true));
    
    if (targetSection) {
      parent.insertBefore(wrapper, targetSection);
    } else if (parent.firstChild) {
      parent.insertBefore(wrapper, parent.firstChild);
    } else {
      parent.appendChild(wrapper);
    }
    return true;
  }

  if (!mountAkumulateoObszar()) {
    if (window.MutationObserver) {
      var obs = new MutationObserver(function() {
        if (mountAkumulateoObszar()) {
          obs.disconnect();
        }
      });
      obs.observe(document.documentElement, { childList: true, subtree: true });
    }
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', mountAkumulateoObszar);
    }
    window.addEventListener('load', mountAkumulateoObszar);
  }
})();
</script>
"""
    final_hub = template_code.replace("__REPLACE_SCHEMA__", schema_str).replace("__REPLACE_TAILWIND__", TAILWIND_CSS).replace("__REPLACE_CONTENT__", content_html)
    out_file = os.path.join(BASE_DIR, "snippets", "squarespace", "obszar-dzialania-page-header-injection.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(final_hub)
    print(f"✅ Zbudowano Hub Injection: {out_file} ({len(final_hub)} znaków)")

def build_mokotow_page_injection():
    schema = {
        "@context": "https://schema.org",
        "@type": "EmergencyService",
        "name": "Akumulateo – Pogotowie Akumulatorowe Warszawa Mokotów 24/7",
        "url": "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-mokotow",
        "telephone": "+48696556446",
        "priceRange": "$$",
        "image": "https://images.squarespace-cdn.com/content/v1/685d174157b18362d5b7b0f3/7c219de6-f0cf-4151-a1a4-eac82a1de5d2/akumulateo-hero-pagespeed.jpg",
        "areaServed": {
            "@type": "AdministrativeArea",
            "name": "Mokotów, Warszawa"
        },
        "description": "Padł akumulator na Mokotowie? Całodobowa wymiana z dojazdem w 20-30 min (Mordor, Służew, Stegny, Sadyba). Dobór, montaż, kodowanie BMS. Zadzwoń: 696 556 446!",
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00",
            "closes": "23:59"
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "5.0",
            "bestRating": "5.0",
            "worstRating": "1.0",
            "ratingCount": "100",
            "reviewCount": "100"
        }
    }
    schema_str = json.dumps(schema, ensure_ascii=False, indent=2)

    content_html = f"""
<div class="akumulateo-root bg-slate-950 text-slate-100 font-sans antialiased overflow-hidden">
  
  {NAV_HEADER_HTML}

  <!-- HERO MOKOTÓW -->
  <section class="relative px-4 py-12 md:py-16 bg-gradient-to-b from-slate-900 via-slate-900 to-slate-950 border-b border-slate-800 text-center">
    <div class="max-w-4xl mx-auto">
      <div class="inline-flex items-center gap-2 bg-amber-500/10 border border-amber-500/30 text-amber-400 px-3.5 py-1.5 rounded-full text-xs font-black uppercase tracking-wider mb-5">
        <span>⚡ Pogotowie Akumulatorowe Warszawa Mokotów 24h</span>
      </div>
      <h1 class="text-3xl sm:text-5xl font-black text-white tracking-tight leading-tight mb-5">
        Wymiana Akumulatora z Dojazdem Warszawa Mokotów 24/7
      </h1>
      <p class="text-slate-300 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed mb-8">
        Rozładowany akumulator na Mokotowie? Dojedziemy pod Twój blok, dom jednorodzinny, biurowiec przy Domaniewskiej (Mordor) lub zjedziemy do ciasnego garażu podziemnego w <strong>20–30 minut</strong>. Fabrycznie nowa bateria z montażem i kodowaniem BMS na miejscu.
      </p>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-3">
        <a href="tel:+48696556446" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black px-6 py-4 rounded-xl shadow-xl shadow-amber-500/25 transition transform active:scale-95 text-base sm:text-lg">
          <span>📞 Zadzwoń: 696 556 446</span>
        </a>
      </div>
      <div class="mt-3 text-xs text-slate-400 font-semibold">
        ⏱️ Czas dojazdu na Mokotowie: <span class="text-emerald-400 font-bold">20–30 minut</span>
      </div>
    </div>
  </section>

  <!-- BANNER PREKWALIFIKACJI MOBILNEJ -->
  <section class="max-w-7xl mx-auto px-4 py-6">
    <div class="bg-amber-500/10 border border-amber-500/30 rounded-2xl p-5 text-center">
      <div class="text-amber-400 font-black text-xs uppercase tracking-wider mb-2">
        ℹ️ Usługa w 100% Mobilna z Dojazdem pod Auto
      </div>
      <p class="text-slate-200 text-sm sm:text-base leading-relaxed max-w-3xl mx-auto">
        Nie trać czasu na szukanie stacjonarnego sklepu ani holowanie auta. Nie prowadzimy punktu odbioru na terenie Mokotowa – <strong>nasz serwisant przyjeżdża bezpośrednio pod Twój adres</strong> z fabrycznie nową baterią i montuje ją na miejscu w 20–30 minut.
      </p>
    </div>
  </section>

  <!-- OBSZAR INTERWENCJI I REJONY MOKOTOWA -->
  <section class="max-w-7xl mx-auto px-4 py-8">
    <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-10 mb-8">
      <h2 class="text-2xl sm:text-3xl font-black text-white mb-3">Rejony obsługi na Mokotowie</h2>
      <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-6">
        Nasi technicy stacjonują mobilnie, obsługując na terenie dzielnicy Mokotów m.in.: <strong>Służewiec / Mordor (Domaniewska, Wołoska), Sadyba, Stegny, Służew nad Dolinką, Wierzbno, Ksawerów, Sielce, Czerniaków, Wyględów, Augustówka</strong>.
      </p>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6">
          <div class="text-3xl mb-3">⚡</div>
          <div class="text-white font-extrabold text-lg mb-2">Awaryjny Rozruch 12V/24V</div>
          <p class="text-slate-400 text-xs sm:text-sm leading-relaxed">
            Bezpieczne uruchomienie boosterem mikroprocesorowym bez ryzyka przepięcia w instalacji pokładowej.
          </p>
        </div>

        <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6">
          <div class="text-3xl mb-3">🔋</div>
          <div class="text-white font-extrabold text-lg mb-2">Montaż Nowego Akumulatora</div>
          <p class="text-slate-400 text-xs sm:text-sm leading-relaxed">
            Fabryczne akumulatory <strong>Varta, Yuasa, Bosch, 4Max</strong>. Dobór wg katalogu producenta pojazdu.
          </p>
        </div>

        <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6">
          <div class="text-3xl mb-3">💻</div>
          <div class="text-white font-extrabold text-lg mb-2">Kodowanie BMS & OBD</div>
          <p class="text-slate-400 text-xs sm:text-sm leading-relaxed">
            Podtrzymanie pamięci radia i sterowników oraz rejestracja nowej baterii w komputerze Start-Stop.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ DZIELNICOWE MOKOTÓW -->
  <section class="max-w-7xl mx-auto px-4 py-8">
    <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-10">
      <h3 class="text-2xl font-black text-white mb-6">Najczęstsze pytania kierowców – Mokotów (FAQ)</h3>
      <div class="space-y-6">
        <div class="border-b border-slate-800 pb-5">
          <div class="text-amber-400 font-bold text-base mb-2">Czy wjedziecie do garażu podziemnego biurowca na Domaniewskiej?</div>
          <p class="text-slate-300 text-sm leading-relaxed">
            Tak. Nasze auta serwisowe oraz przenośne zestawy diagnostyczno-rozruchowe są w pełni przystosowane do wjazdu do garaży podziemnych i hal garażowych (poziomy -1, -2, -3) na terenie całego Mokotowa.
          </p>
        </div>
        <div class="border-b border-slate-800 pb-5">
          <div class="text-amber-400 font-bold text-base mb-2">Jakie formy płatności przyjmuje serwisant?</div>
          <p class="text-slate-300 text-sm leading-relaxed">
            Każdy technik Akumulateo posiada terminal płatniczy. Płatności można dokonać kartą zbliżeniową, kodem BLIK lub gotówką. Dla firm wystawiamy fakturę VAT 23% na miejscu.
          </p>
        </div>
        <div>
          <div class="text-amber-400 font-bold text-base mb-2">Co dzieje się ze starym, zużytym akumulatorem?</div>
          <p class="text-slate-300 text-sm leading-relaxed">
            Stary akumulator odbieramy bezpłatnie i przekazujemy do certyfikowanego recyklingu hutniczego zgodnie z przepisami BDO. Dzięki temu nie ponosisz ustawowej kaucji depozytowej (30 zł).
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- DOLNY CTA -->
  <section class="max-w-4xl mx-auto px-4 py-10 text-center">
    <div class="bg-gradient-to-r from-slate-900 to-slate-950 border border-slate-800 rounded-3xl p-8 sm:p-12 shadow-2xl">
      <h3 class="text-2xl sm:text-3xl font-black text-white mb-4">Padł akumulator na Mokotowie?</h3>
      <p class="text-slate-300 text-base max-w-xl mx-auto mb-6 leading-relaxed">
        Zadzwoń do dyspozytora. Podaj model auta i adres – serwisant wyrusza natychmiast z nową baterią.
      </p>
      <a href="tel:+48696556446" class="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black px-8 py-4 rounded-xl shadow-xl shadow-amber-500/30 text-lg transition transform active:scale-95">
        <span>📞 Zadzwoń: 696 556 446</span>
      </a>
    </div>
  </section>

  {UNIFIED_FOOTER_HTML}

</div>
"""

    template_code = """<!-- ========================================================
     AKUMULATEO – MOKOTÓW PAGE HEADER INJECTION (SQUARESPACE 7.1)
     Dedykowany dla: /wymiana-akumulatora-warszawa-mokotow (collection-6ab4470b50295a294b3a4066)
     ======================================================== -->

<!-- 1. SCHEMA.ORG EMERGENCY SERVICE JSON-LD -->
<script type="application/ld+json">
__REPLACE_SCHEMA__
</script>

<!-- 2. ZOPTYMALIZOWANY WEWNĘTRZNY TAILWIND CSS -->
<style id="akumulateo-optimized-tailwind">
__REPLACE_TAILWIND__
</style>

<!-- 3. STYLE IZOLUJĄCE I UKRYWAJĄCE SZABLON SQUARESPACE -->
<style id="akumulateo-mokotow-custom-styles">
#collection-6ab4470b50295a294b3a4066 {
  background-color: #020617 !important;
}

#collection-6ab4470b50295a294b3a4066 #header,
#collection-6ab4470b50295a294b3a4066 footer.sections,
#collection-6ab4470b50295a294b3a4066 #footer-sections,
#collection-6ab4470b50295a294b3a4066 section[data-section-id="6ab4470b50295a294b3a406a"],
#collection-6ab4470b50295a294b3a4066 section[data-section-id="6ab4470b50295a294b3a406d"],
#collection-6ab4470b50295a294b3a4066 section[data-section-id="6ab4470b50295a294b3a4070"],
#collection-6ab4470b50295a294b3a4066 section[data-section-id="6ab4470b50295a294b3a4073"],
#collection-6ab4470b50295a294b3a4066 .fe-6ab4470b50295a294b3a4069 {
  display: none !important;
}

#collection-6ab4470b50295a294b3a4066 #siteWrapper {
  min-height: 0 !important;
  height: auto !important;
  padding: 0 !important;
  margin: 0 !important;
}

#collection-6ab4470b50295a294b3a4066 #page,
#collection-6ab4470b50295a294b3a4066 #page-regions,
#collection-6ab4470b50295a294b3a4066 section.region,
#collection-6ab4470b50295a294b3a4066 main#page {
  padding: 0 !important;
  margin: 0 !important;
}

@keyframes akumulateo-pulse {
  0% { transform: scale(0.95); opacity: 0.85; }
  50% { transform: scale(1.15); opacity: 1; }
  100% { transform: scale(0.95); opacity: 0.85; }
}
.akumulateo-pulse-dot {
  animation: akumulateo-pulse 2s infinite ease-in-out;
}

/* Mobilny Przycisk Menu – Wysoki Kontrast */
.ak-mobile-menu-btn {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 4px !important;
  background-color: #1e293b !important;
  border: 2px solid #f59e0b !important;
  border-radius: 10px !important;
  padding: 5px 8px !important;
  min-height: 34px !important;
  color: #fbbf24 !important;
  cursor: pointer !important;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4), 0 0 8px rgba(245, 158, 11, 0.25) !important;
  transition: all 0.15s ease !important;
  user-select: none !important;
  flex-shrink: 0 !important;
  -webkit-tap-highlight-color: transparent !important;
}

@media (min-width: 640px) {
  .ak-mobile-menu-btn {
    gap: 5px !important;
    border-radius: 12px !important;
    padding: 6px 10px !important;
    min-height: 38px !important;
  }
}

.ak-mobile-menu-btn:hover,
.ak-mobile-menu-btn:focus-visible {
  background-color: #334155 !important;
  border-color: #fbbf24 !important;
  box-shadow: 0 4px 16px rgba(245, 158, 11, 0.4) !important;
}

.ak-mobile-menu-btn:active {
  transform: scale(0.96) !important;
}

.ak-mobile-menu-btn .ak-menu-text {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  font-size: 10.5px !important;
  font-weight: 900 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: #fbbf24 !important;
  line-height: 1 !important;
}

@media (min-width: 640px) {
  .ak-mobile-menu-btn .ak-menu-text {
    font-size: 11px !important;
    letter-spacing: 0.08em !important;
  }
}

.ak-mobile-menu-btn svg {
  width: 15px !important;
  height: 15px !important;
  stroke: #fbbf24 !important;
  stroke-width: 2.5px !important;
  display: block !important;
  flex-shrink: 0 !important;
}

@media (min-width: 640px) {
  .ak-mobile-menu-btn svg {
    width: 17px !important;
    height: 17px !important;
  }
}
</style>

<!-- 4. TEMPLATE MOKOTOWA -->
<template id="akumulateo-mokotow-template">
__REPLACE_CONTENT__
</template>

<!-- 5. NATYCHMIASTOWY SKRYPT MONTAŻU (HIGH SPEED SSR EMULATION) -->
<script>
(function() {
  function mountAkumulateoMokotow() {
    if (document.getElementById('akumulateo-mokotow-wrapper')) return true;
    
    var tpl = document.getElementById('akumulateo-mokotow-template');
    if (!tpl) return false;
    
    var targetSection = document.querySelector('section[data-section-id="6ab4470b50295a294b3a406a"]');
    var parent = targetSection ? targetSection.parentNode : 
                 (document.querySelector('#sections') || 
                  document.querySelector('main#page') || 
                  document.querySelector('#page') || 
                  document.body);
    if (!parent) return false;
    
    var wrapper = document.createElement('div');
    wrapper.id = 'akumulateo-mokotow-wrapper';
    wrapper.appendChild(tpl.content.cloneNode(true));
    
    if (targetSection) {
      parent.insertBefore(wrapper, targetSection);
    } else if (parent.firstChild) {
      parent.insertBefore(wrapper, parent.firstChild);
    } else {
      parent.appendChild(wrapper);
    }
    return true;
  }

  if (!mountAkumulateoMokotow()) {
    if (window.MutationObserver) {
      var obs = new MutationObserver(function() {
        if (mountAkumulateoMokotow()) {
          obs.disconnect();
        }
      });
      obs.observe(document.documentElement, { childList: true, subtree: true });
    }
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', mountAkumulateoMokotow);
    }
    window.addEventListener('load', mountAkumulateoMokotow);
  }
})();
</script>
"""
    final_mokotow = template_code.replace("__REPLACE_SCHEMA__", schema_str).replace("__REPLACE_TAILWIND__", TAILWIND_CSS).replace("__REPLACE_CONTENT__", content_html)
    out_file = os.path.join(BASE_DIR, "snippets", "squarespace", "mokotow-page-header-injection.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(final_mokotow)
    print(f"✅ Zbudowano Mokotów Injection: {out_file} ({len(final_mokotow)} znaków)")

def build_piaseczno_page_injection():
    schema = {
        "@context": "https://schema.org",
        "@type": "EmergencyService",
        "name": "Akumulateo – Pogotowie Akumulatorowe Piaseczno 24/7",
        "url": "https://www.akumulateo.pl/wymiana-akumulatora-piaseczno",
        "telephone": "+48696556446",
        "priceRange": "$$",
        "image": "https://images.squarespace-cdn.com/content/v1/685d174157b18362d5b7b0f3/7c219de6-f0cf-4151-a1a4-eac82a1de5d2/akumulateo-hero-pagespeed.jpg",
        "areaServed": {
            "@type": "AdministrativeArea",
            "name": "Piaseczno, Powiat Piaseczyński"
        },
        "description": "Padł akumulator w Piasecznie lub okolicy? Całodobowa wymiana z dojazdem w 20-30 min (Józefosław, Julianów, Zalesie Górne/Dolne, Chyliczki, Głosków). Dobór, montaż, kodowanie BMS. Zadzwoń: 696 556 446!",
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00",
            "closes": "23:59"
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "5.0",
            "bestRating": "5.0",
            "worstRating": "1.0",
            "ratingCount": "100",
            "reviewCount": "100"
        }
    }
    schema_str = json.dumps(schema, ensure_ascii=False, indent=2)

    content_html = f"""
<div class="akumulateo-root bg-slate-950 text-slate-100 font-sans antialiased overflow-hidden">
  
  {NAV_HEADER_HTML}

  <!-- HERO PIASECZNO -->
  <section class="relative px-4 py-12 md:py-16 bg-gradient-to-b from-slate-900 via-slate-900 to-slate-950 border-b border-slate-800 text-center">
    <div class="max-w-4xl mx-auto">
      <div class="inline-flex items-center gap-2 bg-amber-500/10 border border-amber-500/30 text-amber-400 px-3.5 py-1.5 rounded-full text-xs font-black uppercase tracking-wider mb-5">
        <span>⚡ Pogotowie Akumulatorowe Piaseczno i Okolice 24h</span>
      </div>
      <h1 class="text-3xl sm:text-5xl font-black text-white tracking-tight leading-tight mb-5">
        Wymiana Akumulatora z Dojazdem Piaseczno 24/7
      </h1>
      <p class="text-slate-300 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed mb-8">
        Rozładowany akumulator w Piasecznie, Józefosławiu, Julianowie lub okolicach? Dojedziemy pod Twój dom, parking osiedlowy lub zjedziemy do garażu podziemnego w <strong>20–30 minut</strong> trasą Puławską lub S7. Fabrycznie nowa bateria z profesjonalnym montażem i adaptacją BMS na miejscu.
      </p>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-3">
        <a href="tel:+48696556446" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black px-6 py-4 rounded-xl shadow-xl shadow-amber-500/25 transition transform active:scale-95 text-base sm:text-lg">
          <span>📞 Zadzwoń: 696 556 446</span>
        </a>
      </div>
      <div class="mt-3 text-xs text-slate-400 font-semibold">
        ⏱️ Czas dojazdu w rejonie Piaseczna: <span class="text-emerald-400 font-bold">20–30 minut</span>
      </div>
    </div>
  </section>

  <!-- BANNER PREKWALIFIKACJI MOBILNEJ -->
  <section class="max-w-7xl mx-auto px-4 py-6">
    <div class="bg-amber-500/10 border border-amber-500/30 rounded-2xl p-5 text-center">
      <div class="text-amber-400 font-black text-xs uppercase tracking-wider mb-2">
        ℹ️ Usługa w 100% Mobilna z Dojazdem pod Auto
      </div>
      <p class="text-slate-200 text-sm sm:text-base leading-relaxed max-w-3xl mx-auto">
        Nie trać czasu na szukanie stacjonarnego sklepu w Piasecznie ani na kosztowne holowanie auta. Nie prowadzimy punktu stacjonarnego – <strong>nasz mobilny technik przyjeżdża bezpośrednio pod wskazany adres</strong> ze świeżym akumulatorem OEM i montuje go od ręki w 20–30 minut.
      </p>
    </div>
  </section>

  <!-- OBSZAR INTERWENCJI PIASECZNO -->
  <section class="max-w-7xl mx-auto px-4 py-8">
    <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-10 mb-8">
      <h2 class="text-2xl sm:text-3xl font-black text-white mb-3">Rejony obsługi w Piasecznie i Aglomeracji</h2>
      <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-6">
        Nasz mobilny serwis stacjonuje w rejonie węzła Puławska / trasy ekspresowej S7, błyskawicznie obsługując: <strong>Piaseczno Centrum, Józefosław, Julianów, Zalesie Górne, Zalesie Dolne, Chyliczki, Głosków, Bobrowiec, Żabieniec, Gołków, Kamionka, Mysiadło, Nowa Iwiczna</strong>.
      </p>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6">
          <div class="text-3xl mb-3">⚡</div>
          <div class="text-white font-extrabold text-lg mb-2">Awaryjny Rozruch 12V/24V</div>
          <p class="text-slate-400 text-xs sm:text-sm leading-relaxed">
            Bezpieczne odpalenie boosterem mikroprocesorowym bez ryzyka przepięcia w czułych modułach auta.
          </p>
        </div>

        <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6">
          <div class="text-3xl mb-3">🔋</div>
          <div class="text-white font-extrabold text-lg mb-2">Dobór Baterii OEM (Varta, Yuasa, Bosch)</div>
          <p class="text-slate-400 text-xs sm:text-sm leading-relaxed">
            Akumulatory kwasowo-ołowiowe, EFB i AGM do aut z systemem Start-Stop. Oficjalne marki najwyższej jakości.
          </p>
        </div>

        <div class="bg-slate-950 border border-slate-800 rounded-2xl p-6">
          <div class="text-3xl mb-3">💻</div>
          <div class="text-white font-extrabold text-lg mb-2">Adaptacja BMS & Kodowanie</div>
          <p class="text-slate-400 text-xs sm:text-sm leading-relaxed">
            Rejestracja nowej baterii w komputerze pokładowym (BMW, Audi, Mercedes, VAG, Volvo) i podtrzymanie pamięci.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- PAKIET GWARANCYJNY I CENNIK -->
  <section class="max-w-7xl mx-auto px-4 py-8">
    <div class="text-center mb-10">
      <h2 class="text-3xl sm:text-4xl font-black text-white mb-3">Przejrzysty Cennik Usług w Piasecznie</h2>
      <p class="text-slate-400 text-sm sm:text-base max-w-xl mx-auto">
        Brak ukrytych kosztów. Zawsze precyzyjna wycena telefoniczna przed wyjazdem technika.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto">
      <!-- Karta 1 -->
      <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-8 flex flex-col justify-between">
        <div>
          <div class="text-xs uppercase font-extrabold text-slate-400 tracking-wider mb-2">Opcja Ratunkowa</div>
          <h3 class="text-2xl font-black text-white mb-2">Awaryjny Rozruch</h3>
          <p class="text-slate-400 text-xs sm:text-sm mb-6 leading-relaxed">
            Dojazd na terenie Piaseczna, podłączenie boostera, uruchomienie silnika i badanie ładowania alternatora.
          </p>
          <div class="text-3xl sm:text-4xl font-black text-amber-400 mb-6">od 150 zł</div>
        </div>
        <a href="tel:+48696556446" class="w-full bg-slate-800 hover:bg-slate-700 text-white font-bold py-3.5 px-4 rounded-xl text-center block text-sm transition">
          📞 Zamów rozruch 24h
        </a>
      </div>

      <!-- Karta 2 (Wyróżniona) -->
      <div class="bg-slate-900 border-2 border-amber-500 rounded-3xl p-6 sm:p-8 flex flex-col justify-between shadow-2xl shadow-amber-500/10 relative">
        <div class="absolute -top-3.5 left-1/2 -translate-x-1/2 bg-amber-500 text-slate-950 font-black text-xs uppercase px-3.5 py-1 rounded-full whitespace-nowrap">
          Najczęściej Wybierana
        </div>
        <div>
          <div class="text-xs uppercase font-extrabold text-amber-400 tracking-wider mb-2 mt-1">Kompleksowy Serwis</div>
          <h3 class="text-2xl font-black text-white mb-2">Wymiana z Dojazdem</h3>
          <p class="text-slate-400 text-xs sm:text-sm mb-6 leading-relaxed">
            Dojazd pod dom w Piasecznie, pełna diagnostyka, demontaż, montaż nowego akumulatora, kodowanie BMS i darmowy recykling starej baterii.
          </p>
          <div class="text-3xl sm:text-4xl font-black text-amber-400 mb-6">od 180 zł <span class="text-xs font-normal text-slate-400">+ koszt baterii</span></div>
        </div>
        <a href="tel:+48696556446" class="w-full bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black py-4 px-4 rounded-xl text-center block text-base shadow-lg shadow-amber-500/25 transition transform active:scale-95">
          📞 Zamów wymianę 24h
        </a>
      </div>

      <!-- Karta 3 -->
      <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-8 flex flex-col justify-between">
        <div>
          <div class="text-xs uppercase font-extrabold text-slate-400 tracking-wider mb-2">Pomiary & Weryfikacja</div>
          <h3 class="text-2xl font-black text-white mb-2">Diagnostyka Instalacji</h3>
          <p class="text-slate-400 text-xs sm:text-sm mb-6 leading-relaxed">
            Test upływu prądu na postoju (czy coś nie rozładowuje baterii nocą) oraz analiza sprawności diod alternatora.
          </p>
          <div class="text-3xl sm:text-4xl font-black text-amber-400 mb-6">od 100 zł</div>
        </div>
        <a href="tel:+48696556446" class="w-full bg-slate-800 hover:bg-slate-700 text-white font-bold py-3.5 px-4 rounded-xl text-center block text-sm transition">
          📞 Zamów diagnostykę
        </a>
      </div>
    </div>
  </section>

  <!-- OFICJALNE MARKI AKUMULATORÓW -->
  <section class="max-w-7xl mx-auto px-4 py-8">
    <div class="bg-slate-900/60 border border-slate-800 rounded-3xl p-6 sm:p-8 text-center">
      <div class="text-xs uppercase font-extrabold text-slate-400 tracking-wider mb-2">Gwarancja Fabryczna 2-3 Lata</div>
      <h3 class="text-xl sm:text-2xl font-black text-white mb-6">Montujemy Wyłącznie Markowe Baterie Klasy Premium</h3>
      <div class="flex flex-wrap items-center justify-center gap-6 sm:gap-10 text-slate-300 font-black text-lg sm:text-xl">
        <span class="hover:text-amber-400 transition">VARTA</span>
        <span class="text-slate-600">•</span>
        <span class="hover:text-amber-400 transition">YUASA</span>
        <span class="text-slate-600">•</span>
        <span class="hover:text-amber-400 transition">BOSCH</span>
        <span class="text-slate-600">•</span>
        <span class="hover:text-amber-400 transition">4MAX</span>
      </div>
    </div>
  </section>

  <!-- DOLNY CTA -->
  <section class="max-w-4xl mx-auto px-4 py-10 text-center">
    <div class="bg-gradient-to-r from-slate-900 to-slate-950 border border-slate-800 rounded-3xl p-8 sm:p-12 shadow-2xl">
      <h3 class="text-2xl sm:text-3xl font-black text-white mb-4">Potrzebujesz pomocy w Piasecznie od zaraz?</h3>
      <p class="text-slate-300 text-base max-w-xl mx-auto mb-6 leading-relaxed">
        Zadzwoń do dyspozytora. Podaj model auta i adres – serwisant wyrusza natychmiast z nową baterią trasą Puławską lub S7.
      </p>
      <a href="tel:+48696556446" class="inline-flex items-center justify-center gap-2 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black px-8 py-4 rounded-xl shadow-xl shadow-amber-500/30 text-lg transition transform active:scale-95">
        <span>📞 Zadzwoń: 696 556 446</span>
      </a>
    </div>
  </section>

  {UNIFIED_FOOTER_HTML}

</div>
"""

    template_code = """<!-- ========================================================
     AKUMULATEO – PIASECZNO PAGE HEADER INJECTION (SQUARESPACE 7.1)
     Dedykowany dla: /wymiana-akumulatora-piaseczno (collection-6ab5053a890503382c8b718e)
     ======================================================== -->

<!-- 1. SCHEMA.ORG EMERGENCY SERVICE JSON-LD -->
<script type="application/ld+json">
__REPLACE_SCHEMA__
</script>

<!-- 2. ZOPTYMALIZOWANY WEWNĘTRZNY TAILWIND CSS -->
<style id="akumulateo-optimized-tailwind">
__REPLACE_TAILWIND__
</style>

<!-- 3. STYLE IZOLUJĄCE I UKRYWAJĄCE SZABLON SQUARESPACE -->
<style id="akumulateo-piaseczno-custom-styles">
#collection-6ab5053a890503382c8b718e {
  background-color: #020617 !important;
}

#collection-6ab5053a890503382c8b718e #header,
#collection-6ab5053a890503382c8b718e footer.sections,
#collection-6ab5053a890503382c8b718e #footer-sections,
#collection-6ab5053a890503382c8b718e section[data-section-id="6ab5053a890503382c8b7192"],
#collection-6ab5053a890503382c8b718e section[data-section-id="6ab5053a890503382c8b7195"],
#collection-6ab5053a890503382c8b718e section[data-section-id="6ab5053a890503382c8b7198"],
#collection-6ab5053a890503382c8b718e section[data-section-id="6ab5053a890503382c8b719b"],
#collection-6ab5053a890503382c8b718e .fe-6ab5053a890503382c8b7191 {
  display: none !important;
}

#collection-6ab5053a890503382c8b718e #siteWrapper {
  min-height: 0 !important;
  height: auto !important;
  padding: 0 !important;
  margin: 0 !important;
}

#collection-6ab5053a890503382c8b718e #page,
#collection-6ab5053a890503382c8b718e #page-regions,
#collection-6ab5053a890503382c8b718e section.region,
#collection-6ab5053a890503382c8b718e main#page {
  padding: 0 !important;
  margin: 0 !important;
}

@keyframes akumulateo-pulse {
  0% { transform: scale(0.95); opacity: 0.85; }
  50% { transform: scale(1.15); opacity: 1; }
  100% { transform: scale(0.95); opacity: 0.85; }
}
.akumulateo-pulse-dot {
  animation: akumulateo-pulse 2s infinite ease-in-out;
}

/* Mobilny Przycisk Menu – Wysoki Kontrast */
.ak-mobile-menu-btn {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 4px !important;
  background-color: #1e293b !important;
  border: 2px solid #f59e0b !important;
  border-radius: 10px !important;
  padding: 5px 8px !important;
  min-height: 34px !important;
  color: #fbbf24 !important;
  cursor: pointer !important;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4), 0 0 8px rgba(245, 158, 11, 0.25) !important;
  transition: all 0.15s ease !important;
  user-select: none !important;
  flex-shrink: 0 !important;
  -webkit-tap-highlight-color: transparent !important;
}

@media (min-width: 640px) {
  .ak-mobile-menu-btn {
    gap: 5px !important;
    border-radius: 12px !important;
    padding: 6px 10px !important;
    min-height: 38px !important;
  }
}

.ak-mobile-menu-btn:hover,
.ak-mobile-menu-btn:focus-visible {
  background-color: #334155 !important;
  border-color: #fbbf24 !important;
  box-shadow: 0 4px 16px rgba(245, 158, 11, 0.4) !important;
}

.ak-mobile-menu-btn:active {
  transform: scale(0.96) !important;
}

.ak-mobile-menu-btn .ak-menu-text {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  font-size: 10.5px !important;
  font-weight: 900 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: #fbbf24 !important;
  line-height: 1 !important;
}

@media (min-width: 640px) {
  .ak-mobile-menu-btn .ak-menu-text {
    font-size: 11px !important;
    letter-spacing: 0.08em !important;
  }
}

.ak-mobile-menu-btn svg {
  width: 15px !important;
  height: 15px !important;
  stroke: #fbbf24 !important;
  stroke-width: 2.5px !important;
  display: block !important;
  flex-shrink: 0 !important;
}

@media (min-width: 640px) {
  .ak-mobile-menu-btn svg {
    width: 17px !important;
    height: 17px !important;
  }
}
</style>

<!-- 4. TEMPLATE PIASECZNA -->
<template id="akumulateo-piaseczno-template">
__REPLACE_CONTENT__
</template>

<!-- 5. NATYCHMIASTOWY SKRYPT MONTAŻU (HIGH SPEED SSR EMULATION) -->
<script>
(function() {
  function mountAkumulateoPiaseczno() {
    if (document.getElementById('akumulateo-piaseczno-wrapper')) return true;
    
    var tpl = document.getElementById('akumulateo-piaseczno-template');
    if (!tpl) return false;
    
    var targetSection = document.querySelector('section[data-section-id="6ab5053a890503382c8b7192"]');
    var parent = targetSection ? targetSection.parentNode : 
                 (document.querySelector('#sections') || 
                  document.querySelector('main#page') || 
                  document.querySelector('#page') || 
                  document.body);
    if (!parent) return false;
    
    var wrapper = document.createElement('div');
    wrapper.id = 'akumulateo-piaseczno-wrapper';
    wrapper.appendChild(tpl.content.cloneNode(true));
    
    if (targetSection) {
      parent.insertBefore(wrapper, targetSection);
    } else if (parent.firstChild) {
      parent.insertBefore(wrapper, parent.firstChild);
    } else {
      parent.appendChild(wrapper);
    }
    return true;
  }

  if (!mountAkumulateoPiaseczno()) {
    if (window.MutationObserver) {
      var obs = new MutationObserver(function() {
        if (mountAkumulateoPiaseczno()) {
          obs.disconnect();
        }
      });
      obs.observe(document.documentElement, { childList: true, subtree: true });
    }
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', mountAkumulateoPiaseczno);
    }
    window.addEventListener('load', mountAkumulateoPiaseczno);
  }
})();
</script>
"""
    final_piaseczno = template_code.replace("__REPLACE_SCHEMA__", schema_str).replace("__REPLACE_TAILWIND__", TAILWIND_CSS).replace("__REPLACE_CONTENT__", content_html)
    out_file = os.path.join(BASE_DIR, "snippets", "squarespace", "piaseczno-page-header-injection.html")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(final_piaseczno)
    print(f"✅ Zbudowano Piaseczno Injection: {out_file} ({len(final_piaseczno)} znaków)")

if __name__ == "__main__":
    build_hub_page_injection()
    build_mokotow_page_injection()
    build_piaseczno_page_injection()
