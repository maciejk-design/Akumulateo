# Akumulateo – Pełna Mapa Integracji, Połączeń i Analityki

Niniejszy dokument stanowi centralne źródło wiedzy o **wszystkich połączeniach zewnętrznych, integracjach API, kodach śledzących, kluczach dostępowych i automatyzacjach** wdrożonych w systemie firmy **Akumulateo**.

---

## 1. Główna Tabela Zbiorcza (Master Matrix)

| Połączenie / System | Identyfikatory / Klucze | Lokalizacja w kodzie | Zastosowanie obecne | Przeznaczenie docelowe |
| :--- | :--- | :--- | :--- | :--- |
| **Google Analytics 4 (GA4)** | • Pomiar: `G-2KXNL0LQWG`<br>• Usługa: `475492247` | • Header: `gtag.js`<br>• Footer: `phone_call_click`<br>• `.env`: `GA4_PROPERTY_ID` | Zliczanie sesji, źródeł ruchu, zaangażowania oraz kliknięć w numer alarmowy `696 556 446`. | • Mierzenie konwersji ze smartfonów.<br>• Analiza zamówień nocnych (22:00–06:00, dopłata +80 PLN).<br>• Analiza konwersji z podstron dzielnicowych. |
| **Google Ads** | • Konto: `AW-16941768870`<br>• Etykieta: `8xEACOaFl60aEKbBu44_` | • Header: `gtag('config', 'AW-...')`<br>• Footer: zdarzenie `conversion` | Rejestracja konwersji z kliknięć w dolny pasek Sticky Call Bar w kampaniach płatnych Google Ads. | • Optymalizacja stawek (Smart Bidding).<br>• W przyszłości: **Offline Conversion Import (OCI)** optymalizujący reklamy pod realny zysk netto (>180 PLN). |
| **FastTony Pixel** | • Pixel ID: `1cf82dd91068403291d066c568c5b152`<br>• Obiekt: `window.forsantLayer` | • Header: skrypt piksela<br>• Footer: `forsantLayer.push` | Zbieranie zdarzeń `phoneClick` i optymalizacja kampanii PPC przez silnik FastTony. | • Prekwalifikacja odbiorców.<br>• Eliminacja przepalania budżetu (wykluczenia sklepów, wulkanizacji, drogiego elektryka). |
| **Google Search Console (GSC)** | • Usługa: `https://www.akumulateo.pl/`<br>• API: `v3/searchAnalytics` | • Skrypt: `scripts/ctr_gap_analyzer.py`<br>• `.env`: `GOOGLE_SEARCH_CONSOLE_SITE_URL` | Monitorowanie pozycji SEO, wyświetleń i CTR na frazach z Warszawy i okolic. | • Zasilanie automatycznego analizatora CTR Gap.<br>• Wykrywanie darmowego ruchu z fraz o wysokich wyświetleniach i niskim CTR.<br>• Wykrywanie ruchu pasożytniczego. |
| **PageSpeed Insights (PSI API)** | • Klucz: `AIzaSyCRpsWkn6mq4V2u3q1VSHFHWoZ2A1n1AOA`<br>• Cel: `https://www.akumulateo.pl/` | • Skrypt: `scripts/audit-pagespeed.py`<br>• `.env`: `GOOGLE_PAGESPEED_API_KEY` | CLI do automatycznego audytu Core Web Vitals (LCP, CLS, FID/INP) dla urządzeń mobilnych. | • Ochrona szybkości ładowania strony (<2.5s).<br>• Gwarancja, że kierowca w sytuacji awaryjnej natychmiast widzi numer telefonu. |
| **Google Cloud Service Account** | • E-mail: `akumulateo-agent@akumulateo-analytics.iam.gserviceaccount.com`<br>• Plik: `service-account.json` | • Główny katalog: `service-account.json`<br>• `.env`: `GOOGLE_SERVICE_ACCOUNT_KEY_PATH` | Bezpieczna, bezhasłowa autoryzacja OAuth2 JWT dla skryptów Pythona/Node. | • Umożliwienie AI i skryptom CLI bezpośredniego odpytywania GSC i GA4 bez używania przeglądarki. |
| **Google Consent Mode v2 + FastTony Bridge** | • Skrypt JS: tryb domyślny `denied`, synchronizacja do `granted` | • Header Injection: linie 1–102 w pliku nagłówkowym | Zgodność z RODO oraz wymogami Digital Markets Act (DMA). Synchronizacja z banerem Squarespace. | • Zapobieganie utracie danych w Google Ads i GA4.<br>• Poprawne modelowanie konwersji w Google bez łamania prywatności. |
| **Squarespace CMS 7.1** | • Instancja: `celery-robin-sffx.squarespace.com`<br>• Domena: `https://www.akumulateo.pl` | • Custom CSS<br>• Header Code Injection<br>• Footer Code Injection | Środowisko produkcyjne witryny, serwowanie treści, formularzy i paska Click-to-Call. | • Hostowanie 18 dedykowanych landing page'y dzielnicowych oraz podstron miast aglomeracji. |
| **Profil Firmy Google (GBP / Maps)** | • Link wizytówki: `https://g.page/r/CXjN9llopHR_EBM/`<br>• Ocena: 5.0★ (100+ opinii) | • Linki w stopce i widżetach<br>• Schema.org JSON-LD | Główne źródło bezpośrednich połączeń telefonicznych z map Google w Warszawie. | • Dominacja w Local SEO na hasła typu „pogotowie akumulatorowe warszawa”.<br>• Zdobycie 300+ opinii 5.0★. |

---

## 2. Architektura Przepływu Danych (Data Flow)

```
[ Kierowca w Warszawie wpisuje w Google: "wymiana akumulatora z dojazdem" ]
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
   [ Google Ads / FastTony ]              [ Wyniki Organiczne (SEO) ]
   Awaryjne nagłówki RSA                  Pozycjonowanie dzielnicowe
            │                                     │
            └──────────────────┬──────────────────┘
                               ▼
        [ Wejście na www.akumulateo.pl (Squarespace CMS) ]
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
  [ Google Consent Mode v2 ]              [ FastTony Pixel ]
  Sprawdza zgodę na ciasteczka             Śledzi sesję i źródło
            │
            ▼
  [ Załadowanie Google Tag: G-2KXNL0LQWG + AW-16941768870 ]
                               │
                               ▼
  [ Kliknięcie w Sticky Call Bar: "Zadzwoń: 696 556 446" ]
                               │
            ┌──────────────────┼──────────────────┐
            ▼                  ▼                  ▼
     [ Zdarzenie GA4 ]  [ Zdarzenie Ads ]  [ FastTony Layer ]
    phone_call_click       conversion         phoneClick
            │                  │                  │
            ▼                  ▼                  ▼
   [ Raporty GA4 ]      [ Smart Bidding ]  [ Optymalizacja PPC ]
```

---

## 3. Szczegółowy Opis Integracji

### 3.1. Google Analytics 4 (GA4)
* **Measurement ID:** `G-2KXNL0LQWG`
* **Property ID:** `475492247` (nazwa konta: `akumulateo GMF`)
* **Implementacja:**
  * Wstrzyknięty w **Settings -> Code Injection -> HEADER** za pomocą oficjalnej biblioteki `gtag.js`.
  * W **Settings -> Code Injection -> FOOTER** funkcja `akumulateoTrackPhoneClick(e)` wysyła zdarzenie:
    ```javascript
    window.gtag('event', 'phone_call_click', {
      event_category: 'Contact',
      event_label: '+48696556446',
      value: 100
    });
    ```
* **Cel biznesowy:** Monitorowanie liczby połączeń ze strony, weryfikacja godzin wzmożonego ruchu nocnego (godziny 22:00–06:00 kwalifikujące się do dopłaty +80 PLN) oraz ocena skuteczności poszczególnych podstron dzielnicowych.

---

### 3.2. Google Ads & FastTony
* **Konto Google Ads:** `AW-16941768870`
* **Identyfikator konwersji telefonu:** `AW-16941768870/8xEACOaFl60aEKbBu44_`
* **FastTony Pixel ID:** `1cf82dd91068403291d066c568c5b152`
* **DataLayer:** `window.forsantLayer`
* **Zasady kampanii (Guardrails):**
  * **Geolokalizacja:** Promień **40 km wokół Warszawy**.
  * **Wykluczenia krytyczne:** Wulkanizacja (`wulkanizacja`, `wulkanizacja mobilna`, `wymiana koła`, `naprawa opon`, `шиномонтаж`), drogi elektryk instalacyjny (`elektryk samochodowy warszawa z dojazdem` – 35 zł/klik), darmowe assistance (`assistance pzu`, `assistance warta`), sklepy stacjonarne (`sklep`, `hurtownia`, `odbiór osobisty`).
  * **Odblokowane słowo `cena`:** Pojedyncze słowo `cena` jest **dopuszczone** (aby nie blokować zapytań `wymiana akumulatora z dojazdem cena`).
* **Planowana innowacja (Backlog):** **Offline Conversion Import (OCI)** – importowanie do Google Ads wyłącznie zrealizowanych zleceń z zyskiem netto > 180 PLN, aby algorytm Smart Bidding uczył się licytować wyżej za klientów płacących, a nie za puste telefony.

---

### 3.3. Google Search Console (GSC) API
* **Adres usługi:** `https://www.akumulateo.pl/`
* **Metoda autoryzacji:** Service Account OAuth2 JWT (brak potrzeby haseł czy refresh tokenów).
* **Aktywne narzędzie:** [`scripts/ctr_gap_analyzer.py`](file:///Users/digo/Documents/antigravity/Akumulateo/scripts/ctr_gap_analyzer.py)
* **Zastosowanie:**
  * Pobiera rzeczywiste zapytania użytkowników z ostatnich 28 dni.
  * Filtruje frazy o wysokiej liczbie wyświetleń i niskim współczynniku klikalności (CTR < 4%).
  * Generuje gotowe do wklejenia w Squarespace warianty `SEO Title` i `SEO Description` oparte na psychologii awarii (np. *„Nie odpali? Dojedziemy w 20-30 min”*).
  * Ostatni wygenerowany raport: [`audits/ppc/ctr-gap-report-2026-09-29.md`](file:///Users/digo/Documents/antigravity/Akumulateo/audits/ppc/ctr-gap-report-2026-09-29.md) (potencjał: **+41 darmowych kliknięć/mies.**).

---

### 3.4. PageSpeed Insights (PSI) API
* **Klucz API:** `AIzaSyCRpsWkn6mq4V2u3q1VSHFHWoZ2A1n1AOA`
* **Ograniczenie klucza:** Wyłącznie PageSpeed Insights API w Google Cloud Console.
* **Aktywne narzędzie:** [`scripts/audit-pagespeed.py`](file:///Users/digo/Documents/antigravity/Akumulateo/scripts/audit-pagespeed.py)
* **Zastosowanie:**
  * Błyskawiczny audyt wydajności mobilnej z poziomu terminala bez otwierania przeglądarki.
  * Stały monitoring wskaźnika **LCP** (Largest Contentful Paint) oraz **CLS** (Cumulative Layout Shift = 0.000).

---

### 3.5. Google Cloud Platform (GCP) – Service Account
* **Projekt GCP:** `akumulateo-analytics` (Numer projektu: `964051019234`)
* **Konto usługi:** `akumulateo-agent@akumulateo-analytics.iam.gserviceaccount.com`
* **Plik klucza:** `service-account.json` w katalogu głównym projektu (zabezpieczony w `.gitignore`).
* **Włączone interfejsy API:**
  1. *Google Search Console API*
  2. *Google Analytics Data API*
  3. *PageSpeed Insights API*
  4. *API Keys API*
* **Nadane uprawnienia:**
  * GSC: Użytkownik z prawami odczytu (Restricted Viewer).
  * GA4: Użytkownik z rolą Przeglądający (Viewer).

---

### 3.6. Google Consent Mode v2 & Baner GDPR
* **Lokalizacja:** Początek pliku nagłówkowego Squarespace Header Code Injection.
* **Działanie:**
  * Domyślnie ustawia stan zgód na `denied` dla `analytics_storage`, `ad_storage`, `ad_user_data` oraz `ad_personalization`.
  * Nasłuchuje zdarzeń kliknięcia na natywnym banerze ciasteczek Squarespace (`.gdpr-cookie-banner`).
  * Gdy użytkownik kliknie akceptację, natychmiast wysyła komendę `gtag('consent', 'update', { ...: 'granted' })`.
  * **Koegzystencja UX:** Baner cookies posiada `z-index: 10000005 !important`, a dolny pasek Sticky Call Bar ustępuje mu miejsca lub układa się poniżej, zapewniając 100% klikalności przycisków RODO.

---

### 3.7. Profil Firmy w Google (GBP / Google Maps)
* **Konto:** Akumulateo – Pogotowie akumulatorowe Warszawa 24h
* **Ocena:** 5.0★ (100+ opinii)
* **Kategoria główna:** **`Sklep z akumulatorami`**
* **Kategorie dodatkowe:** **`Mechanik samochodowy`**, **`Elektryk samochodowy`**
* **Żelazny zakaz:** Kategoria **`Pomoc drogowa`** została trwale usunięta (generowała nieopłacalne telefony o wulkanizację, zmianę kół i holowanie).

---

## 4. Dostępne Skrypty Narzędziowe w Projekcie

Wszystkie skrypty działają natywnie w środowisku macOS / Linux bez potrzeby instalowania zewnętrznych zależności:

| Skrypt | Polecenie uruchomienia | Co robi? |
| :--- | :--- | :--- |
| **Test połączeń API** | `python3 scripts/test_google_connection.py` | Sprawdza ważność tokena JWT oraz pobiera testowe dane z GSC i GA4. |
| **Analizator luki CTR** | `python3 scripts/ctr_gap_analyzer.py` | Analizuje zapytania z GSC i generuje gotowy raport z propozycjami meta tytułów i opisów w `audits/ppc/`. |
| **Audyt mobilny PageSpeed** | `python3 scripts/audit-pagespeed.py https://www.akumulateo.pl` | Mierzy wyniki Core Web Vitals i audyt techniczny dla urządzeń mobilnych. |
| **Kalkulator marży 180 PLN** | `python3 scripts/calculate-margin.py` | Wylicza rentowność zlecenia uwzględniając marżę na akumulatorze, montaż i skup złomu ołowianego. |
| **Wstrzykiwanie nagłówka** | `python3 scripts/apply_squarespace_header.py` | Automatycznie aktualizuje Header Injection w Squarespace przez przeglądarkę Chrome. |

---

## 5. Zasady Bezpieczeństwa (Guardrails)

1. **Pliki poufne:** Pliki `.env`, `service-account.json`, certyfikaty `*.pem` i klucze API pod żadnym pozorem nie mogą być commitowane do repozytorium Git (chronione przez `.gitignore`).
2. **Zakaz ingerencji w finanse przez przeglądarkę:** Agent AI ma bezwzględny zakaz modyfikacji budżetów, płatności czy kart płatniczych w panelach Google Ads, Meta Ads czy systemach bankowych.
3. **Zasada asortymentowa:** W żadnym kodzie, widżecie ani kampanii nie wolno oferować akumulatorów marek Centra ani Banner (zastępowane zawsze marką **Yuasa** lub Varta/Bosch).
4. **Próg rentowności:** Każde zlecenie serwisowe musi generować minimum **180 PLN zysku netto**.
