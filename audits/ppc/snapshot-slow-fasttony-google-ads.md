# Snapshot Słów Kluczowych i Wykluczeń: FastTony vs Google Ads

**Data wykonania snapshotu:** 24 września 2026 r.  
**Konto:** `akumulateo@gmail.com` | Google Ads CID: `698-263-0728` | Kampania ID: `22364165752`  
**Cel:** Trwały punkt odniesienia do weryfikacji stabilności ustawień FastTony oraz kontroli synchronizacji z Google Ads.

---

## 1. Podsumowanie Weryfikacji Synchronizacji

* **Stabilność FastTony:** Przetestowano przełączniki po przeładowaniu strony i zmianie widoków – **brak samoistnego odznaczania się fraz**. Wszystkie stany są zapisane i trwałe.
* **Synchronizacja Słów Pozytywnych z Google Ads (100% SUKCES):**
  - Fraza `sklepy` została natychmiast **Wstrzymana** (Paused) w Google Ads.
  - Wszystkie 9 odblokowanych fraz pogotowia (`akumulator z montażem warszawa`, `awaryjne odpalanie auta`, `akumulatory 24h` itd.) są w Google Ads **Włączone** (Enabled).
* **Synchronizacja Wykluczeń (Negative Keywords):**
  - FastTony zarządza listą współdzieloną przez API Forsant.
  - 5 fraz (`zakładanie akumulatora`, `zamieniecka`, `herbsta`, `herbstadolna`, `dolna`) jest już całkowicie usuniętych z listy wykluczeń Google Ads.
  - Pozostałe odznaczone frazy (`akumulator ursus`, `montowanie akumulatora`, ulice) są w FastTony wyłączone i przetwarzane przez okresowy batch API Forsant.

---

## 2. Inwentarz: Pozytywne Słowa Kluczowe w FastTony

### A. Słowa AKTYWNE (Włączone / ON) – Dokładnie 70 fraz:
1. `pogotowie akumulatorowe warszawa`
2. `Wymiana akumulatora z dojazdem`
3. `Uruchamianie auta boosterem`
4. `Mobilny serwis akumulatorów`
5. `Awaryjne uruchamianie auta Warszawa`
6. `Dowóz akumulatora`
7. `wymiana akumulatora z dojazdem cena`
8. `wymiana akumulatorów`
9. `wymiana akumulatora z dojazdem`
10. `akumulatory 24h`
11. `mobilna wymiana akumulatora`
12. `akumulatory 24h warszawa`
13. `akumulatory warszawa 24h`
14. `akumulator 24h`
15. `pomoc akumulatorowa`
16. `wymiana akumulatora u klienta`
17. `wymiana akumulatora`
18. `mobilny serwis akumulatorów`
19. `wymiana akumulatora samochodowego`
20. `akumulator na miejscu warszawa`
21. `mobilne pogotowie akumulatorowe`
22. `akumulator z montażem warszawa`
23. `akumulator z wymianą warszawa`
24. `awaryjne odpalanie samochodu warszawa`
25. `uruchomienie samochodu boosterem`
26. `wymiana akumulatora na miejscu`
27. `pogotowie akumulatorowe warszawa 24h`
28. `awaryjne uruchamianie samochodu`
29. `Awaryjne odpalenie samochodu`
30. `odpalenia pojazdów`
31. `awaryjne uruchamianie samochodów`
32. `pogotowie akumulatorowe`
33. `odpalanie auta warszawa`
34. `akumulator z dowozem warszawa`
35. `mobilna wymiana akumulatora warszawa`
36. `wymiana akumulatora u klienta warszawa`
37. `wymiana akumulatora warszawa`
38. `wymiana akumulatora z dojazdem warszawa`
39. `rozładowany akumulator warszawa`
40. `odpalanie auta`
41. `awaryjne odpalanie auta`
42. `awaryjne odpalanie samochodu`
43. `rozładowany akumulator`
44. `dojazd z akumulatorem`
45. `pomoc z akumulatorem`
46. `auto nie odpala pomoc`
47. `padł akumulator warszawa`
48. `jump start warsaw`
49. `auto nie odpala warszawa`
50. `awaryjne odpalenie warszawa`
51. `rozładowany akumulator pomoc`
52. `rozruch samochodu warszawa`
53. `akumulatory serwis pogotowie akumulatorowe`
54. `akumulator z dowozem`
55. `pogotowie akumulatorowe modlin`
56. `wymiana akumulatora modlin`
57. `akumulatory 24h modlin`
58. `pogotowie akumulatorowe Piaseczno`
59. `pogotowie akumulatorowe otwock`
60. `Dostawa Akumulatora z Montażem`
61. `montaż akumulatora`
62. `awaryjne uruchomienie auta`
63. `awaryjne uruchomienie samochodu`
64. `awaryjne uruchomienie auta 24/7`
65. `pogotowie akumulatorowe Warszawa`
66. `usługa ładowania akumulatora`
67. `wymiana akumulatora cena`
68. `diagnostyka akumulatora`
69. `pomoc drogowa akumulator`
70. `akumulator wymiana`

### B. Słowa NIEAKTYWNE (Wyłączone / OFF) – Dokładnie 20 fraz:
1. `sklepy` *(Zablokowane – brak sklepu stacjonarnego)*
2. `wymiana akumulatorów warszawa`
3. `akumulatory wymiana warszawa`
4. `wymiana akumulatora w samochodzie`
5. `akumulatory 24 warszawa`
6. `akumulatory 24`
7. `akumulatory 24 7`
8. `Akumulator do samochodu Warszawa`
9. `rozruch samochodu`
10. `odpalanie auta na miejscu`
11. `rozruch samochodu pomoc`
12. `akumulator samochodowy wymiana`
13. `Usługa Dostawy Akumulatora z Montażem`
14. `akumulator warszawa`
15. `akumulator do samochodu`
16. `uruchamianie auta 24h`
17. `wymiana akumulatora pomoc`
18. `akumulatory warszawa`
19. `akumulator 24`
20. `odpalanie samochodów`

---

## 3. Inwentarz: Wykluczenia w FastTony (Negatives)

### A. Słowa AKTYWNIE WYKLUCZONE (Wykluczenie Włączone / ON) – 98 fraz:
* **Ubezpieczalnie i bezpłatne assistance:** `pzu`, `warta`, `hestia`, `pzu assistance`, `pzu assistance telefon`, `warta assistance`, `warta hdi assistance`, `warta pomoc drogowa`, `ergo hestia assistance`, `generali assistance`, `link4 assistance`, `lexus assistance`, `ford assistance`, `arval assistance 24h`, `tip roadside assistance`, `assistance`.
* **Niepasujące usługi i warsztaty:** `wulkanizacja`, `wulkanizator`, `laweta`, `opony`, `warsztat samochodowy`, `warsztat samochodowy 24h`, `warsztat`, `mechanik`, `prostownik`, `ładowarka akumulatorów`, `jump booster`, `booster do samochodu`, `motocykl`, `odbiór osobisty`.
* **Inne miasta i zapytania ogólne:** `radom`, `kraków`, `łódź`, `lublin`, `gdańsk`, `ostrowiec`, `akumulatory radom`, `akumulator radom`, `akumulatory łódź`, `akumulatory lublin`, `budowa akumulatorów`, `budowa akumulator`, `naprawa akumulatorków`, `ceny akumulatorów`, `ceny akumulatorow samochodowych`, `kupic akumulator`, `kupie akumulator`, `kupię akumulator`, `najnowsze akumulatory`, `uszkodzenie akumulatora`, `sprzedam akumulatory`, `obsluga akumulatora`, `błąd akumulatora`, `działanie akumulatora`, `wartość akumulatora`, `wymontowanie akumulatora`, `sprzedaż akumulatorów samochodowych`, `akumulator sprzedaż`, `firmy akumulatorów`, `aku akumulator`, `akumulator 2`, `akumulator pomocniczy`, `odłączanie akumulatora samochodowego`, `przeładowany akumulator`, `naprawa akumulatorow`, `sklep z akumulatorami warszawa`, `sklep akumulatory warszawa`, `tanie akumulatory warszawa`, `akumulator cena`, `ile kosztuje akumulator do samochodu`, `centrum akumulatorów`, `hurtownia akumulatorów`, `sklepy akumulatorów`, `opinie`, `cena`, `Auto Kram`, `in plus`, `serwis 9 18`, `sklep`, `hurtownia`, `Inter Cars`, `tanie`, `kupno`, `sprzedaż`, `parametry`, `akumulatory marki fabryczna`, `centrum akumulatorów józefów`, `akumulatory fabryczna marki`, `specpart`, `dostawcy prądu`, `superakumulatory`, `sklep z akumulatorami`, `sklepy z akumulatorami`, `sklep motoryzacyjny`, `Auto Partner`, `Specpart`, `AK-POL`, `Świat Akumulatorów`, `allegro`, `osram`.

### B. Słowa ODBLOKOWANE (Wykluczenie Wyłączone / OFF) – 13 fraz:
1. `zakładanie akumulatora` *(ODBLOKOWANE)*
2. `montowanie akumulatora` *(ODBLOKOWANE)*
3. `akumulator ursus` *(ODBLOKOWANE)*
4. `akumulatory zamieniecka` *(ODBLOKOWANE)*
5. `radzymińska akumulatory` *(ODBLOKOWANE)*
6. `12 V` *(ODBLOKOWANE)*
7. `60 Ah` *(ODBLOKOWANE)*
8. `akumulatory modlińska` *(ODBLOKOWANE)*
9. `zamieniecka` *(ODBLOKOWANE)*
10. `ostródzka` *(ODBLOKOWANE)*
11. `herbsta` *(ODBLOKOWANE)*
12. `herbstadolna` *(ODBLOKOWANE)*
13. `dolna` *(ODBLOKOWANE)*

---

## 4. Wyniki Weryfikacji po 24 Godzinach (25 września 2026 r.)

### A. Potwierdzenie Stabilności FastTony:
- **0 zmian samoistnych:** Wszystkie 70 słów pozytywnych, fraza `sklepy` (OFF), promień 40 km oraz 13 odblokowanych wykluczeń zachowały swoje stany bez jakiejkolwiek ingerencji.

### B. Wyniki Biznesowe w Google Ads (Pierwsze 24h):
- Fraza `sklepy` wygenerowała **0 kliknięć i 0 zł kosztu** (skuteczna ochrona budżetu).
- Nowo odblokowana fraza `akumulator 24h` wygenerowała **1 kliknięcie przy CTR 50%** (koszt 8,58 zł).
- Fraza `awaryjne uruchamianie hybrydy` przyniosła **2 kliknięcia** (16,64 zł).
- Fraza `akumulatory grodzisk mazowiecki` wygenerowała **1 kliknięcie** z nowego promienia 40 km.

### C. Wnioski Dotyczące Wykluczeń w Google Ads:
- W FastTony wykluczenia są wyłączone, co oznacza, że reguły FastTony nie blokują tych zapytań.
- Współdzielona lista wykluczeń w Google Ads (`[Forsant API] Negative keyword list - 1742476080`) wymaga manualnego zgłoszenia do supportu FastTony lub nadania uprawnień edycyjnych dla konta Google Ads w celu fizycznego usunięcia wpisów takich jak `akumulator ursus`.

---

## 5. Aktualizacja Snapshotu: 29–30 września 2026 r.

### A. Nowe wykluczenia dodane do listy (Blokada wulkanizacji i drogiego elektryka):
1. `шиномонтаж` (wulkanizacja cyrylicą – odcięcie zapytań o serwisy oponiarskie w języku ukraińskim/rosyjskim)
2. `wulkanizacja mobilna`
3. `wymiana koła`
4. `naprawa opon`
5. `elektryk samochodowy warszawa z dojazdem` (ochrona budżetu przed stawkami 35 zł/klik na naprawę wiązek)
6. `mobilny elektryk samochodowy`

### B. Odblokowanie wykluczenia słowa „cena” (Rozwiązanie konfliktu Google Ads):
- **Słowo:** `cena` (dopasowanie przybliżone / broad match)
- **Stan:** **ODBLOKOWANE / WYŁĄCZONE (OFF)** w FastTony i usunięte z listy `[Forsant API] Negative keyword list - 1742476080`.
- **Powód:** Konflikt algorytmiczny w Google Ads. Słowo `cena` blokowało w 100% kluczowe konwertujące frazy: `wymiana akumulatora z dojazdem cena` oraz `wymiana akumulatora cena`.
- **Skutek:** Wynik optymalizacji Google Ads wzrósł do 69,9%, odzyskano wyświetlenia dla klientów poszukujących cennika usługi mobilnej w Warszawie.

### C. Aktualny bilans listy wykluczeń:
- Łączna liczba wykluczeń na liście Google Ads: **115 fraz**.

### D. Włączenie 12 kluczowych fraz ratunkowych (30.09.2026):
- Włączono w sekcji „Uwzględnione” FastTony: `awaryjne odpalanie auta`, `odpalanie auta na miejscu`, `rozruch samochodu`, `rozruch samochodu pomoc`, `uruchamianie auta 24h`, `odpalanie samochodów`, `wymiana akumulatorów warszawa`, `akumulatory wymiana warszawa`, `akumulatory 24 warszawa`, `akumulatory 24 7`, `Usługa Dostawy Akumulatora z Montażem`, `wymiana akumulatora w samochodzie`.

### E. Zdjęcie 7 blokad broad match z wykluczeń (30.09.2026):
- Przestawiono na OFF w FastTony: `sprzedaż`, `kupno`, `mechanik`, `sklep`, `assistance`, `warsztat`, `opinie`.
- Odblokowano wartościowe zapytania wielowyrazowe z intencją usługi mobilnej.
- Przeanalizowano 21 wykluczeń ze statusem OFF: wykazano przepalanie budżetu przez frazę `akumulatory dolna` (39,68 zł za 3 kliknięcia przy sklepie stacjonarnym na Mokotowie).

### F. Włączenie wykluczeń dla adresów sklepów stacjonarnych konkurencji (30.09.2026):
- Włączono aktywne wykluczenia (ON) w FastTony i zsynchronizowano z Google Ads (`[Forsant API] Negative keyword list - 1742476080`):
  * `dolna`, `herbstadolna`, `herbsta`, `zamieniecka`, `akumulatory zamieniecka`, `akumulatory modlińska`, `radzymińska akumulatory`, `akumulatory dolna`.
- Wynik: 100% ochrona przed kliknięciami osób poszukujących wyłącznie fizycznych sklepów stacjonarnych na tych ulicach.




