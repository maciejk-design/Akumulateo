# Akumulateo – Nadrzędne Instrukcje Projektowe (Rules)

Nadrzędna specyfikacja operacyjna, wytyczne biznesowe oraz architektura agentowa dla wszystkich czatów w repozytorium Akumulateo znajdują się w pliku:
👉 **[AGENTS.md](file:///Users/digo/Documents/antigravity/Akumulateo/AGENTS.md)**

### Żelazne reguły dla każdego agenta i podagenta:
1. **Model biznesowy:** Usługa w 100% mobilna 24h z dojazdem w Warszawie i aglomeracji. Brak sklepu stacjonarnego i punktu odbioru.
2. **Zasada asortymentowa:** Oficjalne marki to **Varta, Yuasa (YUASA), Bosch, 4Max, BP, Eco-Force**. **BEZWZGLĘDNY ZAKAZ marki Centra i Banner** (zawsze zastępuj marką Yuasa).
3. **Unit Economics:** Minimalny zysk netto na zleceniu = **180 PLN**.
4. **Architektura Antigravity 2.0:** Zdefiniowane konfiguracje podagentów znajdują się w `.antigravity/agents/` (`seo_auditor`, `copy_strategist`, `ppc_margin_auditor`, `squarespace_integrator`).
5. **Specyfika Squarespace:** Brak backendu na produkcji – wdrożenia wyłącznie przez Header/Footer Code Injection, Custom CSS (`.akumulateo-*`) oraz bloki Code.
6. **Zarządzanie artefaktami:** Raporty i dane zapisuj do `audits/`, `content/`, `snippets/`. Zakaz wklejania surowego kodu HTML (>50 linii) do czatu.
7. **Guardrails:** Całkowity zakaz operacji finansowych/modyfikacji budżetów w panelach przez przeglądarkę. Ochrona plików `.env` i `service-account*.json`.
