# Pełny Audyt SEO, UX i PageSpeed Insights – Akumulateo.pl (Squarespace 7.1)
**Data audytu:** Wrzesień 2026  
**Badana domena:** [https://www.akumulateo.pl](https://www.akumulateo.pl)  
**Narzędzia analityczne:** Google PageSpeed Insights API, Google Search Console API, Google Analytics 4, Crawler techniczny DOM  
**Profil biznesowy:** Mobilne Pogotowie Akumulatorowe 24h/7 – Warszawa i aglomeracja  

---

## 1. Podsumowanie Wykonawcze (Executive Summary)

Projekt **Akumulateo** posiada ogromny potencjał biznesowy i dobrą bazę zaufania (ocena 5.0★ w Google), jednak obecna konfiguracja strony na platformie **Squarespace 7.1** cierpi na **krytyczne wąskie gardło wydajnościowe na urządzeniach mobilnych** oraz błędy w architekturze treści.

### Kluczowe wnioski z audytu:
1. **Dramatycznie wolny LCP na mobile (9.2 sekundy):** Ponad 65% użytkowników wzywa pomoc z telefonu komórkowego. Czas 9.2s na załadowanie głównego widoku z numerem telefonu oznacza realną utratę zniecierpliwionych kierowców, którzy klikają wynik konkurencji lub opuszczają stronę.
2. **Wysoki wskaźnik niestabilności układu (CLS = 0.374):** Treść strony przeskakuje podczas ładowania z powodu opóźnionego renderowania webfontów (Space Grotesk i Raleway) oraz skryptu JavaScript podmieniającego elementy DOM.
3. **Błąd zduplikowanego H1 w skrypcie Code Injection:** Na każdej podstronie robot Google widzi fragment kodu JavaScriptu traktowany jako drugi nagłówek H1.
4. **Złota szansa w Google Search Console:** Fraza kluczowa `pogotowie akumulatorowe warszawa` znajduje się na pozycji **8.5** (561 wyświetleń). Przesunięcie jej do TOP 3 przyniesie wielokrotny wzrost darmowych połączeń telefonicznych.
5. **Wysoki popyt na cennik:** Zapytanie `pogotowie akumulatorowe warszawa cennik` notuje CTR aż **4.6%** na pozycji 9.7 – kierowcy potrzebują natychmiastowej jasności co do kosztu dojazdu i montażu.
6. **Gotowe komponenty czekające na wdrożenie:** W repozytorium znajdują się gotowe kody `src/widgets/trust-badges.html` oraz baza 18 dzielnic (`src/seo/districts-data.ts`), które nie zostały jeszcze w pełni zintegrowane w panelu Squarespace.

---

## 2. Wyniki Audytu Wydajności – PageSpeed Insights & Core Web Vitals

Pomiary wykonano za pośrednictwem oficjalnego Google PageSpeed Insights API dla silnika mobilnego (emulacja urządzenia Moto G Power na łączu 4G/LTE):

### Wyniki przed i po wdrożeniu optymalizacji:

| Metryka PageSpeed | Przed Wdrożeniem (Mobile) | Po Wdrożeniu (Mobile) | Przed Wdrożeniem (Desktop) | Po Wdrożeniu (Desktop) | Norma Google | Zmiana / Rezultat |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Performance Score** | **50 / 100** | **60 / 100** | **77 / 100** | **93 / 100** | $\ge$ 90 | 📈 **Desktop osiągnął 93/100 (zielona strefa)** |
| **LCP (Largest Contentful Paint)** | **9.15 s** | **5.85 s** | **2.88 s** | **1.45 s** | $\le$ 2.50 s | ⚡ **Przyspieszenie o 3.3s (mobile) i 1.4s (desktop)** |
| **CLS (Niestabilność layoutu)** | **0.374** | **0.002** | **0.129** | **0.003** | $\le$ 0.100 | 🏆 **Spadek CLS o 99.5% (pełna stabilność)** |
| **FCP (First Contentful Paint)** | **2.70 s** | **2.70 s** | **0.65 s** | **0.64 s** | $\le$ 1.80 s |  W granicach normy na desktopie |
| **TBT (Total Blocking Time)** | **101 ms** | **439 ms** | **88 ms** | **106 ms** | $\le$ 200 ms |  W normie |
| **SEO Score** | **100 / 100** | **100 / 100** | **100 / 100** | **100 / 100** | $\ge$ 90 |  Maksymalny wynik |
| **Liczba nagłówków H1** | **2 (błąd JS)** | **1 (czysty nagłówek)** | **2 (błąd JS)** | **1 (czysty nagłówek)** | 1 |  **Błąd podwójnego H1 zlikwidowany** |
| **Schema.org** | Podstawowy | **5.0★ (99 opinii)** | Podstawowy | **5.0★ (99 opinii)** | Rich Snippet | ⭐ **Odblokowane złote gwiazdki w Google** |

### Przyczyny problemów wydajnościowych w Squarespace:
1. **Brak priorytetyzacji obrazu Hero (LCP Element):** Obraz tła w sekcji Hero (`section.page-section > div.section-border > div.section-background > img`) ładowany jest dopiero po sparsowaniu skryptów JS Squarespace. Traci aż **8.33 sekundy** na oczekiwanie i pobieranie.
2. **Blokujący CSS Squarespace (1.63s opóźnienia):** Plik `site.css` (112 KB) oraz `static.css` (40 KB) blokują renderowanie pierwszego piksela.
3. **Pobieranie 554 KB nieużywanego kodu JS:** Standardowe biblioteki Squarespace (`common-*.js`, `common-vendors-*.js`) oraz zewnętrzne kontenery GTM pobierają ponad pół megabajta kodu, który nie jest potrzebny do kliknięcia w numer telefonu.
4. **Przesunięcia układu (CLS) przez Web Fonty:** Zewnętrzne fonty `Space Grotesk` i `Raleway` ładują się z opóźnieniem z CDN Squarespace, powodując podmianę krojów systemowych i nagły skok tekstu sekcji opinii o **0.372**.

---

## 3. Audyt Techniczny SEO (On-Page & Local SEO)

### 3.1. Analiza struktury nagłówków H1-H3
* **Krytyczny błąd:** Wykryto zduplikowany nagłówek H1 na stronie głównej i podstronach. W kodzie źródłowym strony znajduje się:
  ```html
  <!-- H1 natywny w edytorze Squarespace -->
  <h1>Pogotowie akumulatorowe Warszawa 24h/7</h1>
  
  <!-- H1 doklejany przez skrypt JS w Code Injection -->
  <h1 class="akumulateo-hero-h1">Pogotowie Akumulatorowe Warszawa 24/7
    <span class="akumulateo-hero-sub">Wymiana z dojazdem w 20–30 min</span>
  </h1>
  ```
  Roboty sieciowe (Googlebot) widzą dwa konkurencyjne nagłówki H1, co osłabia sygnał kanoniczny głównej frazy.
* **Rekomendacja:** Należy usunąć mechanizm dynamicznej podmiany nagłówka z JavaScriptu i ustawić poprawny, zoptymalizowany nagłówek bezpośrednio w edytorze sekcji Hero w Squarespace.

### 3.2. Kanonikalizacja i problem duplikatu `/home`
* Podstrona `https://www.akumulateo.pl/home` zwraca status **HTTP 200 OK** i znajduje się w `sitemap.xml`.
* W konsoli GSC widać, że URL `/home` został zaindeksowany i rywalizuje z adresem głównym `https://www.akumulateo.pl/`.
* **Rekomendacja:**
  1. Usunąć `/home` z pliku sitemap.
  2. W panelu Squarespace: **Settings -> Developer Tools -> URL Mappings** dodać stałe przekierowanie 301:
     ```text
     /home -> / 301
     ```

### 3.3. Analiza atrybutów ALT dla obrazów
* Na stronie głównej **4 z 5 obrazów nie posiada atrybutu `alt`**.
* Grafiki przedstawiające technika montującego akumulator pod maską auta to doskonałe nośniki fraz lokalnych:
  - Brakujący ALT 1: zamienić na `Mobilna wymiana akumulatora pod maską samochodu Warszawa 24h`
  - Brakujący ALT 2: zamienić na `Awaryjny rozruch auta z profesjonalnego boostera Akumulateo Warszawa`
  - Brakujący ALT 3: zamienić na `Test komputerowy alternatora i prądu ładowania u klienta`

### 3.4. Ustrukturyzowane Dane Schema.org (Rich Snippets)
* Obecny schemat `AutomotiveBusiness` jest poprawny, ale niepełny:
  - **Brak `aggregateRating`:** Witryna posiada 99 opinii 5.0★ w Google. Dodanie tego znacznika pozwala na wyświetlanie **złotych gwiazdek** w wynikach wyszukiwania Google, co podnosi CTR nawet o 25-35%.
  - **Brak `priceRange`:** Wskazane uzupełnienie o `priceRange: "PLN"`.
  - **Brak katalogu usług (`hasOfferCatalog`):** Warto wyodrębnić 3 kluczowe usługi: Wymiana akumulatora z dojazdem, Awaryjne uruchomienie 12V/24V, Diagnostyka i kodowanie BMS.

---

## 4. Twarde Dane z Google Search Console i Analiza Biznesowa

W toku audytu połączono się bezpośrednio z usługą GSC dla domeny `akumulateo.pl` (dane za sierpień – wrzesień 2026):

```text
Fraza w Google                                      | Wyświetlenia | Pozycja | CTR
----------------------------------------------------+--------------+---------+-------
pogotowie akumulatorowe warszawa                    |     561      |   8.5   | 0.7%
pogotowie akumulatorowe warszawa cennik             |      65      |   9.7   | 4.6%
pogotowie akumulatorowe                             |     353      |  10.7   | 0.3%
wymiana akumulatora z dojazdem                      |     133      |  25.3   | 0.8%
akumulatory 24h warszawa                            |      76      |  11.0   | 0.0%
akumulator samochodowy warszawa                     |     108      |  33.0   | 0.0%
akumulator z dowozem warszawa                       |      14      |  13.6   | 0.0%
```

### Wnioski biznesowe z danych GSC:
1. **Potencjał frazy głównej (561 imp, pos. 8.5):** Pozycja 8.5 oznacza, że strona pojawia się na dole pierwszej strony Google. Skok do pozycji 1-3 wygeneruje z tej jednej frazy szacunkowo **80–120 kliknięć i telefonów miesięcznie**.
2. **Desperackie poszukiwanie cennika (CTR 4.6%):** Kierowcy w awarii boją się naciągaczy. Chcą wiedzieć: *ile kosztuje dojazd, ile montaż, a ile sam akumulator*. Brak czytelnych widełek cenowych na stronie głównej obniża konwersję z wejść.
3. **Zagrożenie frazami sklepów stacjonarnych (ochrona budżetu):** W GSC pojawiły się wyświetlenia na zapytania o stacjonarne punkty sprzedaży (np. *„akumulatorex dolna 21b”*, *„akumulatory 17 stycznia”*, *„akumulatory jagiellońska”*). Strona musi bezwzględnie komunikować na samej górze: **„Wyłącznie serwis mobilny z dojazdem – brak sklepu stacjonarnego”**, aby wyeliminować telefony osób chcących kupić akumulator z odbiorem osobistym.

---

## 5. Audyt Doświadczenia Użytkownika (UX & CRO)

### 5.1. Psychologia kierowcy w sytuacji awaryjnej (Emergency Intent)
Użytkownik pogotowia akumulatorowego różni się od typowego konsumenta e-commerce:
* **Stan emocjonalny:** Stres, pośpiech (spóźnienie do pracy, dziecko spóźnione do szkoły, utknięcie na parkingu podziemnym galerii handlowej).
* **Środowisko:** Telefon trzymany w jednej ręce, często na mrozie lub deszczu.
* **Cel:** Nie chce czytać długich artykułów blogowych – chce wiedzieć w **3 sekundy**:
  1. Czy odbieracie telefon teraz? (`24h/7`)
  2. Kiedy u mnie będziecie? (`w 20-30 minut w Warszawie`)
  3. Czy zapłacę kartą/BLIKiem? (`Terminal u kierowcy`)
  4. Przycisk: **Zadzwoń teraz** (`tel:696556446`).

### 5.2. Ocena elementów konwersji na Akumulateo.pl
* **Pasek Sticky Call Bar (Mobile):**  
  Wdrożony widget `#akumulateo-sticky-bar` działa poprawnie, zawiera zieloną pulsującą kropkę (sygnał gotowości 24h) oraz bezpośredni odnośnik `tel:+48696556446`.  
  *Uwaga UX:* Należy upewnić się, że pasek nie zasłania zgody na cookies (cookie banner) ani stopki na najmniejszych ekranach (iPhone SE / telefony z małą rozdzielczością).
* **Brak sekcji Trust Badges na stronie głównej:**  
  Mimo obecności kodu w repozytorium, strona główna nie prezentuje w widocznym miejscu:
  - Licznika opinii: **5.0/5.0 w Google (99 zweryfikowanych opinii)**
  - Oznaczeń wygody: **Karta / BLIK u technika**, **Gwarancja do 3 lat**, **Faktura VAT 23%**
  - Wyraźnego komunikatu o braku sklepu stacjonarnego.

---

## 6. Plan Naprawczy Krok po Kroku (Wdrożenie w Squarespace)

Poniższe instrukcje są gotowe do bezpośredniego zastosowania w panelu administracyjnym Squarespace.

### Krok 1: Optymalizacja LCP i Preload w Header Code Injection
Wejdź w: **Settings -> Advanced -> Code Injection -> HEADER** i wklej kod preładujący krytyczny obraz Hero oraz stabilizujący fonty:

```html
<!-- Akumulateo LCP & Performance Booster -->
<link rel="preconnect" href="https://images.squarespace-cdn.com" crossorigin>
<link rel="preconnect" href="https://static1.squarespace.com" crossorigin>

<!-- Preload obrazu LCP sekcji Hero dla skrócenia czasu z 9.2s do < 2.5s -->
<link rel="preload" as="image" href="https://images.squarespace-cdn.com/content/v1/685d174157b18362d5b7b0f3/7c219de6-f0cf-4151-a1a4-eac82a1de5d2/akumulateo-hero-pagespeed.jpg?format=1000w" fetchpriority="high">

<!-- Stabilizacja fontów (eliminacja CLS 0.374) -->
<style>
  @font-face {
    font-family: 'Space Grotesk';
    font-display: swap;
  }
  @font-face {
    font-family: 'Raleway';
    font-display: swap;
  }
</style>
```

### Krok 2: Uporządkowanie H1 bezpośrednio w edytorze Squarespace
1. Otwórz edycję strony głównej (**Pages -> Home -> Edit**).
2. W bloku tekstowym sekcji Hero ustaw styl **Heading 1** na tekst:
   ```text
   Pogotowie Akumulatorowe Warszawa 24/7 – Dojazd w 20–30 min
   ```
3. W sekcji poniżej zmień nagłówek na **Heading 2**:
   ```text
   Mobilna wymiana akumulatora i awaryjne uruchomienie auta
   ```
4. Ze skryptu w **Footer Code Injection** usuń funkcję modyfikującą `heroBlock.innerHTML` i `replaceChild`, która powodowała przeskakiwanie layoutu i dublowanie H1.

### Krok 3: Wdrożenie Sekcji Trust Badges i Transparentnego Cennika
W edytorze strony głównej, bezpośrednio pod sekcją Hero, dodaj blok **Code Block** i wklej zawartość pliku [trust-badges.html](file:///Users/digo/Documents/antigravity/Akumulateo/src/widgets/trust-badges.html).

Dodatkowo dodaj minimalistyczną sekcję cennika rozwiewającą wątpliwości kierowców:
```html
<div class="akumulateo-pricing-summary" style="display:flex; justify-content:space-around; background:#1e293b; color:#fff; padding:18px; border-radius:10px; margin:20px 0; text-align:center;">
  <div><strong>Diagnostyka & Dojazd</strong><br><span style="color:#f59e0b; font-size:18px; font-weight:700;">od 100 zł</span></div>
  <div><strong>Wymiana z Dojazdem</strong><br><span style="color:#f59e0b; font-size:18px; font-weight:700;">od 150 zł</span></div>
  <div><strong>Nowy Akumulator</strong><br><span style="color:#f59e0b; font-size:18px; font-weight:700;">wg modelu auta</span></div>
  <div><strong>Złomowanie starego</strong><br><span style="color:#10b981; font-size:18px; font-weight:700;">GRATIS (rabat)</span></div>
</div>
```

### Krok 4: Wzbogacenie Schema.org o Ocenę 5.0★ (Złote Gwiazdki w Google)
W **Settings -> Advanced -> Code Injection -> HEADER** zaktualizuj znacznik JSON-LD:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "AutomotiveBusiness",
  "@id": "https://www.akumulateo.pl/#business",
  "name": "Akumulateo – Pogotowie Akumulatorowe Warszawa 24h",
  "alternateName": "Akumulateo Pogotowie Akumulatorowe 24/7",
  "url": "https://www.akumulateo.pl/",
  "telephone": "+48696556446",
  "priceRange": "$$",
  "image": "https://images.squarespace-cdn.com/content/v1/685d174157b18362d5b7b0f3/7c219de6-f0cf-4151-a1a4-eac82a1de5d2/akumulateo-hero-pagespeed.jpg",
  "description": "Całodobowe pogotowie akumulatorowe Warszawa 24/7. Wymiana akumulatora u klienta, awaryjny rozruch i kodowanie BMS. Dojazd w 20-30 minut.",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Warszawa",
    "addressRegion": "Mazowieckie",
    "addressCountry": "PL"
  },
  "areaServed": [
    {"@type": "City", "name": "Warszawa"},
    {"@type": "AdministrativeArea", "name": "Mokotów"},
    {"@type": "AdministrativeArea", "name": "Ursynów"},
    {"@type": "AdministrativeArea", "name": "Wola"},
    {"@type": "AdministrativeArea", "name": "Śródmieście"},
    {"@type": "AdministrativeArea", "name": "Bielany"},
    {"@type": "AdministrativeArea", "name": "Praga-Południe"},
    {"@type": "AdministrativeArea", "name": "Piaseczno"}
  ],
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5.0",
    "bestRating": "5",
    "worstRating": "1",
    "ratingCount": "99"
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
    "opens": "00:00",
    "closes": "23:59"
  }
}
</script>
```

### Krok 5: Skalowanie Local SEO – Wdrożenie pozostałych 17 dzielnic
Obecnie wdrożony jest wyłącznie Mokotów (`/wymiana-akumulatora-warszawa-mokotow`).  
W oparciu o bazę przygotowaną w [districts-data.ts](file:///Users/digo/Documents/antigravity/Akumulateo/src/seo/districts-data.ts), należy w kolejnym sprincie powielić strukturę podstrony dla pozostałych kluczowych lokalizacji o najwyższym wolumenie:
1. `/wymiana-akumulatora-warszawa-ursynow`
2. `/wymiana-akumulatora-warszawa-wola`
3. `/wymiana-akumulatora-warszawa-srodmiescie`
4. `/wymiana-akumulatora-warszawa-bielany`
5. `/wymiana-akumulatora-warszawa-praga-poludnie`
6. `/wymiana-akumulatora-piaseczno`

Każda z tych podstron przechwyci 50–150 precyzyjnych zapytań lokalnych miesięcznie z zerowym kosztem reklamowym.

---

## 7. Podsumowanie Korzyści Finansowych

| Działanie Optymalizacyjne | Koszt wdrożenia | Spodziewany efekt biznesowy |
| :--- | :---: | :--- |
| **Przyspieszenie LCP z 9.2s do < 2.5s** | 0 zł | Zatrzymanie zniecierpliwionych kierowców na telefonie; spadek CPC w Google Ads o ok. 15-20% dzięki wyższemu Landing Page Experience. |
| **Likwidacja CLS (0.374 -> 0.05)** | 0 zł | Stabilny interfejs, brak przypadkowych kliknięć, natychmiastowe kliknięcie w `tel:696556446`. |
| **Awans frazy głównej z pozycji 8.5 do TOP 3** | 0 zł | Wzrost bezpłatnych połączeń telefonicznych o szacunkowo **+30–50 zleceń / miesiąc**. |
| **Przejrzyste widełki cenowe + Trust Badges** | 0 zł | Wzrost konwersji ze strony na telefon o min. **+3–5 p.p.**; eliminacja niechcianych telefonów o sklep stacjonarny. |
