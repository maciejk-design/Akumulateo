# Instrukcja Tworzenia Nowych Podstron Lokalnych i Dzielnicowych (v2.2)

Przewodnik wdrożeniowy krok po kroku określający standard tworzenia nowych podstron SEO dla **18 dzielnic Warszawy** oraz **miast aglomeracji warszawskiej** (m.in. Piastów, Brwinów, Milanówek, Legionowo, Nowy Dwór Mazowiecki / Modlin, Mińsk Mazowiecki, Piaseczno, Pruszków, Otwock, Marki, Ząbki).

Standard gwarantuje 100% spójność wizualną z [Brandbookiem v2.2](file:///Users/digo/Documents/antigravity/Akumulateo/docs/brandbook-akumulateo.md), zero błędów typograficznych, pełną responsywność na smartfonach oraz bezbłędne wdrożenie w Squarespace 7.1.

---

## 1. Żelazne Reguły Tworzenia Podstron (Checklista Anty-Błędowa)

1. **Typografia:** Każdy akapit tekstu lokalnego musi mieć klasę `text-[15.5px] sm:text-[16.5px] text-slate-100 font-normal leading-relaxed`. Nigdy nie stosuj fontów mniejszych niż 15.5px!
2. **Kontrast barw:** Tło sekcji to `#020617` lub `#0f172a`. Tekst w kolorze `#f1f5f9` (Slate 100) lub `#f8fafc` (Slate 50). Zakaz wyblakłych szarych czcionek.
3. **Cenzura marek:** Bezwzględny zakaz wspominania marek **Centra** i **Banner**. Wymieniaj wyłącznie oficjalnych partnerów: **Varta, Yuasa (YUASA), Bosch, 4Max, BP, Eco-Force**.
4. **Prekwalifikacja mobilna:** Każda podstrona musi zawierać baner informujący, że Akumulateo to **usługa w 100% mobilna z dojazdem pod dom/firmę** i nie prowadzi sklepu stacjonarnego w danej miejscowości.
5. **Responsywny pasek 24h:** Top Bar musi posiadać `flex-wrap`, aby nie obcinać tekstu na ekranach o szerokości 320px–360px.
6. **Struktura Cennika:** Jeśli podstrona zawiera cennik, karta *„Wymiana Akumulatora + Kodowanie BMS”* musi posiadać wyróżniającą ramkę `border-2 border-amber-500` i pigułkę `★ NAJCZĘŚCIEJ WYBIERANA USŁUGA`.

---

## 2. Architektura URL i Metadane SEO

Dla każdej nowej podstrony stosujemy ujednolicony standard nazewnictwa i metadanych:

### Tabela Przykładowych Slugów i Tytułów SEO:

| Miejscowość / Dzielnica | URL Slug | Meta Title (max 60 znaków) | Meta Description (max 155 znaków) |
| :--- | :--- | :--- | :--- |
| **Piastów** | `/wymiana-akumulatora-piastow` | Pogotowie Akumulatorowe Piastów 24h – Wymiana z Dojazdem | Rozładowany akumulator w Piastowie? Dojazd 20-30 min, diagnostyka, montaż i kodowanie BMS pod domem. Zadzwoń: 696 556 446! |
| **Brwinów** | `/wymiana-akumulatora-brwinow` | Pogotowie Akumulatorowe Brwinów 24h – Wymiana z Dojazdem | Mobilny serwis akumulatorów Brwinów i okolice 24/7. Dowozimy nową baterię Varta/Yuasa, montujemy na miejscu. Tel: 696 556 446. |
| **Milanówek** | `/wymiana-akumulatora-milanowek` | Pogotowie Akumulatorowe Milanówek 24h – Wymiana z Dojazdem | Awaryjny rozruch i wymiana akumulatora Milanówek 24h. Podtrzymanie pamięci OBD, płatność kartą u technika. Zadzwoń: 696 556 446! |
| **Legionowo** | `/wymiana-akumulatora-legionowo` | Pogotowie Akumulatorowe Legionowo 24h – Wymiana z Dojazdem | Całodobowe pogotowie akumulatorowe Legionowo. Szybki dojazd DK61, montaż baterii AGM/EFB i kodowanie Start-Stop. Tel: 696 556 446. |
| **Modlin / Nowy Dwór** | `/wymiana-akumulatora-modlin` | Pogotowie Akumulatorowe Modlin Lotnisko 24h – Rozruch i Wymiana | Auto nie odpala na parkingu przy Lotnisku Warszawa-Modlin? Błyskawiczny rozruch boosterem i dowóz akumulatora 24h. Tel: 696 556 446. |
| **Mińsk Mazowiecki** | `/wymiana-akumulatora-minsk-mazowiecki` | Pogotowie Akumulatorowe Mińsk Mazowiecki 24h – Wymiana z Dojazdem | Mobilna wymiana akumulatora Mińsk Mazowiecki i trasa A2/DK92. Nowe baterie z gwarancją do 3 lat, płatność BLIK/karta. Tel: 696 556 446. |

---

## 3. Wzorcowy Szablon JSON-LD Schema.org dla Podstrony Lokalnej

Wklejany w: **Page Settings -> Advanced -> Page Header Code Injection**.

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AutomotiveBusiness",
  "name": "Akumulateo – Pogotowie Akumulatorowe {NAZWA_MIEJSCOWOSCI} 24h",
  "url": "https://www.akumulateo.pl/{SLUG}",
  "telephone": "+48696556446",
  "priceRange": "$$",
  "image": "https://www.akumulateo.pl/assets/brand/akumulateo-og.png",
  "description": "Mobilne pogotowie akumulatorowe 24h w {MIEJSCOWOSC}. Dojazd w 20-30 minut, awaryjny rozruch 12V/24V, dowóz i profesjonalny montaż akumulatora pod domem klienta.",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "{MIEJSCOWOSC}",
    "addressRegion": "Mazowieckie",
    "addressCountry": "PL"
  },
  "areaServed": [
    { "@type": "City", "name": "{MIEJSCOWOSC}" },
    { "@type": "AdministrativeArea", "name": "Aglomeracja Warszawska" }
  ],
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
    "ratingCount": "104",
    "reviewCount": "104"
  }
}
</script>
```

---

## 4. Wzorcowy Kod HTML Sekcji Lokalnej (Do Bloku Code)

Poniższy kod wklej do bloku **Code** w edytorze podstrony (upewnij się, że opcja **Display Source** jest **wyłączona**):

```html
<div class="akumulateo-root bg-slate-950 text-slate-100 min-h-screen font-sans antialiased">
  
  <!-- 1. TOP EMERGENCY BAR 24H (PEŁNA RESPONSYWNOŚĆ 320PX) -->
  <div class="bg-gradient-to-r from-amber-500 via-amber-400 to-amber-500 text-slate-950 py-1.5 px-3 sm:px-4 text-xs font-black tracking-wide shadow-sm">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-x-2.5 gap-y-1">
      <div class="flex items-center space-x-1.5">
        <span class="inline-block w-2.5 h-2.5 bg-emerald-700 rounded-full animate-pulse shadow-sm"></span>
        <span class="uppercase tracking-wider">DYŻUR POGOTOWIA 24H/7</span>
        <span class="hidden xs:inline text-slate-800 font-bold">• {NAZWA_MIEJSCOWOSCI} i okolice</span>
      </div>
      <div class="flex items-center space-x-3 text-slate-950 text-right">
        <span class="hidden sm:inline font-bold">🇬🇧 We speak English</span>
        <a href="https://g.page/r/CXjN9llopHR_EBM/" target="_blank" rel="noopener noreferrer" class="inline-flex items-center font-black hover:underline transition-all">
          ⭐ 5.0 w Google (100+ opinii) ↗
        </a>
      </div>
    </div>
  </div>

  <!-- 2. HERO SEKCYJNY DLA LOKALIZACJI -->
  <header class="py-12 sm:py-16 px-4 bg-gradient-to-b from-slate-900 to-slate-950 border-b border-slate-800 text-center">
    <div class="max-w-4xl mx-auto">
      <div class="inline-flex items-center space-x-2 bg-amber-500/10 border border-amber-500/30 text-amber-400 px-3.5 py-1.5 rounded-full text-xs font-bold uppercase tracking-wider mb-4">
        <span>⚡ Mobilny Serwis z Dojazdem 20-30 min</span>
      </div>
      
      <h1 class="text-3xl sm:text-5xl font-black text-white tracking-tight mb-4">
        Wymiana Akumulatora <span class="text-amber-400">{NAZWA_MIEJSCOWOSCI}</span> 24h
      </h1>
      
      <p class="text-[16px] sm:text-[18px] text-slate-200 font-normal leading-relaxed max-w-2xl mx-auto mb-8">
        Rozładowany akumulator pod domem, w garażu podziemnym lub na trasie w rejonie miejscowości {NAZWA_MIEJSCOWOSCI}? 
        Nasz mobilny technik dojedzie z nową baterią, bezpiecznie zamontuje i zakoduje system BMS.
      </p>

      <div class="flex flex-col sm:flex-row items-center justify-center gap-3">
        <a href="tel:+48696556446" class="w-full sm:w-auto inline-flex items-center justify-center bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 text-base font-black px-8 py-4 rounded-xl shadow-lg transition-all">
          📞 Zadzwoń: 696 556 446 (Dyżur 24h)
        </a>
      </div>
    </div>
  </header>

  <!-- 3. MOBILITY NOTICE BANNER (BRAK ODBIORU OSOBISTEGO) -->
  <section class="max-w-5xl mx-auto mt-8 px-4">
    <div class="bg-gradient-to-r from-amber-500/10 via-slate-900 to-amber-500/10 border-2 border-amber-500/40 rounded-2xl p-4 sm:p-5 text-center shadow-lg">
      <div class="inline-flex items-center space-x-2 text-amber-400 font-black text-sm uppercase tracking-wider mb-1">
        <span>ℹ️ Usługa w 100% Mobilna</span>
      </div>
      <p class="text-[15.5px] sm:text-base font-medium text-slate-100 leading-relaxed max-w-3xl mx-auto">
        Nie trać czasu na szukanie sklepu w {MIEJSCOWOSC} ani holowanie auta na warsztat. 
        Akumulateo to <strong>mobilne pogotowie akumulatorowe</strong> – przyjeżdżamy na miejsce z fabrycznie nowym akumulatorem dobranym z katalogu OEM i kompletem narzędzi.
      </p>
    </div>
  </section>

  <!-- 4. LOKALNY OPIS PROCEDURY I WARUNKÓW (ŚCISŁY STANDARD TYPOGRAFII) -->
  <section class="max-w-5xl mx-auto py-10 px-4">
    <div class="bg-slate-900 border border-slate-800 rounded-2xl p-6 sm:p-8">
      <h2 class="text-2xl sm:text-3xl font-bold text-white mb-4">
        Jak wygląda pomoc pogotowia akumulatorowego w miejscowości {NAZWA_MIEJSCOWOSCI}?
      </h2>
      
      <p class="text-[15.5px] sm:text-[16.5px] text-slate-100 font-normal leading-relaxed mb-4">
        Po przyjęciu zgłoszenia telefonicznego pod numerem <strong>696 556 446</strong> dyspozytor dobiera akumulator zgodnie ze specyfikacją fabryczną Twojego samochodu (pojemność Ah, prąd rozruchowy A, technologia EFB lub AGM dla aut z systemem Start-Stop).
      </p>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-6">
        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800">
          <div class="text-amber-400 font-bold text-lg mb-1">1. Błyskawiczny dojazd</div>
          <p class="text-[15.5px] text-slate-100 leading-relaxed">Dojazd serwisowy pod wskazany adres na terenie {MIEJSCOWOSC} w 20-30 minut od zgłoszenia.</p>
        </div>
        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800">
          <div class="text-amber-400 font-bold text-lg mb-1">2. Diagnostyka i wymiana</div>
          <p class="text-[15.5px] text-slate-100 leading-relaxed">Test instalacji i alternatora, montaż nowej baterii (Varta, Yuasa, Bosch) z podtrzymaniem pamięci OBD.</p>
        </div>
        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800">
          <div class="text-amber-400 font-bold text-lg mb-1">3. Kodowanie BMS & Gwarancja</div>
          <p class="text-[15.5px] text-slate-100 leading-relaxed">Elektroniczna rejestracja baterii w sterowniku silnika, pisemna gwarancja do 3 lat, płatność kartą/BLIK.</p>
        </div>
      </div>

      <p class="text-[15.5px] sm:text-[16.5px] text-slate-100 font-normal leading-relaxed">
        Zużyty akumulator odbieramy bezpłatnie i przekazujemy do legalnego recyklingu hutniczego – nie ponosisz żadnej ustawowej opłaty depozytowej (0 zł kaucji).
      </p>
    </div>
  </section>

</div>
```

---

## 5. Procedura Publikacji w Panelu Squarespace 7.1

1. W panelu bocznym przejdź do: **Pages** -> sekcja **Not Linked**.
2. Kliknij ikonę **`+`** i wybierz **Blank Page**.
3. Wpisz tytuł strony (np. *Wymiana Akumulatora Piastów*).
4. Kliknij ikonę koła zębatego (Ustawienia strony):
   * **General:** ustaw Page Title oraz URL Slug (np. `wymiana-akumulatora-piastow`).
   * **SEO:** wklej Meta Title i Meta Description z Tabeli w Rozdziale 2.
   * **Advanced:** w polu **Page Header Code Injection** wklej przygotowany kod Schema.org JSON-LD.
   * Kliknij **Save**.
5. W edytorze podstrony:
   * Kliknij **Edit** -> **Add a blank section**.
   * Kliknij **+ Add Block** -> wybierz blok **Code**.
   * Rozciągnij blok na całą szerokość siatki.
   * W edytorze bloku upewnij się, że opcja **Display Source** jest **wyłączona**, a język ustawiony na **HTML**.
   * Wklej przygotowany kod sekcji lokalnej.
   * Kliknij **Done -> Save**.
6. Wykonaj **Test Pre-Flight**:
   * Otwórz stronę w nowej karcie Incognito.
   * Sprawdź czy baner cookies działa poprawnie, a tekst opisowy ma właściwy rozmiar (min. 15.5px).

---
*Instrukcja Tworzenia Podstron Lokalnych v2.2 | Wrzesień 2026*
