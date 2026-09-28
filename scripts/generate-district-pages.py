#!/usr/bin/env python3
"""
Generator kompletnych podstron SEO dla wszystkich 18 dzielnic Warszawy (Squarespace 7.1).
Wdraża standard Brandbook v2.2:
- Kontrastowy Dark Mode (#020617 / #0f172a)
- Zero mikrofontów (min. 15.5px/16.5px, line-height 1.65)
- Czas dojazdu: 20-30 min
- Prekwalifikacja mobilna (Brak sklepu stacjonarnego)
- Oficjalne marki: Varta, Yuasa (YUASA), Bosch, 4Max (zero Centra/Banner)
- Ustrukturyzowane dane Schema.org EmergencyService JSON-LD
"""

import os
import json

WARSAW_DISTRICTS = [
    {
        "slug": "mokotow",
        "url_slug": "wymiana-akumulatora-warszawa-mokotow",
        "name": "Mokotów",
        "eta": "20-30 min",
        "title": "Wymiana Akumulatora z Dojazdem Warszawa Mokotów 24/7 | Akumulateo",
        "desc": "Padł akumulator na Mokotowie? Całodobowa wymiana z dojazdem w 20-30 min (Mordor, Służew, Stegny, Sadyba). Dobór, montaż, kodowanie BMS. Zadzwoń: 696 556 446!",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Mokotów 24/7",
        "areas": "Służewiec / Mordor (Domaniewska, Wołoska), Sadyba, Stegny, Służew nad Dolinką, Wierzbno, Ksawerów, Sielce, Czerniaków",
        "description_body": "Rozładowany akumulator na Mokotowie? Dojedziemy pod Twój blok, dom jednorodzinny, biurowiec przy Domaniewskiej lub zjedziemy do ciasnego garażu podziemnego w 20–30 minut. Sprawdzimy stan baterii i instalacji testerem obciążeniowym, zamontujemy fabrycznie nowy akumulator AGM/EFB i zakodujemy go w komputerze auta."
    },
    {
        "slug": "ursynow",
        "url_slug": "wymiana-akumulatora-warszawa-ursynow",
        "name": "Ursynów",
        "eta": "20-30 min",
        "title": "Wymiana Akumulatora z Dojazdem Warszawa Ursynów 24h | Akumulateo",
        "desc": "Mobilny serwis akumulatorów na Ursynowie (Kabaty, Imielin, Stokłosy, Natolin). Awaryjny rozruch i wymiana akumulatora z dojazdem 24/7. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Ursynów 24/7",
        "areas": "Kabaty, Imielin, Stokłosy, Natolin, Dąbrówka, Grabów, Pyry, hale garażowe wzdłuż al. KEN i ul. Rosoła",
        "description_body": "Rozładowany akumulator na Ursynowie? Dojedziemy pod Twój blok, dom jednorodzinny lub do garażu podziemnego w 20–30 minut. Sprawdzimy stan starej baterii testerem cyfrowym, a gdy to konieczne – zamontujemy fabrycznie nowy akumulator AGM lub kwasowy i zakodujemy go w komputerze auta."
    },
    {
        "slug": "wola",
        "url_slug": "wymiana-akumulatora-warszawa-wola",
        "name": "Wola",
        "eta": "20-30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Wola 24/7 | Rozruch i Wymiana",
        "desc": "Rozładowany akumulator na Woli (Odolany, Koło, Mirów, Czyste)? Przyjedziemy w 20-30 minut. Awaryjny rozruch boosterem i montaż akumulatora 24h. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Wola 24h/7",
        "areas": "Odolany (Jana Kazimierza, Ordona), Koło, Czyste, Mirów, Młynów, Ulrychów, Rondo Daszyńskiego, Kasprzaka",
        "description_body": "Błyskawiczna pomoc z akumulatorem na warszawskiej Woli. Obsługujemy zarówno nowe osiedla na Odolanach, jak i biurowce w centrum biznesowym przy Rondzie Daszyńskiego. Wjeżdżamy do podziemnych hal garażowych, montujemy akumulator z podtrzymaniem pamięci OBD."
    },
    {
        "slug": "srodmiescie",
        "url_slug": "wymiana-akumulatora-warszawa-srodmiescie",
        "name": "Śródmieście",
        "eta": "20-30 min",
        "title": "Awaryjne Odpalanie i Wymiana Akumulatora Śródmieście 24h | Akumulateo",
        "desc": "Śródmieście Warszawa: pogotowie akumulatorowe 24/7. Wjazd do stref i garaży podziemnych. Diagnostyka, montaż i kodowanie akumulatora. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Śródmieście 24/7",
        "areas": "Muranów, Powiśle, Solec, Ujazdów, Stare Miasto, Centrum, Plac Zbawiciela, Dworzec Centralny",
        "description_body": "Pomoc z akumulatorem w ścisłym centrum Warszawy. Znamy specyfikę stref płatnego parkowania, ograniczonego ruchu i ciasnych parkingów. Przyjeżdżamy z boosterem 12V/24V i nową baterią pod wskazany adres o każdej porze dnia i nocy."
    },
    {
        "slug": "bielany",
        "url_slug": "wymiana-akumulatora-warszawa-bielany",
        "name": "Bielany",
        "eta": "20-30 min",
        "title": "Pogotowie Akumulatorowe Bielany 24/7 | Wymiana Akumulatora z Dojazdem",
        "desc": "Pomoc z akumulatorem Warszawa Bielany: Chomiczówka, Wrzeciono, Młociny, Słodowiec. Sprawdzenie prądu i nowy akumulator u klienta. Zadzwoń: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Bielany 24h",
        "areas": "Chomiczówka, Wrzeciono, Młociny, Wawrzyszew, Słodowiec, Stare Bielany, trasa S7 / Wisłostrada",
        "description_body": "Całodobowy mobilny serwis akumulatorów na Bielanach. Dowozimy akumulatory do aut osobowych, dostawczych i hybryd. Zabieramy zużytą baterię do utylizacji, zdejmując z Ciebie konieczność płacenia kaucji 30 zł."
    },
    {
        "slug": "praga-poludnie",
        "url_slug": "wymiana-akumulatora-warszawa-praga-poludnie",
        "name": "Praga-Południe",
        "eta": "20-30 min",
        "title": "Wymiana Akumulatora z Dojazdem Praga-Południe (Gocław, Grochów, Saska Kępa)",
        "desc": "Pogotowie akumulatorowe Praga-Południe: Grochów, Saska Kępa, Gocław. Dojazd w 20-30 min, diagnostyka ładowania i wymiana na miejscu 24h. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Praga-Południe 24/7",
        "areas": "Gocław, Grochów, Saska Kępa, Kamionek, Gocławek, Przyczółek Grochowski, ul. Bora-Komorowskiego",
        "description_body": "Nie trać czasu na szukanie stacjonarnych sklepów po prawej stronie Wisły. Technik Akumulateo przyjedzie na Gocław, Grochów lub Saską Kępę w 20–30 minut i wymieni akumulator na miejscu, kodując nowy sterownik Start-Stop."
    },
    {
        "slug": "praga-polnoc",
        "url_slug": "wymiana-akumulatora-warszawa-praga-polnoc",
        "name": "Praga-Północ",
        "eta": "20-30 min",
        "title": "Wymiana Akumulatora Warszawa Praga-Północ 24h | Akumulateo",
        "desc": "Pogotowie akumulatorowe Praga-Północ: Szmulowizna, Nowa Praga, Plac Hallera. Dojazd 20-30 min, test ładowania i wymiana 24h. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Praga-Północ 24/7",
        "areas": "Szmulowizna, Nowa Praga, Stara Praga, Plac Hallera, ul. Jagiellońska, ul. Targowa, Dworzec Wileński",
        "description_body": "Znamy specyfikę praskich kamienic, ciasnych podwórek i parkingów. Przyjeżdżamy ze specjalistycznym sprzętem rozruchowym i nowym akumulatorem pod Twój adres na Pradze-Północ o każdej porze."
    },
    {
        "slug": "bemowo",
        "url_slug": "wymiana-akumulatora-warszawa-bemowo",
        "name": "Bemowo",
        "eta": "20-30 min",
        "title": "Wymiana Akumulatora z Dojazdem Warszawa Bemowo 24h | Akumulateo",
        "desc": "Auto nie odpala na Bemowie? Jelonki, Górce, Chrzanów, Boernerowo. Dojazd z nowym akumulatorem w 20-30 min. Sprawdź cennik: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Bemowo 24/7",
        "areas": "Jelonki Północne i Południowe, Górce, Chrzanów, Boernerowo, Fort Bema, Nowe Bemowo, Powstańców Śląskich",
        "description_body": "Błyskawiczny dojazd na Bemowie pod domy jednorodzinne, nowoczesne osiedla na Chrzanowie oraz parkingi wzdłuż trasy S8. Sprawdzimy prąd ładowania i zamontujemy właściwy akumulator z kodowaniem BMS."
    },
    {
        "slug": "bialoleka",
        "url_slug": "wymiana-akumulatora-warszawa-bialoleka",
        "name": "Białołęka",
        "eta": "20-30 min",
        "title": "Pogotowie Akumulatorowe Białołęka 24h | Dojazd z Akumulatorem Tarchomin",
        "desc": "Pogotowie akumulatorowe Białołęka (Tarchomin, Nowodwory, Derby, Brzeziny). Rozruch auta boosterem i montaż akumulatora 24/7. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Białołęka 24h",
        "areas": "Tarchomin, Nowodwory, Żerań, Osiedle Derby, Grodzisk, Modlińska, Brzeziny, Płochocińska",
        "description_body": "Dojazd na całą Białołękę. Wymiana akumulatora bez stania w korkach na Modlińskiej i szukania warsztatów. Technik przyjeżdża z fabrycznie nową baterią pod Twoje drzwi lub na parking osiedlowy."
    },
    {
        "slug": "targowek",
        "url_slug": "wymiana-akumulatora-warszawa-targowek",
        "name": "Targówek",
        "eta": "20-30 min",
        "title": "Pogotowie Akumulatorowe Targówek 24h | Bródno, Zacisze – Dojazd",
        "desc": "Wymiana akumulatora Targówek (Bródno, Zacisze, Targówek Mieszkaniowy/Fabryczny). Mobilny serwis z dojazdem i kodowaniem 24/7. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Targówek 24h",
        "areas": "Bródno, Zacisze, Targówek Mieszkaniowy, Targówek Fabryczny, Elsnerów, Kondratowicza, Radzymińska",
        "description_body": "Całodobowy dojazd na Bródno i Zacisze. Awaryjny rozruch samochodów osobowych, hybrydowych i dostawczych. Szybki montaż akumulatora pod blokiem bez konieczności holowania auta."
    },
    {
        "slug": "ochota",
        "url_slug": "wymiana-akumulatora-warszawa-ochota",
        "name": "Ochota",
        "eta": "20-30 min",
        "title": "Wymiana Akumulatora Ochota 24h | Dojazd, Diagnostyka i Kodowanie",
        "desc": "Ochota (Szczęśliwice, Rakowiec, Stara Ochota): natychmiastowa pomoc z rozładowanym akumulatorem. Dojazd w 20-30 min, test ładowania. Zadzwoń: 696 556 446!",
        "h1": "Pogotowie Akumulatorowe Warszawa Ochota 24/7",
        "areas": "Szczęśliwice, Rakowiec, Stara Ochota, Filtry, Plac Narutowicza, Grójecka, Al. Jerozolimskie",
        "description_body": "Obsługa rejonu Szczęśliwic, Rakowca i Starej Ochoty. Dojazd w 20–30 minut z pełnym asortymentem akumulatorów AGM, EFB i standardowych. Wymiana na miejscu bez utraty ustawień komputera i radia."
    },
    {
        "slug": "wawer",
        "url_slug": "wymiana-akumulatora-warszawa-wawer",
        "name": "Wawer",
        "eta": "20-30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Wawer 24h | Wymiana z Dojazdem",
        "desc": "Auto nie odpala w Wawrze? Międzylesie, Falenica, Radość, Anin. Dojazd 24/7 z nowym akumulatorem pod Twój dom. Zadzwoń: 696 556 446!",
        "h1": "Pogotowie Akumulatorowe Warszawa Wawer 24h/7",
        "areas": "Międzylesie, Falenica, Radość, Anin, Marysin Wawerski, Zerzeń, Nadwiśle, Wał Miedzeszyński, Patriotów",
        "description_body": "Obsługujemy całą dzielnicę Wawer – dojeżdżamy na prywatne posesje, osiedla domów jednorodzinnych i parkingi wzdłuż Wału Miedzeszyńskiego. Pełna diagnostyka alternatora i dowóz akumulatora 24h."
    },
    {
        "slug": "ursus",
        "url_slug": "wymiana-akumulatora-warszawa-ursus",
        "name": "Ursus",
        "eta": "20-30 min",
        "title": "Wymiana Akumulatora Warszawa Ursus 24h | Rozruch i Kodowanie BMS",
        "desc": "Rozładowany akumulator w Ursusie? Skorosze, Szamoty, Niedźwiadek. Przyjedziemy w 20-30 minut z fabrycznie nową baterią. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Ursus 24/7",
        "areas": "Skorosze, Szamoty, Niedźwiadek, Gołąbki, Czechowice, Al. 4 Czerwca 1989 r., Traktorzystów",
        "description_body": "Błyskawiczna pomoc na nowych osiedlach na Szamotach i Skoroszach. Wjeżdżamy do podziemnych hal garażowych, montujemy akumulatory AGM i kodujemy w systemie auta. Zero stresu z holowaniem."
    },
    {
        "slug": "wilanow",
        "url_slug": "wymiana-akumulatora-warszawa-wilanow",
        "name": "Wilanów",
        "eta": "20-30 min",
        "title": "Wymiana Akumulatora Miasteczko Wilanów 24h | Kodowanie AGM Akumulateo",
        "desc": "Pogotowie akumulatorowe Miasteczko Wilanów, Zawady, Powsinek. Akumulatory AGM/EFB z montażem i kodowaniem w garażach podziemnych 24/7. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Wilanów 24/7",
        "areas": "Miasteczko Wilanów, Zawady, Powsinek, Kępa Zawadowska, Wilanów Wysoki, Klimczaka, Rzeczypospolitej",
        "description_body": "Specjalizujemy się w nowoczesnych autach z systemem Start-Stop wymagających kodowania BMS w Miasteczku Wilanów i na Zawadach. Wjeżdżamy do podziemnych hal garażowych, montujemy akumulatory Varta i Yuasa."
    },
    {
        "slug": "wlochy",
        "url_slug": "wymiana-akumulatora-warszawa-wlochy",
        "name": "Włochy",
        "eta": "20-30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Włochy 24h | Okęcie, Dojazd 24/7",
        "desc": "Padł akumulator we Włochach lub w okolicach Okęcia? Szybka wymiana z dojazdem, awaryjne odpalanie boosterem 12V/24V. Zadzwoń: 696 556 446!",
        "h1": "Pogotowie Akumulatorowe Warszawa Włochy 24h",
        "areas": "Okęcie, Lotnisko Chopina (parkingi), Salomea, Raków, Opacz Wielka, Al. Krakowska, Hynka, Łopuszańska",
        "description_body": "Dojazd pod biurowce przy Łopuszańskiej, osiedla we Włochach oraz parkingi wokół Okęcia. Pełna diagnostyka komputerowa na miejscu zdarzenia – uruchamiamy auto lub montujemy nowy akumulator."
    },
    {
        "slug": "rembertow",
        "url_slug": "wymiana-akumulatora-warszawa-rembertow",
        "name": "Rembertów",
        "eta": "20-30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Rembertów 24h | Dojazd z Baterią",
        "desc": "Awaria akumulatora w Rembertowie? Nowy i Stary Rembertów, Wygoda, Kawęczyn. Dojazd 20-30 min, profesjonalny montaż i kodowanie. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Rembertów 24h",
        "areas": "Stary Rembertów, Nowy Rembertów, Kawęczyn, Wygoda, ul. Żołnierska, ul. Cyrulików, ul. Chruściela",
        "description_body": "Całodobowy dojazd do kierowców w Rembertowie. Wymiana akumulatora bez konieczności jazdy do stacjonarnego warsztatu – technik dobiera akumulator OEM, montuje na miejscu i rozlicza kartą/BLIK."
    },
    {
        "slug": "wesola",
        "url_slug": "wymiana-akumulatora-warszawa-wesola",
        "name": "Wesoła",
        "eta": "20-30 min",
        "title": "Wymiana Akumulatora Warszawa Wesoła 24h | Stara Miłosna, Dojazd",
        "desc": "Samochód nie odpala w Wesołej lub Starej Miłosnej? Pogotowie akumulatorowe 24/7. Dowóz nowej baterii, montaż i adaptacja BMS. Zadzwoń: 696 556 446!",
        "h1": "Pogotowie Akumulatorowe Warszawa Wesoła 24h/7",
        "areas": "Stara Miłosna, Wola Grzybowska, Groszówka, Grzybowa, Zielona, Trakt Brzeski",
        "description_body": "Obsługujemy całą Wesołą i Starą Miłosną. Dojeżdżamy na posesje prywatne trasą Trakt Brzeski w 20–30 minut o dowolnej porze dnia i nocy. Nowe akumulatory AGM i kwasowe z gwarancją do 3 lat."
    },
    {
        "slug": "zoliborz",
        "url_slug": "wymiana-akumulatora-warszawa-zoliborz",
        "name": "Żoliborz",
        "eta": "20-30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Żoliborz 24h | Wymiana z Dojazdem",
        "desc": "Rozładowany akumulator na Żoliborzu? Plac Wilsona, Marymont, Sady Żoliborskie. Dojazd w 20-30 min, bezpieczny montaż z podtrzymaniem OBD. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Żoliborz 24/7",
        "areas": "Plac Wilsona, Marymont-Potok, Sady Żoliborskie, Żoliborz Oficerski, Żoliborz Dziennikarski, ul. Krasińskiego, ul. Mickiewicza",
        "description_body": "Szybki dojazd na Żoliborzu – wjeżdżamy na podwórka kamienic, parkingi przy Krasińskiego i Mickiewicza oraz do podziemnych hal garażowych. Bezpieczny montaż z podtrzymaniem pamięci komputera."
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
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "5.0",
            "bestRating": "5.0",
            "worstRating": "1.0",
            "ratingCount": "160",
            "reviewCount": "160"
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
<div class="akumulateo-root bg-slate-950 text-slate-100 font-sans antialiased" style="background:#020617; color:#f8fafc; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif; max-width:960px; margin:0 auto; padding:16px;">
  
  <!-- TOP EMERGENCY BAR -->
  <div style="background:linear-gradient(90deg, #f59e0b 0%, #fbbf24 50%, #f59e0b 100%); color:#020617; padding:8px 16px; border-radius:12px; font-size:12px; font-weight:900; margin-bottom:20px; display:flex; flex-wrap:wrap; align-items:center; justify-content:between; gap:8px;">
    <div style="display:flex; align-items:center; gap:8px;">
      <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#020617;"></span>
      <span style="text-transform:uppercase; letter-spacing:0.5px;">Dyżur Pogotowia 24h/7</span>
      <span>• Dojazd 20–30 min: Warszawa {d['name']}</span>
    </div>
    <div style="font-weight:800;">
      ⭐ 5.0 w Google (160+ opinii)
    </div>
  </div>

  <!-- HERO KARTA GŁÓWNA -->
  <div style="background:linear-gradient(180deg, #0f172a 0%, #020617 100%); border:1px solid #1e293b; border-radius:20px; padding:36px 20px; text-align:center; margin-bottom:20px;">
    <span style="display:inline-block; background:rgba(245,158,11,0.15); border:1px solid rgba(245,158,11,0.35); color:#fbbf24; font-weight:900; font-size:12px; padding:6px 16px; border-radius:9999px; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:16px;">
      ⚡ Pogotowie Akumulatorowe Warszawa {d['name']} 24h
    </span>
    
    <h1 style="color:#ffffff; font-size:30px; font-weight:900; line-height:1.2; margin:0 0 16px 0; letter-spacing:-0.5px;">
      {d['h1']}
    </h1>
    
    <p style="color:#cbd5e1; font-size:16.5px; line-height:1.65; max-width:720px; margin:0 auto 24px auto;">
      {d['description_body']}
    </p>
    
    <div style="display:flex; flex-direction:column; gap:12px; align-items:center; justify-content:center;">
      <a href="tel:+48696556446" style="display:inline-flex; align-items:center; justify-content:center; gap:10px; background:linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color:#020617; font-weight:900; font-size:18px; padding:16px 32px; border-radius:14px; text-decoration:none; box-shadow:0 8px 25px -5px rgba(245,158,11,0.4); width:100%; max-width:380px;">
        <span style="font-size:22px;">📞</span>
        <span>Zadzwoń: 696 556 446</span>
      </a>
      <div style="font-size:13px; color:#94a3b8; font-weight:700;">
        ⏱️ Czas dojazdu na terenie dzielnicy: <span style="color:#34d399;">20–30 minut</span>
      </div>
    </div>
  </div>

  <!-- BANNER PREKWALIFIKACJI MOBILNEJ -->
  <div style="background:rgba(245,158,11,0.08); border:1px solid rgba(245,158,11,0.3); border-radius:14px; padding:16px 20px; text-align:center; margin-bottom:20px;">
    <div style="color:#fbbf24; font-weight:900; font-size:13px; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:4px;">
      ℹ️ Usługa w 100% Mobilna z Dojazdem
    </div>
    <p style="color:#f1f5f9; font-size:15.5px; line-height:1.6; margin:0;">
      Nie trać czasu na szukanie stacjonarnego sklepu ani holowanie auta. Nie prowadzimy punktu odbioru na terenie dzielnicy {d['name']} – <strong>nasz serwisant przyjeżdża pod Twój blok, dom lub do garażu podziemnego</strong> z fabrycznie nową baterią i montuje ją na miejscu.
    </p>
  </div>

  <!-- REJONY OBSŁUGI & USŁUGI -->
  <div style="background:#0f172a; border:1px solid #1e293b; border-radius:18px; padding:28px 24px; margin-bottom:20px;">
    <h2 style="font-size:22px; font-weight:900; color:#ffffff; margin:0 0 12px 0;">
      Obszar interwencji pogotowia: Warszawa {d['name']}
    </h2>
    <p style="color:#cbd5e1; font-size:16px; line-height:1.65; margin:0 0 20px 0;">
      Nasi technicy stacjonują mobilnie na terenie stolicy, obsługując w dzielnicy {d['name']} m.in. rejony: <strong>{d['areas']}</strong>.
    </p>

    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:16px; margin-top:20px;">
      <div style="background:#020617; border:1px solid #1e293b; border-radius:14px; padding:18px;">
        <div style="font-size:20px; margin-bottom:8px;">⚡</div>
        <div style="color:#ffffff; font-weight:800; font-size:16px; margin-bottom:6px;">Awaryjny Rozruch 12V/24V</div>
        <p style="color:#94a3b8; font-size:14.5px; line-height:1.6; margin:0;">
          Bezpieczne odpalenie boosterem mikroprocesorowym bez ryzyka przepięcia w komputerze pojazdu.
        </p>
      </div>

      <div style="background:#020617; border:1px solid #1e293b; border-radius:14px; padding:18px;">
        <div style="font-size:20px; margin-bottom:8px;">🔋</div>
        <div style="color:#ffffff; font-weight:800; font-size:16px; margin-bottom:6px;">Montaż Nowego Akumulatora</div>
        <p style="color:#94a3b8; font-size:14.5px; line-height:1.6; margin:0;">
          Fabryczne akumulatory marek premium: <strong>Varta, Yuasa, Bosch, 4Max</strong>. Gwarancja do 3 lat.
        </p>
      </div>

      <div style="background:#020617; border:1px solid #1e293b; border-radius:14px; padding:18px;">
        <div style="font-size:20px; margin-bottom:8px;">💻</div>
        <div style="color:#ffffff; font-weight:800; font-size:16px; margin-bottom:6px;">Kodowanie BMS & OBD</div>
        <p style="color:#94a3b8; font-size:14.5px; line-height:1.6; margin:0;">
          Podtrzymanie napięcia pamięci sterowników i rejestracja nowej baterii w systemie Start-Stop.
        </p>
      </div>
    </div>
  </div>

  <!-- FAQ DZIELNICOWE -->
  <div style="background:#0f172a; border:1px solid #1e293b; border-radius:18px; padding:28px 24px; margin-bottom:24px;">
    <h3 style="font-size:20px; font-weight:900; color:#ffffff; margin:0 0 16px 0;">
      Najczęstsze pytania kierowców – {d['name']} (FAQ)
    </h3>
    
    <div style="display:flex; flex-direction:column; gap:16px;">
      <div style="border-bottom:1px solid #1e293b; padding-bottom:14px;">
        <div style="color:#fbbf24; font-weight:800; font-size:16px; margin-bottom:6px;">
          Czy wjedziecie do garażu podziemnego o niskim stropie?
        </div>
        <p style="color:#cbd5e1; font-size:15.5px; line-height:1.65; margin:0;">
          Tak. Nasze auta serwisowe oraz przenośne zestawy rozruchowo-diagnostyczne są przystosowane do wjazdu do garaży podziemnych i hal garażowych (poziomy -1, -2, -3) na terenie całej dzielnicy {d['name']}.
        </p>
      </div>

      <div style="border-bottom:1px solid #1e293b; padding-bottom:14px;">
        <div style="color:#fbbf24; font-weight:800; font-size:16px; margin-bottom:6px;">
          Jakie formy płatności przyjmuje serwisant?
        </div>
        <p style="color:#cbd5e1; font-size:15.5px; line-height:1.65; margin:0;">
          Każdy technik Akumulateo posiada terminal płatniczy. Płatności można dokonać kartą zbliżeniową, kodem BLIK lub gotówką. Dla firm wystawiamy fakturę VAT 23% na miejscu.
        </p>
      </div>

      <div>
        <div style="color:#fbbf24; font-weight:800; font-size:16px; margin-bottom:6px;">
          Co dzieje się ze starym, zużytym akumulatorem?
        </div>
        <p style="color:#cbd5e1; font-size:15.5px; line-height:1.65; margin:0;">
          Stary akumulator odbieramy bezpłatnie i przekazujemy do certyfikowanego recyklingu hutniczego zgodnie z przepisami BDO. Dzięki temu nie ponosisz ustawowej kaucji depozytowej (30 zł).
        </p>
      </div>
    </div>
  </div>

  <!-- DOLNY CALL TO ACTION -->
  <div style="text-align:center; padding:20px; background:linear-gradient(145deg, #090e1a 0%, #0f172a 100%); border:1px solid #1e293b; border-radius:18px;">
    <div style="color:#ffffff; font-size:20px; font-weight:900; margin-bottom:8px;">
      Potrzebujesz natychmiastowej pomocy z akumulatorem?
    </div>
    <p style="color:#cbd5e1; font-size:16px; margin:0 0 16px 0;">
      Zadzwoń do dyspozytora pogotowia. Podaj model auta i lokalizację – technik wyrusza natychmiast.
    </p>
    <a href="tel:+48696556446" style="display:inline-flex; align-items:center; justify-content:center; gap:10px; background:linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color:#020617; font-weight:900; font-size:18px; padding:16px 36px; border-radius:14px; text-decoration:none; box-shadow:0 8px 25px -5px rgba(245,158,11,0.4);">
      <span>📞 Zadzwoń: 696 556 446</span>
    </a>
  </div>

</div>
"""

def main():
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src", "seo", "generated-pages")
    os.makedirs(out_dir, exist_ok=True)

    print(f"🚀 Rozpoczynam generowanie {len(WARSAW_DISTRICTS)} podstron dzielnicowych Warszawy...")

    for d in WARSAW_DISTRICTS:
        html = generate_district_html(d)
        file_path = os.path.join(out_dir, f"{d['url_slug']}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  ✅ Wygenerowano podstronę: {d['name']} (/{d['url_slug']}) -> {len(html)} znaków")

    print(f"\n🎉 Pomyślnie wygenerowano komplet {len(WARSAW_DISTRICTS)} podstron w: {out_dir}")

if __name__ == "__main__":
    main()
