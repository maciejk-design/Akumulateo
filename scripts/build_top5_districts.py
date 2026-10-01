#!/usr/bin/env python3
"""
Generator kompletnych pakietów Page Header Injection dla TOP 5 dzielnic Warszawy:
1. Bemowo (/wymiana-akumulatora-warszawa-bemowo)
2. Wola (/wymiana-akumulatora-warszawa-wola)
3. Ursynów (/wymiana-akumulatora-warszawa-ursynow)
4. Śródmieście (/wymiana-akumulatora-warszawa-srodmiescie)
5. Bielany (/wymiana-akumulatora-warszawa-bielany)

Standard Brandbook v2.2:
- Kontrastowy Dark Mode (#020617 / #0f172a)
- Zero mikrofontów (min. 15.5px/16.5px, line-height 1.65)
- Aktywny link w logo (href="/")
- Responsywny nagłówek <= 340px (bez ucinania przycisku na 360px+)
- Wyrazisty przycisk MENU z bursztynową ramką (#f59e0b) i etykietą MENU/ZAMKNIJ
- Czas dojazdu: 20-30 min
- Prekwalifikacja mobilna (Brak sklepu stacjonarnego)
- Oficjalne marki: Varta, Yuasa (YUASA), Bosch, 4Max (zero Centra/Banner)
- Schema.org EmergencyService JSON-LD (5.0★, 100+ opinii)
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPETS_DIR = os.path.join(BASE_DIR, "snippets", "squarespace")

# Załaduj skompilowany Tailwind CSS
with open(os.path.join(SNIPPETS_DIR, "compiled-tailwind.min.css"), "r", encoding="utf-8") as f:
    TAILWIND_CSS = f.read().strip()

NAV_HEADER_HTML = """
  <!-- 1. TOP EMERGENCY BAR (PASEK DYŻURU 24H) -->
  <div class="bg-gradient-to-r from-amber-500 via-amber-400 to-amber-500 text-slate-950 py-1.5 px-3 sm:px-4 text-xs font-black tracking-wide shadow-sm">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-x-2.5 gap-y-1">
      <div class="flex items-center gap-1.5 flex-shrink-0">
        <span class="w-2 h-2 rounded-full bg-slate-950 akumulateo-pulse-dot flex-shrink-0"></span>
        <span class="uppercase font-black tracking-wider">Dyżur Pogotowia 24h/7</span>
        <span class="hidden sm:inline font-bold text-slate-900">• Dojazd 20–30 min w Warszawie i aglomeracji</span>
      </div>
      <div class="flex items-center gap-2.5 flex-shrink-0 text-[11px] font-bold">
        <span class="hidden md:inline-flex items-center gap-1 font-extrabold text-slate-950 bg-amber-300/90 px-1.5 py-0.5 rounded text-[10px]" title="We speak English – call us directly">🇬🇧 We speak English</span>
        <a href="https://g.page/r/CXjN9llopHR_EBM/" target="_blank" rel="noopener noreferrer" class="hover:text-slate-800 hover:underline flex items-center gap-1 transition cursor-pointer" title="Zobacz opinie Akumulateo w Google Maps">
          <span>⭐ 5.0 w Google (100+ opinii) ↗</span>
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
        <button id="akMobileMenuBtn" onclick="var m=document.getElementById('akSubpageMobileDrawer');if(m){var isHidden=m.classList.toggle('hidden');this.setAttribute('aria-expanded',!isHidden);var icon=this.querySelector('.ak-menu-icon');var closeIcon=this.querySelector('.ak-close-icon');var label=this.querySelector('.ak-menu-text');if(icon&&closeIcon){icon.classList.toggle('hidden',!isHidden);closeIcon.classList.toggle('hidden',isHidden);}if(label){label.textContent=isHidden?'MENU':'ZAMKNIJ';}}" aria-label="Menu nawigacji" aria-expanded="false" class="ak-mobile-menu-btn lg:hidden">
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
        <div class="text-xs text-amber-400 font-bold">⭐ 5.0 w Google (100+ recenzji)</div>
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

TOP5_DISTRICTS = [
    {
        "slug": "bemowo",
        "url_slug": "wymiana-akumulatora-warszawa-bemowo",
        "name": "Bemowo",
        "eta": "20–30 min",
        "title": "Wymiana Akumulatora z Dojazdem Warszawa Bemowo 24/7 | Akumulateo",
        "desc": "Auto nie odpala na Bemowie? Jelonki, Górce, Chrzanów, Boernerowo, Fort Bema. Dojazd z nowym akumulatorem w 20-30 min. Sprawdź cennik: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Bemowo 24/7",
        "areas": "Jelonki Północne, Jelonki Południowe, Górce, Chrzanów, Boernerowo, Fort Bema, Lotnisko Babice, Bemowo-Lotnisko, Marynin, ul. Powstańców Śląskich, trasa S8",
        "description_body": "Rozładowany akumulator na Bemowie? Nasi mobilni mechanicy dojeżdżają w 20–30 minut na Jelonki, Górce, Chrzanów czy Boernerowo. Wjeżdżamy do podziemnych hal garażowych, testujemy instalację elektryczną i montujemy nową, markową baterię AGM/EFB z kodowaniem BMS.",
        "faq_garage": "Czy serwisant zjedzie do garażu podziemnego na osiedlu przy ul. Pełczyńskiego lub Batalionów Chłopskich?",
        "faq_garage_ans": "Tak. Nasze auta serwisowe oraz przenośne startery mikroprocesorowe bez trudu mieszczą się we wszystkich podziemnych halach garażowych na Bemowie (wysokość wjazdu od 1.90m)."
    },
    {
        "slug": "wola",
        "url_slug": "wymiana-akumulatora-warszawa-wola",
        "name": "Wola",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Wola 24/7 | Rozruch i Wymiana",
        "desc": "Rozładowany akumulator na Woli (Odolany, Koło, Mirów, Czyste)? Przyjedziemy w 20-30 minut. Awaryjny rozruch boosterem i montaż akumulatora 24h. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Wola 24h/7",
        "areas": "Odolany (Jana Kazimierza, Ordona), Koło, Czyste, Mirów, Młynów, Ulrychów, Rondo Daszyńskiego, Kasprzaka, Towarowa",
        "description_body": "Błyskawiczna pomoc z akumulatorem na warszawskiej Woli. Obsługujemy zarówno nowe osiedla na Odolanach, jak i biurowce w centrum biznesowym przy Rondzie Daszyńskiego. Wjeżdżamy do podziemnych hal garażowych, montujemy akumulator z podtrzymaniem pamięci OBD.",
        "faq_garage": "Czy dojedziecie do ciasnego garażu podziemnego na Odolanach (ul. Jana Kazimierza)?",
        "faq_garage_ans": "Tak. Codziennie realizujemy interwencje w halach garażowych na Odolanach i przy Kasprzaka. Posiadamy mobilny sprzęt rozruchowy i podnośnikowy dostosowany do ciasnych miejsc parkingowych."
    },
    {
        "slug": "ursynow",
        "url_slug": "wymiana-akumulatora-warszawa-ursynow",
        "name": "Ursynów",
        "eta": "20–30 min",
        "title": "Wymiana Akumulatora z Dojazdem Warszawa Ursynów 24h | Akumulateo",
        "desc": "Mobilny serwis akumulatorów na Ursynowie (Kabaty, Imielin, Stokłosy, Natolin). Awaryjny rozruch i wymiana akumulatora z dojazdem 24/7. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Ursynów 24/7",
        "areas": "Kabaty, Imielin, Stokłosy, Natolin, Dąbrówka, Grabów, Pyry, hale garażowe wzdłuż al. KEN, ul. Rosoła, Płaskowickiej",
        "description_body": "Rozładowany akumulator na Ursynowie? Dojedziemy pod Twój blok, dom jednorodzinny lub do garażu podziemnego w 20–30 minut. Sprawdzimy stan starej baterii testerem cyfrowym, a gdy to konieczne – zamontujemy fabrycznie nowy akumulator AGM lub kwasowy i zakodujemy go w komputerze auta.",
        "faq_garage": "Mieszkam na Kabatach / Natolinie – jak szybko dotrze mechanik?",
        "faq_garage_ans": "Średni czas dotarcia na Ursynowie wynosi 20–25 minut. Nasze patrole stacjonują w pobliżu trasy S2 / Puławskiej i al. KEN."
    },
    {
        "slug": "srodmiescie",
        "url_slug": "wymiana-akumulatora-warszawa-srodmiescie",
        "name": "Śródmieście",
        "eta": "20–30 min",
        "title": "Awaryjne Odpalanie i Wymiana Akumulatora Śródmieście 24h | Akumulateo",
        "desc": "Śródmieście Warszawa: pogotowie akumulatorowe 24/7. Wjazd do stref i garaży podziemnych. Diagnostyka, montaż i kodowanie akumulatora. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Śródmieście 24/7",
        "areas": "Muranów, Powiśle, Solec, Ujazdów, Stare Miasto, Centrum, Plac Zbawiciela, Dworzec Centralny, Marszałkowska, Aleje Jerozolimskie",
        "description_body": "Pomoc z akumulatorem w ścisłym centrum Warszawy. Znamy specyfikę stref płatnego parkowania, ograniczonego ruchu i ciasnych parkingów. Przyjeżdżamy z boosterem 12V/24V i nową baterią pod wskazany adres o każdej porze dnia i nocy.",
        "faq_garage": "Samochód stoi w strefie płatnego parkowania w Centrum – jak wygląda dojazd?",
        "faq_garage_ans": "Nasz serwisant podjeżdża bezpośrednio pod pojazd. Koszty postoju w strefie podczas interwencji są po naszej stronie."
    },
    {
        "slug": "bielany",
        "url_slug": "wymiana-akumulatora-warszawa-bielany",
        "name": "Bielany",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Bielany 24/7 | Wymiana Akumulatora z Dojazdem",
        "desc": "Pomoc z akumulatorem Warszawa Bielany: Chomiczówka, Wrzeciono, Młociny, Słodowiec. Sprawdzenie prądu i nowy akumulator u klienta. Zadzwoń: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Bielany 24h/7",
        "areas": "Chomiczówka, Wrzeciono, Młociny, Wawrzyszew, Słodowiec, Stare Bielany, Marymont, trasa S7 / Wisłostrada / Kasprowicza",
        "description_body": "Całodobowy mobilny serwis akumulatorów na Bielanach. Dowozimy akumulatory do aut osobowych, dostawczych i hybryd. Zabieramy zużytą baterię do utylizacji, zdejmując z Ciebie konieczność płacenia kaucji 30 zł.",
        "faq_garage": "Czy akumulator jest wymieniany od ręki, czy trzeba czekać na dostawę?",
        "faq_garage_ans": "Wymiana odbywa się od ręki w 20–30 minut. Nasz bus serwisowy wozi pełen asortyment baterii Varta, Yuasa i Bosch dopasowanych do 98% marek aut."
    }
]

def generate_district_injection(d):
    schema = {
        "@context": "https://schema.org",
        "@type": "EmergencyService",
        "name": f"Akumulateo – Pogotowie Akumulatorowe Warszawa {d['name']} 24/7",
        "url": f"https://www.akumulateo.pl/{d['url_slug']}",
        "telephone": "+48696556446",
        "priceRange": "$$",
        "image": "https://images.squarespace-cdn.com/content/v1/685d174157b18362d5b7b0f3/7c219de6-f0cf-4151-a1a4-eac82a1de5d2/akumulateo-hero-pagespeed.jpg",
        "areaServed": {
            "@type": "AdministrativeArea",
            "name": f"{d['name']}, Warszawa"
        },
        "description": d["desc"],
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

  <!-- HERO DZIELNICY -->
  <section class="relative px-4 py-12 md:py-16 bg-gradient-to-b from-slate-900 via-slate-900 to-slate-950 border-b border-slate-800 text-center">
    <div class="max-w-4xl mx-auto">
      <div class="inline-flex items-center gap-2 bg-amber-500/10 border border-amber-500/30 text-amber-400 px-3.5 py-1.5 rounded-full text-xs font-black uppercase tracking-wider mb-5">
        <span>⚡ Pogotowie Akumulatorowe Warszawa {d['name']} 24h</span>
      </div>
      <h1 class="text-3xl sm:text-5xl font-black text-white tracking-tight leading-tight mb-5">
        {d['h1']}
      </h1>
      <p class="text-slate-300 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed mb-8">
        {d['description_body']}
      </p>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-3">
        <a href="tel:+48696556446" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black px-6 py-4 rounded-xl shadow-xl shadow-amber-500/25 transition transform active:scale-95 text-base sm:text-lg">
          <span>📞 Zadzwoń: 696 556 446</span>
        </a>
      </div>
      <div class="mt-3 text-xs text-slate-400 font-semibold">
        ⏱️ Czas dojazdu na {d['name']}: <span class="text-emerald-400 font-bold">{d['eta']}</span>
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
        Nie trać czasu na szukanie stacjonarnego sklepu ani holowanie auta. Nie prowadzimy punktu odbioru na terenie {d['name']} – <strong>nasz serwisant przyjeżdża bezpośrednio pod Twój adres</strong> z fabrycznie nową baterią i montuje ją na miejscu w 20–30 minut.
      </p>
    </div>
  </section>

  <!-- OBSZAR INTERWENCJI I REJONY -->
  <section class="max-w-7xl mx-auto px-4 py-8">
    <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-10 mb-8">
      <h2 class="text-2xl sm:text-3xl font-black text-white mb-3">Rejony obsługi: Warszawa {d['name']}</h2>
      <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-6">
        Nasi technicy stacjonują mobilnie, obsługując na terenie dzielnicy {d['name']} m.in.: <strong>{d['areas']}</strong>.
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

  <!-- FAQ DZIELNICOWE -->
  <section class="max-w-7xl mx-auto px-4 py-8">
    <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-10">
      <h3 class="text-2xl font-black text-white mb-6">Najczęstsze pytania kierowców – {d['name']} (FAQ)</h3>
      <div class="space-y-6">
        <div class="border-b border-slate-800 pb-5">
          <div class="text-amber-400 font-bold text-base mb-2">{d['faq_garage']}</div>
          <p class="text-slate-300 text-sm leading-relaxed">
            {d['faq_garage_ans']}
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
      <h3 class="text-2xl sm:text-3xl font-black text-white mb-4">Padł akumulator: Warszawa {d['name']}?</h3>
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

    injection_code = f"""<!-- ========================================================
     AKUMULATEO – {d['name'].upper()} PAGE HEADER INJECTION (SQUARESPACE 7.1)
     Dedykowany dla: /{d['url_slug']}
     ======================================================== -->

<!-- 1. SCHEMA.ORG EMERGENCY SERVICE JSON-LD -->
<script type="application/ld+json">
{schema_str}
</script>

<!-- 2. ZOPTYMALIZOWANY WEWNĘTRZNY TAILWIND CSS -->
<style id="akumulateo-optimized-tailwind">
{TAILWIND_CSS}
</style>

<!-- 3. STYLE IZOLUJĄCE I UKRYWAJĄCE SZABLON SQUARESPACE -->
<style id="akumulateo-{d['slug']}-custom-styles">
body {{
  background-color: #020617 !important;
}}

body #header,
body footer.sections,
body #footer-sections,
body section.page-section,
body #page-regions section,
body #sections > section {{
  display: none !important;
}}

body #siteWrapper {{
  min-height: 0 !important;
  height: auto !important;
  padding: 0 !important;
  margin: 0 !important;
}}

body #page,
body #page-regions,
body section.region,
body main#page {{
  padding: 0 !important;
  margin: 0 !important;
  max-width: 100% !important;
  width: 100% !important;
}}

@keyframes akumulateo-pulse {{
  0% {{ transform: scale(0.95); opacity: 0.85; }}
  50% {{ transform: scale(1.15); opacity: 1; }}
  100% {{ transform: scale(0.95); opacity: 0.85; }}
}}
.akumulateo-pulse-dot {{
  animation: akumulateo-pulse 2s infinite ease-in-out;
}}

/* Mobilny Przycisk Menu – Wysoki Kontrast */
.ak-mobile-menu-btn {{
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
}}

@media (min-width: 640px) {{
  .ak-mobile-menu-btn {{
    gap: 5px !important;
    border-radius: 12px !important;
    padding: 6px 10px !important;
    min-height: 38px !important;
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
  font-size: 10.5px !important;
  font-weight: 900 !important;
  letter-spacing: 0.06em !important;
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
  width: 15px !important;
  height: 15px !important;
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
</style>

<!-- 4. TEMPLATE DZIELNICY -->
<template id="akumulateo-{d['slug']}-template">
{content_html}
</template>

<!-- 5. NATYCHMIASTOWY SKRYPT MONTAŻU (HIGH SPEED SSR EMULATION) -->
<script>
(function() {{
  function mountAkumulateo{d['name'].replace('Ś','S').replace('Ł','L').replace('Ó','O')} () {{
    if (document.getElementById('akumulateo-{d['slug']}-wrapper')) return true;
    
    var tpl = document.getElementById('akumulateo-{d['slug']}-template');
    if (!tpl) return false;
    
    var parent = document.querySelector('#sections') || 
                 document.querySelector('main#page') || 
                 document.querySelector('#page') || 
                 document.body;
    if (!parent) return false;
    
    var wrapper = document.createElement('div');
    wrapper.id = 'akumulateo-{d['slug']}-wrapper';
    wrapper.appendChild(tpl.content.cloneNode(true));
    
    if (parent.firstChild) {{
      parent.insertBefore(wrapper, parent.firstChild);
    }} else {{
      parent.appendChild(wrapper);
    }}
    return true;
  }}

  if (!mountAkumulateo{d['name'].replace('Ś','S').replace('Ł','L').replace('Ó','O')}()) {{
    if (window.MutationObserver) {{
      var obs = new MutationObserver(function() {{
        if (mountAkumulateo{d['name'].replace('Ś','S').replace('Ł','L').replace('Ó','O')}()) {{
          obs.disconnect();
        }}
      }});
      obs.observe(document.documentElement, {{ childList: true, subtree: true }});
    }}
    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', mountAkumulateo{d['name'].replace('Ś','S').replace('Ł','L').replace('Ó','O')});
    }}
    window.addEventListener('load', mountAkumulateo{d['name'].replace('Ś','S').replace('Ł','L').replace('Ó','O')});
  }}
}})();
</script>
"""
    return injection_code

def main():
    print("🚀 Generowanie pakietów Page Header Injection dla TOP 5 dzielnic...")
    for d in TOP5_DISTRICTS:
        code = generate_district_injection(d)
        file_path = os.path.join(SNIPPETS_DIR, f"{d['slug']}-page-header-injection.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"  ✅ {d['name']} -> {file_path} ({len(code)} znaków)")

    print("\n🎉 Sukces! Wszystkie 5 pakietów wstrzyknięć zostały pomyślnie wygenerowane.")

if __name__ == "__main__":
    main()
