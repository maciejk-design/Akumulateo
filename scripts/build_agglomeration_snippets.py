#!/usr/bin/env python3
"""
Generator kompletnych pakietów Page Header Injection dla 14 miast aglomeracji podwarszawskiej:
1. Pruszków (/wymiana-akumulatora-pruszkow)
2. Piastów (/wymiana-akumulatora-piastow)
3. Brwinów (/wymiana-akumulatora-brwinow)
4. Milanówek (/wymiana-akumulatora-milanowek)
5. Legionowo (/wymiana-akumulatora-legionowo)
6. Modlin (/wymiana-akumulatora-modlin)
7. Nowy Dwór Mazowiecki (/wymiana-akumulatora-nowy-dwor-mazowiecki)
8. Mińsk Mazowiecki (/wymiana-akumulatora-minsk-mazowiecki)
9. Konstancin-Jeziorna (/wymiana-akumulatora-konstancin-jeziorna)
10. Łomianki (/wymiana-akumulatora-lomianki)
11. Otwock (/wymiana-akumulatora-otwock)
12. Marki (/wymiana-akumulatora-marki)
13. Grodzisk Mazowiecki (/wymiana-akumulatora-grodzisk-mazowiecki)
14. Wołomin (/wymiana-akumulatora-wolomin)

Standard Brandbook v2.2:
- Kontrastowy Dark Mode (#020617 / #0f172a)
- Zero mikrofontów (min. 15.5px/16.5px, line-height 1.65)
- Aktywny link w logo (href="/")
- Responsywny nagłówek <= 340px
- Wyrazisty przycisk MENU z bursztynową ramką (#f59e0b) i etykietą MENU/ZAMKNIJ
- Czas dojazdu ekspresowego
- Prekwalifikacja mobilna (Brak sklepu stacjonarnego)
- Oficjalne marki: Varta, Yuasa (YUASA), Bosch, 4Max (zero Centra/Banner)
- Schema.org EmergencyService JSON-LD (5.0★, 160+ opinii)
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
        <span class="hidden sm:inline font-bold text-slate-900">• Dojazd 20–40 min w aglomeracji warszawskiej</span>
      </div>
      <div class="flex items-center gap-2.5 flex-shrink-0 text-[11px] font-bold">
        <span class="hidden md:inline-flex items-center gap-1 font-extrabold text-slate-950 bg-amber-300/90 px-1.5 py-0.5 rounded text-[10px]" title="We speak English – call us directly">🇬🇧 We speak English</span>
        <a href="https://g.page/r/CXjN9llopHR_EBM/" target="_blank" rel="noopener noreferrer" class="hover:text-slate-800 hover:underline flex items-center gap-1 transition cursor-pointer" title="Zobacz opinie Akumulateo w Google Maps">
          <span>⭐ 5.0 w Google (160+ opinii) ↗</span>
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
  </header>

  <!-- MOBILNE MENU ROZWIJANE (DRAWER) -->
  <div id="akSubpageMobileDrawer" class="hidden lg:hidden bg-slate-900 border-b border-slate-800 px-4 py-4 space-y-3 text-slate-200 text-sm font-bold shadow-2xl">
    <a href="/#uslugi" class="block py-2 px-3 rounded-lg hover:bg-slate-800 transition">Usługi mobilne 24h</a>
    <a href="/#cennik" class="block py-2 px-3 rounded-lg hover:bg-slate-800 transition">Cennik interwencji</a>
    <a href="/#marki" class="block py-2 px-3 rounded-lg hover:bg-slate-800 transition">Oficjalne Marki (Varta, Yuasa, Bosch)</a>
    <a href="/obszar-dzialania-warszawa-i-okolice" class="block py-2 px-3 rounded-lg bg-amber-500/10 text-amber-400 font-extrabold transition">Obszar działania (18 dzielnic & miasta)</a>
    <a href="/#opinie" class="block py-2 px-3 rounded-lg hover:bg-slate-800 transition">Opinie klientów Google (5.0★)</a>
    <a href="/#faq" class="block py-2 px-3 rounded-lg hover:bg-slate-800 transition">Częste pytania (FAQ)</a>
    <div class="pt-2 border-t border-slate-800">
      <a href="tel:+48696556446" class="flex items-center justify-center gap-2 w-full bg-amber-500 text-slate-950 font-black py-3 rounded-xl shadow-lg">
        <span>📞 Zadzwoń: 696 556 446</span>
      </a>
    </div>
  </div>
"""

UNIFIED_FOOTER_HTML = """
  <!-- STOPKA UNIWERSALNA -->
  <footer class="bg-slate-950 border-t border-slate-800 px-4 py-12 text-slate-300 text-sm">
    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-8 mb-10">
      
      <div class="space-y-3">
        <div class="text-xl font-black text-white">AKUMULAT<span class="text-amber-500">E</span>O</div>
        <p class="text-slate-400 text-xs leading-relaxed">
          Mobilny serwis i pogotowie akumulatorowe 24h na terenie Warszawy oraz aglomeracji podwarszawskiej. Wymiana, diagnostyka i awaryjny rozruch pod domem klienta.
        </p>
        <div class="text-xs text-amber-400 font-bold">⭐ 5.0 w Google (160+ recenzji)</div>
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

AGGLOMERATION_TOWNS = [
    {
        "slug": "pruszkow",
        "url_slug": "wymiana-akumulatora-pruszkow",
        "name": "Pruszków",
        "eta": "20–30 min",
        "title": "Wymiana Akumulatora z Dojazdem Pruszków 24/7 | Akumulateo",
        "desc": "Rozładowany akumulator w Pruszkowie? Centrum, Gąsin, Żbików, Bąki, Ostoja, Michałowice. Dojazd 24/7 z nową baterią pod dom. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Pruszków 24/7",
        "areas": "Pruszków Centrum, Gąsin, Żbików, Ostoja, Bąki, Malichy, Tworki, Michałowice, Raszyn, Al. Jerozolimskie, autostrada A2",
        "description_body": "Awaria akumulatora w Pruszkowie lub okolicach? Nasi technicy docierają autostradą A2 oraz Alejami Jerozolimskimi w 20–30 minut pod Twój dom, blok lub firmę. Pełna diagnostyka komputerowa alternatora, montaż nowej baterii AGM/EFB i kodowanie BMS na miejscu.",
        "faq_garage": "Czy dojeżdżacie do osiedli w Pruszkowie (np. Osiedle Staszica, Parkowe) i garaży podziemnych?",
        "faq_garage_ans": "Tak, nasze wozy serwisowe i mobilne startery bez trudu wjeżdżają do hal garażowych na pruszkowskich osiedlach."
    },
    {
        "slug": "piastow",
        "url_slug": "wymiana-akumulatora-piastow",
        "name": "Piastów",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Piastów 24/7 | Wymiana Akumulatora z Dojazdem",
        "desc": "Rozładowany akumulator w Piastowie? Całodobowa wymiana z dojazdem pod dom lub firmę. Diagnostyka, montaż i kodowanie BMS. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Piastów 24h/7",
        "areas": "Piastów Północ, Piastów Południe, Osiedle Ogińskiego, Al. Tysiąclecia, Dworzec PKP Piastów, ul. Warszawska, Orzeszkowej",
        "description_body": "Padł akumulator w Piastowie? Błyskawiczny dojazd Alejami Jerozolimskimi prosto pod wskazany adres. Badamy stan instalacji elektrycznej, instalujemy nowy markowy akumulator i odbieramy stary do utylizacji.",
        "faq_garage": "Stoję pod blokiem w Piastowie – jak szybko dotrze mechanik?",
        "faq_garage_ans": "Średni czas dojazdu do Piastowa wynosi 20–25 minut. Technik ma przy sobie terminal płatniczy i pełen asortyment baterii."
    },
    {
        "slug": "brwinow",
        "url_slug": "wymiana-akumulatora-brwinow",
        "name": "Brwinów",
        "eta": "25–35 min",
        "title": "Wymiana Akumulatora z Dojazdem Brwinów 24/7 | Pogotowie Akumulateo",
        "desc": "Awaria akumulatora w Brwinowie, Otrębusach lub Żółwinie? Mobilny serwis akumulatorów 24/7. Wymiana na posesji klienta. Zadzwoń: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Brwinów i Okolice 24/7",
        "areas": "Brwinów Centrum, Otrębusy, Żółwin, Owczarnia, Kotowice, Biskupice, ul. Grodziska, Pszczelińska, droga 719",
        "description_body": "Auto nie odpala w Brwinowie lub Otrębusach? Przyjeżdżamy w 25–35 minut pod Twój dom lub na posesję. Wymiana akumulatora odbywa się bez konieczności holowania pojazdu do warsztatu.",
        "faq_garage": "Mieszkam w domu w Żółwinie / Owczarni – czy dojedziecie na posesję?",
        "faq_garage_ans": "Tak, obsługujemy całą gminę Brwinów wraz z okolicznymi miejscowościami. Dojeżdżamy bezpośrednio na podjazdy posesji prywatnych."
    },
    {
        "slug": "milanowek",
        "url_slug": "wymiana-akumulatora-milanowek",
        "name": "Milanówek",
        "eta": "25–35 min",
        "title": "Pogotowie Akumulatorowe Milanówek 24/7 | Wymiana Akumulatora z Dojazdem",
        "desc": "Samochód nie odpala w Milanówku? Całodobowy mobilny serwis akumulatorów z dojazdem. Markowe baterie Varta, Yuasa, Bosch. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Milanówek 24h/7",
        "areas": "Milanówek Centrum, Grudów, Turczynek, Kazimierówka, Podkowa Leśna, ul. Królewska, Warszawska, trasa 719, A2",
        "description_body": "Rozładowana bateria w Milanówku lub Podkowie Leśnej? Dojedziemy w 25–35 minut autostradą A2 lub drogą 719. Wymiana baterii z podtrzymaniem pamięci OBD i adaptacją komputerową.",
        "faq_garage": "Czy obsługujecie także Podkowę Leśną?",
        "faq_garage_ans": "Tak, regularnie interweniujemy w Milanówku oraz sąsiadującej Podkowie Leśnej."
    },
    {
        "slug": "legionowo",
        "url_slug": "wymiana-akumulatora-legionowo",
        "name": "Legionowo",
        "eta": "25–35 min",
        "title": "Pogotowie Akumulatorowe Legionowo 24/7 | Wymiana z Dojazdem",
        "desc": "Rozładowany akumulator w Legionowie lub Jabłonnie? Całodobowa wymiana z dojazdem pod dom. Diagnostyka, montaż i kodowanie BMS. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Legionowo i Jabłonna 24/7",
        "areas": "Legionowo Centrum, Jabłonna, Piaski, Osiedle Sobieskiego, Bukowiec, Chotomów, ul. Zegrzyńska, DK61, al. Legionów",
        "description_body": "Padł akumulator w Legionowie lub Jabłonnie? Ekspresowy dojazd drogą DK61 prosto pod wskazany adres. Oferujemy nowe baterie AGM/EFB z fabryczną gwarancją oraz bezpieczny rozruch boosterem.",
        "faq_garage": "Czy wymienicie akumulator na parkingu osiedlowym w Legionowie?",
        "faq_garage_ans": "Tak, wymieniamy akumulatory bezpośrednio na parkingach pod blokami, pod domami jednorodzinnymi oraz pod firmami w Legionowie."
    },
    {
        "slug": "modlin",
        "url_slug": "wymiana-akumulatora-modlin",
        "name": "Modlin i Lotnisko Modlin",
        "eta": "35–50 min",
        "title": "Pogotowie Akumulatorowe Lotnisko Modlin 24/7 | Rozruch i Wymiana",
        "desc": "Rozładowany akumulator na parkingu przy Lotnisku Modlin? Całodobowa pomoc, awaryjny rozruch boosterem i montaż nowej baterii. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Lotnisko Modlin 24h/7",
        "areas": "Parkingi Lotniska Modlin P1–P7, Twierdza Modlin, Czosnów, Nowy Dwór Mazowiecki, trasa S7, DK62",
        "description_body": "Wróciłeś z podróży samolotem i auto nie odpala na parkingu przy Lotnisku Warszawa-Modlin? Pełnimy całodobowy dyżur ratunkowy z dojazdem trasą S7 bezpośrednio pod Twoje auto na parkingach lotniskowych.",
        "faq_garage": "Auto stoi na parkingu długoterminowym przy Lotnisku Modlin – jak szybko dotrzecie?",
        "faq_garage_ans": "Czas dojazdu trasą S7 wynosi zazwyczaj 35–45 minut. Posiadamy mocne startery 12V/24V i nowe baterie od ręki."
    },
    {
        "slug": "nowy-dwor-mazowiecki",
        "url_slug": "wymiana-akumulatora-nowy-dwor-mazowiecki",
        "name": "Nowy Dwór Mazowiecki",
        "eta": "35–50 min",
        "title": "Pogotowie Akumulatorowe Nowy Dwór Mazowiecki 24/7 | Akumulateo",
        "desc": "Padł akumulator w Nowym Dworze Mazowieckim? Całodobowa pomoc akumulatorowa, rozruch boosterem i wymiana pod domem. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Nowy Dwór Mazowiecki 24h/7",
        "areas": "Nowy Dwór Centrum, Osiedle Młodych, Twierdza Modlin, Kazuń Nowy, Czosnów, ul. Warszawska, Leśna, DK85",
        "description_body": "Awaria akumulatora w Nowym Dworze Mazowieckim? Przyjeżdżamy w 35–50 minut trasą S7 pod dom, blok lub zakład pracy. Diagnostyka alternatora i montaż nowej baterii na miejscu.",
        "faq_garage": "Czy obsługujecie Osiedle Młodych w Nowym Dworze?",
        "faq_garage_ans": "Tak, obsługujemy całe miasto Nowy Dwór Mazowiecki wraz z Osiedlem Młodych i okolicznymi miejscowościami."
    },
    {
        "slug": "minsk-mazowiecki",
        "url_slug": "wymiana-akumulatora-minsk-mazowiecki",
        "name": "Mińsk Mazowiecki",
        "eta": "35–50 min",
        "title": "Wymiana Akumulatora Mińsk Mazowiecki 24/7 | Pogotowie Akumulateo",
        "desc": "Pogotowie akumulatorowe Mińsk Mazowiecki, Halinów, Sulejówek. Wymiana akumulatora pod domem z kodowaniem BMS 24/7. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Mińsk Mazowiecki 24/7",
        "areas": "Mińsk Mazowiecki Centrum, Halinów, Sulejówek, Dębe Wielkie, Stojadła, autostrada A2, DK92, ul. Warszawska",
        "description_body": "Rozładowany akumulator w Mińsku Mazowieckim lub Halinowie? Dojeżdżamy autostradą A2 w 35–50 minut. Profesjonalny dobór baterii wg katalogu producenta, montaż i adaptacja BMS.",
        "faq_garage": "Czy dojedziecie do Stojadeł lub Dębego Wielkiego?",
        "faq_garage_ans": "Tak, obsługujemy trasę autostrady A2 i drogi 92 wraz ze wszystkimi przyległymi miejscowościami."
    },
    {
        "slug": "konstancin-jeziorna",
        "url_slug": "wymiana-akumulatora-konstancin-jeziorna",
        "name": "Konstancin-Jeziorna",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Konstancin-Jeziorna 24/7 | Dojazd z Baterią",
        "desc": "Konstancin-Jeziorna, Bielawa, Skolimów: mobilny serwis akumulatorów 24/7. Dojazd pod posesję, wymiana baterii AGM i kodowanie. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Konstancin-Jeziorna 24h/7",
        "areas": "Konstancin Centrum, Skolimów, Bielawa, Klarysew, Chylice, Obory, Jeziorna, ul. Warszawska, Piaseczyńska, droga 724",
        "description_body": "Padł akumulator w Konstancinie-Jeziornie, Skolimowie lub Bielawie? Szybki dojazd od strony Wilanowa i Ursynowa w 20–30 minut bezpośrednio pod rezydencję, dom lub parking.",
        "faq_garage": "Posiadam nowoczesne auto hybrydowe z akumulatorem AGM w Konstancinie – czy poradzicie sobie z kodowaniem?",
        "faq_garage_ans": "Tak, dysponujemy zaawansowanymi testerami diagnostycznymi do kodowania BMS w autach marek BMW, Mercedes, Porsche, Audi, Lexus i Volvo."
    },
    {
        "slug": "lomianki",
        "url_slug": "wymiana-akumulatora-lomianki",
        "name": "Łomianki",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Łomianki 24/7 | Wymiana Akumulatora z Dojazdem",
        "desc": "Rozładowany akumulator w Łomiankach, Dziekanowie lub Kiełpinie? Pogotowie akumulatorowe 24/7. Przyjedziemy w 20-30 min. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Łomianki 24h/7",
        "areas": "Łomianki Centralne, Dziekanów Leśny, Dziekanów Polski, Kiełpin, Buraków, Dąbrowa, trasa DK7, ul. Warszawska",
        "description_body": "Awaria akumulatora w Łomiankach? Dojeżdżamy Wisłostradą i trasą DK7 w 20–30 minut prosto z Bielan pod Twój dom lub firmę. Pomiary, montaż nowej baterii i bezpłatny recykling zużytego akumulatora.",
        "faq_garage": "Mieszkam w Dziekanowie Leśnym – jak szybko przyjedzie serwis?",
        "faq_garage_ans": "Czas dojazdu do Łomianek i Dziekanowa wynosi średnio 20–25 minut od zgłoszenia telefonicznego."
    },
    {
        "slug": "otwock",
        "url_slug": "wymiana-akumulatora-otwock",
        "name": "Otwock i Józefów",
        "eta": "25–40 min",
        "title": "Wymiana Akumulatora z Dojazdem Otwock, Józefów 24/7 | Akumulateo",
        "desc": "Awaria akumulatora w Otwocku, Józefowie lub Karczewie? Pogotowie akumulatorowe 24h z dojazdem. Nowe baterie Varta, Yuasa, Bosch. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Otwock i Józefów 24h/7",
        "areas": "Otwock Centrum, Józefów, Świdry Wielkie, Karczew, Michalin, Falenica, Wał Miedzeszyński, trasa S17, ul. Kołłątaja",
        "description_body": "Auto nie odpala w Otwocku, Józefowie lub Karczewie? Docieramy trasą S17 i Wałem Miedzeszyńskim w 25–40 minut. Montujemy baterię na posesji klienta, eliminując potrzebę wzywania lawety.",
        "faq_garage": "Czy dojeżdżacie do domów w Józefowie i Michalinie?",
        "faq_garage_ans": "Tak, obsługujemy cały powiat otwocki. Dojeżdżamy pod domy w Józefowie, Świdrze i Karczewie."
    },
    {
        "slug": "marki",
        "url_slug": "wymiana-akumulatora-marki",
        "name": "Marki i Ząbki",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Marki, Ząbki 24/7 | Dojazd z Akumulatorem",
        "desc": "Padł akumulator w Markach lub Ząbkach? Mobilna wymiana z montażem na miejscu 24/7. Dojazd w 20-30 min. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Marki i Ząbki 24h/7",
        "areas": "Marki Pustelnik, Marki Struga, Ząbki Centrum, Drewnica, ul. Piłsudskiego, Radzymińska, trasa S8",
        "description_body": "Rozładowany akumulator w Markach lub Ząbkach? Nasi technicy docierają trasą S8 oraz ul. Radzymińską w 20–30 minut pod Twój adres. Badanie instalacji, montaż nowej baterii i kodowanie Start-Stop.",
        "faq_garage": "Stoję w Ząbkach pod blokiem – ile potrwa dojazd?",
        "faq_garage_ans": "Dojazd do Marek i Ząbek zajmuje średnio 20–25 minut. Przyjeżdżamy w pełni wyposażonym autem serwisowym."
    },
    {
        "slug": "grodzisk-mazowiecki",
        "url_slug": "wymiana-akumulatora-grodzisk-mazowiecki",
        "name": "Grodzisk Mazowiecki",
        "eta": "30–45 min",
        "title": "Wymiana Akumulatora Grodzisk Mazowiecki 24/7 | Pogotowie z Dojazdem",
        "desc": "Mobilne pogotowie akumulatorowe Grodzisk Mazowiecki. Dowóz markowego akumulatora i profesjonalny montaż pod domem 24/7. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Grodzisk Mazowiecki 24/7",
        "areas": "Grodzisk Mazowiecki Centrum, Łąki, Osiedle Piaskowa, Książenice, Chlebnia, autostrada A2, trasa S8, ul. Królewska",
        "description_body": "Padł akumulator w Grodzisku Mazowieckim lub Książenicach? Dojeżdżamy autostradą A2 w 30–45 minut z fabrycznie nową baterią Varta, Yuasa lub Bosch. Montaż, adaptacja BMS i recykling na miejscu.",
        "faq_garage": "Czy dojeżdżacie do domów w Książenicach pod Grodziskiem?",
        "faq_garage_ans": "Tak, obsługujemy miasto Grodzisk Mazowiecki oraz przyległe osiedla domów jednorodzinnych w Książenicach i Chlebni."
    },
    {
        "slug": "wolomin",
        "url_slug": "wymiana-akumulatora-wolomin",
        "name": "Wołomin i Kobyłka",
        "eta": "25–40 min",
        "title": "Pogotowie Akumulatorowe Wołomin, Kobyłka 24/7 | Montaż pod Domem",
        "desc": "Auto nie odpala w Wołominie, Kobyłce lub Zielonce? Mobilny serwis akumulatorów 24/7. Dowóz, montaż i kodowanie na miejscu. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Wołomin i Kobyłka 24h/7",
        "areas": "Wołomin Centrum, Kobyłka, Zielonka, Ossów, Majdan, Duczki, trasa S8, droga 634, ul. Armii Krajowej",
        "description_body": "Awaria akumulatora w Wołominie, Kobyłce czy Zielonce? Szybki dojazd trasą S8 w 25–40 minut. Montaż akumulatora pod domem klienta z 2-letnią gwarancją producenta i badaniem alternatora.",
        "faq_garage": "Czy obsługujecie także Zielonkę i Kobyłkę?",
        "faq_garage_ans": "Tak, technicy Akumulateo obsługują cały powiat wołomiński – Wołomin, Kobyłkę, Zielonkę i Ossów."
    }
]

def generate_town_injection(t):
    schema = {
        "@context": "https://schema.org",
        "@type": "EmergencyService",
        "name": f"Akumulateo – Pogotowie Akumulatorowe {t['name']} 24/7",
        "url": f"https://www.akumulateo.pl/{t['url_slug']}",
        "telephone": "+48696556446",
        "priceRange": "$$",
        "image": "https://images.squarespace-cdn.com/content/v1/685d174157b18362d5b7b0f3/7c219de6-f0cf-4151-a1a4-eac82a1de5d2/akumulateo-hero-pagespeed.jpg",
        "areaServed": {
            "@type": "AdministrativeArea",
            "name": f"{t['name']}, Aglomeracja Warszawska"
        },
        "description": t["desc"],
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
            "ratingCount": "160",
            "reviewCount": "160"
        }
    }
    schema_str = json.dumps(schema, ensure_ascii=False, indent=2)

    content_html = f"""
<div class="akumulateo-root bg-slate-950 text-slate-100 font-sans antialiased overflow-hidden">
  
  {NAV_HEADER_HTML}

  <!-- HERO MIASTA -->
  <section class="relative px-4 py-12 md:py-16 bg-gradient-to-b from-slate-900 via-slate-900 to-slate-950 border-b border-slate-800 text-center">
    <div class="max-w-4xl mx-auto">
      <div class="inline-flex items-center gap-2 bg-amber-500/10 border border-amber-500/30 text-amber-400 px-3.5 py-1.5 rounded-full text-xs font-black uppercase tracking-wider mb-5">
        <span>⚡ Pogotowie Akumulatorowe {t['name']} 24h</span>
      </div>
      <h1 class="text-3xl sm:text-5xl font-black text-white tracking-tight leading-tight mb-5">
        {t['h1']}
      </h1>
      <p class="text-slate-300 text-base sm:text-lg max-w-2xl mx-auto leading-relaxed mb-8">
        {t['description_body']}
      </p>
      <div class="flex flex-col sm:flex-row items-center justify-center gap-3">
        <a href="tel:+48696556446" class="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black px-6 py-4 rounded-xl shadow-xl shadow-amber-500/25 transition transform active:scale-95 text-base sm:text-lg">
          <span>📞 Zadzwoń: 696 556 446</span>
        </a>
      </div>
      <div class="mt-3 text-xs text-slate-400 font-semibold">
        ⏱️ Czas dojazdu w rejonie {t['name']}: <span class="text-emerald-400 font-bold">{t['eta']}</span>
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
        Nie trać czasu na szukanie stacjonarnego sklepu ani lawety. Nie prowadzimy punktu stacjonarnego w miejscowości {t['name']} – <strong>nasz serwisant przyjeżdża bezpośrednio pod Twój dom lub firmę</strong> z nową baterią i montuje ją na miejscu w kilkadziesiąt minut.
      </p>
    </div>
  </section>

  <!-- OBSZAR INTERWENCJI I REJONY -->
  <section class="max-w-7xl mx-auto px-4 py-8">
    <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-10 mb-8">
      <h2 class="text-2xl sm:text-3xl font-black text-white mb-3">Rejony obsługi: {t['name']} i okolice</h2>
      <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-6">
        Nasi technicy dyżurują mobilnie, obsługując w rejonie {t['name']} m.in.: <strong>{t['areas']}</strong>.
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

  <!-- FAQ MIASTA -->
  <section class="max-w-7xl mx-auto px-4 py-8">
    <div class="bg-slate-900 border border-slate-800 rounded-3xl p-6 sm:p-10">
      <h3 class="text-2xl font-black text-white mb-6">Najczęstsze pytania kierowców – {t['name']} (FAQ)</h3>
      <div class="space-y-6">
        <div class="border-b border-slate-800 pb-5">
          <div class="text-amber-400 font-bold text-base mb-2">{t['faq_garage']}</div>
          <p class="text-slate-300 text-sm leading-relaxed">
            {t['faq_garage_ans']}
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
      <h3 class="text-2xl sm:text-3xl font-black text-white mb-4">Padł akumulator: {t['name']} i okolice?</h3>
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

    clean_name = t['name'].replace('Ś','S').replace('Ł','L').replace('Ó','O').replace('Ż','Z').replace('–','-').replace(' ','_').replace('-','_').replace('ą','a').replace('ę','e').replace('ó','o').replace('ś','s').replace('ł','l').replace('ż','z').replace('ź','z').replace('ć','c').replace('ń','n')

    injection_code = f"""<!-- ========================================================
     AKUMULATEO – {t['name'].upper()} PAGE HEADER INJECTION (SQUARESPACE 7.1)
     Dedykowany dla: /{t['url_slug']}
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
<style id="akumulateo-{t['slug']}-custom-styles">
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
  color: #fbbf24 !important;
  font-weight: 900 !important;
  font-size: 11px !important;
  line-height: 1 !important;
  letter-spacing: 0.05em !important;
  padding: 6px 9px !important;
  border-radius: 10px !important;
  box-shadow: 0 0 10px rgba(245, 158, 11, 0.25) !important;
  cursor: pointer !important;
  transition: all 0.15s ease-in-out !important;
  flex-shrink: 0 !important;
}}

.ak-mobile-menu-btn:hover,
.ak-mobile-menu-btn:active {{
  background-color: #334155 !important;
  border-color: #fbbf24 !important;
  color: #ffffff !important;
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

<!-- 4. TEMPLATE MIASTA -->
<template id="akumulateo-{t['slug']}-template">
{content_html}
</template>

<!-- 5. NATYCHMIASTOWY SKRYPT MONTAŻU (HIGH SPEED SSR EMULATION) -->
<script>
(function() {{
  function mountAkumulateo{clean_name} () {{
    if (document.getElementById('akumulateo-{t['slug']}-wrapper')) return true;
    
    var tpl = document.getElementById('akumulateo-{t['slug']}-template');
    if (!tpl) return false;
    
    var parent = document.querySelector('#sections') || 
                 document.querySelector('main#page') || 
                 document.querySelector('#page') || 
                 document.body;
    if (!parent) return false;
    
    var wrapper = document.createElement('div');
    wrapper.id = 'akumulateo-{t['slug']}-wrapper';
    wrapper.appendChild(tpl.content.cloneNode(true));
    
    if (parent.firstChild) {{
      parent.insertBefore(wrapper, parent.firstChild);
    }} else {{
      parent.appendChild(wrapper);
    }}
    return true;
  }}

  if (!mountAkumulateo{clean_name}()) {{
    if (window.MutationObserver) {{
      var obs = new MutationObserver(function() {{
        if (mountAkumulateo{clean_name}()) {{
          obs.disconnect();
        }}
      }});
      obs.observe(document.documentElement, {{ childList: true, subtree: true }});
    }}
    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', mountAkumulateo{clean_name});
    }}
    window.addEventListener('load', mountAkumulateo{clean_name});
  }}
}})();
</script>
"""
    return injection_code

def main():
    print("🚀 Generowanie pakietów Page Header Injection dla 14 miast aglomeracji...")
    for t in AGGLOMERATION_TOWNS:
        code = generate_town_injection(t)
        file_path = os.path.join(SNIPPETS_DIR, f"{t['slug']}-page-header-injection.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"  ✅ {t['name']} -> {file_path} ({len(code)} znaków)")

    print("\n🎉 Sukces! Wszystkie 14 pakietów wstrzyknięć zostały pomyślnie wygenerowane.")

if __name__ == "__main__":
    main()
