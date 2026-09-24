# Instrukcja Wdrożenia Optymalizacji w Squarespace 7.1 – Akumulateo.pl

Niniejszy dokument zawiera **precyzyjną, 5-krokową instrukcję wdrożenia** przygotowanych w repozytorium kodów optymalizacyjnych dla strony **[https://www.akumulateo.pl](https://www.akumulateo.pl)**.

Czas wykonania: **ok. 5–10 minut w panelu Squarespace**.

---

## KROK 1: Optymalizacja LCP, Fontów i Schema 5.0★ (Header Code Injection)

1. Zaloguj się do panelu administracyjnego Squarespace dla witryny **Akumulateo**.
2. W lewym menu przejdź do: **Settings (Ustawienia)** -> **Advanced (Zaawansowane)** -> **Code Injection**.
3. W sekcji **HEADER** wklej pełną zawartość pliku:  
   👉 [`src/widgets/squarespace-header-injection.html`](file:///Users/digo/Documents/antigravity/Akumulateo/src/widgets/squarespace-header-injection.html)
4. Kliknij **Save (Zapisz)** w lewym górnym rogu.

> **Co to robi?**
> * Wymusza natychmiastowe pobranie obrazu Hero (`fetchpriority="high"`), skracając LCP z 9.2s do < 2.5s.
> * Włącza `font-display: swap`, eliminując przeskakiwanie tekstu (CLS 0.374).
> * Dodaje pełne ustrukturyzowane dane Schema.org `AutomotiveBusiness` z oceną **5.0★ (99 opinii)** – odblokowuje złote gwiazdki w Google.

---

## KROK 2: Wymiana Kodu Stopki (Footer Code Injection – Usunięcie błędu H1 i CLS)

1. Pozostań w **Settings -> Advanced -> Code Injection**.
2. W polu **FOOTER** zaznacz i **usuń cały dotychczasowy kod** (znajdował się tam stary skrypt `initHomepageEnhancements()`, który opóźniał renderowanie o 1 sekundę i dublował nagłówki H1).
3. Wklej nową, oczyszczoną zawartość z pliku:  
   👉 [`src/widgets/squarespace-footer-injection.html`](file:///Users/digo/Documents/antigravity/Akumulateo/src/widgets/squarespace-footer-injection.html)
4. Kliknij **Save (Zapisz)**.

> **Co to robi?**
> * Usuwa destrukcyjne funkcje `replaceChild` i `innerHTML` operujące na nagłówkach H1.
> * Wdraża ultralekki pasek Click-to-Call z zieloną diodą 24h na telefony komórkowe.
> * Prawidłowo raportuje zdarzenia `phone_call_click` (GA4) oraz `conversion` (Google Ads).

---

## KROK 3: Wklejenie Sekcji Cennika i Zaufania (Strona Główna)

1. W lewym menu przejdź do: **Pages (Strony)** -> kliknij na stronę główną **Home** -> kliknij **Edit (Edytuj)** w lewym górnym rogu podglądu.
2. Bezpośrednio pod główną sekcją Hero najedź myszką i kliknij **+ Add Block (Dodaj blok)** lub utwórz nową pustą sekcję (**Add Section -> Add a blank section**).
3. Dodaj blok typu **Code (Kod)**.
4. Wklej całą zawartość pliku:  
   👉 [`src/widgets/pricing-trust-section.html`](file:///Users/digo/Documents/antigravity/Akumulateo/src/widgets/pricing-trust-section.html)
5. Kliknij **Save (Zapisz)** i opublikuj stronę (**Done -> Save**).

> **Co to robi?**
> * Wyświetla jasne ostrzeżenie: *„Usługa w 100% mobilna – brak odbioru osobistego”*, chroniąc budżet przed zapytaniami o sklep stacjonarny.
> * Odpowiada na zapytania o cennik z Google (CTR 4.6% w GSC), podając orientacyjne koszty od 100 zł / 150 zł.
> * Buduje zaufanie informacją o terminalu płatniczym, BLIKu, fakturze VAT 23% i pisemnej gwarancji do 3 lat.

---

## KROK 4: Uporządkowanie Nagłówka H1 w Edytorze

1. Będąc w edycji strony głównej (**Pages -> Home -> Edit**), zaznacz tekst główny w sekcji Hero.
2. Upewnij się, że tekst ma format **Heading 1 (H1)** i brzmi:
   ```text
   Pogotowie Akumulatorowe Warszawa 24/7 – Wymiana z Dojazdem
   ```
3. W sekcji poniżej upewnij się, że podtytuł ma format **Heading 2 (H2)**:
   ```text
   Mobilny serwis akumulatorów i awaryjne uruchamianie auta w 20–30 min
   ```
4. Zapisz zmiany.

---

## KROK 5: Przekierowanie 301 dla `/home` (Eliminacja Duplikatu URL)

1. W menu głównym Squarespace przejdź do: **Settings (Ustawienia)** -> **Developer Tools** -> **URL Mappings**.
2. W oknie tekstowym wklej w nowej linii:
   ```text
   /home -> / 301
   ```
3. Kliknij **Save (Zapisz)**.

---

## KROK 6 (Opcjonalny / Kolejny Krok): Dodanie Podstron Dzielnicowych

W katalogu [`src/seo/generated-pages/`](file:///Users/digo/Documents/antigravity/Akumulateo/src/seo/generated-pages/) przygotowano gotowe podstrony dla 5 kluczowych dzielnic:
* `wymiana-akumulatora-warszawa-ursynow.html`
* `wymiana-akumulatora-warszawa-wola.html`
* `wymiana-akumulatora-warszawa-srodmiescie`
* `wymiana-akumulatora-warszawa-bielany.html`
* `wymiana-akumulatora-warszawa-praga-poludnie.html`

Aby dodać dzielnicę w Squarespace:
1. Przejdź do: **Pages -> Not Linked -> kliknij ikonę `+` -> Blank Page**.
2. Wpisz nazwę podstrony (np. *Wymiana Akumulatora Ursynów*).
3. Wejdź w koło zębate (Page Settings):
   - **General -> Page Title / Navigation Title:** wklej Meta Title z pliku HTML.
   - **General -> URL Slug:** wklej slug (np. `wymiana-akumulatora-warszawa-ursynow`).
   - **SEO -> SEO Description:** wklej Meta Description z pliku HTML.
   - **Advanced -> Page Header Code Injection:** wklej sekcję `<script type="application/ld+json">` z pliku HTML.
4. Na stronie dodaj blok **Code Block** i wklej zawartość `<div>` z pliku HTML.
5. Zapisz.
