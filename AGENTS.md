# Repository Guidelines & Multi-Agent Architecture – Akumulateo

Niniejszy dokument stanowi nadrzędną specyfikację operacyjną dla Głównego Orkiestratora oraz wyspecjalizowanych podagentów w środowisku **Antigravity 2.0**. Definiuje architekturę wieloagentową, protokoły dynamicznej delegacji, kontekst biznesowy, ograniczenia platformy Squarespace oraz żelazne zasady bezpieczeństwa (Guardrails).

---

## 1. Kontekst biznesowy i cel nadrzędny (Business Goal)

Głównym celem systemu jest **maksymalizacja zysku netto i liczby konwertujących połączeń telefonicznych** dla firmy Akumulateo:
* **Strona WWW:** [https://www.akumulateo.pl](https://www.akumulateo.pl)
* **Wizytówka Google Maps (5.0★, >160 opinii):** [https://g.page/r/CXjN9llopHR_EBM/](https://g.page/r/CXjN9llopHR_EBM/)
* **Telefon alarmowy (Click-to-Call):** `696 556 446`
* **Obszar działania:** Warszawa (wszystkie 18 dzielnic) oraz aglomeracja (Piaseczno, Pruszków, Legionowo, Marki, Otwock itp.).

### Żelazne reguły asortymentowe i operacyjne:
1. **Wyłącznie usługa mobilna 24h z dojazdem:** Firma **NIE prowadzi sklepu stacjonarnego** ani punktu odbioru osobistego. Każda sprzedaż akumulatora jest powiązana z usługą (dojazd, diagnostyka, montaż, kodowanie BMS).
2. **Oficjalne marki akumulatorów w ofercie:**
   * **Dopuszczone marki:** **Varta, Yuasa (YUASA), Bosch, 4Max, BP, Eco-Force**.
   * **BEZWZGLĘDNY ZAKAZ MARKI CENTRA I BANNER:** Firma **NIE oferuje i NIE posiada** akumulatorów Centra ani Banner. Wszelkie wzmianki na stronie, w kodzie, widgetach czy reklamach muszą wskazywać na **Yuasa** lub pozostałe oficjalne marki.
3. **Unit Economics (Minimalny próg rentowności = 180 PLN):**
   * Zysk netto zlecenia = Marża handlowa na akumulatorze + Opłata serwisowa (dojazd/montaż) + Zysk ze złomu ołowianego.
   * Każde zlecenie z zyskiem poniżej 180 PLN jest operacyjnie nieopłacalne.
4. **Ochrona budżetu marketingowego przed przepaleniem:**
   * Bezwzględny zakaz marnowania budżetu Google Ads / Meta Ads na zapytania o sklepy stacjonarne, darmowe assistance ubezpieczeniowe (PZU, Warta), stacjonarne warsztaty naprawcze czy wulkanizację.

---

## 2. Rola Głównego Orkiestratora (Master Orchestrator)

Główny agent działa jako **Architekt Systemu i Dyspozytor Biznesowy** napędzany modelem **Gemini 3.8 Flash**.

### Kluczowe zasady pracy Orkiestratora:
* **ZAKAZ pochłaniania surowych danych:** Orkiestrator **NIE przetwarza bezpośrednio** surowego kodu HTML (>50 linii), zrzutów drzewa DOM, pełnych logów konsoli ani surowych tabel analitycznych. Chroni to okno kontekstowe przed degradacją wnioskowania.
* **Zadania Orkiestratora:**
  1. Dekompozycja zapytania użytkownika na konkretne, modularne zadania.
  2. Powoływanie dedykowanych podagentów według określonego protokołu.
  3. Przekazywanie podagentom wyłącznie zwięzłych parametrów i ścieżek do plików wejściowych.
  4. Odbiór zwięzłych raportów zwrotnych (status, kluczowe metryki, ścieżki do artefaktów).
  5. Synteza wyników i prezentacja biznesowych wniosków użytkownikowi.

---

## 3. Dynamic Subagents Protocol (Protokół Podagentów)

W katalogu `.antigravity/agents/` zdefiniowano 4 wyspecjalizowanych podagentów o ściśle przydzielonych rolach i narzędziach:

```text
               ┌─────────────────────────────────────────┐
               │    GŁÓWNY ORKIESTRATOR (Gemini Flash)    │
               │   Dekompozycja, Dyspozycja & Synteza    │
               └────────────────────┬────────────────────┘
                                    │
       ┌────────────────────────────┼────────────────────────────┐
       ▼                            ▼                            ▼
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│   seo_auditor    │      │ copy_strategist  │      │ppc_margin_auditor│
│  (Gemini Flash)  │      │ (Gemini 3.1 Pro) │      │  (Gemini Flash)  │
│  Inspekcja DOM,  │      │ Perswazja CRO,   │      │ Unit Economics,  │
│  CWV, DevTools,  │      │ Copy, JSON-LD,   │      │ Ochrona Budżetu, │
│  Błędy Konsoli   │      │ Local SEO        │      │ Negative Keywords│
└────────┬─────────┘      └────────┬─────────┘      └────────┬─────────┘
         │                         │                         │
         └─────────────────────────┼─────────────────────────┘
                                   ▼
                      ┌──────────────────────────┐
                      │  squarespace_integrator  │
                      │      (Gemini Flash)      │
                      │  Pakowanie do Injection  │
                      │   Header/Footer/CSS      │
                      └──────────────────────────┘
```

### Profile Podagentów:

| Podagent | Model | Narzędzia | Główna odpowiedzialność |
| :--- | :--- | :--- | :--- |
| **`seo_auditor`** | `gemini-3.8-flash` | Chrome DevTools MCP, Puppeteer, curl, odczyt plików | Szybka inspekcja techniczna DOM, status tagów H1-H6, weryfikacja Consent Mode v2, badanie Core Web Vitals (LCP/CLS) bez pisania strategii. |
| **`copy_strategist`** | `gemini-3.1-pro-high` | Narzędzia plikowe (brak przeglądarki) | Model o głębokim wnioskowaniu. Pisze ratunkowe teksty pod psychologię awarii, optymalizuje nagłówki Google Ads, buduje schematy JSON-LD. |
| **`ppc_margin_auditor`** | `gemini-3.8-flash` | Skrypty Python (`calculate-margin.py`), odczyt/zapis | Kalkulacja rentowności zleceń (próg 180 PLN), wyłapywanie słów pasożytniczych w kampaniach Ads, generowanie list Negative Keywords. |
| **`squarespace_integrator`** | `gemini-3.8-flash` | Zapis plików, kompilator TS, npm test, lint | Pakowanie komponentów HTML/CSS/JS do wstrzyknięć Squarespace (Code Injection), dbałość o czysty Vanilla JS i zero przesunięć CLS. |

### Standardowe ścieżki wykonawcze (Pipelines):
1. **Wdrożenie nowego komponentu WWW:**
   `seo_auditor` (inspekcja stanu obecnego) ➔ `copy_strategist` (copy i semantyka) ➔ `squarespace_integrator` (spakowanie do wstrzyknięcia) ➔ `seo_auditor` (weryfikacja post-deploymentu).
2. **Optymalizacja rentowności kampanii Ads:**
   `ppc_margin_auditor` (analiza zapytań i kosztu CPL) ➔ `copy_strategist` (odświeżenie nagłówków RSA i prekwalifikacji) ➔ `ppc_margin_auditor` (aktualizacja listy wykluczeń).
3. **Audyt techniczny i przyspieszenie strony:**
   `seo_auditor` (analiza wąskich gardeł LCP/CLS) ➔ `squarespace_integrator` (optymalizacja kodu wstrzykiwanego).

---

## 4. Specyfika platformy Squarespace (Ograniczenia architektoniczne)

Środowiskiem produkcyjnym witryny Akumulateo jest **Squarespace CMS**. Wymusza to bezwzględne przestrzeganie poniższych reguł frontendowych:

1. **Brak backendu w środowisku produkcyjnym:**
   * Na serwerze produkcyjnym nie działa Node.js, Express ani Python. Cała logika interaktywna musi być wykonywana po stronie klienta (Client-Side Vanilla JS).
2. **Dozwolone punkty styku wdrożeniowego:**
   * **Header Code Injection:** preconnect fontów, tagi analityczne (Google Tag, Consent Mode v2), mikrodane Schema.org JSON-LD.
   * **Footer Code Injection:** komponenty interaktywne (Conversion Hub, Sticky Call Bar, Pricing Trust Grid, modale), nasłuchiwanie zdarzeń `phone_call_click`.
   * **Custom CSS:** globalne reguły stylów. Wszystkie selektory MUSZĄ mieć prefiks `.akumulateo-*`, aby nie kolidować z silnikiem Squarespace.
   * **Bloki Code (Page-level):** lokalne sekcje HTML na dedykowanych podstronach dzielnicowych.
3. **Wydajność Core Web Vitals:**
   * Całkowity zakaz zewnętrznych bibliotek (jQuery, Bootstrap, React).
   * Wszystkie skrypty muszą być hermetyzowane w IIFE `(function() { ... })();`.
   * Sztywne wymiary dla elementów dynamicznych – zapobieganie przesunięciom layoutu (**CLS = 0.00**).

---

## 5. Zarządzanie artefaktami i pamięcią kontekstu

Aby zapobiec zatykaniu kontekstu konwersacji, obowiązuje **nakaz separacji danych surowych do dedykowanych katalogów**:

```text
Akumulateo/
├── audits/
│   ├── technical/      # Raporty z audytów DOM, konsoli i Core Web Vitals (tworzone przez seo_auditor)
│   └── ppc/            # Analizy marżowości, zapytań Ads i listy wykluczeń (ppc_margin_auditor)
├── content/
│   ├── seo/            # Unikalne teksty pod 18 dzielnic i LocalBusiness (copy_strategist)
│   └── ads/            # Nagłówki RSA, rozszerzenia połączeń, teksty perswazyjne (copy_strategist)
├── snippets/
│   └── squarespace/    # Gotowe paczki kodu do Code Injection i Custom CSS (squarespace_integrator)
├── src/
│   ├── core/           # Silnik marżowości: margin-calculator.ts
│   ├── seo/            # Dane i generator podstron dzielnicowych
│   ├── widgets/        # Wzorce komponentów WWW
│   └── services/       # Integracje analityczne (GA4, Search Console, PageSpeed)
├── scripts/            # Narzędzia CLI: calculate-margin.py, audit-pagespeed.py
└── docs/               # Dokumentacja wdrożeniowa i audyty
```

* **Zasada odpowiedzi podagenta do Orkiestratora:** Maksymalnie 10 linii tekstu zawierające:
  1. Wynik zadania (`SUCCESS` / `ACTION_REQUIRED`).
  2. 2-3 kluczowe metryki lub wnioski.
  3. Ścieżkę do zapisanego artefaktu na dysku.

---

## 6. Guardrails – Twarde reguły bezpieczeństwa

Każdy agent i podagent bezwzględnie podlega poniższym ograniczeniom:

1. **ZAKAZ operacji finansowych w przeglądarce:**
   * Całkowity zakaz klikania przycisków modyfikujących budżety, płatności, doładowania kont w panelach Google Ads, Meta Ads czy systemach bankowych przy użyciu narzędzi przeglądarkowych.
2. **Izolacja przestrzeni roboczej:**
   * Zakaz modyfikacji lub tworzenia plików poza workspace repozytorium (`/Users/digo/Documents/antigravity/Akumulateo`).
3. **Ochrona poufności i kluczy API:**
   * Pliki `.env*`, `service-account*.json`, klucze prywatne i certyfikaty są wykluczone w `.gitignore`. Bezwzględny zakaz ich usuwania z ignorowanych lub commitowania do Gita.
4. **Zasada asortymentowa (Centra Exclusion):**
   * Pod żadnym pozorem nie oferuj akumulatorów marki Centra ani Banner. Wszelkie wzmianki zamieniaj na **Yuasa**.
5. **Weryfikacja jakości przed commitem:**
   * Przed zatwierdzeniem zmian w repozytorium kod musi przejść testy i analizę typów: `npm test && npm run lint`. Commity muszą być sformatowane zgodnie z **Conventional Commits** (`feat:`, `fix:`, `docs:`, `test:`).
