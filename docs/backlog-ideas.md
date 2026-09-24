# Akumulateo – Backlog Pomysłów i Rozwoju Biznesu (Wstrzymane / Do Wdrożenia)

Ten dokument gromadzi pomysły, funkcjonalności oraz optymalizacje marketingowo-operacyjne odłożone w czasie, które mogą przynieść firmie Akumulateo dodatkowy zysk lub usprawnić procesy w kolejnych etapach rozwoju.

---

## 0. Kalkulator Marży i Doboru Akumulatora (`src/core/margin-calculator.ts`)
* **Status:** Wstrzymane / Zapisane jako pomysł (na ten moment nie wdrażamy, zrealizowany zalążek kodu w repozytorium pozostaje do ewentualnego użycia w przyszłości).
* **Priorytet:** Średni / Do decyzji po ustabilizowaniu bieżącej sprzedaży.
* **Cel:** Automatyzacja wyceny zleceń w dyspozytorni, wyliczanie czystej marży (akumulator + usługa + zysk ze złomu) oraz szybki dobór typu akumulatora (AGM/EFB/kwasowy) pod markę i rocznik auta.
* **Istniejące zasoby:**
  - Logika kalkulatora marży: `src/core/margin-calculator.ts`
  - Testy jednostkowe: `tests/unit/margin-calculator.test.ts`
  - Prosty skrypt CLI: `scripts/calculate-margin.py`

---

## 1. Dynamic Call Tracking (DNI – Dynamic Number Insertion)
* **Status:** Wstrzymane (do wdrożenia po ustabilizowaniu kampanii Google Ads i stałego wolumenu połączeń)
* **Priorytet:** Średni / Wysoki w skali 3–6 miesięcy.
* **Cel:** 100% precyzyjne przypisanie każdego telefonu przychodzącego do konkretnego słowa kluczowego i kampanii w Google Ads / Meta Ads.

### Opis koncepcji:
Obecnie na stronie `akumulateo.pl` znajduje się jeden stały numer telefonu (`696 556 446`). Kliknięcia na urządzeniach mobilnych mierzone są przez zdarzenie `phone_call_click` (gtag). Dynamic Call Tracking podmienia numer na stronie w czasie rzeczywistym w zależności od źródła ruchu (np. użytkownik z Google Ads widzi wirtualny numer A, użytkownik z SEO numer B, a z bezpośredniego wejścia numer C).

### Rekomendowane rozwiązania:
1. **Darmowe / natywne Google Forwarding Numbers (GFN):**
   * Wykorzystanie wbudowanego w Google Ads skryptu podmiany numeru na numer przekierowujący Google.
   * Koszt: 0 zł (w ramach Google Ads).
   * Mierzy: czas trwania połączenia (np. odrzuca połączenia < 30s), słowo kluczowe, godzinę.
2. **Zaawansowane platformy Call Tracking (np. CallPage, Dzinga, Ringostat):**
   * Nagrywanie rozmów (kontrola jakości ofertowania przez technika).
   * Integracja webhookiem z CRM.
   * Koszt: abonament od ok. 100-250 zł/miesięcznie.

---

## 2. Zautomatyzowany System Pozyskiwania Opinii Google (5.0★) przez SMS
* **Status:** Wstrzymane (wymaga API do bramki SMS lub prostej automatyzacji na telefonie technika)
* **Priorytet:** Wysoki (kluczowy lewar w Local SEO i zaufaniu klientów w nagłych wypadkach).
* **Cel:** Zwiększenie liczby ocen 5.0★ na profilu Google (`https://g.page/r/CXjN9llopHR_EBM/`) po każdej udanej wymianie akumulatora.

### Scenariusz działania:
1. Po zakończeniu montażu i rozliczeniu gotówką/BLIKiem/kartą technik wysyła automatyczny SMS do klienta (np. 15-30 minut po usłudze).
2. Treść wiadomości:
   > *"Dziękujemy za skorzystanie z pogotowia akumulatorowego Akumulateo! Cieszymy się, że auto znów odpala. Czy mógłbyś poświęcić 10 sekund i zostawić nam krótką opinię w Google? Pomaga nam to pomagać kolejnym uwięzionym kierowcom: https://g.page/r/CXjN9llopHR_EBM/review - Pozdrawiamy, Akumulateo 24h"*
3. Zwiększenie liczby recenzji z 20 do 100+ dramatycznie podniesie pozycję w Mapach Google (Local 3-Pack) w Warszawie bez wydawania ani 1 zł na reklamy.

---

## 3. Baza Doboru Akumulatorów dla Dyspozytora (Automated Battery Matching)
* **Status:** Pomysł do rozbudowy modułu `src/core/`
* **Cel:** Skrócenie czasu rozmowy telefonicznej i eliminacja błędów przy doborze baterii (np. Start-Stop AGM vs EFB, polaryzacja lewy/prawy plus, mocowanie stopki B13/B14).
* **Architektura:** Prosty interfejs lub CLI, w którym dyspozytor wpisuje markę, model, rok i silnik (np. `BMW 320d F30 2014`), a system podaje:
  * Wymagany typ: AGM, 80Ah, 800A CCA.
  * Czy wymagane jest kodowanie BMS: TAK (+60 PLN).
  * Numery katalogowe w hurtowni (Varta Silver Dynamic AGM F21, Yuasa YBX9019, Bosch S5 A11 itp.).
  * Rekomendowaną cenę dla klienta z montażem i minimalną marżą.

---

## 4. Retargeting SMS przed sezonem zimowym (Listopad / Grudzień)
* **Status:** Pomysł sezonowy
* **Cel:** Przypomnienie się klientom, którym robiono jedynie awaryjny rozruch boosterem (bez wymiany akumulatora).
* **Zasada:** Kierowca, któremu rozładował się akumulator latem/jesienią i odpalił z kabli, niemal na pewno stanie na mrozie w grudniu/styczniu.
* **Działanie:** Propozycja bezpłatnego testu akumulatora lub rabatu 30 PLN na nowy akumulator z montażem przed pierwszymi mrozami.
