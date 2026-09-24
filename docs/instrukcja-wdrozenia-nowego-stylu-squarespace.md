# Instrukcja Wdrożenia Nowego Stylu Strony Głównej i Komponentów w Squarespace 7.1 (v2.2)

Dokument zawiera precyzyjną, odporną na błędy procedurę wdrożenia zaakceptowanego projektu strony głównej, paska dyżuru 24h, nawigacji, sekcji cennika, marek, obszaru działania oraz stopki dla witryny **[https://www.akumulateo.pl](https://www.akumulateo.pl)**.

Czas wykonania: **ok. 5–8 minut w panelu Squarespace**.

---

## ⚠️ ŻELAZNE OSTRZEŻENIE ANTY-BŁĘDOWE (PRZECZYTAJ PRZED WDROŻENIEM!)

W poprzednich iteracjach wystąpiły błędy, których **bezwzględnie nie wolno powtórzyć**:

1. **WYCIEK SUROWEGO KODU CSS W NAGŁÓWKU:**
   * ❌ **BŁĄD:** Wklejenie zawartości `custom-css.css` do pola *Header Code Injection*. Spowodowało to wyświetlanie surowego kodu CSS na samej górze strony dla wszystkich odwiedzających.
   * ✅ **ZASADA:** Plik `custom-css.css` wklejamy **WYŁĄCZNIE** w sekcji **Website Tools -> Custom CSS**. Nigdy w Code Injection!
2. **KOLIZJA BANERA COOKIES Z PASKIEM MOBILNYM (TRYB INCOGNITO):**
   * ❌ **BŁĄD:** Dolny pasek telefoniczny zasłaniał przyciski *„Zarządzaj”* i *„Akceptuj wszystkie”* banera zgody Squarespace.
   * ✅ **ZASADA:** Plik `footer-code-injection.html` zawiera zintegrowaną funkcję `syncCookieBannerWithStickyBar()` oraz regułę `z-index: 10000005 !important`. Zawsze weryfikuj działanie w trybie Incognito!
3. **ZBYT MAŁA CZCIONKA W OPISACH (11–12px):**
   * ❌ **BŁĄD:** Mikroskopijne opisy usług nieczytelne na ekranie smartfona.
   * ✅ **ZASADA:** Każdy opis usługi ma minimum **15.5px na mobile** i **16.5px na desktopie** z kontrastowym kolorem `#f1f5f9`.
4. **ZAKAZ MARKI CENTRA I BANNER:**
   * ❌ **BŁĄD:** Oferowanie lub wspominanie o akumulatorach Centra / Banner.
   * ✅ **ZASADA:** Firma oferuje wyłącznie **Varta, Yuasa, Bosch, 4Max, BP, Eco-Force**.

---

## Przegląd Przygotowanych Paczek Wdrożeniowych:

Wszystkie pliki znajdują się w katalogu [`snippets/squarespace/`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/):

| Plik w repozytorium | Miejsce docelowe w Squarespace | Rola komponentu |
| :--- | :--- | :--- |
| [`custom-css.css`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/custom-css.css) | **Website Tools -> Custom CSS** | Globalne style motywu, typografia (15.5px/16.5px), karta wyróżniona, reguły cookies. |
| [`header-code-injection.html`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/header-code-injection.html) | **Settings -> Advanced -> Code Injection -> HEADER** | Preconnect fontów, Consent Mode v2, Google Tag, Schema.org 5.0★ (100+ opinii). |
| [`footer-code-injection.html`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/footer-code-injection.html) | **Settings -> Advanced -> Code Injection -> FOOTER** | Pasek telefoniczny Sticky Call Bar, synchronizacja banera cookies, analityka GA4. |
| [`home-page-header-injection.html`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/home-page-header-injection.html) | **Pages -> Home -> Settings (Koło zębate) -> Advanced -> Page Header Code Injection** | Pełna izolacja strony głównej, zintegrowany layout, sekcja Hero, cennik i opinie. |

---

## KROK 1: Wklejenie Globalnego Stylu (Custom CSS)

1. Zaloguj się do panelu Squarespace witryny **Akumulateo**.
2. W lewym menu przejdź do: **Website** -> **Website Tools** -> **Custom CSS** (lub wpisz w wyszukiwarkę panelu: *Custom CSS*).
3. Wklej całą zawartość pliku:  
   👉 [`snippets/squarespace/custom-css.css`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/custom-css.css)
4. Kliknij **Save (Zapisz)** w lewym górnym rogu edytora CSS.

> **Dlaczego to jest kluczowe?**
> * Definiuje podwyższony rozmiar fontów dla akapitów (`15.5px` mobile / `16.5px` desktop).
> * Ustala `z-index: 10000005` dla banera ciasteczek Squarespace.
> * Wymusza bursztynową ramkę i podświetlenie dla karty *„Najczęściej Wybierana Usługa”*.

---

## KROK 2: Aktualizacja Header Code Injection (Schema 5.0★, Tag, Preload)

1. W lewym menu przejdź do: **Website** -> **Website Tools** -> **Code Injection** (lub **Settings -> Developer Tools -> Code Injection**).
2. W pierwszym polu tekstowym o nazwie **HEADER**:
   * Zastąp istniejący kod zawartością pliku:  
     👉 [`snippets/squarespace/header-code-injection.html`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/header-code-injection.html)
3. ⚠️ **Upewnij się, że nie ma tam surowego kodu CSS bez tagu `<style>`!**
4. Kliknij **Save (Zapisz)**.

> **Co to daje?**
> * Uaktualnia mikrodane Schema.org do oceny **5.0★ z liczbą 100+ opinii**.
> * Wdraża Google Consent Mode v2 i integrację Google Ads / GA4.
> * Eliminuje przesunięcia układu (CLS = 0.00).

---

## KROK 3: Aktualizacja Footer Code Injection (Sticky Bar + Cookies Sync)

1. Pozostań w oknie **Code Injection**.
2. Przewiń do drugiego pola tekstowego o nazwie **FOOTER**:
   * Zastąp dotychczasową treść kodem z pliku:  
     👉 [`snippets/squarespace/footer-code-injection.html`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/footer-code-injection.html)
3. Kliknij **Save (Zapisz)**.

> **Co to daje?**
> * Wdraża dyskretny, przyklejony na dole smartfona pasek z zieloną diodą dyżuru i przyciskiem połączenia `696 556 446`.
> * Aktywuje skrypt `syncCookieBannerWithStickyBar()`, który chowa pasek mobilny dopóki użytkownik nie zaakceptuje ciasteczek w trybie incognito.
> * Raportuje kliknięcie połączenia telefonicznego do Google Analytics 4 (`phone_call_click`).

---

## KROK 4: Wdrożenie Strony Głównej (Page Header Code Injection)

1. W lewym menu przejdź do: **Pages (Strony)**.
2. Przy pozycji **Home (Strona Główna)** najedź kursorem i kliknij ikonę **koła zębatego (Ustawienia strony)**.
3. W oknie modalnym przejdź do zakładki **Advanced (Zaawansowane)**.
4. W polu **Page Header Code Injection**:
   * Wklej całą zawartość skompilowanego pliku:  
     👉 [`snippets/squarespace/home-page-header-injection.html`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/home-page-header-injection.html)
5. Kliknij **Save (Zapisz)** w lewym górnym rogu okna modalnego.

> **Alternatywna metoda (Blok Code w edytorze):**  
> Jeśli preferujesz edytor sekcji Squarespace, możesz wkleić zawartość [`snippets/squarespace/homepage-content.html`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/homepage-content.html) bezpośrednio do bloku typu **Code** (z wyłączoną opcją *Display Source*).

---

## KROK 5: Procedura Weryfikacji Jakości (Pre-Flight Testing)

Po zapisaniu zmian przeprowadź 5-punktowy test weryfikacyjny:

1. **Test braku wycieku CSS (Terminal):**
   ```bash
   curl -s https://www.akumulateo.pl/ | grep -c "GLOBAL CUSTOM CSS"
   ```
   *Wynik musi wynosić `0`.*
2. **Test trybu Incognito (Chrome / Safari Mobile):**
   * Otwórz nowe okno incognito na smartfonie pod adresem `https://www.akumulateo.pl`.
   * Sprawdź, czy baner cookies Squarespace wyświetla się na dole i czy przyciski **„Zarządzaj”** oraz **„Akceptuj wszystkie”** są w 100% widoczne i klikalne.
   * Kliknij „Akceptuj wszystkie” – upewnij się, że baner znika, a pod kciukiem płynnie pojawia się bursztynowy przycisk `Zadzwoń: 696 556 446`.
3. **Test responsywności paska dyżuru (Wąski ekran 320px):**
   * W Chrome DevTools włącz tryb urządzenia o szerokości `320px` (np. iPhone SE).
   * Sprawdź, czy pasek `● DYŻUR POGOTOWIA 24H/7` oraz link `⭐ 5.0 w Google (100+ opinii) ↗` nie są obcięte na krawędziach ekranu.
4. **Test czytelności typografii:**
   * Przewiń do sekcji Cennika.
   * Sprawdź opisy usług (np. *„Dojazd technika, bezpieczne uruchomienie profesjonalnym boosterem...”*) – tekst musi być wyraźny, duży (15.5px) i jasny (`#f1f5f9`).
5. **Test spójności karty wyróżnionej:**
   * Karta *„Wymiana Akumulatora + Kodowanie BMS”* musi posiadać bursztynową ramkę 2px, pigułkę `★ NAJCZĘŚCIEJ WYBIERANA USŁUGA` i harmonijny układ ceny.

---
*Instrukcja Wdrożenia Squarespace 7.1 v2.2 | Wrzesień 2026*
