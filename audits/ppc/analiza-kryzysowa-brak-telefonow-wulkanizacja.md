# Raport ze Śledztwa Kryzysowego: Analiza Przyczyn Braku Telefonów i Zapytań o Wulkanizację

**Data śledztwa:** 29 września 2026 r.  
**Adresaci:** Maciej Klafczyński, Tomek Równicki, Piotr Jeronim (Właściciele Akumulateo)  
**Okres analizy:** 20.09.2026 – 28.09.2026  
**Źródła danych:** Google Ads (CID `698-263-0728`), Profil Firmy w Google Maps (CID `9184146308208184696`), Serwis `akumulateo.pl`

---

## 1. Executive Summary (Najważniejsze Wnioski)

Śledztwo wykazało **trzy bezpośrednie przyczyny**, które nałożyły się na siebie w dniach 24–28 września, powodując załamanie liczby połączeń o akumulatory oraz telefony z pytaniami o wulkanizację:

1. **Ukrywanie dolnego paska z telefonem przez baner cookies na smartfonach:**  
   W kodzie stopki wdrożono funkcję, która przy aktywnym banerze ciasteczek całkowicie ukrywała dolny pasek z numerem telefonu (`display: none !important`). Dla **100% nowych użytkowników z reklam mobilnych** numer telefonu nie był widoczny przy wejściu na stronę, co zablokowało dzwonienie kierowców w sytuacjach awaryjnych.
2. **Telefony o wulkanizację (Dwa zidentyfikowane źródła):**  
   - **Google Maps:** Kategoria `Pomoc drogowa` dodana 24 września do Wizytówki Google w algorytmach Map kwalifikuje firmę do zapytań o przebite opony i mobilną wulkanizację.
   - **Google Ads:** Kampania zarejestrowała płatne kliknięcie (7,69 zł) na hasło `шиномонтаж варшава 24 7` (ros./ukr. *wulkanizacja Warszawa 24/7*), które dopasowało się w dopasowaniu przybliżonym.
3. **Załamanie licytacji w sobotę 26.09 i przepalanie budżetu na drogiego elektryka:**  
   - W sobotę 26.09 Smart Bidding drastycznie obniżył średnie CPC z ~8 zł do zaledwie **2,14 zł** i wydał tylko **27,78 zł** na całą sobotę (kampania wypadła z aukcji na wartościowe hasła rozruchowe).
   - W niedzielę i poniedziałek (27–28.09) budżet wrócił, ale aż **70,26 zł** poszło na zaledwie 2 kliknięcia na ogólne zapytanie `elektryk samochodowy warszawa z dojazdem` (35 zł za kliknięcie!).

---

## 2. Szczegółowa Analiza Źródeł Problemu

### A. Problem #1: Strona WWW – Pasek telefonu ukryty przez Cookies na Mobile
* **Mechanizm błędu:** W skrypcie stopki znajdowała się funkcja sprawdzająca co 250 ms:
  ```javascript
  if (isBannerActive) {
    bar.style.setProperty('display', 'none', 'important');
  }
  ```
* **Skutek biznesowy:** Użytkownik z awarią akumulatora wchodzi na stronę ze smartfona. Widzi wyskakujący baner RODO/cookies Squarespace na dole ekranu, a **przycisk „Zadzwoń: 696 556 446” znika pod spodem**. Kierowca w stresie nie czyta polityki prywatności, tylko opuszcza stronę i klika kolejną reklamę konkurencji.
* **Rozwiązanie:** Natychmiastowa zmiana logiki – pasek telefonu ma być **zawsze widoczny na dole (`bottom: 0`, `display: flex !important`)**, a baner cookies umieszczony **nad paskiem (`bottom: 74px !important`)**.

---

### B. Problem #2: Skąd wzięły się telefony o wulkanizację?
* **Źródło Google Maps:** 24 września dodano kategorię dodatkową `Pomoc drogowa`. W Mapach Google kierowcy szukający pomocy przy przebitym kole, zapieczonej śrubie czy nocnej wymianie opony trafiali na profil Akumulateo.
* **Źródło Google Ads:** Mimo że polskie słowo `wulkanizacja` było na liście wykluczeń, Google Ads w dopasowaniu przybliżonym dopasował frazę zapisaną cyrylicą: `шиномонтаж варшава 24 7` (wulkanizacja Warszawa 24/7).
* **Rozwiązanie:** 
  1. Usunąć kategorię `Pomoc drogowa` z Profilu Firmy Google (pozostawić `Sklep z akumulatorami` i `Elektryk samochodowy`).
  2. Wykluczyć w FastTony/Google Ads frazy: `шиномонтаж`, `wulkanizacja mobilna`, `wymiana koła`, `opony`.

---

### C. Problem #3: Statystyki Google Ads i Sobota 26.09

| Data | Kliknięcia | Wyświetlenia | Śr. CPC | Koszt dzienny | Uwagi |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **20.09 (Nd)** | 30 | 434 | 5,68 zł | 170,46 zł | Ruch stabilny przed zmianami |
| **21.09 (Pn)** | 26 | 427 | 6,83 zł | 177,60 zł | Ruch stabilny |
| **22.09 (Wt)** | 13 | 280 | 9,18 zł | 119,33 zł | Wahanie stawek |
| **23.09 (Śr)** | 16 | 390 | 7,92 zł | 126,69 zł | Wahanie stawek |
| **24.09 (Cz)** | 16 | 170 | 7,17 zł | 114,68 zł | Wdrożenie zmian w FastTony |
| **25.09 (Pt)** | 20 | 365 | 3,89 zł | 77,83 zł | Spadek stawek licytacji |
| **26.09 (Sb)** | **13** | **362** | **2,14 zł** | **27,78 zł** | **KATASTROFA:** Algorytm obciął stawki, 27 zł za cały dzień |
| **27.09 (Nd)** | 23 | 412 | 8,56 zł | 196,84 zł | Wzrost kosztu, drogie kliki na elektryka |
| **28.09 (Pn)** | 30 | 273 | 7,17 zł | 215,09 zł | Ruch powrócił, ale brak konwersji ze strony |

* **Dlaczego sobota była pusta:** Średnie CPC spadło do 2,14 zł. Przy stawkach rzędu 2 zł w branży pomocy akumulatorowej w Warszawie reklamy wyświetlają się na dole drugiej strony wyników, ściągając przypadkowy ruch informacyjny zamiast realnych kierowców unieruchomionych na drodze.
* **Przepalanie na zapytania o elektryka:** Zapytanie `elektryk samochodowy warszawa z dojazdem` kosztowało 70,26 zł za 2 kliknięcia (35 zł/klik). Należy je wykluczyć, bo Akumulateo to pogotowie akumulatorowe, a nie mobilny warsztat elektromechaniczny naprawiający instalacje i wiązki.

---

## 3. Plan Działań Naprawczych (Gotowy do natychmiastowego wdrożenia)

### KROK 1: Naprawa Strony WWW (Squarespace FOOTER)
- Zmiana kodu wstrzykiwanego w stopce:
  - Usunięcie ukrywania paska (`display: none !important`).
  - Pasek telefonu zawsze widoczny na smartfonach pod kciukiem (`position: fixed; bottom: 0; z-index: 9999999; display: flex !important;`).
  - Baner cookies przeniesiony nad pasek: `.gdpr-cookie-banner { bottom: 74px !important; z-index: 10000000 !important; }`.
  - Dzięki temu każdy użytkownik wchodzący z reklamy natychmiast widzi przycisk **„Zadzwoń: 696 556 446”**.

### KROK 2: Oczyszczenie Wizytówki Google Maps
- Usunięcie kategorii `Pomoc drogowa`.
- Pozostawienie kategorii: `Sklep z akumulatorami` (główna) oraz `Elektryk samochodowy` (pod kodowanie BMS).
- To natychmiast utnie puste telefony o wulkanizację, opony i lawetę z Map Google.

### KROK 3: Ochrona Budżetu Google Ads (FastTony)
- Dodanie do wykluczeń: `шиномонтаж`, `wulkanizacja mobilna`, `wymiana koła`, `naprawa opon`.
- Dodanie do wykluczeń ogólnych drogich fraz elektrycznych: `elektryk samochodowy warszawa z dojazdem`, `mobilny elektryk samochodowy`, które drenują budżet po 35 zł za kliknięcie bez związku z wymianą akumulatora.
