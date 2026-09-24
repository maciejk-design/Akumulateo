#!/usr/bin/env python3
"""
Generator kompletnych podstron SEO dla dzielnic Warszawy (Squarespace 7.1)
Tworzy gotowe do wklejenia pliki HTML dla kluczowych dzielnic na podstawie bazy districts-data.
"""

import os
import json

DISTRICTS = [
    {
        "slug": "ursynow",
        "url_slug": "wymiana-akumulatora-warszawa-ursynow",
        "name": "Ursynów",
        "eta": "15-25 min",
        "title": "Wymiana Akumulatora z Dojazdem Warszawa Ursynów 24h | Akumulateo",
        "desc": "Mobilny serwis akumulatorów na Ursynowie (Kabaty, Imielin, Stokłosy, Natolin). Awaryjny rozruch i wymiana akumulatora z dojazdem 24/7. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Ursynów 24/7",
        "areas": "Kabaty, Imielin, Stokłosy, Natolin, Dąbrówka, Grabów, Pyry",
        "description_body": "Rozładowany akumulator na Ursynowie? Dojedziemy pod Twój blok, dom jednorodzinny lub do garażu podziemnego w 15–25 minut. Sprawdzimy stan starej baterii testerem obciążeniowym, a gdy to konieczne – zamontujemy fabrycznie nowy akumulator AGM lub kwasowy i zakodujemy go w komputerze auta."
    },
    {
        "slug": "wola",
        "url_slug": "wymiana-akumulatora-warszawa-wola",
        "name": "Wola",
        "eta": "15-25 min",
        "title": "Pogotowie Akumulatorowe Warszawa Wola 24/7 | Rozruch i Wymiana",
        "desc": "Rozładowany akumulator na Woli (Odolany, Koło, Mirów, Czyste)? Przyjedziemy w 20 minut. Awaryjny rozruch boosterem i montaż akumulatora 24h. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Wola 24h/7",
        "areas": "Odolany, Koło, Czyste, Mirów, Młynów, Ulrychów, Rondo Daszyńskiego",
        "description_body": "Błyskawiczna pomoc z akumulatorem na warszawskiej Woli. Obsługujemy zarówno nowe osiedla na Odolanach, jak i biurowce w centrum biznesowym przy Rondzie Daszyńskiego. Wjeżdżamy do podziemnych hal garażowych."
    },
    {
        "slug": "srodmiescie",
        "url_slug": "wymiana-akumulatora-warszawa-srodmiescie",
        "name": "Śródmieście",
        "eta": "15-25 min",
        "title": "Awaryjne Odpalanie i Wymiana Akumulatora Śródmieście 24h | Akumulateo",
        "desc": "Śródmieście Warszawa: pogotowie akumulatorowe 24/7. Wjazd do stref i garaży podziemnych. Diagnostyka, montaż i kodowanie akumulatora. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Śródmieście 24/7",
        "areas": "Muranów, Powiśle, Solec, Ujazdów, Stare Miasto, Centrum, Plac Zbawiciela",
        "description_body": "Pomoc z akumulatorem w ścisłym centrum Warszawy. Znamy specyfikę stref ograniczonego ruchu i ciasnych parkingów. Przyjeżdżamy z boosterem i nową baterią pod wskazany adres o każdej porze dnia i nocy."
    },
    {
        "slug": "bielany",
        "url_slug": "wymiana-akumulatora-warszawa-bielany",
        "name": "Bielany",
        "eta": "20-30 min",
        "title": "Pogotowie Akumulatorowe Bielany 24/7 | Wymiana Akumulatora z Dojazdem",
        "desc": "Pomoc z akumulatorem Warszawa Bielany: Chomiczówka, Wrzeciono, Młociny, Słodowiec. Sprawdzenie prądu i nowy akumulator u klienta. Zadzwoń: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Bielany 24h",
        "areas": "Chomiczówka, Wrzeciono, Młociny, Wawrzyszew, Słodowiec, Stare Bielany",
        "description_body": "Całodobowy mobilny serwis akumulatorów na Bielanach. Dowozimy akumulatory do aut osobowych, dostawczych i hybryd. Zabieramy zużytą baterię, zdejmując z Ciebie konieczność płacenia kaucji 30 zł."
    },
    {
        "slug": "praga-poludnie",
        "url_slug": "wymiana-akumulatora-warszawa-praga-poludnie",
        "name": "Praga-Południe",
        "eta": "15-25 min",
        "title": "Wymiana Akumulatora z Dojazdem Praga-Południe (Gocław, Grochów, Saska Kępa)",
        "desc": "Pogotowie akumulatorowe Praga-Południe: Grochów, Saska Kępa, Gocław. Dojazd w 20 min, diagnostyka ładowania i wymiana na miejscu 24h. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Praga-Południe 24/7",
        "areas": "Gocław, Grochów, Saska Kępa, Kamionek, Gocławek, Przyczółek Grochowski",
        "description_body": "Nie trać czasu na szukanie stacjonarnych sklepów po prawej stronie Wisły. Technik Akumulateo przyjedzie na Gocław, Grochów lub Saską Kępę w 15–25 minut i wymieni akumulator na miejscu."
    }
]

def generate_district_html(d):
    schema = {
        "@context": "https://schema.org",
        "@type": "EmergencyService",
        "name": f"Akumulateo – Pogotowie Akumulatorowe Warszawa {d['name']}",
        "url": f"https://www.akumulateo.pl/{d['url_slug']}",
        "telephone": "+48696556446",
        "priceRange": "$$",
        "image": "https://images.squarespace-cdn.com/content/v1/685d174157b18362d5b7b0f3/7c219de6-f0cf-4151-a1a4-eac82a1de5d2/akumulateo-hero-pagespeed.jpg",
        "areaServed": {
            "@type": "AdministrativeArea",
            "name": f"{d['name']}, Warszawa"
        },
        "description": d["desc"],
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00",
            "closes": "23:59"
        }
    }

    schema_str = json.dumps(schema, ensure_ascii=False, indent=2)

    return f"""<!-- ========================================================
     AKUMULATEO - PODSTRONA DZIELNICOWA: {d['name'].upper()}
     URL Slug w Squarespace: /{d['url_slug']}
     Meta Title: {d['title']}
     Meta Description: {d['desc']}
     ======================================================== -->

<!-- 1. Schema.org JSON-LD (Wklej w: Page Settings -> Advanced -> Page Header Code Injection) -->
<script type="application/ld+json">
{schema_str}
</script>

<!-- 2. Treść sekcji (Wklej jako Code Block na nowej podstronie w Squarespace) -->
<div class="akumulateo-district-landing" style="max-width:900px; margin:0 auto; padding:20px; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif; color:#1e293b;">
  
  <div style="background:#0f172a; color:#fff; border-radius:12px; padding:30px; margin-bottom:24px; text-align:center;">
    <span style="background:#f59e0b; color:#000; font-weight:800; font-size:12px; padding:4px 10px; border-radius:12px; text-transform:uppercase;">Dojazd w {d['eta']}</span>
    <h1 style="color:#fff; font-size:28px; margin:14px 0 10px 0;">{d['h1']}</h1>
    <p style="color:#cbd5e1; font-size:16px; max-width:650px; margin:0 auto 20px auto;">
      {d['description_body']}
    </p>
    <a href="tel:+48696556446" style="display:inline-flex; align-items:center; gap:10px; background:#f59e0b; color:#000; font-weight:800; font-size:18px; padding:14px 28px; border-radius:8px; text-decoration:none;">
      📞 Zadzwoń: 696 556 446
    </a>
  </div>

  <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:24px; margin-bottom:24px;">
    <h2 style="font-size:20px; margin-top:0; color:#0f172a;">Rejony obsługi: {d['name']}</h2>
    <p style="color:#475569; font-size:15px; line-height:1.5;">
      Dojeżdżamy pod domy, biura i garaże podziemne w rejonach: <strong>{d['areas']}</strong>.
    </p>
    <ul style="color:#334155; line-height:1.8; font-size:14px;">
      <li>⚡ <strong>Awaryjne uruchamianie auta</strong> – bezpieczny rozruch boosterem 12V/24V bez ryzyka spalenia elektroniki.</li>
      <li>🔋 <strong>Dobór i montaż nowego akumulatora</strong> – markowe akumulatory AGM, EFB i standardowe na miejscu u klienta.</li>
      <li>💻 <strong>Kodowanie BMS i kasowanie błędów</strong> – adaptacja nowego akumulatora w systemie Start-Stop.</li>
      <li>💳 <strong>Płatność kartą lub BLIKiem u technika</strong> – każdy mobilny serwisant posiada terminal płatniczy.</li>
      <li>♻️ <strong>Bezpłatny odbiór zużytego akumulatora</strong> – brak ustawowej kaucji depozytowej.</li>
    </ul>
  </div>

  <div style="text-align:center; padding:15px; background:#fffbeb; border:1px solid #fde68a; border-radius:8px;">
    <strong style="color:#92400e;">⚠️ Ważna informacja:</strong>
    <span style="color:#b45309; font-size:14px;"> Usługa wyłącznie z dojazdem. Nie prowadzimy sklepu stacjonarnego na terenie dzielnicy {d['name']}. Technik przyjeżdża z akumulatorem pod Twój samochód.</span>
  </div>

</div>
"""

def main():
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "seo", "generated-pages")
    os.makedirs(out_dir, exist_ok=True)

    for d in DISTRICTS:
        html = generate_district_html(d)
        file_path = os.path.join(out_dir, f"{d['url_slug']}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ Wygenerowano podstronę dla: {d['name']} -> {file_path}")

if __name__ == "__main__":
    main()
