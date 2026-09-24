# Akumulateo – Przewodnik Integracji Analitycznych (GSC + GA4 + PageSpeed + MCP)

Dokument zawiera kompletną instrukcję konfiguracji i uruchomienia integracji z **Google Search Console (GSC)**, **Google Analytics 4 (GA4)** oraz **PageSpeed Insights (PSI)** w projekcie **Akumulateo**.

---

## 1. Dlaczego ten zestaw narzędzi maksymalizuje zysk firmy?

Dla mobilnego pogotowia akumulatorowego 24h w Warszawie kluczem do rentowności jest:
1. **Szybkość strony na telefonie (PageSpeed Insights):** 90% kierowców wzywa pomoc z telefonu komórkowego. Każda sekunda opóźnienia powyżej 2.5s obniża konwersję i podnosi koszt kliknięcia w Google Ads.
2. **Dzielnicowe Local SEO (Google Search Console):** Monitorowanie widoczności podstron 18 dzielnic Warszawy (Mokotów, Wola, Ursynów itd.) oraz **wykrywanie niepożądanych zapytań** o sklepy stacjonarne, które marnują budżet.
3. **Mierzenie realnych telefonów (Google Analytics 4):** Zliczanie zdarzeń `phone_call_click` (zdefiniowanych w [sticky-call-bar.html](file:///Users/digo/Documents/antigravity/Akumulateo/src/widgets/sticky-call-bar.html)) w podziale na źródła ruchu (Ads vs SEO) i godziny nocne 24h (dopłata +80 PLN).

---

## 2. Krok 1: Konfiguracja Google Cloud Platform (Wspólne konto usługi)

Zarówno Search Console, jak i GA4 korzystają z jednego konta usługi (**Service Account**) w Google Cloud.

### A. Włączenie API w Google Cloud Console
1. Wejdź na [Google Cloud Console](https://console.cloud.google.com/).
2. Utwórz nowy projekt (np. `Akumulateo-Analytics`) lub wybierz istniejący.
3. W menu bocznym przejdź do: **Interfejsy API i usługi -> Biblioteka**.
4. Wyszukaj i **włącz (Enable)** 3 biblioteki:
   * **Google Search Console API**
   * **Google Analytics Data API**
   * **PageSpeed Insights API** (opcjonalnie wygeneruj standardowy klucz API w *Dane logowania*)

### B. Utworzenie konta usługi (Service Account)
1. W Google Cloud Console przejdź do: **IAM i administracja -> Konta usługi (Service Accounts)**.
2. Kliknij **Utwórz konto usługi**:
   * Nazwa: `akumulateo-analyst`
   * Identyfikator: `akumulateo-analyst@twoj-projekt.iam.gserviceaccount.com`
3. Rola: Możesz pominąć nadawanie ról w projekcie Google Cloud (uprawnienia nadamy w panelach GSC i GA4).
4. Kliknij na utworzone konto usługi, przejdź do zakładki **Klucze (Keys)** -> **Dodaj klucz** -> **Utwórz nowy klucz** -> wybierz **JSON**.
5. Plik JSON zostanie pobrany na Twój komputer.

### C. Zapisanie klucza w projekcie
1. Umieść pobrany plik w głównym katalogu projektu jako `service-account.json`.
2. Skopiuj [.env.example](file:///Users/digo/Documents/antigravity/Akumulateo/.env.example) do `.env`:
   ```bash
   cp .env.example .env
   ```
3. Upewnij się, że w `.env` ścieżka wskazuje na Twój klucz:
   ```env
   GOOGLE_SERVICE_ACCOUNT_KEY_PATH="./service-account.json"
   GOOGLE_SEARCH_CONSOLE_SITE_URL="https://www.akumulateo.pl/"
   GA4_PROPERTY_ID="TWÓJ_ID_USŁUGI_GA4"
   ```
> [!CAUTION]
> Plik `service-account.json` oraz `.env` są na stałe wpisane do [.gitignore](file:///Users/digo/Documents/antigravity/Akumulateo/.gitignore). **Nigdy ich nie commituj do repozytorium GitHub.**

---

## 3. Krok 2: Nadanie uprawnień w Google Search Console

1. Otwórz [Google Search Console](https://searchconsole.google.com/).
2. Wybierz usługę `https://www.akumulateo.pl/` (lub domenę `sc-domain:akumulateo.pl`).
3. W lewym menu na dole kliknij **Ustawienia (Settings)** -> **Użytkownicy i uprawnienia (Users and permissions)**.
4. Kliknij **Dodaj użytkownika (Add user)**:
   * **E-mail:** wpisz adres swojego Service Account (np. `akumulateo-analyst@twoj-projekt.iam.gserviceaccount.com`).
   * **Uprawnienia:** `Pełne` lub `Ograniczone` (do odczytu analityki wystarczą ograniczone).
5. Zapisz.

---

## 4. Krok 3: Nadanie uprawnień w Google Analytics 4

1. Otwórz [Google Analytics](https://analytics.google.com/).
2. Kliknij **Administracja (koło zębate w lewym dolnym rogu)**.
3. W kolumnie *Usługa* przejdź do: **Zarządzanie dostępem do usługi (Property Access Management)**.
4. Kliknij niebieski plusik `+` w prawym górnym rogu -> **Dodaj użytkowników**:
   * **Adres e-mail:** wklej adres Service Account (ten sam co wyżej).
   * **Rola:** `Przeglądający (Viewer)`.
5. Sprawdź identyfikator usługi w **Administracja -> Szczegóły usługi**:
   * Skopiuj numeryczny **Identyfikator usługi (Property ID)** (np. `428192837`) i wklej go do pliku `.env` jako `GA4_PROPERTY_ID`.

---

## 5. Krok 4: Uruchamianie raportów w projekcie

W repozytorium przygotowane są gotowe narzędzia:

### A. Szybki audyt mobilny PageSpeed (CLI Python – bez instalacji paczek)
Działa natychmiastowo na dowolnym komputerze Mac/Linux:
```bash
python3 scripts/audit-pagespeed.py https://www.akumulateo.pl
```
Lub dla konkretnego landing page'a dzielnicowego:
```bash
python3 scripts/audit-pagespeed.py https://www.akumulateo.pl/warszawa-mokotow
```

### B. Zintegrowany raport biznesowy (PSI + GSC + GA4)
Pobiera i łączy dane ze wszystkich trzech usług w zwięzłą analizę dla właściciela:
```bash
npm run analytics
```

---

## 6. Krok 5: Konfiguracja MCP (Model Context Protocol) dla Agenta AI

Jeśli korzystasz ze środowiska **Antigravity** lub **Claude Desktop**, możesz udostępnić asystentowi AI bezpośrednie narzędzia MCP do odpytywania analityki w promptach.

### Konfiguracja w Antigravity / Claude Desktop (`mcpServers`):

Dodaj poniższe wpisy do pliku konfiguracyjnego MCP (np. `claude_desktop_config.json` lub konfiguracji Antigravity):

```json
{
  "mcpServers": {
    "pagespeed": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-pagespeed"]
    },
    "google-search-console": {
      "command": "npx",
      "args": ["-y", "mcp-server-gsc"],
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "/bezwzgledna/sciezka/do/Akumulateo/service-account.json",
        "GSC_SITE_URL": "https://www.akumulateo.pl/"
      }
    }
  }
}
```

### Przykładowe prompty dla Agenta AI po spięciu MCP:
* *„Sprawdź w GSC, które dzielnice Warszawy wygenerowały najwięcej wyświetleń w zeszłym tygodniu.”*
* *„Przeanalizuj w GA4 liczbę zdarzeń phone_call_click po godzinie 22:00.”*
* *„Przeprowadź audyt PageSpeed podstrony /warszawa-ursynow i powiedz, co opóźnia kliknięcie w numer telefonu.”*

---

## 7. Playbook Biznesowy: Jak interpretować dane

| Wskaźnik | Wartość pożądana | Znaczenie biznesowe dla Akumulateo | Działanie korygujące przy odchyleniu |
| :--- | :--- | :--- | :--- |
| **LCP (Mobile)** | **< 2.5s** | Kierowca natychmiast widzi numer telefonu `696 556 446`. | Kompresja zdjęć, wyłączenie ciężkich skryptów w Squarespace. |
| **Frakcja fraz stacjonarnych** | **0%** | Zero telefonów z pytaniem o sklep stacjonarny lub odbiór osobisty. | Wzmocnienie nagłówka *„Wyłącznie z dojazdem 24h – brak sklepu stacjonarnego”*. |
| **CR z wejść na `phone_call_click`** | **> 10%** | Wysoka intencja zakupowa osób wchodzących na stronę. | Jeśli < 5%: uatrakcyjnienie paska Sticky Bar, dodanie obietnicy dojazdu w 20-30 min. |
| **Udział zleceń nocnych** | **15–30%** | Zlecenia z najwyższą marżą (+80 PLN dopłaty nocnej). | Dostosowanie harmonogramu kampanii Google Ads na godziny 22:00–06:00. |
