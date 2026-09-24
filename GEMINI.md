# Akumulateo – Nadrzędne Instrukcje Projektowe (Rules)

Nadrzędna specyfikacja operacyjna, wytyczne biznesowe oraz architektura agentowa dla wszystkich czatów w repozytorium Akumulateo znajdują się w pliku:
👉 **[AGENTS.md](file:///Users/digo/Documents/antigravity/Akumulateo/AGENTS.md)**

### Żelazne reguły dla każdego agenta i podagenta:
1. **Model biznesowy:** Usługa w 100% mobilna 24h z dojazdem w Warszawie i aglomeracji. Brak sklepu stacjonarnego i punktu odbioru.
2. **Zasada asortymentowa:** Oficjalne marki to **Varta, Yuasa (YUASA), Bosch, 4Max, BP, Eco-Force**. **BEZWZGLĘDNY ZAKAZ marki Centra i Banner** (zawsze zastępuj marką Yuasa).
3. **Unit Economics:** Minimalny zysk netto na zleceniu = **180 PLN**.
4. **Architektura Antigravity 2.0:** Zdefiniowane konfiguracje podagentów znajdują się w `.antigravity/agents/` (`seo_auditor`, `copy_strategist`, `ppc_margin_auditor`, `squarespace_integrator`).
5. **Specyfika Squarespace & Zero wycieków CSS:** Czysty CSS wklejany wyłącznie do **Website Tools -> Custom CSS**. Zakaz surowego CSS w Header Code Injection. Koegzystencja banera zgody cookies (`.gdpr-cookie-banner`, `z-index: 10000005 !important`) z mobilnym paskiem Sticky Call Bar (`syncCookieBannerWithStickyBar()`).
6. **Standard Typografii i Responsywności:** Zero mikrofontów w opisach – opisy usług i akapity mają **minimum 15.5px na mobile** i **16.5px na desktopie** (`line-height: 1.65`, kolor `#f1f5f9`). Pasek dyżuru 24h musi być w pełni elastyczny (`flex-wrap`) i nie ulegać ucięciu na ekranach 320px+. Karta „Najczęściej Wybierana Usługa” musi mieć wyrazistą ramkę bursztynową i solidny badge.
7. **Brand Kit & Brandbook v2.2:** Przy wszelkich edycjach strony oraz tworzeniu nowych podstron (dla 18 dzielnic i miast: Piastów, Brwinów, Milanówek, Legionowo, Modlin, Mińsk Maz.) należy bezwzględnie stosować wzorce z [`docs/brandbook-akumulateo.md`](file:///Users/digo/Documents/antigravity/Akumulateo/docs/brandbook-akumulateo.md) oraz [`docs/brand-kit-design-system.md`](file:///Users/digo/Documents/antigravity/Akumulateo/docs/brand-kit-design-system.md).
8. **Zarządzanie artefaktami:** Raporty i dane zapisuj do `audits/`, `content/`, `snippets/`. Zakaz wklejania surowego kodu HTML (>50 linii) do czatu.
9. **Guardrails:** Całkowity zakaz operacji finansowych/modyfikacji budżetów w panelach przez przeglądarkę. Ochrona plików `.env` i `service-account*.json`. Obowiązkowa weryfikacja Pre-Flight QA (curl grep CSS = 0, test incognito).

