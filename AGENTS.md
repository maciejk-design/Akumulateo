# Repository Guidelines – Akumulateo

Niniejszy dokument stanowi przewodnik dla deweloperów oraz agentów AI uczestniczących w rozwoju projektu **Akumulateo**. Definiuje kontekst biznesowy, standardy architektoniczne, zasady optymalizacji zysku, konwencje kodowania oraz procedury weryfikacji.

---

## 1. Kontekst biznesowy i cel nadrzędny (Business Goal)

Głównym celem tego projektu jest **osiąganie i maksymalizacja zysku z działalności firmy Akumulateo**:
* **Strona WWW:** [https://www.akumulateo.pl](https://www.akumulateo.pl)
* **Wizytówka Google (5.0★):** [https://g.page/r/CXjN9llopHR_EBM/](https://g.page/r/CXjN9llopHR_EBM/)
* **Telefon alarmowy:** `696 556 446`
* **Obszar działania:** Warszawa (wszystkie 18 dzielnic) oraz aglomeracja warszawska (Piaseczno, Pruszków, Legionowo, Marki, Otwock itp.).

### Kluczowe reguły biznesowe:
1. **Wyłącznie usługa mobilna 24h z dojazdem:** Firma **NIE prowadzi sklepu stacjonarnego** ani odbioru osobistego. Każda sprzedaż akumulatora jest powiązana z usługą (dojazd, diagnostyka, montaż, kodowanie BMS).
2. **Struktura marży (Unit Economics):**
   * Marża na akumulatorze (cena detaliczna z montażem vs cena zakupu hurtowego w Inter Cars / hurtowni).
   * Opłata za usługę dojazdu i montażu (zależna od pory dnia, nocy 24h, lokalizacji).
   * Zysk ze złomu ołowianego (odbiór starego akumulatora od klienta).
3. **Zasada ochrony budżetu reklamowego:**
   * Bezwzględny zakaz przepalania budżetu w Google Ads / FastTony na zapytania o sklepy stacjonarne, darmowe assistance ubezpieczeniowe (PZU, Warta itp.), warsztaty stacjonarne czy wulkanizację.

---

## 2. Struktura projektu i organizacja modułów

Projekt łączy narzędzia operacyjne, analitykę marketingową oraz automatyzacje wspierające zysk:

```text
Akumulateo/
├── src/
│   ├── core/           # Logika domenowa: kalkulatory marży, baza doboru akumulatorów (Ah, CCA, AGM/EFB)
│   ├── services/       # Integracje: Google Ads API, FastTony, analityka połączeń, integracje SMS
│   ├── widgets/        # Komponenty i skrypty wstrzykiwane na stronę Squarespace (Click-to-Call, Call Tracking)
│   ├── seo/            # Generator danych pod Local SEO (dzielnice Warszawy, schema.org, metadane)
│   ├── utils/          # Narzędzia pomocnicze, walidatory numerów telefonów, formatery walut
│   └── config/         # Konfiguracja środowiskowa, reguły wykluczeń i stawek
├── tests/              # Testy automatyczne (jednostkowe i integracyjne)
├── docs/               # Dokumentacja operacyjna, audyty Google Ads, procedury obsługi klienta
└── scripts/            # Skrypty analityczne, generatory raportów opłacalności kampanii
```

---

## 3. Standardy techniczne i kodowania

- **Język i typowanie:** TypeScript w trybie ścisłym (`strict: true`). Brak typu `any` – używaj precyzyjnych typów domenowych (`BatteryType`, `CarModel`, `OrderMargin`).
- **Formatowanie:** Wcięcia o szerokości 2 spacji, zakaz tabulatorów, UTF-8.
- **Konwencje nazewnictwa:**
  - Zmienne, funkcje i metody: `camelCase` (np. `calculateJobProfit`, `filterNegativeKeywords`).
  - Typy, interfejsy i klasy: `PascalCase` (np. `BatterySpecification`, `DispatchOrder`).
  - Stałe i konfiguracje: `UPPER_SNAKE_CASE` (np. `MIN_ACCEPTABLE_MARGIN_PLN`).
  - Pliki i katalogi: `kebab-case` (np. `battery-calculator.ts`, `margin-tracker/`).
- **Język w kodzie:** Kod źródłowy (zmienne, funkcje, komentarze w kodzie) w języku angielskim. Treści marketingowe, dokumentacja biznesowa i komunikaty dla klientów w języku polskim.

---

## 4. Polecenia operacyjne i deweloperskie

- `npm run dev` – uruchomienie środowiska deweloperskiego narzędzi pomocniczych.
- `npm run build` – kompilacja skryptów i narzędzi do katalogu `dist/`.
- `npm test` – uruchomienie testów jednostkowych (Vitest/Jest).
- `npm run lint` – statyczna analiza kodu pod kątem błędów i standardów stylu.

---

## 5. Wytyczne dla agentów AI (Wymagania bezwzględne)

Każdy agent AI pracujący w tym repozytorium musi przestrzegać poniższych zasad:
1. **Filtr biznesowy każdej decyzji:** Zanim zaproponujesz kod, zmianę w kampanii lub konfigurację strony, zadaj pytanie: *„Czy to przyniesie realne telefony i zysk dla Akumulateo, czy spali budżet?”*.
2. **Świadomość braku sklepu stacjonarnego:** Wszelkie tworzone teksty reklamowe, strony czy metadane muszą jasno komunikować usługę mobilną z dojazdem 24h, aby odsiać osoby szukające odbioru stacjonarnego.
3. **Poufność:** Pod żadnym pozorem nie commituj kluczy API (FastTony, Google Ads, SMS API), danych osobowych klientów ani numerów telefonów w publicznych plikach. Stosuj wyłącznie pliki `.env` ignorowane w git.
4. **Minimalne, precyzyjne diffy:** Modyfikacje kodu i konfiguracji muszą być celowe, przetestowane i udokumentowane w języku polskim.
