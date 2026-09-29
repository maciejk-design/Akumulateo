#!/usr/bin/env python3
"""
Generator kompletnych pakietów Page Header Injection dla pozostałych 12 dzielnic Warszawy:
1. Białołęka (/wymiana-akumulatora-warszawa-bialoleka)
2. Targówek (/wymiana-akumulatora-warszawa-targowek)
3. Praga-Południe (/wymiana-akumulatora-warszawa-praga-poludnie)
4. Praga-Północ (/wymiana-akumulatora-warszawa-praga-polnoc)
5. Ochota (/wymiana-akumulatora-warszawa-ochota)
6. Włochy (/wymiana-akumulatora-warszawa-wlochy)
7. Ursus (/wymiana-akumulatora-warszawa-ursus)
8. Wilanów (/wymiana-akumulatora-warszawa-wilanow)
9. Wawer (/wymiana-akumulatora-warszawa-wawer)
10. Rembertów (/wymiana-akumulatora-warszawa-rembertow)
11. Wesoła (/wymiana-akumulatora-warszawa-wesola)
12. Żoliborz (/wymiana-akumulatora-warszawa-zoliborz)

Standard Brandbook v2.2:
- Kontrastowy Dark Mode (#020617 / #0f172a)
- Zero mikrofontów (min. 15.5px/16.5px, line-height 1.65)
- Aktywny link w logo (href="/")
- Responsywny nagłówek <= 340px
- Wyrazisty przycisk MENU z bursztynową ramką (#f59e0b) i etykietą MENU/ZAMKNIJ
- Czas dojazdu: 20-30 min
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
        <span class="hidden sm:inline font-bold text-slate-900">• Dojazd 20–30 min w Warszawie i aglomeracji</span>
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

REMAINING_12_DISTRICTS = [
    {
        "slug": "bialoleka",
        "url_slug": "wymiana-akumulatora-warszawa-bialoleka",
        "name": "Białołęka",
        "eta": "20–30 min",
        "title": "Wymiana Akumulatora z Dojazdem Warszawa Białołęka 24/7 | Akumulateo",
        "desc": "Rozładowany akumulator na Białołęce? Tarchomin, Nowodwory, Derby, Brzeziny. Dojazd pogotowia w 20-30 min. Sprawdź cennik: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Białołęka 24/7",
        "areas": "Tarchomin, Nowodwory, Żerań, Osiedle Derby, Grodzisk, Brzeziny, Choszczówka, Płudy, Dąbrówka Szlachecka, ul. Modlińska, Trasa Toruńska S8",
        "description_body": "Rozładowany akumulator na Białołęce? Nasi mobilni technicy stacjonują w pobliżu trasy S8 i ul. Modlińskiej, docierając w 20–30 minut na Tarchomin, Nowodwory czy Zieloną Białołękę (Derby). Wjeżdżamy do podziemnych hal garażowych, testujemy alternator i montujemy nową baterię AGM/EFB z kodowaniem BMS.",
        "faq_garage": "Mieszkam na Zielonej Białołęce (osiedle Derby / Skarbka z Gór) – jak szybko dojedziecie?",
        "faq_garage_ans": "Dojazd na Zieloną Białołękę realizujemy w około 20–30 minut. Nasze wozy serwisowe korzystają z trasy Toruńskiej S8 oraz ul. Głębockiej."
    },
    {
        "slug": "targowek",
        "url_slug": "wymiana-akumulatora-warszawa-targowek",
        "name": "Targówek",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Targówek 24/7 | Wymiana z Dojazdem",
        "desc": "Auto nie odpala na Targówku? Bródno, Zacisze, Targówek Mieszkaniowy/Fabryczny. Dojazd z akumulatorem w 20-30 min. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Targówek 24/7",
        "areas": "Bródno, Zacisze, Targówek Mieszkaniowy, Targówek Fabryczny, Elsnerów, ul. Kondratowicza, Radzymińska, św. Wincentego",
        "description_body": "Padł akumulator na Targówku lub Bródnie? Niezależnie czy stoisz pod blokiem przy Kondratowicza, w domku na Zaciszu czy w podziemnym garażu, przyjedziemy w 20–30 minut. Profesjonalny montaż, podtrzymanie zasilania OBD i recykling starej baterii.",
        "faq_garage": "Czy obsługujecie ciasne parkingi i garaże podziemne na Bródnie?",
        "faq_garage_ans": "Tak, posiadamy kompaktowe auta serwisowe oraz przenośne mikroprocesorowe startery booster, co pozwala na bezpieczną interwencję w każdej hali podziemnej na terenie Targówka."
    },
    {
        "slug": "praga-poludnie",
        "url_slug": "wymiana-akumulatora-warszawa-praga-poludnie",
        "name": "Praga-Południe",
        "eta": "20–30 min",
        "title": "Wymiana Akumulatora z Dojazdem Praga-Południe 24/7 | Gocław, Grochów",
        "desc": "Pogotowie akumulatorowe Praga-Południe: Gocław, Grochów, Saska Kępa, Kamionek. Dojazd w 20-30 min, diagnostyka ładowania i wymiana 24h. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Praga-Południe 24/7",
        "areas": "Gocław, Grochów, Saska Kępa, Kamionek, Przyczółek Grochowski, Witolin, ul. Ostrobramska, al. Waszyngtona, al. Stanów Zjednoczonych",
        "description_body": "Rozładowany akumulator na Pradze-Południe? Obsługujemy Gocław, Grochów, Saską Kępę i Kamionek. Dojeżdżamy w 20–30 minut pod dom lub do garażu podziemnego. Na miejscu dobieramy i montujemy markowy akumulator Varta, Yuasa lub Bosch.",
        "faq_garage": "Stoję w garażu podziemnym na osiedlu na Gocławiu – czy serwisant zjedzie na dół?",
        "faq_garage_ans": "Oczywiście. Nasz mobilny sprzęt diagnostyczno-montażowy i przenośne boostery pozwalają na pełną wymianę i odpalenie auta w dowolnym garażu podziemnym na Gocławiu."
    },
    {
        "slug": "praga-polnoc",
        "url_slug": "wymiana-akumulatora-warszawa-praga-polnoc",
        "name": "Praga-Północ",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Praga-Północ 24/7 | Akumulateo",
        "desc": "Pomoc z akumulatorem Praga-Północ: Nowa Praga, Szmulowizna, Plac Hallera, Port Praski. Dojazd w 20-30 min, test alternatora, wymiana 24h. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Praga-Północ 24/7",
        "areas": "Nowa Praga, Stara Praga, Szmulowizna, Plac Hallera, Port Praski, ul. Targowa, Jagiellońska, al. Solidarności, rondo Starzyńskiego",
        "description_body": "Awaria akumulatora na Pradze-Północ? Znamy specyfikę praskich podwórek kamienic oraz nowoczesnych osiedli w Porcie Praskim. Serwisant przyjeżdża w 20–30 minut ze sprzętem pomiarowym, podtrzymaniem pamięci OBD i fabrycznie nową baterią.",
        "faq_garage": "Auto stoi na ciasnym podwórku starej praskiej kamienicy – czy dacie radę wymienić akumulator?",
        "faq_garage_ans": "Tak, posiadamy przenośne zestawy narzędziowe i boostery, dzięki czemu możemy zrealizować wymianę lub rozruch nawet w najbardziej niedostępnych podwórkach i bramach kamienic."
    },
    {
        "slug": "ochota",
        "url_slug": "wymiana-akumulatora-warszawa-ochota",
        "name": "Ochota",
        "eta": "20–30 min",
        "title": "Wymiana Akumulatora z Dojazdem Warszawa Ochota 24/7 | Akumulateo",
        "desc": "Rozładowany akumulator na Ochocie? Szczęśliwice, Rakowiec, Stara Ochota, Filtry. Dojazd w 20-30 min. Sprawdzenie ładowania i nowa bateria 24h: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Ochota 24/7",
        "areas": "Szczęśliwice, Rakowiec, Stara Ochota, Filtry, Plac Narutowicza, ul. Grójecka, Al. Jerozolimskie, Włodarzewska, Bitwy Warszawskiej 1920 r.",
        "description_body": "Padł akumulator na Ochocie? Nasi mechanicy docierają w 20–30 minut na Szczęśliwice (m.in. osiedla przy Włodarzewskiej), Rakowiec czy Starą Ochotę. Badamy prąd spoczynkowy, montujemy akumulator AGM/EFB i kodujemy system Start-Stop.",
        "faq_garage": "Mieszkam na osiedlu przy ul. Włodarzewskiej – czy wjedziecie do garażu podziemnego?",
        "faq_garage_ans": "Tak, regularnie interweniujemy w halach garażowych na Szczęśliwicach i przy ul. Włodarzewskiej. Wymiana baterii odbywa się bezpośrednio na Twoim miejscu postojowym."
    },
    {
        "slug": "wlochy",
        "url_slug": "wymiana-akumulatora-warszawa-wlochy",
        "name": "Włochy",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Włochy 24/7 | Okęcie, Dojazd",
        "desc": "Auto nie odpala w dzielnicy Włochy lub przy Okęciu? Mobilna wymiana akumulatora, awaryjny rozruch 12V/24V w 20-30 min. Zadzwoń: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Włochy 24/7",
        "areas": "Okęcie, Nowe Włochy, Stare Włochy, Salomea, Raków, parkingi Lotniska Chopina, Al. Krakowska, ul. Łopuszańska, Kleszczowa",
        "description_body": "Rozładowany akumulator w dzielnicy Włochy lub na parkingu przy Lotnisku Chopina? Nasi technicy dyżurują w pobliżu Al. Krakowskiej i Łopuszańskiej, zapewniając dojazd w 20–30 minut. Pełna diagnostyka komputerowa, wymiana baterii i kodowanie BMS na miejscu.",
        "faq_garage": "Wróciłem z podróży i auto nie odpala na parkingu przy Lotnisku Chopina (Okęcie) – pomożecie?",
        "faq_garage_ans": "Tak! Często ratujemy kierowców na parkingach długoterminowych wokół Okęcia. Podjeżdżamy bezpośrednio pod auto i w zależności od stanu baterii odpalamy ją boosterem lub montujemy nowy akumulator."
    },
    {
        "slug": "ursus",
        "url_slug": "wymiana-akumulatora-warszawa-ursus",
        "name": "Ursus",
        "eta": "20–30 min",
        "title": "Wymiana Akumulatora z Dojazdem Warszawa Ursus 24/7 | Akumulateo",
        "desc": "Rozładowany akumulator w Ursusie? Skorosze, Szamoty, Niedźwiadek, Czechowice. Szybki dojazd z nową baterią w 20-30 min. Zadzwoń: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Ursus 24/7",
        "areas": "Skorosze, Szamoty (osiedla po ZPC Ursus), Niedźwiadek, Czechowice, Gołąbki, Al. 4 Czerwca 1989 r., ul. Dzieci Warszawy, Traktorzystów",
        "description_body": "Awaria akumulatora w Ursusie? Błyskawicznie obsługujemy nowe osiedla na Szamotach i Skoroszach oraz starszą część dzielnicy. Przyjeżdżamy z nowym akumulatorem AGM/EFB dobranym według specyfikacji producenta i montujemy go w 20–30 minut.",
        "faq_garage": "Mieszkam na nowym osiedlu na Szamotach (np. ul. Posag 7 Panien) – jak szybko dotrze technik?",
        "faq_garage_ans": "Czas dojazdu na Szamoty i Skorosze wynosi zazwyczaj 20–25 minut. Posiadamy kody dostępu i wjeżdżamy do podziemnych hal garażowych."
    },
    {
        "slug": "wilanow",
        "url_slug": "wymiana-akumulatora-warszawa-wilanow",
        "name": "Wilanów",
        "eta": "20–30 min",
        "title": "Wymiana Akumulatora Miasteczko Wilanów 24/7 | Kodowanie BMS AGM",
        "desc": "Pogotowie akumulatorowe Wilanów: Miasteczko Wilanów, Zawady, Powsinek. Akumulatory AGM/EFB z montażem i kodowaniem w garażach podziemnych 24/7. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Wilanów 24/7",
        "areas": "Miasteczko Wilanów, Wilanów Wysoki, Wilanów Niski, Zawady, Powsinek, Kępa Zawadowska, al. Rzeczypospolitej, al. Wilanowska, ul. Klimczaka",
        "description_body": "Padł akumulator w Miasteczku Wilanów lub na Zawadach? Specjalizujemy się w nowoczesnych autach premium i hybrydach z systemem Start-Stop. Wjeżdżamy do podziemnych hal garażowych, montujemy akumulatory Varta AGM i rejestrujemy nową baterię w komputerze pokładowym.",
        "faq_garage": "Czy kodujecie akumulatory AGM w autach marek BMW, Mercedes, Audi, Volvo w Miasteczku Wilanów?",
        "faq_garage_ans": "Tak, posiadamy profesjonalne testery diagnostyczne OBD, które przeprowadzają pełną adaptację i rejestrację nowego akumulatora AGM w sterowniku BMS/IBS pojazdu."
    },
    {
        "slug": "wawer",
        "url_slug": "wymiana-akumulatora-warszawa-wawer",
        "name": "Wawer",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Wawer 24/7 | Wymiana z Dojazdem",
        "desc": "Rozładowany akumulator w Wawrze? Międzylesie, Falenica, Radość, Anin, Marysin. Dojazd 24/7 z nowym akumulatorem pod Twój dom: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Wawer 24/7",
        "areas": "Międzylesie, Falenica, Radość, Anin, Marysin Wawerski, Zerzeń, Nadwiśle, Aleksandrów, Wał Miedzeszyński, ul. Patriotów, Płowiecka",
        "description_body": "Auto nie odpala w Wawrze? Obsługujemy całą rozległą dzielnicę Wawer – od Marysina po Falenicę. Dojeżdżamy pod domy jednorodzinne, posesje i firmy wzdłuż Wału Miedzeszyńskiego i ul. Patriotów. Wymiana na miejscu bez konieczności holowania.",
        "faq_garage": "Mieszkam w domu jednorodzinnym w Radości / Falenicy – czy serwisant dojedzie bezpośrednio na posesję?",
        "faq_garage_ans": "Tak, dojeżdżamy pod wskazany adres na prywatną posesję, do ogrodu lub podjazdu. Na miejscu sprawdzamy układ ładowania i instalujemy nową baterię."
    },
    {
        "slug": "rembertow",
        "url_slug": "wymiana-akumulatora-warszawa-rembertow",
        "name": "Rembertów",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Rembertów 24/7 | Akumulateo",
        "desc": "Awaria akumulatora w Rembertowie? Nowy i Stary Rembertów, Wygoda, Kawęczyn. Dojazd w 20-30 min, profesjonalny montaż i kodowanie 24h. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Rembertów 24/7",
        "areas": "Stary Rembertów, Nowy Rembertów, Kawęczyn-Wygoda, Kolonia Rembertów, ul. Żołnierska, ul. Cyrulików, Strażacka, al. gen. Chruściela „Montera”",
        "description_body": "Rozładowany akumulator w Rembertowie? Dojedziemy w 20–30 minut na Stary lub Nowy Rembertów oraz Kawęczyn. Sprawdzimy prąd upływu, podłączymy podtrzymanie pamięci i zamontujemy fabrycznie nowy akumulator z 2-letnią gwarancją producenta.",
        "faq_garage": "Czy wymieniacie akumulatory także w nocy i w niedziele w Rembertowie?",
        "faq_garage_ans": "Tak, nasze pogotowie akumulatorowe pełni całodobowy dyżur 24h/7, w tym we wszystkie święta i niedziele niehandlowe."
    },
    {
        "slug": "wesola",
        "url_slug": "wymiana-akumulatora-warszawa-wesola",
        "name": "Wesoła",
        "eta": "20–30 min",
        "title": "Wymiana Akumulatora z Dojazdem Warszawa Wesoła 24/7 | Stara Miłosna",
        "desc": "Samochód nie odpala w Wesołej lub Starej Miłosnej? Pogotowie akumulatorowe 24/7. Dowóz nowej baterii, montaż i adaptacja BMS. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Wesoła 24/7",
        "areas": "Stara Miłosna, Wola Grzybowska, Groszówka, Grzybowa, Zielona, Trakt Brzeski, ul. Jana Pawła II, Wspólna",
        "description_body": "Padł akumulator w Wesołej lub w Starej Miłosnej? Nasz technik dociera Traktem Brzeskim w 20–30 minut pod Twój dom lub parking. Testujemy stan starej baterii cyfrowym analizatorem, a w razie potrzeby montujemy nową i odbieramy stary złom ołowiany.",
        "faq_garage": "Stoję w Starej Miłosnej pod domem – jak szybko dotrze pogotowie?",
        "faq_garage_ans": "Dojazd do Starej Miłosnej i Wesołej zajmuje średnio 20–30 minut. Nasze patrole stacjonują przy kluczowych węzłach wylotowych Warszawy."
    },
    {
        "slug": "zoliborz",
        "url_slug": "wymiana-akumulatora-warszawa-zoliborz",
        "name": "Żoliborz",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Żoliborz 24/7 | Wymiana z Dojazdem",
        "desc": "Rozładowany akumulator na Żoliborzu? Plac Wilsona, Marymont, Sady Żoliborskie. Dojazd w 20-30 min, montaż z podtrzymaniem OBD 24h: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Żoliborz 24/7",
        "areas": "Plac Wilsona, Marymont-Potok, Sady Żoliborskie, Żoliborz Oficerski, Żoliborz Dziennikarski, Żoliborz Artystyczny, ul. Krasińskiego, Mickiewicza, Rydygiera",
        "description_body": "Awaria akumulatora na Żoliborzu? Obsługujemy zarówno tradycyjne kamienice przy Placu Wilsona, jak i nowoczesne osiedla na Żoliborzu Artystycznym (ul. Rydygiera). Dojeżdżamy w 20–30 minut, testujemy ładowanie alternatora i montujemy baterię AGM/EFB.",
        "faq_garage": "Czy wjedziecie do garażu podziemnego na Żoliborzu Artystycznym (ul. Rydygiera / Powązkowska)?",
        "faq_garage_ans": "Tak, nasze wozy serwisowe oraz mobilne boostery mikroprocesorowe bez problemu zjeżdżają do hal garażowych na osiedlach Żoliborza Artystycznego."
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
            "ratingCount": "160",
            "reviewCount": "160"
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
        Nie trać czasu na szukanie stacjonarnego sklepu ani holowanie auta. Nie prowadzimy punktu odbioru na terenie dzielnicy {d['name']} – <strong>nasz serwisant przyjeżdża bezpośrednio pod Twój adres</strong> z fabrycznie nową baterią i montuje ją na miejscu w 20–30 minut.
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

    clean_name = d['name'].replace('Ś','S').replace('Ł','L').replace('Ó','O').replace('Ż','Z').replace('–','-').replace(' ','_').replace('-','_')

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

<!-- 4. TEMPLATE DZIELNICY -->
<template id="akumulateo-{d['slug']}-template">
{content_html}
</template>

<!-- 5. NATYCHMIASTOWY SKRYPT MONTAŻU (HIGH SPEED SSR EMULATION) -->
<script>
(function() {{
  function mountAkumulateo{clean_name} () {{
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
    print("🚀 Generowanie pakietów Page Header Injection dla pozostałych 12 dzielnic Warszawy...")
    for d in REMAINING_12_DISTRICTS:
        code = generate_district_injection(d)
        file_path = os.path.join(SNIPPETS_DIR, f"{d['slug']}-page-header-injection.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)
        print(f"  ✅ {d['name']} -> {file_path} ({len(code)} znaków)")

    print("\n🎉 Sukces! Wszystkie 12 pakietów wstrzyknięć zostały pomyślnie wygenerowane.")

if __name__ == "__main__":
    main()
