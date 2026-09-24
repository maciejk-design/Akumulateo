# Instrukcja Wdrożenia Nowego Stylu Strony Głównej i Komponentów w Squarespace 7.1

Dokument zawiera precyzyjną, 5-krokową procedurę wdrożenia zaakceptowanego projektu strony głównej, nowoczesnego paska dyżuru, nawigacji, sekcji cennika, marek, obszaru działania oraz stopki dla witryny **[https://www.akumulateo.pl](https://www.akumulateo.pl)**.

Czas wykonania: **ok. 5–8 minut w panelu Squarespace**.

---

## Przegląd przygotowanych paczek wdrożeniowych:

Wszystkie pliki znajdują się w katalogu [`snippets/squarespace/`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/):
1. **Header Code Injection:** [`snippets/squarespace/header-code-injection.html`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/header-code-injection.html)
2. **Footer Code Injection:** [`snippets/squarespace/footer-code-injection.html`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/footer-code-injection.html)
3. **Custom CSS:** [`snippets/squarespace/custom-css.css`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/custom-css.css)
4. **Strona Główna (Code Block):** [`snippets/squarespace/homepage-content.html`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/homepage-content.html)

---

## KROK 1: Aktualizacja Header Code Injection (Schema 5.0★ 100+ opinii, GA4, Consent Mode v2)

1. Zaloguj się do panelu Squarespace witryny **Akumulateo**.
2. W lewym menu przejdź do: **Settings (Ustawienia)** -> **Advanced (Zaawansowane)** -> **Code Injection**.
3. W polu **HEADER**:
   * Zastąp istniejący kod zawartością pliku:  
     👉 [`snippets/squarespace/header-code-injection.html`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/header-code-injection.html)
4. Kliknij **Save (Zapisz)** w lewym górnym rogu.

> **Co to daje?**
> * Uaktualnia mikrodane Schema.org do oceny **5.0★ z liczbą 100+ opinii** oraz pełnym zasięgiem 18 dzielnic i miast aglomeracji (Piastów, Brwinów, Milanówek, Legionowo, Modlin itd.).
> * Zapewnia pełną zgodność z Google Consent Mode v2 i FastTony.
> * Wymusza pobieranie czcionek z `font-display: swap` (eliminacja przesunięć CLS = 0.00).

---

## KROK 2: Aktualizacja Footer Code Injection (Centralne opinie, Pasek mobilny 24/7)

1. Pozostań w **Settings -> Advanced -> Code Injection**.
2. W polu **FOOTER**:
   * Zastąp dotychczasową treść kodem z pliku:  
     👉 [`snippets/squarespace/footer-code-injection.html`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/footer-code-injection.html)
3. Kliknij **Save (Zapisz)**.

> **Co to daje?**
> * Aktywuje centralny obiekt `window.AKUMULATEO_CONFIG` (aktualizacja opinii i linków w jednym miejscu).
> * Wdraża dyskretny, przyklejony na dole smartfona pasek z zieloną diodą dyżuru i przyciskiem połączenia `696 556 446`.
> * Raportuje każde kliknięcie w numer telefonu do Google Analytics 4 (`phone_call_click`).

---

## KROK 3: Wklejenie Stylów Custom CSS

1. W menu panelu przejdź do: **Website** -> **Pages** -> na samym dole kliknij **Custom CSS** (lub **Design -> Custom CSS**).
2. Na końcu istniejących stylów (lub zastępując stare reguły Akumulateo) wklej zawartość pliku:  
   👉 [`snippets/squarespace/custom-css.css`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/custom-css.css)
3. Kliknij **Save (Zapisz)**.

> **Co to daje?**
> * Wszystkie selektory mają bezpieczny prefiks `.akumulateo-*`, więc nie kolidują z motywem Squarespace.
> * Zabezpiecza siatkę 2x2 na smartfonach, zapobiegając rozjeżdżaniu się kafelków.

---

## KROK 4: Wklejenie Nowej Strony Głównej (Blok Code)

1. W lewym menu przejdź do: **Pages (Strony)** -> kliknij na stronę główną **Home** -> kliknij **Edit (Edytuj)** w lewym górnym rogu.
2. Na stronie głównej usuń stare, niespójne sekcje lub dodaj nową pustą sekcję na całą szerokość (**Add a blank section**).
3. Kliknij **+ Add Block (Dodaj blok)** i wybierz **Code (Kod)**.
4. Rozciągnij blok kodu na całą szerokość siatki edytora.
5. Kliknij ikonę ołówka (edycja bloku kodu):
   * Upewnij się, że opcja **Display Source (Wyświetlaj źródło)** jest **WYŁĄCZONA**.
   * Język ustaw na **HTML**.
   * Wklej całą zawartość pliku:  
     👉 [`snippets/squarespace/homepage-content.html`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/homepage-content.html)
6. W lewym górnym rogu kliknij **Done -> Save (Gotowe -> Zapisz)**.

---

## KROK 5: Weryfikacja na Telefonie i Desktopie

Po zapisaniu zmian wejdź na [https://www.akumulateo.pl](https://www.akumulateo.pl) i sprawdź:
1. **Klikalność opinii Google:** Czy kliknięcie w `⭐ 5.0 w Google (100+ opinii) ↗` na samej górze i w pasku zaufania otwiera wizytówkę w Google Maps.
2. **Pasek mobilny:** Czy na telefonie na dole ekranu pojawia się pod kciukiem przycisk `📞 696 556 446` z zieloną pulsującą diodą dyżuru.
3. **Pasek zaufania w Hero:** Czy kafelki na telefonie układają się w czysty układ 2x2 z pojedynczymi linijkami tekstu.
4. **Angielski akcent:** Czy w górnym pasku widnieje `🇬🇧 We speak English`.
5. **Cennik i opinie:** Czy boks przejrzystości cenowej oraz 3 autentyczne recenzje wyglądają czytelnie i elegancko.
