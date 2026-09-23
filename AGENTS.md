# Repository Guidelines – Akumulateo

Niniejszy dokument stanowi przewodnik dla deweloperów oraz agentów AI uczestniczących w rozwoju projektu **Akumulateo**. Definiuje kontekst biznesowy, standardy architektoniczne, zasady optymalizacji zysku, konwencje kodowania, procedury weryfikacji oraz workflow Git.

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
   * Marża na akumulatorze (cena detaliczna z montażem vs cena zakupu hurtowego w hurtowni / Inter Cars).
   * Opłata za usługę dojazdu i montażu (zależna od pory dnia, nocy 24h, strefy dojazdu).
   * Zysk ze złomu ołowianego (odbiór zużytego akumulatora od klienta).
3. **Zasada ochrony budżetu reklamowego:**
   * Bezwzględny zakaz przepalania budżetu w Google Ads / FastTony na zapytania o sklepy stacjonarne, darmowe assistance ubezpieczeniowe (PZU, Warta), stacjonarne warsztaty czy wulkanizację.

---

## 2. Struktura projektu i istniejące moduły

Projekt łączy narzędzia operacyjne, analitykę marżową, optymalizacje konwersji oraz Local SEO:

```text
Akumulateo/
├── src/
│   ├── core/           # Logika marżowa: margin-calculator.ts (kalkulator rentowności zlecenia)
│   ├── seo/            # Local SEO: districts-data.ts, districts-content.ts (18 dzielnic + aglomeracja)
│   ├── widgets/        # Komponenty WWW: sticky-call-bar.html (pasek Click-to-Call na telefonie)
│   ├── services/       # Planowane integracje: Google Ads API, FastTony, bramki SMS
│   └── utils/          # Walidatory numerów, formatery walut i narzędzia pomocnicze
├── tests/              # Testy automatyczne: tests/unit/margin-calculator.test.ts (Vitest)
├── scripts/            # Skrypty analityczne CLI: calculate-margin.py
├── docs/               # Dokumentacja biznesowa i backlog: backlog-ideas.md
├── package.json        # Zależności TypeScript, Vitest, tsx
└── tsconfig.json       # Konfiguracja kompilatora TypeScript (strict mode)
```

---

## 3. Workflow Git i zdalne repozytorium

* **Zdalne repozytorium GitHub:** [https://github.com/maciejk-design/Akumulateo.git](https://github.com/maciejk-design/Akumulateo.git)
* **Główna gałąź:** `main` (śledzi `origin/main`).
* **Format commitów (Conventional Commits):**
  - `feat`: nowa funkcjonalność (np. `feat(seo): add Mokotow district landing data`)
  - `fix`: naprawa błędu (np. `fix(margin): correct night surcharge calculation`)
  - `docs`: zmiany w dokumentacji (np. `docs: update backlog ideas`)
  - `test`: dodanie lub poprawa testów (np. `test(margin): add AGM battery unit test`)
  - `chore`: zmiany konfiguracji, zależności (np. `chore: update gitignore`)
* **Zasada przed wysyłką (`push`):** Przed wykonaniem commita i pusha do `main` upewnij się, że testy i linter przechodzą bez błędów (`npm test && npm run lint`).

---

## 4. Polecenia operacyjne i deweloperskie

* `npm install` – instalacja zależności deweloperskich projektu.
* `npm run dev` – uruchomienie środowiska deweloperskiego w trybie obserwacji (`tsx watch src/index.ts`).
* `npm run build` – kompilacja kodu TypeScript do katalogu `dist/` (`tsc`).
* `npm test` – wykonanie testów jednostkowych (`vitest run`).
* `npm run lint` – statyczna analiza typów TypeScript (`tsc --noEmit`).
* `python3 scripts/calculate-margin.py` – szybki kalkulator marży zlecenia w terminalu CLI.

---

## 5. Standardy kodowania i konwencje nazewnictwa

- **Typowanie:** TypeScript w trybie ścisłym (`strict: true`). Całkowity zakaz typu `any` – używaj precyzyjnych typów domenowych (`BatteryType`, `OrderCalculationResult`).
- **Formatowanie:** Wcięcia o szerokości 2 spacji, brak tabulatorów, kodowanie UTF-8, maksymalna długość linii 100 znaków.
- **Konwencje nazewnictwa:**
  - Funkcje i zmienne: `camelCase` (np. `calculateOrderMargin`, `districtName`).
  - Typy, interfejsy i klasy: `PascalCase` (np. `BatteryOrderInput`, `DistrictInfo`).
  - Stałe i konfiguracje: `UPPER_SNAKE_CASE` (np. `LEAD_SCRAP_VALUE_PLN`).
  - Pliki i katalogi: `kebab-case` (np. `margin-calculator.ts`, `districts-data.ts`).
- **Język w kodzie:** Kod źródłowy (zmienne, funkcje, komentarze techniczne) w języku angielskim. Treści marketingowe, Local SEO oraz komunikacja z klientami w języku polskim.

---

## 6. Wytyczne bezwzględne dla agentów AI

Każdy agent AI pracujący w tym repozytorium musi przestrzegać poniższych zasad:
1. **Biznesowy filtr decyzji:** Każda zmiana kodu, kampanii czy treści musi odpowiadać na pytanie: *„Czy to przyniesie realne telefony i marżę dla Akumulateo, czy spali budżet?”*.
2. **Jasny komunikat braku sklepu stacjonarnego:** Wszelkie tworzone teksty i metadane muszą jednoznacznie komunikować usługę mobilną 24h z dojazdem, eliminując nieopłacalne zapytania o odbiór osobisty.
3. **Ochrona poufności i kluczy API:** Bezwzględny zakaz commitowania kluczy API, tokenów (Google Ads, FastTony, GitHub, bramki SMS) oraz danych klientów. Pliki `.env*` muszą pozostać wykluczone w `.gitignore`.
4. **Minimalne, przetestowane diffy:** Modyfikacje kodu muszą być celowe, poparte testami jednostkowymi i opisane w języku polskim.
