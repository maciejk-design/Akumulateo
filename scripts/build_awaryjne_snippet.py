#!/usr/bin/env python3
"""
Generator dedykowanego pakietu Page Header Code Injection dla podstrony:
https://www.akumulateo.pl/awaryjne-uruchomienie-auta-warszawa

ŚCISŁY STANDARD BRANDBOOK V2.2 & DESIGN SYSTEM:
1. ZERO MIKROFONTÓW:
   - H1: 32px mobile / 46px sm / 54px desktop (font-black 900)
   - H2: 24px mobile / 32px sm / 38px desktop (font-black 900)
   - H3: 20px mobile / 22px sm (font-bold 800)
   - Lead: 16.5px mobile / 18.5px desktop (Slate 100 #f1f5f9)
   - Body / Opisy / Opinie / FAQ: 15.5px mobile / 16.5px desktop (Slate 100 #f1f5f9, line-height 1.70)
   - Punkty cennika i procedur: 15.5px mobile / 16.5px desktop (Slate 100 #f1f5f9)
   - Nadtytuły / Eyebrows: 12.5px mobile / 13.5px desktop (uppercase font-black)
   - Tagi / Daty / Metki: 13.5px font-bold (brak wartości 10–12px)
   - Ceny: 32px mobile / 40px desktop (font-black 900)
   - Stopka: 14px / 14.5px
2. SPÓJNE ODSTĘPY I RYTM SEKCJI (ZMIENNOŚĆ TŁA):
   - Hero: Canvas #020617
   - S4 (Uczciwa diagnoza): Alt #0b1329
   - S5 (Dlaczego booster): Canvas #020617
   - S6 (4 kroki procedury): Alt #0b1329
   - S7 (Koło ratunkowe): Canvas #020617
   - S8 (Cennik 180 / 220 zł): Alt #0b1329
   - S9 (Opinie Google 5.0★): Canvas #020617
   - S10 (FAQ akordeon): Alt #0b1329
   - S11 (Obszar działania): Canvas #020617
   - Stopka: Slate 950 z border-t #1e293b
3. JEDNOLITY KONTENER: max-w-6xl mx-auto px-4 sm:px-6 dla każdej sekcji.
4. MIKRODANE SCHEMA.ORG: EmergencyService, AutoRepair, AggregateRating (5.0, 102 recenzje) + Review.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPETS_DIR = os.path.join(BASE_DIR, "snippets", "squarespace")

COLLECTION_ID = "collection-6a8c91070972152cc2fde180"

# Odczytujemy bazowy CSS Tailwind z szablonu Mokotowa
mokotow_path = os.path.join(SNIPPETS_DIR, "mokotow-page-header-injection.html")
with open(mokotow_path, "r", encoding="utf-8") as f:
    mokotow_raw = f.read()

tw_css_match = re.search(r'(<style id="akumulateo-optimized-tailwind">.*?</style>)', mokotow_raw, re.DOTALL)
if not tw_css_match:
    raise ValueError("Nie znaleziono stylu Tailwind w mokotow-page-header-injection.html")
TAILWIND_STYLE_TAG = tw_css_match.group(1)

HTML_CONTENT = f"""<!-- ========================================================
     AKUMULATEO – AWARYJNE URUCHOMIENIE AUTA WARSZAWA 24/7
     Dedykowany dla: /awaryjne-uruchomienie-auta-warszawa ({COLLECTION_ID})
     Zgodność: Brandbook v2.2, Core Web Vitals, Schema.org EmergencyService
     ======================================================== -->

<!-- 1. SCHEMA.ORG EMERGENCY SERVICE & AUTOREPAIR JSON-LD -->
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "EmergencyService",
  "name": "Akumulateo – Awaryjne Uruchomienie Auta Warszawa 24/7",
  "url": "https://www.akumulateo.pl/awaryjne-uruchomienie-auta-warszawa",
  "telephone": "+48696556446",
  "priceRange": "180 PLN - 650 PLN",
  "image": "https://images.squarespace-cdn.com/content/v1/685d174157b18362d5b7b0f3/f8da5f14-890b-4f74-b2f5-47fb173e0390/awaryjne-uruchomienie-auta-warszawa.png",
  "areaServed": [
    {{
      "@type": "AdministrativeArea",
      "name": "Warszawa"
    }},
    {{
      "@type": "AdministrativeArea",
      "name": "Aglomeracja Warszawska"
    }}
  ],
  "description": "Auto nie odpala? Całodobowe awaryjne uruchamianie auta w Warszawie i okolicach. Dojazd w 20-30 min, bezpieczny rozruch boosterem 12V/24V ze stabilizacją napięcia (Anti-Spike), wjazd do garaży podziemnych -1/-2/-3, diagnostyka alternatora pod obciążeniem oraz opcja natychmiastowej wymiany baterii pod domem. Zadzwoń: 696 556 446!",
  "openingHoursSpecification": {{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
      "Sunday"
    ],
    "opens": "00:00",
    "closes": "23:59"
  }},
  "aggregateRating": {{
    "@type": "AggregateRating",
    "ratingValue": "5.0",
    "bestRating": "5.0",
    "worstRating": "1.0",
    "ratingCount": "100",
    "reviewCount": "100"
  }},
  "review": [
    {{
      "@type": "Review",
      "author": {{
        "@type": "Person",
        "name": "Tomasz M."
      }},
      "datePublished": "2024-11-12",
      "reviewRating": {{
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5",
        "worstRating": "1"
      }},
      "reviewBody": "Awaria akumulatora na podziemnym parkingu (-2) w biurowcu na Mokotowie. Szybki przyjazd w 20 minut, nowa Yuasa zamontowana i zakodowana komputerem od ręki. Pełen profesjonalizm."
    }},
    {{
      "@type": "Review",
      "author": {{
        "@type": "Person",
        "name": "Katarzyna P."
      }},
      "datePublished": "2024-11-28",
      "reviewRating": {{
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5",
        "worstRating": "1"
      }},
      "reviewBody": "Niedziela rano, auto unieruchomione przed wyjazdem rodzinnym. Pan przyjechał do Piaseczna z nowym akumulatorem, sprawdził instalację, płatność BLIKiem u technika. Uratowana niedziela!"
    }},
    {{
      "@type": "Review",
      "author": {{
        "@type": "Person",
        "name": "Marcin W."
      }},
      "datePublished": "2024-12-05",
      "reviewRating": {{
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5",
        "worstRating": "1"
      }},
      "reviewBody": "Bez holowania i bez straty czasu na szukanie sklepu. Komputerowy test ładowania alternatora, montaż nowej Varty i darmowy odbiór starej baterii. Polecam każdemu."
    }},
    {{
      "@type": "Review",
      "author": {{
        "@type": "Person",
        "name": "Paweł K."
      }},
      "datePublished": "2024-12-18",
      "reviewRating": {{
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5",
        "worstRating": "1"
      }},
      "reviewBody": "Pomoc drogowa odmówiła wjazdu do garażu wielopoziomowego w Śródmieściu. Technik z Akumulateo wszedł z przenośnym boosterem, odpalił auto w 3 minuty i sprawdził prąd ładowania. Klasa!"
    }},
    {{
      "@type": "Review",
      "author": {{
        "@type": "Person",
        "name": "Anna S."
      }},
      "datePublished": "2025-01-08",
      "reviewRating": {{
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5",
        "worstRating": "1"
      }},
      "reviewBody": "Ekspresowy rozruch i wymiana akumulatora w aucie ze Start-Stop na Pradze. Wszystko zakodowane, zegary i radio nie straciły ustawień. Paragon i gwarancja na miejscu."
    }},
    {{
      "@type": "Review",
      "author": {{
        "@type": "Person",
        "name": "Grzegorz B."
      }},
      "datePublished": "2025-01-22",
      "reviewRating": {{
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5",
        "worstRating": "1"
      }},
      "reviewBody": "Wzorowa uczciwość. Technik na Bemowie sprawdził akumulator testerem – okazało się, że to poluzowana klema i pobór prądu przez wideorejestrator, a nie martwa bateria. Nie naciągają na koszty!"
    }}
  ]
}}
</script>

<!-- 2. BAZOWY WEWNĘTRZNY TAILWIND CSS -->
{TAILWIND_STYLE_TAG}

<!-- 3. AUTONOMICZNY DESIGN SYSTEM BRANDBOOK V2.2 (PRECYZYJNA TYPOGRAFIA I SPÓJNE ODSTĘPY) -->
<style id="akumulateo-awaryjne-custom-styles">
/* Twardy reset i zabezpieczenie szerokości dla całej strony */
html, body {{
  overflow-x: hidden !important;
  max-width: 100vw !important;
  width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
  box-sizing: border-box !important;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif !important;
}}

*, *:before, *:after {{
  box-sizing: border-box !important;
}}

#{COLLECTION_ID} {{
  background-color: #020617 !important;
  overflow-x: hidden !important;
  max-width: 100vw !important;
  width: 100% !important;
}}

#{COLLECTION_ID} #header,
#{COLLECTION_ID} footer.sections,
#{COLLECTION_ID} #footer-sections,
#{COLLECTION_ID} section[data-section-id="6a8c912f5849182127a62d59"],
#{COLLECTION_ID} section[data-section-id="6aa6dea4020991289c72c2d9"],
#{COLLECTION_ID} section[data-section-id="685d17bd78d1f26a9c224ebe"],
#{COLLECTION_ID} main > article > section,
#{COLLECTION_ID} #sections > section:not(#akumulateo-awaryjne-wrapper section) {{
  display: none !important;
}}

#{COLLECTION_ID} #siteWrapper,
#{COLLECTION_ID} #page,
#{COLLECTION_ID} #page-regions,
#{COLLECTION_ID} section.region,
#{COLLECTION_ID} main#page,
#{COLLECTION_ID} #akumulateo-awaryjne-wrapper,
#{COLLECTION_ID} .akumulateo-root {{
  min-height: 0 !important;
  height: auto !important;
  padding: 0 !important;
  margin: 0 !important;
  max-width: 100vw !important;
  width: 100% !important;
  overflow-x: hidden !important;
  background-color: #020617 !important;
}}

/* ==========================================================================
   ŻELAZNY STANDARD TYPOGRAFII BRANDBOOK V2.2 (ZERO MIKROFONTÓW)
   ========================================================================== */
.ak-h1 {{
  font-size: 32px !important;
  font-weight: 900 !important;
  line-height: 1.15 !important;
  letter-spacing: -0.025em !important;
  color: #ffffff !important;
}}
@media (min-width: 640px) {{
  .ak-h1 {{
    font-size: 46px !important;
    line-height: 1.10 !important;
  }}
}}
@media (min-width: 1024px) {{
  .ak-h1 {{
    font-size: 54px !important;
    line-height: 1.08 !important;
  }}
}}

.ak-h2 {{
  font-size: 24px !important;
  font-weight: 900 !important;
  line-height: 1.25 !important;
  letter-spacing: -0.02em !important;
  color: #ffffff !important;
  margin-bottom: 1rem !important;
}}
@media (min-width: 640px) {{
  .ak-h2 {{
    font-size: 32px !important;
    line-height: 1.20 !important;
    margin-bottom: 1.25rem !important;
  }}
}}
@media (min-width: 1024px) {{
  .ak-h2 {{
    font-size: 38px !important;
  }}
}}

.ak-h3 {{
  font-size: 20px !important;
  font-weight: 800 !important;
  line-height: 1.30 !important;
  color: #ffffff !important;
  margin-bottom: 0.75rem !important;
}}
@media (min-width: 640px) {{
  .ak-h3 {{
    font-size: 22px !important;
  }}
}}

/* Lead text (Wprowadzenia) */
.ak-lead {{
  font-size: 16.5px !important;
  line-height: 1.72 !important;
  color: #f1f5f9 !important;
  font-weight: 400 !important;
}}
@media (min-width: 640px) {{
  .ak-lead {{
    font-size: 18.5px !important;
    line-height: 1.75 !important;
  }}
}}

/* Główny tekst opisów we wszystkich kartach i sekcjach */
.ak-body {{
  font-size: 15.5px !important;
  line-height: 1.70 !important;
  color: #f1f5f9 !important;
  font-weight: 400 !important;
}}
@media (min-width: 640px) {{
  .ak-body {{
    font-size: 16.5px !important;
    line-height: 1.72 !important;
  }}
}}

/* Punkty procedur i listy zalet */
.ak-list-item {{
  font-size: 15.5px !important;
  line-height: 1.65 !important;
  color: #f1f5f9 !important;
  font-weight: 500 !important;
}}
@media (min-width: 640px) {{
  .ak-list-item {{
    font-size: 16.5px !important;
    line-height: 1.68 !important;
  }}
}}

/* Nadtytuły i pigułki statusowe */
.ak-eyebrow {{
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
  background-color: rgba(245, 158, 11, 0.12) !important;
  border: 1px solid rgba(245, 158, 11, 0.35) !important;
  color: #fbbf24 !important;
  padding: 6px 16px !important;
  border-radius: 9999px !important;
  font-size: 12.5px !important;
  font-weight: 900 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.06em !important;
  margin-bottom: 1rem !important;
}}
@media (min-width: 640px) {{
  .ak-eyebrow {{
    font-size: 13.5px !important;
    padding: 7px 18px !important;
  }}
}}

/* Tagi lokalizacyjne i metki */
.ak-badge-tag {{
  display: inline-flex !important;
  align-items: center !important;
  gap: 6px !important;
  background-color: #1e293b !important;
  border: 1px solid #334155 !important;
  color: #cbd5e1 !important;
  padding: 5px 12px !important;
  border-radius: 8px !important;
  font-size: 13.5px !important;
  font-weight: 700 !important;
}}

/* ==========================================================================
   SPÓJNE ODSTĘPY MIĘDZY SEKCJSMI (RYTM WIZUALNY DESKTOP & MOBILE)
   ========================================================================== */
.ak-section {{
  width: 100% !important;
  padding-top: 3.5rem !important;
  padding-bottom: 3.5rem !important;
  position: relative !important;
  box-sizing: border-box !important;
}}
@media (min-width: 640px) {{
  .ak-section {{
    padding-top: 4rem !important;
    padding-bottom: 4rem !important;
  }}
}}
@media (min-width: 1024px) {{
  .ak-section {{
    padding-top: 4.75rem !important;
    padding-bottom: 4.75rem !important;
  }}
}}

/* Naprzemienne tła sekcji dla rytmu wizualnego */
.ak-section-alt {{
  background-color: #0b1329 !important;
  border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
}}

/* ==========================================================================
   RAMKI I KARTY (PRZESTRONNE PADDINGI, EQUAL-HEIGHT & WYRAŹNE KONTRASTY)
   ========================================================================== */
.ak-card {{
  background-color: #0f172a !important;
  border: 1px solid #334155 !important;
  border-radius: 1.5rem !important;
  padding: 1.75rem 1.5rem !important;
  transition: all 0.25s ease-in-out !important;
  width: 100% !important;
  box-sizing: border-box !important;
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.4) !important;
  display: flex !important;
  flex-direction: column !important;
  justify-content: space-between !important;
  height: 100% !important;
}}
@media (min-width: 640px) {{
  .ak-card {{
    padding: 2.25rem 2rem !important;
  }}
}}
.ak-card:hover {{
  border-color: rgba(245, 158, 11, 0.6) !important;
  transform: translateY(-3px) !important;
  box-shadow: 0 15px 35px -5px rgba(0, 0, 0, 0.6), 0 0 20px -3px rgba(245, 158, 11, 0.2) !important;
}}

/* Karta wyróżniona cennika */
.ak-card-featured {{
  background-color: #090e1d !important;
  border: 2px solid #f59e0b !important;
  box-shadow: 0 15px 40px -5px rgba(0, 0, 0, 0.7), 0 0 30px -5px rgba(245, 158, 11, 0.25) !important;
}}
.ak-card-featured:hover {{
  border-color: #fbbf24 !important;
  box-shadow: 0 20px 45px -5px rgba(0, 0, 0, 0.8), 0 0 35px -3px rgba(245, 158, 11, 0.35) !important;
}}

/* Specjalne panele bannerowe – Uczciwa Diagnoza i Koło Ratunkowe */
.ak-guarantee-card {{
  background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.9) 100%) !important;
  border: 1px solid rgba(245, 158, 11, 0.35) !important;
  border-radius: 1.5rem !important;
  padding: 2.25rem 1.75rem !important;
  text-align: center !important;
  max-width: 56rem !important;
  margin-left: auto !important;
  margin-right: auto !important;
  box-shadow: 0 15px 35px -5px rgba(0, 0, 0, 0.5), 0 0 25px -5px rgba(245, 158, 11, 0.15) !important;
  box-sizing: border-box !important;
}}
@media (min-width: 640px) {{
  .ak-guarantee-card {{
    padding: 3rem 3.5rem !important;
  }}
}}

.ak-rescue-card {{
  background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(9, 14, 29, 0.98) 100%) !important;
  border: 2px solid #f59e0b !important;
  border-radius: 1.5rem !important;
  padding: 2.25rem 1.75rem !important;
  text-align: center !important;
  max-width: 56rem !important;
  margin-left: auto !important;
  margin-right: auto !important;
  box-shadow: 0 20px 45px -5px rgba(0, 0, 0, 0.7), 0 0 35px -5px rgba(245, 158, 11, 0.25) !important;
  box-sizing: border-box !important;
}}
@media (min-width: 640px) {{
  .ak-rescue-card {{
    padding: 3rem 3.5rem !important;
  }}
}}


/* Kompaktowe boksy ikon i numerów kroków */
.ak-icon-box {{
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 54px !important;
  height: 54px !important;
  min-width: 54px !important;
  max-width: 54px !important;
  min-height: 54px !important;
  max-height: 54px !important;
  border-radius: 14px !important;
  background-color: rgba(245, 158, 11, 0.12) !important;
  border: 1px solid rgba(245, 158, 11, 0.35) !important;
  font-size: 26px !important;
  margin-bottom: 1.25rem !important;
  flex-shrink: 0 !important;
}}

.ak-step-num {{
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 48px !important;
  height: 48px !important;
  min-width: 48px !important;
  max-width: 48px !important;
  min-height: 48px !important;
  max-height: 48px !important;
  border-radius: 14px !important;
  background-color: rgba(245, 158, 11, 0.12) !important;
  border: 1px solid rgba(245, 158, 11, 0.35) !important;
  color: #f59e0b !important;
  font-weight: 900 !important;
  font-size: 19px !important;
  margin-bottom: 1.25rem !important;
  flex-shrink: 0 !important;
}}

/* ==========================================================================
   SIATKI Z DUŻYMI ODSTĘPAMI MIĘDZY KARTAMI (GAPS)
   ========================================================================== */
.ak-grid-3 {{
  display: grid !important;
  grid-template-columns: 1fr !important;
  gap: 1.75rem !important;
  width: 100% !important;
  align-items: stretch !important;
}}
@media (min-width: 768px) {{
  .ak-grid-3 {{
    grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
    gap: 2rem !important;
    align-items: stretch !important;
  }}
}}
@media (min-width: 1280px) {{
  .ak-grid-3 {{
    gap: 2.25rem !important;
  }}
}}

.ak-grid-2 {{
  display: grid !important;
  grid-template-columns: 1fr !important;
  gap: 1.75rem !important;
  width: 100% !important;
}}
@media (min-width: 640px) {{
  .ak-grid-2 {{
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    gap: 2rem !important;
  }}
}}
@media (min-width: 1280px) {{
  .ak-grid-2 {{
    gap: 2.25rem !important;
  }}
}}

.ak-grid-4 {{
  display: grid !important;
  grid-template-columns: 1fr !important;
  gap: 1.75rem !important;
  width: 100% !important;
}}
@media (min-width: 640px) {{
  .ak-grid-4 {{
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    gap: 2rem !important;
  }}
}}
@media (min-width: 1024px) {{
  .ak-grid-4 {{
    grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
    gap: 2.25rem !important;
  }}
}}

/* ==========================================================================
   PRZYCISKI AKCJI
   ========================================================================== */
.ak-btn-primary {{
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 10px !important;
  background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%) !important;
  color: #020617 !important;
  font-weight: 900 !important;
  border-radius: 14px !important;
  text-decoration: none !important;
  box-shadow: 0 10px 25px -5px rgba(245, 158, 11, 0.35) !important;
  transition: all 0.2s ease-in-out !important;
  padding: 15px 26px !important;
  font-size: 16px !important;
  max-width: 100% !important;
  width: 100% !important;
  text-align: center !important;
  box-sizing: border-box !important;
  user-select: none !important;
  cursor: pointer !important;
}}
@media (min-width: 640px) {{
  .ak-btn-primary {{
    width: auto !important;
    padding: 17px 38px !important;
    font-size: 18px !important;
    border-radius: 16px !important;
  }}
}}
.ak-btn-primary:hover {{
  background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%) !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 15px 30px -5px rgba(245, 158, 11, 0.5) !important;
}}
.ak-btn-primary:active {{
  transform: scale(0.98) !important;
}}

.ak-btn-secondary {{
  display: block !important;
  width: 100% !important;
  text-align: center !important;
  background-color: #1e293b !important;
  border: 1px solid #475569 !important;
  color: #ffffff !important;
  font-weight: 800 !important;
  padding: 15px !important;
  border-radius: 12px !important;
  font-size: 16px !important;
  transition: all 0.2s ease-in-out !important;
  text-decoration: none !important;
}}
.ak-btn-secondary:hover {{
  background-color: #334155 !important;
  border-color: #f59e0b !important;
  color: #fbbf24 !important;
}}

/* Przycisk w nagłówku */
.ak-header-phone-btn {{
  padding: 5px 8px !important;
  font-size: 11px !important;
  border-radius: 9px !important;
}}
@media (min-width: 640px) {{
  .ak-header-phone-btn {{
    padding: 10px 18px !important;
    font-size: 14.5px !important;
    border-radius: 12px !important;
  }}
}}

/* ==========================================================================
   PRZYCISK MENU MOBILNEGO (WCZYTYWANY I WYRAŹNY – BUDŻET <= 340px)
   ========================================================================== */
.ak-mobile-menu-btn {{
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 3px !important;
  background-color: #1e293b !important;
  border: 2px solid #f59e0b !important;
  border-radius: 9px !important;
  padding: 5px 7px !important;
  min-height: 30px !important;
  color: #fbbf24 !important;
  cursor: pointer !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.4), 0 0 8px rgba(245, 158, 11, 0.3) !important;
  transition: all 0.15s ease !important;
  user-select: none !important;
  flex-shrink: 0 !important;
  -webkit-tap-highlight-color: transparent !important;
}}
@media (min-width: 640px) {{
  .ak-mobile-menu-btn {{
    gap: 5px !important;
    border-radius: 12px !important;
    padding: 6px 10px !important;
    min-height: 38px !important;
  }}
}}
@media (min-width: 1024px) {{
  .ak-mobile-menu-btn {{
    display: none !important;
  }}
}}
.ak-mobile-menu-btn:hover,
.ak-mobile-menu-btn:focus-visible {{
  background-color: #334155 !important;
  border-color: #fbbf24 !important;
  box-shadow: 0 4px 16px rgba(245, 158, 11, 0.4) !important;
}}
.ak-mobile-menu-btn:active {{
  transform: scale(0.96) !important;
}}
.ak-mobile-menu-btn .ak-menu-text {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  font-size: 10.5px !important;
  font-weight: 900 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  color: #fbbf24 !important;
  line-height: 1 !important;
}}
@media (max-width: 350px) {{
  .ak-mobile-menu-btn .ak-menu-text {{
    display: none !important;
  }}
}}
@media (min-width: 640px) {{
  .ak-mobile-menu-btn .ak-menu-text {{
    font-size: 11px !important;
    letter-spacing: 0.08em !important;
  }}
}}
.ak-mobile-menu-btn svg {{
  width: 14px !important;
  height: 14px !important;
  stroke: #fbbf24 !important;
  stroke-width: 2.5px !important;
  display: block !important;
  flex-shrink: 0 !important;
}}
@media (min-width: 640px) {{
  .ak-mobile-menu-btn svg {{
    width: 17px !important;
    height: 17px !important;
  }}
}}

/* Koegzystencja banera ciasteczek Squarespace */
.gdpr-cookie-banner, .cookie-banner-mount-point, .sqs-cookie-banner-v2 {{
  z-index: 10000005 !important;
}}
body:has(.gdpr-cookie-banner) #akumulateo-sticky-call-bar,
body:has(.sqs-cookie-banner-v2) #akumulateo-sticky-call-bar,
body:has(.cookie-banner-mount-point:not(:empty)) #akumulateo-sticky-call-bar {{
  display: none !important;
}}

/* FAQ Accordion */
details.ak-faq-item {{
  width: 100% !important;
  box-sizing: border-box !important;
}}
details.ak-faq-item summary {{
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 16px !important;
  list-style: none !important;
  cursor: pointer !important;
  user-select: none !important;
}}
details.ak-faq-item summary::-webkit-details-marker {{
  display: none !important;
}}
.ak-faq-icon {{
  width: 22px !important;
  height: 22px !important;
  min-width: 22px !important;
  max-width: 22px !important;
  color: #f59e0b !important;
  flex-shrink: 0 !important;
  transition: transform 0.25s ease-in-out !important;
}}
details.ak-faq-item[open] summary .ak-faq-icon {{
  transform: rotate(180deg) !important;
}}

@keyframes akumulateo-pulse {{
  0% {{ transform: scale(0.95); opacity: 0.85; }}
  50% {{ transform: scale(1.15); opacity: 1; }}
  100% {{ transform: scale(0.95); opacity: 0.85; }}
}}
.akumulateo-pulse-dot {{
  animation: akumulateo-pulse 2s infinite ease-in-out;
}}

.ak-break-text {{
  word-break: break-word !important;
  overflow-wrap: break-word !important;
}}

/* ==========================================================================
   WIDŻET OPINII GOOGLE 5.0★ (CRO-04: ZERO-OVERHEAD & SEO RICH SNIPPETS)
   ========================================================================== */
.ak-google-summary-card {{
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 16px !important;
  background: linear-gradient(145deg, #0f172a 0%, #1e293b 100%) !important;
  border: 1px solid #334155 !important;
  border-radius: 20px !important;
  padding: 22px 26px !important;
  max-width: 680px !important;
  margin: 0 auto 36px auto !important;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35) !important;
}}
@media (min-width: 640px) {{
  .ak-google-summary-card {{
    flex-direction: row !important;
    justify-content: space-between !important;
    padding: 20px 30px !important;
  }}
}}
.ak-google-logo-wrapper {{
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  background: #ffffff !important;
  border-radius: 14px !important;
  width: 50px !important;
  height: 50px !important;
  min-width: 50px !important;
  box-shadow: 0 4px 10px rgba(0,0,0,0.15) !important;
}}
.ak-google-score-col {{
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
}}
@media (min-width: 640px) {{
  .ak-google-score-col {{
    align-items: flex-start !important;
  }}
}}
.ak-google-score-row {{
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
}}
.ak-google-rating-number {{
  font-size: 30px !important;
  font-weight: 900 !important;
  color: #ffffff !important;
  line-height: 1 !important;
}}
.ak-stars-row {{
  display: flex !important;
  align-items: center !important;
  gap: 2px !important;
}}
.ak-star-icon {{
  width: 20px !important;
  height: 20px !important;
  color: #f59e0b !important;
  display: block !important;
  flex-shrink: 0 !important;
}}
.ak-stars-gold {{
  color: #f59e0b !important;
  font-size: 18px !important;
  letter-spacing: 2px !important;
}}
.ak-google-reviews-count-text {{
  font-size: 14.5px !important;
  color: #cbd5e1 !important;
  margin-top: 4px !important;
}}
.ak-google-reviews-count-text strong {{
  color: #ffffff !important;
}}
.ak-google-view-all-btn {{
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  background-color: #1e293b !important;
  color: #fbbf24 !important;
  font-size: 14px !important;
  font-weight: 800 !important;
  padding: 11px 20px !important;
  border-radius: 12px !important;
  border: 1px solid #475569 !important;
  text-decoration: none !important;
  transition: all 0.2s ease-in-out !important;
  white-space: nowrap !important;
}}
.ak-google-view-all-btn:hover {{
  background-color: #334155 !important;
  border-color: #f59e0b !important;
  color: #ffffff !important;
  box-shadow: 0 4px 14px rgba(245, 158, 11, 0.2) !important;
}}
.ak-review-top {{
  display: flex !important;
  align-items: center !important;
  gap: 12px !important;
  margin-bottom: 12px !important;
}}
.ak-review-avatar {{
  width: 48px !important;
  height: 48px !important;
  min-width: 48px !important;
  background: linear-gradient(135deg, #1e293b 0%, #334155 100%) !important;
  border: 1px solid #475569 !important;
  border-radius: 9999px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  font-weight: 900 !important;
  font-size: 16px !important;
  color: #fbbf24 !important;
}}
.ak-review-user-info {{
  display: flex !important;
  flex-direction: column !important;
}}
.ak-review-name {{
  color: #ffffff !important;
  font-weight: 800 !important;
  font-size: 17px !important;
  line-height: 1.2 !important;
}}
.ak-review-verified {{
  display: inline-flex !important;
  align-items: center !important;
  gap: 4px !important;
  color: #10b981 !important;
  font-size: 13.5px !important;
  font-weight: 700 !important;
  margin-top: 3px !important;
}}
.ak-check-icon {{
  width: 15px !important;
  height: 15px !important;
  display: block !important;
  flex-shrink: 0 !important;
}}
.ak-review-meta {{
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  margin-bottom: 12px !important;
  padding-bottom: 10px !important;
  border-bottom: 1px solid #1e293b !important;
}}
.ak-review-date {{
  color: #cbd5e1 !important;
  font-size: 13.5px !important;
  font-style: normal !important;
}}
.ak-review-tag {{
  background-color: #1e293b !important;
  color: #cbd5e1 !important;
  font-size: 13.5px !important;
  font-weight: 700 !important;
  padding: 5px 12px !important;
  border-radius: 8px !important;
  margin-bottom: 14px !important;
  align-self: flex-start !important;
  border: 1px solid #334155 !important;
}}
.ak-review-text {{
  margin: 0 !important;
  padding: 0 !important;
  color: #f1f5f9 !important;
  font-size: 15.5px !important;
  line-height: 1.70 !important;
  font-style: italic !important;
  flex-grow: 1 !important;
}}
@media (min-width: 640px) {{
  .ak-review-text {{
    font-size: 16.5px !important;
    line-height: 1.72 !important;
  }}
}}
.ak-review-text strong {{
  color: #fbbf24 !important;
  font-weight: 700 !important;
  font-style: normal !important;
}}
.ak-reviews-footer {{
  background: linear-gradient(145deg, #090e1a 0%, #0f172a 100%) !important;
  border: 1px solid #334155 !important;
  border-radius: 20px !important;
  padding: 26px !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  text-align: center !important;
  gap: 18px !important;
  box-sizing: border-box !important;
  margin-top: 36px !important;
}}
@media (min-width: 768px) {{
  .ak-reviews-footer {{
    flex-direction: row !important;
    justify-content: space-between !important;
    text-align: left !important;
    padding: 26px 34px !important;
  }}
}}
.ak-reviews-footer-text {{
  color: #f1f5f9 !important;
  font-size: 15.5px !important;
  line-height: 1.55 !important;
  max-width: 580px !important;
}}
.ak-reviews-footer-text strong {{
  color: #ffffff !important;
}}
.ak-reviews-footer-actions {{
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 12px !important;
  align-items: center !important;
  justify-content: center !important;
}}
.ak-reviews-cta-google {{
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  background-color: #1e293b !important;
  color: #f1f5f9 !important;
  font-size: 14.5px !important;
  font-weight: 700 !important;
  padding: 13px 20px !important;
  border-radius: 12px !important;
  border: 1px solid #475569 !important;
  text-decoration: none !important;
  transition: all 0.2s ease !important;
  white-space: nowrap !important;
}}
.ak-reviews-cta-google:hover {{
  background-color: #334155 !important;
  border-color: #f59e0b !important;
}}
</style>

<!-- 4. TEMPLATE AWARYJNEGO URUCHOMIENIA (SYSTEM BRANDBOOK V2.2) -->
<template id="akumulateo-awaryjne-template">

<div class="akumulateo-root bg-slate-950 text-slate-100 font-sans antialiased overflow-hidden w-full">
  
  <!-- 1. TOP EMERGENCY BAR (PASEK DYŻURU 24H) -->
  <div class="bg-gradient-to-r from-amber-500 via-amber-400 to-amber-500 text-slate-950 px-3 sm:px-6 py-2 sm:py-2.5 text-xs sm:text-[13px] font-black tracking-wide w-full shadow-sm">
    <div class="max-w-6xl mx-auto flex flex-wrap items-center justify-between gap-x-3 gap-y-1">
      <div class="flex items-center gap-2 flex-shrink-0">
        <span class="w-2.5 h-2.5 rounded-full bg-slate-950 akumulateo-pulse-dot flex-shrink-0"></span>
        <span class="uppercase font-black tracking-wider text-xs sm:text-[13px]">Dyżur Pogotowia 24h/7</span>
        <span class="hidden sm:inline font-bold text-slate-900">• Dojazd 20–30 min w Warszawie i aglomeracji</span>
      </div>
      <div class="flex items-center gap-3 flex-shrink-0 text-xs sm:text-[13px] font-bold">
        <span class="hidden md:inline-flex items-center gap-1 font-extrabold text-slate-950 bg-amber-300/90 px-2 py-0.5 rounded text-xs">🇬🇧 English</span>
        <a href="https://g.page/r/CXjN9llopHR_EBM/" target="_blank" rel="noopener noreferrer" class="hover:text-slate-800 flex items-center gap-1 transition cursor-pointer font-black">
          <span>⭐ <span>5.0</span> w Google (102 opinie) ↗</span>
        </a>
      </div>
    </div>
  </div>

  <!-- 2. STICKY NAVIGATION HEADER -->
  <header class="bg-slate-900/95 backdrop-filter backdrop-blur-md sticky top-0 z-40 border-b border-slate-800 px-2 sm:px-6 py-2 sm:py-3.5 w-full">
    <div class="max-w-6xl mx-auto flex items-center justify-between gap-1 sm:gap-4 w-full">
      
      <!-- LOGO: LINK NA STRONĘ GŁÓWNĄ -->
      <a href="/" class="flex items-center gap-1 sm:gap-2 group text-decoration-none min-w-0 cursor-pointer flex-shrink-0" aria-label="Akumulateo – Strona główna">
        <div class="rounded-lg sm:rounded-xl bg-slate-800 border border-slate-700 flex items-center justify-center p-0.5 sm:p-1 shadow-md group-hover:border-amber-500 transition flex-shrink-0 w-6 h-6 sm:w-9 sm:h-9">
          <svg viewBox="0 0 68 68" class="w-full h-full block" fill="none">
            <rect x="14" y="6" width="10" height="7" rx="2" fill="#94A3B8" />
            <rect x="44" y="6" width="10" height="7" rx="2" fill="#EF4444" />
            <rect x="6" y="12" width="56" height="52" rx="10" fill="#0F172A" stroke="#475569" stroke-width="2" />
            <path d="M37 17L22 38h9l-5 19 19-24h-10l7-16z" fill="#F59E0B" />
            <circle cx="53" cy="56" r="3" fill="#10B981" />
          </svg>
        </div>
        <div class="leading-none">
          <div class="text-[13px] sm:text-lg md:text-xl font-black tracking-tight sm:tracking-wider text-white whitespace-nowrap">
            AKUMULAT<span class="text-amber-500">E</span>O
          </div>
          <div class="hidden sm:flex text-xs font-bold text-slate-400 mt-0.5 items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
            Pogotowie 24h
          </div>
        </div>
      </a>

      <!-- MENU DESKTOP -->
      <nav class="hidden lg:flex items-center gap-6 text-sm font-semibold text-slate-300">
        <a href="/#uslugi" class="hover:text-amber-400 transition font-bold">Usługi mobilne</a>
        <a href="/awaryjne-uruchomienie-auta-warszawa" class="text-amber-400 font-extrabold border-b-2 border-amber-400 pb-0.5">Awaryjny rozruch 24h</a>
        <a href="/wymiana-akumulatora-warszawa-mokotow" class="hover:text-amber-400 transition font-bold">Wymiana akumulatora</a>
        <a href="/#cennik" class="hover:text-amber-400 transition font-bold">Cennik</a>
        <a href="/obszar-dzialania-warszawa-i-okolice" class="hover:text-amber-400 transition font-bold">Warszawa & Aglomeracja</a>
        <a href="/#faq" class="hover:text-amber-400 transition font-bold">FAQ</a>
      </nav>

      <!-- PRAWA STRONA: PRZYCISK TELEFONU + MENU MOBILNE -->
      <div class="flex items-center gap-1 sm:gap-2.5 flex-shrink-0">
        <a href="tel:+48696556446" class="ak-header-phone-btn flex items-center gap-1 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black rounded-xl shadow-md transition transform active:scale-95 whitespace-nowrap">
          <span class="text-xs sm:text-sm">📞</span>
          <span class="tracking-tight sm:tracking-wide font-black">696 556 446</span>
        </a>
        <button id="akAwaryjneMenuBtn" onclick="var m=document.getElementById('akAwaryjneMobileDrawer');if(m){{var isHidden=m.classList.toggle('hidden');this.setAttribute('aria-expanded',!isHidden);var icon=this.querySelector('.ak-menu-icon');var closeIcon=this.querySelector('.ak-close-icon');var label=this.querySelector('.ak-menu-text');if(icon&&closeIcon){{icon.classList.toggle('hidden',!isHidden);closeIcon.classList.toggle('hidden',isHidden);}}if(label){{label.textContent=isHidden?'MENU':'ZAMKNIJ';}}}}" aria-label="Menu nawigacji" aria-expanded="false" class="ak-mobile-menu-btn lg:hidden">
          <span class="ak-menu-icon flex items-center">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"></path></svg>
          </span>
          <span class="ak-close-icon hidden flex items-center">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"></path></svg>
          </span>
          <span class="ak-menu-text">MENU</span>
        </button>
      </div>

    </div>

    <!-- MOBILNY DRAWER -->
    <div id="akAwaryjneMobileDrawer" class="hidden lg:hidden bg-slate-900 border-t border-slate-800 px-4 py-5 space-y-3 text-slate-100 text-base font-bold shadow-2xl mt-2">
      <a href="/#uslugi" onclick="var m=document.getElementById('akAwaryjneMobileDrawer');if(m)m.classList.add('hidden');" class="block py-2.5 px-3 rounded-lg hover:bg-slate-800 transition">⚡ Usługi mobilne 24h</a>
      <a href="/awaryjne-uruchomienie-auta-warszawa" onclick="var m=document.getElementById('akAwaryjneMobileDrawer');if(m)m.classList.add('hidden');" class="block py-2.5 px-3 rounded-lg bg-amber-500/10 text-amber-400 font-extrabold transition">🚨 Awaryjne uruchomienie 24h</a>
      <a href="/wymiana-akumulatora-warszawa-mokotow" onclick="var m=document.getElementById('akAwaryjneMobileDrawer');if(m)m.classList.add('hidden');" class="block py-2.5 px-3 rounded-lg hover:bg-slate-800 transition">🔋 Wymiana akumulatora z dojazdem</a>
      <a href="/#cennik" onclick="var m=document.getElementById('akAwaryjneMobileDrawer');if(m)m.classList.add('hidden');" class="block py-2.5 px-3 rounded-lg hover:bg-slate-800 transition">💰 Cennik interwencji</a>
      <a href="/obszar-dzialania-warszawa-i-okolice" onclick="var m=document.getElementById('akAwaryjneMobileDrawer');if(m)m.classList.add('hidden');" class="block py-2.5 px-3 rounded-lg hover:bg-slate-800 transition">📍 Obszar działania (Warszawa & Okolice)</a>
      <a href="/#opinie" onclick="var m=document.getElementById('akAwaryjneMobileDrawer');if(m)m.classList.add('hidden');" class="block py-2.5 px-3 rounded-lg hover:bg-slate-800 transition">⭐ Opinie kierowców (Google 5.0★)</a>
      <a href="/#faq" onclick="var m=document.getElementById('akAwaryjneMobileDrawer');if(m)m.classList.add('hidden');" class="block py-2.5 px-3 rounded-lg hover:bg-slate-800 transition">❓ Częste pytania (FAQ)</a>
      <div class="pt-2">
        <a href="tel:+48696556446" class="flex items-center justify-center gap-2 bg-gradient-to-r from-amber-500 to-amber-600 text-slate-950 font-black py-3.5 rounded-xl text-center shadow-lg text-base">
          <span>📞 Zadzwoń: 696 556 446</span>
        </a>
      </div>
    </div>
  </header>

  <!-- 3. HERO SECTION (CANVAS #020617 – WYŚRODKOWANY, ELEGANCKI, PRZESTRONNY) -->
  <section class="relative px-4 pt-14 pb-16 sm:pt-20 sm:pb-24 bg-gradient-to-b from-slate-900 via-slate-900 to-slate-950 border-b border-slate-800 text-center w-full">
    <div class="max-w-5xl mx-auto w-full">
      
      <!-- PIGUŁKA STATUSOWA -->
      <div class="ak-eyebrow mb-6">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 akumulateo-pulse-dot flex-shrink-0"></span>
        <span>Pogotowie Rozruchowe Warszawa 24h/7 • Dojazd 20–30 min</span>
      </div>

      <!-- NAGŁÓWEK H1 (DUŻY I CZYTELNY) -->
      <h1 class="ak-h1 mb-6 ak-break-text">
        Awaryjne Uruchomienie Auta <br class="hidden sm:inline" /><span class="text-amber-400 font-black">Warszawa 24h/7</span>
      </h1>

      <!-- OPIS PERSWAZYJNY LEAD (MIN 16.5px MOBILE / 18.5px DESKTOP) -->
      <p class="ak-lead max-w-3xl mx-auto mb-10 ak-break-text">
        Auto nie odpala pod domem, biurem lub w ciasnym garażu podziemnym? Rozrusznik tylko cicho cyka albo kontrolki przygasają? Nie ryzykuj spalenia komputera pokładowego tanimi kablami od sąsiada. Dojeżdżamy w <strong>20–30 minut</strong> z profesjonalną stacją rozruchową (Anti-Spike), bezpieczną dla silników benzynowych, diesla, skrzyń automatycznych oraz hybryd.
      </p>

      <!-- GŁÓWNY PRZYCISK CTA -->
      <div class="flex flex-col sm:flex-row items-center justify-center gap-4 w-full max-w-lg mx-auto mb-10">
        <a href="tel:+48696556446" class="ak-btn-primary">
          <span>📞 Wezwij Pomoc: 696 556 446</span>
        </a>
      </div>

      <!-- TRUST BADGES GRID (4 KAFELKI Z CZYTELNĄ TYPOGRAFIĄ) -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-3 sm:gap-4 max-w-4xl mx-auto my-8">
        
        <div class="bg-slate-900/90 border border-slate-800 p-4 sm:p-5 rounded-2xl text-center shadow-md">
          <div class="text-amber-400 font-black text-base sm:text-lg">⭐ 5.0 w Google</div>
          <div class="text-slate-300 text-[13.5px] sm:text-sm font-semibold mt-1">102 opinie kierowców</div>
        </div>

        <div class="bg-slate-900/90 border border-slate-800 p-4 sm:p-5 rounded-2xl text-center shadow-md">
          <div class="text-emerald-400 font-black text-base sm:text-lg">⏱️ 20–30 min</div>
          <div class="text-slate-300 text-[13.5px] sm:text-sm font-semibold mt-1">Średni czas dojazdu</div>
        </div>

        <div class="bg-slate-900/90 border border-slate-800 p-4 sm:p-5 rounded-2xl text-center shadow-md">
          <div class="text-white font-black text-base sm:text-lg">🛡️ Anti-Spike</div>
          <div class="text-slate-300 text-[13.5px] sm:text-sm font-semibold mt-1">Ochrona ECU i hybryd</div>
        </div>

        <div class="bg-slate-900/90 border border-slate-800 p-4 sm:p-5 rounded-2xl text-center shadow-md">
          <div class="text-amber-400 font-black text-base sm:text-lg">🅿️ Garaże -1 / -2 / -3</div>
          <div class="text-slate-300 text-[13.5px] sm:text-sm font-semibold mt-1">Wjazd pod niski strop</div>
        </div>

      </div>

      <!-- AUTENTYCZNE ZDJĘCIE ZE SQUARESPACE W ELEGANCKIM PANELU -->
      <div class="mt-10 rounded-3xl overflow-hidden border border-slate-800 shadow-2xl relative max-w-4xl mx-auto group">
        <img src="https://images.squarespace-cdn.com/content/v1/685d174157b18362d5b7b0f3/f8da5f14-890b-4f74-b2f5-47fb173e0390/awaryjne-uruchomienie-auta-warszawa.png" alt="Awaryjne uruchamianie auta Warszawa – Mobilny Serwis Akumulateo" class="w-full h-auto object-cover max-h-[380px] brightness-90 group-hover:brightness-100 transition duration-300" loading="eager" />
        <div class="absolute bottom-3 left-3 sm:bottom-5 sm:left-5 bg-slate-950/90 backdrop-filter backdrop-blur-md border border-slate-700/80 px-4 py-3 rounded-2xl text-left max-w-[92%] shadow-xl">
          <div class="text-sm sm:text-base font-black text-amber-400 flex items-center gap-2">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 akumulateo-pulse-dot flex-shrink-0"></span>
            <span>Technik Mobilny w Twojej Dzielnicy</span>
          </div>
          <div class="text-[13px] sm:text-sm text-slate-200 font-medium mt-1">Atestowane stacje rozruchowe 12V/24V i cyfrowe testery oporowe</div>
        </div>
      </div>

    </div>
  </section>

  <!-- 4. SEKCJA: UCZCIWA DIAGNOZA & USŁUGA MOBILNA (ALT #0b1329) -->
  <section class="ak-section ak-section-alt">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 w-full">
      <div class="ak-guarantee-card">
        <div class="ak-eyebrow mb-4">
          <span>🛡️</span> Gwarancja Uczciwej Diagnozy Akumulateo
        </div>
        <h2 class="ak-h2 mb-4 ak-break-text">
          Najpierw sprawdzamy przyczynę – nie wymieniamy akumulatora w ciemno!
        </h2>
        <p class="ak-body max-w-3xl mx-auto leading-relaxed mb-6">
          Nie każde rozładowanie oznacza konieczność zakupu nowej baterii. Przyczyną może być pozostawione oświetlenie, radio, długi postój na mrozie lub chwilowy spadek napięcia. Po uruchomieniu silnika nasz technik <strong>zawsze bezpłatnie mierzy ładowanie alternatora pod obciążeniem oraz bada sprawność akumulatora testerem oporowym</strong>. Wiesz dokładnie, na czym stoisz.
        </p>
        <div class="inline-flex items-center gap-2 bg-slate-950/80 border border-amber-500/30 text-amber-300 px-4 py-2 rounded-xl text-xs sm:text-sm font-bold">
          <span>ℹ️ Usługa w 100% mobilna – technik przyjeżdża bezpośrednio pod Twój adres w Warszawie i okolicach.</span>
        </div>
      </div>
    </div>
  </section>

  <!-- 5. SEKCJA: DLACZEGO BOOSTER, A NIE KABLE OD SĄSIADA? (CANVAS #020617) -->
  <section class="ak-section">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 w-full">
      <div class="text-center mb-10 sm:mb-16">
        <div class="ak-eyebrow mb-3">Bezpieczeństwo Elektroniki</div>
        <h2 class="ak-h2 tracking-tight ak-break-text">
          Dlaczego profesjonalny booster, a nie przypadkowe kable od sąsiada?
        </h2>
        <p class="ak-body max-w-2xl mx-auto mt-2">
          Współczesne samochody to zaawansowane komputery na kołach. Przypadkowy rozruch z drugiego auta stwarza realne ryzyko kosztownych awarii elektroniki.
        </p>
      </div>

      <div class="ak-grid-3">
        
        <div class="ak-card flex flex-col justify-between">
          <div>
            <div class="ak-icon-box">
              🛡️
            </div>
            <h3 class="ak-h3 mb-3">Zabezpieczenie Anti-Spike</h3>
            <p class="ak-body">
              Tanie kable marketowe przy odpinaniu generują szpilki napięciowe (voltage spikes) sięgające kilkudziesięciu woltów. Nasze stacje rozruchowe posiadają wbudowane warystory i tłumiki przepięć, chroniąc sterownik silnika (ECU), moduły komfortu (BCM) oraz delikatną elektronikę hybryd.
            </p>
          </div>
        </div>

        <div class="ak-card flex flex-col justify-between">
          <div>
            <div class="ak-icon-box">
              🅿️
            </div>
            <h3 class="ak-h3 mb-3">Wjazd do garaży -1 / -2 / -3</h3>
            <p class="ak-body">
              Auto stoi przodem do ściany na parkingu podziemnym, gdzie nie ma miejsca na manewr drugim autem, a laweta nie wjedzie przez niski strop (2.0m)? Nasz technik dociera z w pełni przenośnym, ultra-wydajnym boosterem o prądzie udarowym do 3000A.
            </p>
          </div>
        </div>

        <div class="ak-card flex flex-col justify-between">
          <div>
            <div class="ak-icon-box">
              ⚡
            </div>
            <h3 class="ak-h3 mb-3">Cyfrowy test alternatora</h3>
            <p class="ak-body">
              Sam rozruch to dopiero połowa sukcesu. Po odpaleniu mierzymy cyfrowym testerem napięcie pod pełnym obciążeniem (światła mijania, dmuchawa, ogrzewanie szyb). Dzięki temu masz 100% pewności, że alternator ładuje baterię i bezpiecznie dojedziesz do celu.
            </p>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- 6. SEKCJA: JAK POMAGAMY W 4 PROSTYCH KROKACH (ALT #0b1329) -->
  <section class="ak-section ak-section-alt">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 w-full">
      <div class="text-center mb-10 sm:mb-16">
        <div class="ak-eyebrow mb-3">Szybka Procedura Interwencji</div>
        <h2 class="ak-h2 tracking-tight ak-break-text">
          Jak pomagamy w 4 prostych krokach?
        </h2>
      </div>

      <div class="ak-grid-4">
        
        <div class="ak-card">
          <div class="ak-step-num">
            01
          </div>
          <h3 class="ak-h3">Telefon 696 556 446</h3>
          <p class="ak-body">
            Podajesz dzielnicę, adres oraz markę i model pojazdu. Dyspozytor od razu potwierdza czas dojazdu technika oraz stały, z góry ustalony koszt usługi.
          </p>
        </div>

        <div class="ak-card">
          <div class="ak-step-num">
            02
          </div>
          <h3 class="ak-h3">Dojazd w 20–30 min</h3>
          <p class="ak-body">
            Mobilny serwisant wyrusza natychmiast na miejsce. Dojeżdżamy pod dom, biuro, centrum handlowe lub do garażu podziemnego w całej Warszawie i aglomeracji.
          </p>
        </div>

        <div class="ak-card">
          <div class="ak-step-num">
            03
          </div>
          <h3 class="ak-h3">Bezpieczny rozruch</h3>
          <p class="ak-body">
            Technik podłącza atestowaną stację rozruchową 12V/24V, weryfikuje polaryzację i uruchamia silnik ze stabilizacją napięcia (Anti-Spike), bez ryzyka błędu komputera pokładowego.
          </p>
        </div>

        <div class="ak-card">
          <div class="ak-step-num">
            04
          </div>
          <h3 class="ak-h3">Pomiar i płatność</h3>
          <p class="ak-body">
            Sprawdzamy stan akumulatora i alternatora. Płatności dokonasz wygodnie kartą, kodem BLIK lub gotówką. Dla firm wystawiamy fakturę VAT 23% na miejscu.
          </p>
        </div>

      </div>
    </div>
  </section>

  <!-- 7. SEKCJA: KOŁO RATUNKOWE AKUMULATEO (CANVAS #020617) -->
  <section class="ak-section">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 w-full">
      <div class="ak-rescue-card">
        
        <div class="ak-eyebrow mb-5">
          <span>⭐ Koło Ratunkowe Akumulateo</span>
        </div>

        <h2 class="ak-h2 mb-4 ak-break-text">
          Co jeśli akumulator ma zwarcie w celi i jest trwale martwy?
        </h2>

        <p class="ak-lead max-w-3xl mx-auto mb-8 ak-break-text">
          Jeżeli po uruchomieniu test wykaże, że akumulator nie trzyma pojemności i zgaśnie na pierwszym skrzyżowaniu – nie zostawiamy Cię na lodzie. Nasz technik ma w busie serwisowym <strong>fabrycznie nowe akumulatory marek Varta, Yuasa, Bosch, 4Max</strong> dobrane ściśle pod Twój model auta.
        </p>

        <div class="bg-slate-950/90 border border-slate-800 rounded-2xl p-5 sm:p-7 max-w-3xl mx-auto mb-8 text-left space-y-4">
          <div class="flex items-start gap-3 text-slate-100 font-bold ak-list-item">
            <span class="text-emerald-400 text-xl leading-none font-black">✓</span>
            <span><strong>Opłata za rozruch zostaje anulowana:</strong> Płacisz tylko za nowy akumulator z montażem!</span>
          </div>
          <div class="flex items-start gap-3 text-slate-100 ak-list-item">
            <span class="text-emerald-400 text-xl leading-none font-black">✓</span>
            <span>Profesjonalny montaż z podtrzymaniem pamięci komputera i kodowaniem BMS Start-Stop</span>
          </div>
          <div class="flex items-start gap-3 text-slate-100 ak-list-item">
            <span class="text-emerald-400 text-xl leading-none font-black">✓</span>
            <span>Brak kaucji depozytowej (30 zł) – bezpłatnie odbieramy starą baterię do legalnego recyklingu BDO</span>
          </div>
        </div>

        <div class="flex justify-center w-full">
          <a href="tel:+48696556446" class="ak-btn-primary max-w-md mx-auto">
            <span>📞 Zadzwoń: 696 556 446 (Pomoc 24h)</span>
          </a>
        </div>

      </div>
    </div>
  </section>

  <!-- 8. SEKCJA: CENNIK INTERWENCJI (ALT #0b1329) -->
  <section id="cennik" class="ak-section ak-section-alt">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 w-full">
      <div class="text-center mb-10 sm:mb-16">
        <div class="ak-eyebrow mb-3">Przejrzyste Warunki Cenowe</div>
        <h2 class="ak-h2 tracking-tight ak-break-text">
          Cennik awaryjnego uruchomienia w Warszawie
        </h2>
        <p class="ak-body max-w-2xl mx-auto mt-2">
          Brak ukrytych kosztów. Cenę potwierdzamy telefonicznie przed wyruszeniem technika.
        </p>
      </div>

      <div class="ak-grid-3">
        
        <!-- PAKIET 1: ROZRUCH PODSTAWOWY -->
        <div class="ak-card">
          <div class="flex-grow flex flex-col">
            <div class="text-xs sm:text-[13px] uppercase font-black text-slate-400 tracking-wider mb-2">Pakiet Podstawowy</div>
            <h3 class="ak-h3 text-white">Awaryjny Rozruch 12V</h3>
            <div class="text-3xl sm:text-4xl font-black text-white mb-6">od 180 zł</div>
            <ul class="space-y-3.5 mb-8">
              <li class="flex items-start gap-2.5 ak-list-item"><span class="text-emerald-400 font-black text-lg leading-none">✓</span> <span>Dojazd technika w 20–30 min</span></li>
              <li class="flex items-start gap-2.5 ak-list-item"><span class="text-emerald-400 font-black text-lg leading-none">✓</span> <span>Bezpieczny rozruch boosterem Anti-Spike</span></li>
              <li class="flex items-start gap-2.5 ak-list-item"><span class="text-emerald-400 font-black text-lg leading-none">✓</span> <span>Wjazd do garażu podziemnego (-1/-2/-3)</span></li>
              <li class="flex items-start gap-2.5 ak-list-item"><span class="text-emerald-400 font-black text-lg leading-none">✓</span> <span>Podstawowa kontrola ładowania</span></li>
            </ul>
          </div>
          <div class="mt-auto pt-4 w-full">
            <a href="tel:+48696556446" class="ak-btn-secondary">
              Zamów rozruch ➔
            </a>
          </div>
        </div>

        <!-- PAKIET 2: WYRÓŻNIONY – ROZRUCH + PEŁNA DIAGNOSTYKA -->
        <div class="ak-card ak-card-featured relative">
          <div class="flex-grow flex flex-col">
            <div class="inline-flex items-center self-start bg-amber-500 text-slate-950 font-black text-xs sm:text-[13px] uppercase tracking-wider px-3.5 py-1.5 rounded-full shadow-md mb-3">
              ★ Najczęściej Wybierany Pakiet
            </div>
            <div class="text-xs sm:text-[13px] uppercase font-black text-amber-400 tracking-wider mb-2">Pakiet Bezpieczeństwo</div>
            <h3 class="ak-h3 text-white">Rozruch + Pełna Diagnoza</h3>
            <div class="text-3xl sm:text-4xl font-black text-amber-400 mb-6">od 220 zł</div>
            <ul class="space-y-3.5 mb-8">
              <li class="flex items-start gap-2.5 ak-list-item"><span class="text-amber-400 font-black text-lg leading-none">✓</span> <span><strong>Wszystko z pakietu podstawowego</strong></span></li>
              <li class="flex items-start gap-2.5 ak-list-item"><span class="text-emerald-400 font-black text-lg leading-none">✓</span> <span>Cyfrowy test sprawności pod obciążeniem</span></li>
              <li class="flex items-start gap-2.5 ak-list-item"><span class="text-emerald-400 font-black text-lg leading-none">✓</span> <span>Badanie prądu upływu (czy coś kradnie prąd)</span></li>
              <li class="flex items-start gap-2.5 ak-list-item"><span class="text-emerald-400 font-black text-lg leading-none">✓</span> <span>Test diod i regulatora alternatora</span></li>
              <li class="flex items-start gap-2.5 ak-list-item"><span class="text-emerald-400 font-black text-lg leading-none">✓</span> <span>Rekomendacja dalszej eksploatacji</span></li>
            </ul>
          </div>
          <div class="mt-auto pt-4 w-full">
            <a href="tel:+48696556446" class="ak-btn-primary w-full">
              Wybierz Pełną Diagnozę ➔
            </a>
          </div>
        </div>

        <!-- PAKIET 3: PEŁNE ROZWIĄZANIE – WYMIANA BATERII -->
        <div class="ak-card">
          <div class="flex-grow flex flex-col">
            <div class="text-xs sm:text-[13px] uppercase font-black text-slate-400 tracking-wider mb-2">Rozwiązanie Trwałe</div>
            <h3 class="ak-h3 text-white">Rozruch z Wymianą Baterii</h3>
            <div class="text-3xl sm:text-4xl font-black text-white mb-6">Cena baterii + montaż</div>
            <ul class="space-y-3.5 mb-8">
              <li class="flex items-start gap-2.5 ak-list-item"><span class="text-emerald-400 font-black text-lg leading-none">✓</span> <span><strong>GRATIS:</strong> Opłata za rozruch anulowana</span></li>
              <li class="flex items-start gap-2.5 ak-list-item"><span class="text-emerald-400 font-black text-lg leading-none">✓</span> <span>Nowa markowa bateria Varta / Yuasa / Bosch</span></li>
              <li class="flex items-start gap-2.5 ak-list-item"><span class="text-emerald-400 font-black text-lg leading-none">✓</span> <span>Montaż z podtrzymaniem pamięci OBD</span></li>
              <li class="flex items-start gap-2.5 ak-list-item"><span class="text-emerald-400 font-black text-lg leading-none">✓</span> <span>Kodowanie BMS / adaptacja Start-Stop</span></li>
              <li class="flex items-start gap-2.5 ak-list-item"><span class="text-emerald-400 font-black text-lg leading-none">✓</span> <span>Odbiór starej baterii (brak kaucji 30 zł)</span></li>
            </ul>
          </div>
          <div class="mt-auto pt-4 w-full">
            <a href="tel:+48696556446" class="ak-btn-secondary">
              Wymień na miejscu ➔
            </a>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- 9. SEKCJA: OPINIE KLIENTÓW GOOGLE 5.0★ (CANVAS #020617) -->
  <section id="opinie" class="ak-section" itemscope itemtype="https://schema.org/AutoRepair">
    <meta itemprop="name" content="Akumulateo – Pogotowie Akumulatorowe 24h Warszawa">
    <meta itemprop="telephone" content="+48696556446">
    <meta itemprop="priceRange" content="180 PLN - 650 PLN">
    <meta itemprop="image" content="https://www.akumulateo.pl/assets/images/logo.png">

    <div class="max-w-6xl mx-auto px-4 sm:px-6 w-full">
      <div class="text-center mb-10 sm:mb-14">
        <div class="ak-eyebrow mb-3">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-400 inline-block shadow-sm"></span>
          <span>100% Autentyczne Opinie Kierowców</span>
        </div>
        <h2 class="ak-h2 tracking-tight ak-break-text">
          Ocena 5.0 ★★★★★ w Google Maps
        </h2>
        <p class="ak-body max-w-2xl mx-auto mt-2">
          <strong>102 zweryfikowane opinie (100% 5.0★)</strong> od kierowców uratowanych w Warszawie i okolicach. Dojazd w 20–30 min, profesjonalny sprzęt i zero naciągania.
        </p>
      </div>

      <!-- KARTA PODSUMOWANIA GOOGLE MAPS -->
      <div class="ak-google-summary-card" itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating">
        <meta itemprop="ratingValue" content="5.0">
        <meta itemprop="bestRating" content="5.0">
        <meta itemprop="worstRating" content="1.0">
        <meta itemprop="ratingCount" content="102">
        <meta itemprop="reviewCount" content="102">

        <div class="ak-google-logo-wrapper" aria-hidden="true">
          <svg viewBox="0 0 24 24" width="34" height="34" class="ak-google-logo-svg" focusable="false">
            <path fill="#4285F4" d="M23.745 12.27c0-.7-.06-1.4-.19-2.07H12v4.51h6.6c-.29 1.52-1.14 2.8-2.4 3.65v3.03h3.88c2.27-2.09 3.66-5.17 3.66-9.12z"/>
            <path fill="#34A853" d="M12 24c3.24 0 5.95-1.08 7.93-2.91l-3.88-3.03c-1.08.72-2.45 1.16-4.05 1.16-3.12 0-5.77-2.1-6.72-4.93H1.26v3.13C3.29 21.41 7.37 24 12 24z"/>
            <path fill="#FBBC05" d="M5.28 14.29c-.25-.72-.38-1.49-.38-2.29s.13-1.57.38-2.29V6.58H1.26C.46 8.18 0 9.98 0 12s.46 3.82 1.26 5.42l4.02-3.13z"/>
            <path fill="#EA4335" d="M12 4.75c1.77 0 3.35.61 4.6 1.8l3.42-3.42C17.95 1.19 15.24 0 12 0 7.37 0 3.29 2.59 1.26 6.58l4.02 3.13c.95-2.83 3.6-4.96 6.72-4.96z"/>
          </svg>
        </div>

        <div class="ak-google-score-col">
          <div class="ak-google-score-row">
            <span class="ak-google-rating-number">5.0</span>
            <div class="ak-stars-row" aria-label="Ocena: 5 na 5 gwiazdek">
              <svg class="ak-star-icon" viewBox="0 0 20 20" fill="currentColor"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              <svg class="ak-star-icon" viewBox="0 0 20 20" fill="currentColor"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              <svg class="ak-star-icon" viewBox="0 0 20 20" fill="currentColor"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              <svg class="ak-star-icon" viewBox="0 0 20 20" fill="currentColor"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
              <svg class="ak-star-icon" viewBox="0 0 20 20" fill="currentColor"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
            </div>
          </div>
          <div class="ak-google-reviews-count-text">
            Średnia ze <strong>100+ recenzji (100% 5.0★)</strong> w Google Maps
          </div>
        </div>

        <a href="https://g.page/r/CXjN9llopHR_EBM/" target="_blank" rel="noopener noreferrer" class="ak-google-view-all-btn" aria-label="Zobacz profil Akumulateo w Google Maps">
          <span>Otwórz w Google Maps ↗</span>
        </a>
      </div>

      <!-- SIATKA 6 AUTENTYCZNYCH OPINII KLIENTÓW -->
      <div class="ak-grid-3">
        
        <!-- OPINIA 1: TOMASZ M. (MOKOTÓW) -->
        <article class="ak-card flex flex-col justify-between" itemprop="review" itemscope itemtype="https://schema.org/Review">
          <div>
            <div class="ak-review-top">
              <div class="ak-review-avatar" aria-hidden="true">TM</div>
              <div class="ak-review-user-info">
                <div class="ak-review-name" itemprop="author" itemscope itemtype="https://schema.org/Person">
                  <span itemprop="name">Tomasz M.</span>
                </div>
                <div class="ak-review-verified">
                  <svg class="ak-check-icon" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                  <span>Zweryfikowany klient Google</span>
                </div>
              </div>
            </div>

            <div class="ak-review-meta">
              <div class="ak-stars-row" itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating">
                <meta itemprop="ratingValue" content="5">
                <meta itemprop="bestRating" content="5">
                <meta itemprop="worstRating" content="1">
                <span class="ak-stars-gold">★★★★★</span>
              </div>
              <time class="ak-review-date" itemprop="datePublished" datetime="2024-11-12">listopad 2024</time>
            </div>

            <div class="ak-review-tag">
              📍 Warszawa Mokotów • Parking -2
            </div>

            <blockquote class="ak-review-text" itemprop="reviewBody">
              „Awaria akumulatora na podziemnym parkingu (-2) w biurowcu na Mokotowie. Szybki przyjazd w 20 minut, nowa <strong>Yuasa</strong> zamontowana i zakodowana komputerem od ręki. Pełen profesjonalizm.”
            </blockquote>
          </div>
        </article>

        <!-- OPINIA 2: KATARZYNA P. (PIASECZNO) -->
        <article class="ak-card flex flex-col justify-between" itemprop="review" itemscope itemtype="https://schema.org/Review">
          <div>
            <div class="ak-review-top">
              <div class="ak-review-avatar" aria-hidden="true">KP</div>
              <div class="ak-review-user-info">
                <div class="ak-review-name" itemprop="author" itemscope itemtype="https://schema.org/Person">
                  <span itemprop="name">Katarzyna P.</span>
                </div>
                <div class="ak-review-verified">
                  <svg class="ak-check-icon" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                  <span>Zweryfikowany klient Google</span>
                </div>
              </div>
            </div>

            <div class="ak-review-meta">
              <div class="ak-stars-row" itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating">
                <meta itemprop="ratingValue" content="5">
                <meta itemprop="bestRating" content="5">
                <meta itemprop="worstRating" content="1">
                <span class="ak-stars-gold">★★★★★</span>
              </div>
              <time class="ak-review-date" itemprop="datePublished" datetime="2024-11-28">listopad 2024</time>
            </div>

            <div class="ak-review-tag">
              📍 Piaseczno • Niedziela rano
            </div>

            <blockquote class="ak-review-text" itemprop="reviewBody">
              „Niedziela rano, auto unieruchomione przed wyjazdem rodzinnym. Pan przyjechał do Piaseczna z nowym akumulatorem, sprawdził instalację, płatność BLIKiem u technika. Uratowana niedziela!”
            </blockquote>
          </div>
        </article>

        <!-- OPINIA 3: MARCIN W. (WOLA) -->
        <article class="ak-card flex flex-col justify-between" itemprop="review" itemscope itemtype="https://schema.org/Review">
          <div>
            <div class="ak-review-top">
              <div class="ak-review-avatar" aria-hidden="true">MW</div>
              <div class="ak-review-user-info">
                <div class="ak-review-name" itemprop="author" itemscope itemtype="https://schema.org/Person">
                  <span itemprop="name">Marcin W.</span>
                </div>
                <div class="ak-review-verified">
                  <svg class="ak-check-icon" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                  <span>Zweryfikowany klient Google</span>
                </div>
              </div>
            </div>

            <div class="ak-review-meta">
              <div class="ak-stars-row" itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating">
                <meta itemprop="ratingValue" content="5">
                <meta itemprop="bestRating" content="5">
                <meta itemprop="worstRating" content="1">
                <span class="ak-stars-gold">★★★★★</span>
              </div>
              <time class="ak-review-date" itemprop="datePublished" datetime="2024-12-05">grudzień 2024</time>
            </div>

            <div class="ak-review-tag">
              📍 Warszawa Wola • Wymiana Varta
            </div>

            <blockquote class="ak-review-text" itemprop="reviewBody">
              „Bez holowania i bez straty czasu na szukanie sklepu. Komputerowy test ładowania alternatora, montaż nowej <strong>Varty</strong> i darmowy odbiór starej baterii. Polecam każdemu.”
            </blockquote>
          </div>
        </article>

        <!-- OPINIA 4: PAWEŁ K. (ŚRÓDMIEŚCIE) -->
        <article class="ak-card flex flex-col justify-between" itemprop="review" itemscope itemtype="https://schema.org/Review">
          <div>
            <div class="ak-review-top">
              <div class="ak-review-avatar" aria-hidden="true">PK</div>
              <div class="ak-review-user-info">
                <div class="ak-review-name" itemprop="author" itemscope itemtype="https://schema.org/Person">
                  <span itemprop="name">Paweł K.</span>
                </div>
                <div class="ak-review-verified">
                  <svg class="ak-check-icon" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                  <span>Zweryfikowany klient Google</span>
                </div>
              </div>
            </div>

            <div class="ak-review-meta">
              <div class="ak-stars-row" itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating">
                <meta itemprop="ratingValue" content="5">
                <meta itemprop="bestRating" content="5">
                <meta itemprop="worstRating" content="1">
                <span class="ak-stars-gold">★★★★★</span>
              </div>
              <time class="ak-review-date" itemprop="datePublished" datetime="2024-12-18">grudzień 2024</time>
            </div>

            <div class="ak-review-tag">
              📍 Warszawa Śródmieście • Garaż wielopoziomowy
            </div>

            <blockquote class="ak-review-text" itemprop="reviewBody">
              „Pomoc drogowa odmówiła wjazdu do garażu wielopoziomowego w Śródmieściu ze względu na niski strop. Technik z Akumulateo wszedł z przenośnym boosterem, odpalił auto w 3 minuty i sprawdził prąd ładowania. Klasa!”
            </blockquote>
          </div>
        </article>

        <!-- OPINIA 5: ANNA S. (PRAGA-POŁUDNIE) -->
        <article class="ak-card flex flex-col justify-between" itemprop="review" itemscope itemtype="https://schema.org/Review">
          <div>
            <div class="ak-review-top">
              <div class="ak-review-avatar" aria-hidden="true">AS</div>
              <div class="ak-review-user-info">
                <div class="ak-review-name" itemprop="author" itemscope itemtype="https://schema.org/Person">
                  <span itemprop="name">Anna S.</span>
                </div>
                <div class="ak-review-verified">
                  <svg class="ak-check-icon" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                  <span>Zweryfikowany klient Google</span>
                </div>
              </div>
            </div>

            <div class="ak-review-meta">
              <div class="ak-stars-row" itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating">
                <meta itemprop="ratingValue" content="5">
                <meta itemprop="bestRating" content="5">
                <meta itemprop="worstRating" content="1">
                <span class="ak-stars-gold">★★★★★</span>
              </div>
              <time class="ak-review-date" itemprop="datePublished" datetime="2025-01-08">styczeń 2025</time>
            </div>

            <div class="ak-review-tag">
              📍 Praga-Południe • Start-Stop (BMS)
            </div>

            <blockquote class="ak-review-text" itemprop="reviewBody">
              „Ekspresowy rozruch i wymiana akumulatora w aucie ze Start-Stop na Pradze. Wszystko zakodowane, zegary i radio nie straciły ustawień. Paragon i gwarancja na miejscu.”
            </blockquote>
          </div>
        </article>

        <!-- OPINIA 6: GRZEGORZ B. (BEMOWO) -->
        <article class="ak-card flex flex-col justify-between" itemprop="review" itemscope itemtype="https://schema.org/Review">
          <div>
            <div class="ak-review-top">
              <div class="ak-review-avatar" aria-hidden="true">GB</div>
              <div class="ak-review-user-info">
                <div class="ak-review-name" itemprop="author" itemscope itemtype="https://schema.org/Person">
                  <span itemprop="name">Grzegorz B.</span>
                </div>
                <div class="ak-review-verified">
                  <svg class="ak-check-icon" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/></svg>
                  <span>Zweryfikowany klient Google</span>
                </div>
              </div>
            </div>

            <div class="ak-review-meta">
              <div class="ak-stars-row" itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating">
                <meta itemprop="ratingValue" content="5">
                <meta itemprop="bestRating" content="5">
                <meta itemprop="worstRating" content="1">
                <span class="ak-stars-gold">★★★★★</span>
              </div>
              <time class="ak-review-date" itemprop="datePublished" datetime="2025-01-22">styczeń 2025</time>
            </div>

            <div class="ak-review-tag">
              📍 Warszawa Bemowo • Uczciwa diagnoza
            </div>

            <blockquote class="ak-review-text" itemprop="reviewBody">
              „Wzorowa uczciwość. Technik na Bemowie sprawdził akumulator testerem – okazało się, że to poluzowana klema i pobór prądu przez kamerkę, a nie martwa bateria. Nie naciągają na koszty!”
            </blockquote>
          </div>
        </article>

      </div>

      <!-- DOLNA BELKA ZAUFANIA I CTA W OPINIACH -->
      <div class="ak-reviews-footer">
        <div class="ak-reviews-footer-text">
          <strong>Bezpieczeństwo i pewność:</strong> Płacisz u technika dopiero po wykonaniu usługi i uruchomieniu samochodu (karta, BLIK, gotówka).
        </div>
        <div class="ak-reviews-footer-actions">
          <a href="tel:+48696556446" class="ak-btn-primary">
            <span>📞 Zadzwoń: 696 556 446</span>
          </a>
          <a href="https://g.page/r/CXjN9llopHR_EBM/" target="_blank" rel="noopener noreferrer" class="ak-reviews-cta-google">
            <span>⭐ Sprawdź profil w Google Maps ↗</span>
          </a>
        </div>
      </div>

    </div>
  </section>

  <!-- 10. SEKCJA: NAJCZĘSTSZE PYTANIA KIEROWCÓW (ALT #0b1329) -->
  <section id="faq" class="ak-section ak-section-alt">
    <div class="max-w-5xl mx-auto px-4 sm:px-6 w-full">
      <div class="text-center mb-10 sm:mb-16">
        <div class="ak-eyebrow mb-3">Częste Wątpliwości</div>
        <h2 class="ak-h2 tracking-tight ak-break-text">
          Pytania przed wezwaniem pomocy (FAQ)
        </h2>
      </div>

      <div class="space-y-4 max-w-4xl mx-auto w-full">
        
        <details class="ak-faq-item bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-7 group transition hover:border-slate-700 shadow-md">
          <summary class="font-bold text-white text-lg sm:text-xl">
            <span>Co mam przygotować przed telefonem?</span>
            <svg class="ak-faq-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7" /></svg>
          </summary>
          <p class="ak-body mt-4 pt-4 border-t border-slate-800/80 ak-break-text">
            Podaj lokalizację samochodu (dzielnica, ulica lub charakterystyczny punkt), markę, model oraz rodzaj silnika (benzyna, diesel, hybryda). Jeśli auto stoi w garażu podziemnym na poziomie -1, -2 lub -3, poinformuj o tym od razu dyspozytora.
          </p>
        </details>

        <details class="ak-faq-item bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-7 group transition hover:border-slate-700 shadow-md">
          <summary class="font-bold text-white text-lg sm:text-xl">
            <span>Czy od razu muszę kupować nowy akumulator?</span>
            <svg class="ak-faq-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7" /></svg>
          </summary>
          <p class="ak-body mt-4 pt-4 border-t border-slate-800/80 ak-break-text">
            Absolutnie nie! W Akumulateo najpierw rzetelnie badamy akumulator cyfrowym testerem. Jeśli bateria była tylko rozładowana przez pozostawione światła, wystarczy sam rozruch i naładowanie podczas jazdy. Wymianę sugerujemy wyłącznie wtedy, gdy akumulator jest trwale zasiarczony lub ma zwarcie w celi.
          </p>
        </details>

        <details class="ak-faq-item bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-7 group transition hover:border-slate-700 shadow-md">
          <summary class="font-bold text-white text-lg sm:text-xl">
            <span>Czy uruchamiacie samochody hybrydowe i ze skrzynią automatyczną?</span>
            <svg class="ak-faq-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7" /></svg>
          </summary>
          <p class="ak-body mt-4 pt-4 border-t border-slate-800/80 ak-break-text">
            Tak. W autach hybrydowych (gdzie rozładowuje się mały akumulator pomocniczy 12V zasilający komputer pokładowy) oraz w samochodach z automatyczną skrzynią biegów nasza procedura rozruchu ze stabilizacją napięcia (Anti-Spike) jest w 100% bezpieczna i zgodna ze standardami fabrycznymi.
          </p>
        </details>

        <details class="ak-faq-item bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-7 group transition hover:border-slate-700 shadow-md">
          <summary class="font-bold text-white text-lg sm:text-xl">
            <span>Co jeśli auto nadal się nie uruchomi (inna usterka)?</span>
            <svg class="ak-faq-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7" /></svg>
          </summary>
          <p class="ak-body mt-4 pt-4 border-t border-slate-800/80 ak-break-text">
            Brak reakcji na podanie właściwego napięcia z mocnego boostera oznacza inną usterkę (np. uszkodzony rozrusznik, immobilizer, pompa paliwa czy bezpiecznik główny). Na miejscu nasz technik oceni objawy, sprawdzi bezpieczniki i doradzi najlepsze rozwiązanie.
          </p>
        </details>

        <details class="ak-faq-item bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-7 group transition hover:border-slate-700 shadow-md">
          <summary class="font-bold text-white text-lg sm:text-xl">
            <span>Czy pomagacie w nocy, w weekendy i poza Warszawą?</span>
            <svg class="ak-faq-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M19 9l-7 7-7-7" /></svg>
          </summary>
          <p class="ak-body mt-4 pt-4 border-t border-slate-800/80 ak-break-text">
            Tak! Dyżurujemy 24 godziny na dobę, 7 dni w tygodniu, w niedziele i wszystkie święta. Obsługujemy wszystkie 18 dzielnic Warszawy oraz miejscowości aglomeracji (Piaseczno, Pruszków, Otwock, Legionowo, Marki, Łomianki, Ząbki i inne).
          </p>
        </details>

      </div>
    </div>
  </section>

  <!-- 11. SEKCJA: OBSZAR DZIAŁANIA I SZYBKI KONTAKT (CANVAS #020617) -->
  <section class="ak-section">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 w-full">
      <div class="bg-gradient-to-r from-slate-900 via-slate-900 to-slate-950 border border-slate-800 rounded-3xl p-6 sm:p-12 shadow-2xl">
        <div class="text-center max-w-3xl mx-auto mb-8">
          <div class="ak-eyebrow mb-3">📍 Warszawa i Aglomeracja</div>
          <h2 class="ak-h2 tracking-tight">Dojazd 20–30 minut we wszystkich dzielnicach</h2>
          <p class="ak-body mt-2">
            Nasi serwisanci dyżurują mobilnie w strategicznych punktach Warszawy i okolic, dzięki czemu docieramy błyskawicznie na miejsce awarii:
          </p>
        </div>

        <div class="flex flex-wrap justify-center gap-2.5 max-w-4xl mx-auto mb-10">
          <span class="ak-badge-tag">Mokotów</span>
          <span class="ak-badge-tag">Wola</span>
          <span class="ak-badge-tag">Ursynów</span>
          <span class="ak-badge-tag">Śródmieście</span>
          <span class="ak-badge-tag">Bielany</span>
          <span class="ak-badge-tag">Bemowo</span>
          <span class="ak-badge-tag">Praga-Południe</span>
          <span class="ak-badge-tag">Praga-Północ</span>
          <span class="ak-badge-tag">Targówek</span>
          <span class="ak-badge-tag">Ochota</span>
          <span class="ak-badge-tag">Białołęka</span>
          <span class="ak-badge-tag">Wawer</span>
          <span class="ak-badge-tag">Żoliborz</span>
          <span class="ak-badge-tag">Ursus</span>
          <span class="ak-badge-tag">Włochy</span>
          <span class="ak-badge-tag">Wilanów</span>
          <span class="ak-badge-tag">Rembertów</span>
          <span class="ak-badge-tag">Wesoła</span>
          <span class="ak-badge-tag">Piaseczno</span>
          <span class="ak-badge-tag">Pruszków</span>
          <span class="ak-badge-tag">Legionowo</span>
          <span class="ak-badge-tag">Marki</span>
          <span class="ak-badge-tag">Otwock</span>
          <span class="ak-badge-tag">Łomianki</span>
        </div>

        <div class="text-center pt-6 border-t border-slate-800/80">
          <a href="tel:+48696556446" class="ak-btn-primary">
            <span>📞 Zadzwoń po technika: 696 556 446</span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- 12. STOPKA AKUMULATEO -->
  <footer class="bg-slate-950 border-t border-slate-800 py-14 sm:py-20 px-4 sm:px-6 w-full text-sm text-slate-300">
    <div class="max-w-6xl mx-auto ak-grid-4 gap-8 sm:gap-12 mb-12">
      
      <div class="space-y-3">
        <div class="text-white font-black text-xl flex items-center gap-2">
          <span>AKUMULAT<span class="text-amber-500">E</span>O</span>
        </div>
        <p class="text-slate-300 leading-relaxed text-sm">
          Mobilny serwis akumulatorowy w Warszawie i aglomeracji. Całodobowy dojazd, awaryjny rozruch 12V/24V, diagnostyka alternatora oraz profesjonalny montaż nowych baterii pod domem klienta.
        </p>
      </div>

      <div class="space-y-3">
        <div class="text-white font-bold text-base mb-3">Usługi Mobilne 24h</div>
        <div><a href="/awaryjne-uruchomienie-auta-warszawa" class="hover:text-amber-400 transition text-amber-400 font-bold text-sm">Awaryjne Uruchomienie Auta</a></div>
        <div><a href="/wymiana-akumulatora-warszawa-mokotow" class="hover:text-amber-400 transition text-slate-300 text-sm">Wymiana Akumulatora z Dojazdem</a></div>
        <div><a href="/#cennik" class="hover:text-amber-400 transition text-slate-300 text-sm">Cennik Usług</a></div>
        <div><a href="/obszar-dzialania-warszawa-i-okolice" class="hover:text-amber-400 transition text-slate-300 text-sm">Obszar Działania (18 dzielnic)</a></div>
      </div>

      <div class="space-y-3">
        <div class="text-white font-bold text-base mb-3">Oficjalne Marki</div>
        <div><span class="text-slate-300 text-sm">Akumulatory Yuasa (YBX Series)</span></div>
        <div><span class="text-slate-300 text-sm">Akumulatory Varta (AGM / EFB)</span></div>
        <div><span class="text-slate-300 text-sm">Akumulatory Bosch (S4 / S5)</span></div>
        <div><span class="text-slate-300 text-sm">Akumulatory 4Max & Eco-Force</span></div>
      </div>

      <div class="space-y-3">
        <div class="text-white font-bold text-base mb-2">Telefon Alarmowy 24h</div>
        <a href="tel:+48696556446" class="inline-flex items-center gap-2 bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-black px-6 py-3.5 rounded-xl shadow-lg text-sm sm:text-base">
          <span>📞 696 556 446</span>
        </a>
        <div class="text-xs sm:text-sm text-slate-400">Dyżur dyspozytora 7 dni w tygodniu 24h</div>
      </div>

    </div>

    <div class="max-w-6xl mx-auto pt-8 border-t border-slate-900 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs sm:text-sm text-slate-400">
      <div>© 2026 Akumulateo. Wszystkie prawa zastrzeżone. Mobilny serwis akumulatorów.</div>
      <div class="flex items-center gap-6">
        <span class="text-emerald-400 font-semibold">Eko Recykling BDO</span>
        <a href="/" class="hover:text-white transition">Strona Główna</a>
        <a href="/obszar-dzialania-warszawa-i-okolice" class="hover:text-white transition">Obszar Działania</a>
      </div>
    </div>
  </footer>

</div>

</template>

<!-- 5. SKRYPT MONTAŻU I LOGIKI INTERAKTYWNEJ -->
<script>
(function() {{
  function mountAkumulateoAwaryjne() {{
    if (document.getElementById('akumulateo-awaryjne-wrapper')) return true;
    
    var tpl = document.getElementById('akumulateo-awaryjne-template');
    if (!tpl) return false;
    
    var targetSection = document.querySelector('section[data-section-id="6a8c912f5849182127a62d59"]');
    var parent = targetSection ? targetSection.parentNode : 
                 (document.querySelector('#sections') || 
                  document.querySelector('main#page') || 
                  document.querySelector('#page') || 
                  document.body);
    if (!parent) return false;
    
    var wrapper = document.createElement('div');
    wrapper.id = 'akumulateo-awaryjne-wrapper';
    wrapper.appendChild(tpl.content.cloneNode(true));
    
    if (targetSection) {{
      parent.insertBefore(wrapper, targetSection);
    }} else if (parent.firstChild) {{
      parent.insertBefore(wrapper, parent.firstChild);
    }} else {{
      parent.appendChild(wrapper);
    }}

    return true;
  }}

  // Synchronizacja Sticky Call Bar z banerem cookies
  function syncCookieBannerWithStickyBar() {{
    var banner = document.querySelector('.gdpr-cookie-banner, .sqs-cookie-banner-v2, .cookie-banner-mount-point');
    var bar = document.getElementById('akumulateo-sticky-call-bar');
    if (!bar) return;
    var hasBanner = banner && banner.offsetHeight > 0 && window.getComputedStyle(banner).display !== 'none';
    if (hasBanner) {{
      bar.style.setProperty('display', 'none', 'important');
    }} else {{
      bar.style.display = '';
    }}
  }}

  if (!mountAkumulateoAwaryjne()) {{
    if (window.MutationObserver) {{
      var obs = new MutationObserver(function() {{
        if (mountAkumulateoAwaryjne()) {{
          obs.disconnect();
        }}
      }});
      obs.observe(document.documentElement, {{ childList: true, subtree: true }});
    }}
    if (document.readyState === 'loading') {{
      document.addEventListener('DOMContentLoaded', mountAkumulateoAwaryjne);
    }}
    window.addEventListener('load', mountAkumulateoAwaryjne);
  }}

  setInterval(syncCookieBannerWithStickyBar, 300);
}})();
</script>
"""

out_path = os.path.join(SNIPPETS_DIR, "awaryjne-uruchomienie-page-header-injection.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"✅ Zaktualizowano pakiet wstrzyknięcia dla awaryjnego uruchomienia:")
print(f"   Ścieżka: {out_path}")
print(f"   Rozmiar: {len(HTML_CONTENT)} znaków")
