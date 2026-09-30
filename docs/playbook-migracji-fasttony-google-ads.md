# Playbook Migracji: Bezpieczne Przejęcie Kontroli Google Ads od FastTony

**Dokument operacyjny dla:** Piotr Jeronim, Tomek Równicki, Maciej Klafczyński  
**Status konta (stan na 30.09.2026 r.):**  
* **Google Ads CID:** `698-263-0728`  
* **Użytkownik:** `akumulateo@gmail.com` – rola: `Tylko do odczytu` (zaproszenie od `integrations@fasttony.com` z 20.03.2025)  
* **Menedżer MCC:** `FastTony` (ID: `426-060-4535`, status: `Właściciel: Tak`)  
* **Kampania główna ID:** `22364165752`  
* **Płatności:** Karta firmowa bezpośrednio w Google Ads (Google Ireland Ltd)  
* **Meta Ads (Facebook/Instagram):** Brak aktywnych reklam (OAuth służył tylko do spięcia platform)  

---

## 1. Wykonane Koki Zabezpieczające (Wykonane 30.09.2026 r.)

Wszystkie dane kampanii zostały trwale zabezpieczone w repozytorium w formatach zgodnych z Google Ads Editor oraz Google Ads CSV:

1. **Archiwum Słów Pozytywnych (70 fraz):**  
   [`audits/ppc/backup/google-ads-keywords-backup.csv`](file:///Users/digo/Documents/antigravity/Akumulateo/audits/ppc/backup/google-ads-keywords-backup.csv)  
   Zawiera kompletne frazy ratunkowe, montażowe i nocne pogotowia.
2. **Archiwum Wykluczeń (116 fraz):**  
   [`audits/ppc/backup/google-ads-negative-keywords-116.csv`](file:///Users/digo/Documents/antigravity/Akumulateo/audits/ppc/backup/google-ads-negative-keywords-116.csv)  
   Zawiera pełną ochronę przed wulkanizacją (PL + cyrylica `шиномонтаж`), drogim elektrykiem (35 zł/klik), darmowymi assistance ubezpieczalni, sklepami stacjonarnymi konkurencji oraz nieobsługiwanymi markami (Centra, Banner). **Słowo `cena` jako broad match pozostaje odblokowane.**
3. **Archiwum Reklam RSA:**  
   [`audits/ppc/backup/google-ads-rsa-ads-backup.csv`](file:///Users/digo/Documents/antigravity/Akumulateo/audits/ppc/backup/google-ads-rsa-ads-backup.csv)  
   Zawiera 12 przetestowanych nagłówków i 4 opisy oparte na psychologii awarii.
4. **Oczyszczony Kod Squarespace (Header Code Injection):**  
   [`snippets/squarespace/header-code-injection-clean-google-ads.html`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/header-code-injection-clean-google-ads.html)  
   Gotowy do wklejenia w 10 sekund pakiet bez zewnętrznego piksela `pixel.fasttony.com` i tablicy `forsantLayer`, z pełnym zachowaniem Consent Mode v2, Google Tag `AW-16941768870`, GA4 `G-2KXNL0LQWG` oraz mikrodanych Schema.org.

---

## 2. Gotowy Wzór Zgłoszenia do FastTony (Kopiuj i Wklej)

Gdy w przyszłości zdecydujesz o odpięciu FastTony, **nie klikaj anulowania subskrypcji w panelu**. Najpierw wyślij poniższą wiadomość z adresu `akumulateo@gmail.com` na adres **`integrations@fasttony.com`** (lub przez formularz pomocy w panelu FastTony):

```text
Temat: Przekazanie pełnej własności administracyjnej konta Google Ads CID: 698-263-0728

Dzień dobry,

W związku z reorganizacją procesów marketingowych w firmie Akumulateo i planowanym przejściem na samodzielne zarządzanie kampaniami Google Ads, zwracam się z formalną prośbą o:

1. Podniesienie poziomu uprawnień dla użytkownika: akumulateo@gmail.com na koncie Google Ads CID: 698-263-0728 z obecnego poziomu "Tylko do odczytu" na poziom: "Administrator".
2. Przekazanie własności administracyjnej (Administrative Ownership) konta CID: 698-263-0728 na rzecz użytkownika akumulateo@gmail.com.
3. Odłączenie konta menedżera MCC FastTony (ID: 426-060-4535) od naszego konta Google Ads.

Płatności za budżet reklamowy są rozliczane bezpośrednio z naszej karty firmowej podpiętej w Google Ads.

Proszę o potwierdzenie realizacji powyższych zmian, po czym przystąpimy do formalnego zamknięcia subskrypcji w panelu FastTony.

Z poważaniem,
Piotr Jeronim / Tomasz Równicki
Akumulateo – Pogotowie Akumulatorowe
Tel. +48 696 556 446
```

---

## 3. Procedura Dnia Migracji (Krok po Kroku po Zgodzie FastTony)

Operacja zajmuje **łącznie 5–10 minut** i nie wymaga wstrzymywania reklam:

### Krok 1: Weryfikacja Uprawnień w Google Ads
1. Zaloguj się na `https://ads.google.com` kontem `akumulateo@gmail.com`.
2. Wejdź w **Narzędzia i ustawienia ➔ Dostęp i bezpieczeństwo**.
3. Sprawdź zakładkę **Użytkownicy**: Twój status musi wynosić **Administrator**.
4. Sprawdź zakładkę **Menedżerowie**: 
   * Jeśli FastTony już się odpięło – lista jest pusta.
   * Jeśli FastTony jeszcze widnieje, ale zrzekło się własności – przycisk **„Usuń dostęp”** będzie aktywny (niebieski/czarny). Kliknij go.

### Krok 2: Cofnięcie Dostępu do Aplikacji Google (Forsant API)
1. Wejdź na stronę bezpieczeństwa konta Google:  
   👉 [https://myaccount.google.com/connections](https://myaccount.google.com/connections)
2. Znajdź pozycję **FastTony** lub **Forsant**.
3. Kliknij **Usuń dostęp / Cofnij uprawnienia**. Zapobiega to wysyłaniu w tle zapytań API modyfikujących kampanie.

### Krok 3: Oczyszczenie Kodu na Stronie Squarespace
1. Otwórz plik [`snippets/squarespace/header-code-injection-clean-google-ads.html`](file:///Users/digo/Documents/antigravity/Akumulateo/snippets/squarespace/header-code-injection-clean-google-ads.html) i skopiuj całą jego zawartość.
2. W panelu Squarespace przejdź do:  
   **Website Tools ➔ Code Injection ➔ HEADER** (lub *Settings ➔ Advanced ➔ Code Injection ➔ HEADER*).
3. Podmień dotychczasową zawartość nagłówka na skopiowany kod i kliknij **Save**.
4. *Skutek:* Strona ładuje się szybciej na smartfonach, usunięto zbędny piksel, Consent Mode v2 i Google Tag działają bez zakłóceń.

### Krok 4: Zabezpieczenie Stawek i Wykluczeń w Google Ads
1. W Google Ads wejdź w kampanię **`22364165752` ➔ Ustawienia ➔ Określanie stawek**.
2. Ustaw: **Maksymalizuj liczbę kliknięć** z zaznaczoną opcją:  
   * **Limit maksymalnej stawki za kliknięcie (Max CPC): `8,00 PLN`**.
   * *Dlaczego to ważne:* Chroni to konto przed anomaliami (spadek stawek w weekendy do 2 zł lub przepalanie 35 zł na elektryka).
3. Wejdź w **Narzędzia ➔ Listy wykluczających słów kluczowych**. Jeśli lista `[Forsant API]` została odpięta, kliknij **+ (Nowa lista)**, nazwij ją `[Akumulateo] Wykluczenia Główne` i wklej zawartość pliku `audits/ppc/backup/google-ads-negative-keywords-116.csv`. Przypisz listę do kampanii.

### Krok 5: Zamknięcie Konta w FastTony
1. Zaloguj się do panelu FastTony.
2. Przejdź do ustawień subskrypcji i kliknij **Anuluj subskrypcję**.

---

## 4. Testy i Weryfikacja (Post-Migration QA)

* [ ] **Google Ads:** Kampania ma status *Włączona (Eligible)*, rejestruje wyświetlenia i kliknięcia.
* [ ] **Koszt kliknięcia:** Średnie CPC mieści się w zdrowym przedziale 6,00 – 8,50 PLN.
* [ ] **Strona WWW:** Konsola przeglądarki Chrome na `akumulateo.pl` nie zgłasza błędów skryptów.
* [ ] **Konwersje telefoniczne:** Kliknięcie w dolny Sticky Call Bar rejestruje zdarzenie `phone_call_click` w GA4 i konwersję w Google Ads.
