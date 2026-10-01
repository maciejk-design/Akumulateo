#!/usr/bin/env python3
"""
Generator kompletnych podstron SEO dla wszystkich 18 dzielnic Warszawy oraz 15 miejscowości aglomeracji (Squarespace 7.1).
Wdraża standard Brandbook v2.2:
- Kontrastowy Dark Mode (#020617 / #0f172a)
- Zero mikrofontów (min. 15.5px/16.5px, line-height 1.65)
- Czas dojazdu: 20-30 min w Warszawie, 20-40 min w aglomeracji
- Prekwalifikacja mobilna (Brak sklepu stacjonarnego)
- Oficjalne marki: Varta, Yuasa (YUASA), Bosch, 4Max (zero Centra/Banner)
- Ustrukturyzowane dane Schema.org EmergencyService JSON-LD (5.0★, 100+ opinii)
- Generuje stronę zbiorczą Hub: /obszar-dzialania-warszawa-i-okolice z kompletną siatką linków wewnętrznych
"""

import os
import json
import re

WARSAW_DISTRICTS = [
    {
        "slug": "mokotow",
        "url_slug": "wymiana-akumulatora-warszawa-mokotow",
        "name": "Mokotów",
        "eta": "20–30 min",
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
        "eta": "20–30 min",
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
        "eta": "20–30 min",
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
        "eta": "20–30 min",
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
        "eta": "20–30 min",
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
        "eta": "20–30 min",
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
        "eta": "20–30 min",
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
        "eta": "20–30 min",
        "title": "Wymiana Akumulatora z Dojazdem Warszawa Bemowo 24h | Akumulateo",
        "desc": "Auto nie odpala na Bemowie? Jelonki, Górce, Chrzanów, Boernerowo. Dojazd z nowym akumulatorem w 20-30 min. Sprawdź cennik: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Bemowo 24h/7",
        "areas": "Jelonki Północne/Południowe, Górce, Chrzanów, Boernerowo, Fort Bema, Lotnisko Babice, trasa S8 / Powstańców Śląskich",
        "description_body": "Szybki dojazd na Bemowie z akumulatorem dopasowanym do Twojego samochodu. Wymieniamy baterie w autach benzynowych, dieslach i nowoczesnych miękkich hybrydach (MHEV)."
    },
    {
        "slug": "bialoleka",
        "url_slug": "wymiana-akumulatora-warszawa-bialoleka",
        "name": "Białołęka",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Białołęka 24/7 | Wymiana Akumulatora",
        "desc": "Pomoc z akumulatorem Białołęka: Tarchomin, Nowodwory, Derby, Brzeziny. Dojazd 20-30 min, profesjonalny montaż i kodowanie. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Białołęka 24/7",
        "areas": "Tarchomin, Nowodwory, Osiedle Derby, Żerań, Brzeziny, Choszczówka, Kępa Tarchomińska, ul. Modlińska",
        "description_body": "Dojedziemy w każdy zakątek Białołęki – od Tarchomina po Zieloną Białołękę. Wymiana akumulatora bez stania w korkach na Modlińskiej lub Moście Północnym."
    },
    {
        "slug": "targowek",
        "url_slug": "wymiana-akumulatora-warszawa-targowek",
        "name": "Targówek",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Targówek 24h | Wymiana Akumulatora z Dojazdem",
        "desc": "Rozładowany akumulator na Targówku? Bródno, Zacisze, Targówek Mieszkaniowy. Dojazd w 20-30 min, diagnostyka i montaż. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Targówek 24h/7",
        "areas": "Bródno, Zacisze, Targówek Mieszkaniowy, Targówek Fabryczny, Elsnerów, ul. Kondratowicza, ul. Radzymińska",
        "description_body": "Całodobowa pomoc akumulatorowa na Targówku. Bezpieczny rozruch boosterem z zabezpieczeniem przeciwzwarciowym oraz montaż nowej baterii z testem ładowania alternatora."
    },
    {
        "slug": "ochota",
        "url_slug": "wymiana-akumulatora-warszawa-ochota",
        "name": "Ochota",
        "eta": "20–30 min",
        "title": "Wymiana Akumulatora Warszawa Ochota 24h | Szczęśliwice, Dojazd",
        "desc": "Mobilny serwis akumulatorów Warszawa Ochota: Szczęśliwice, Rakowiec, Stara Ochota. Przyjedziemy w 20-30 min. Sprawdź: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Ochota 24/7",
        "areas": "Szczęśliwice, Rakowiec, Stara Ochota, Filtry, Park Szczęśliwicki, Al. Jerozolimskie, ul. Grójecka",
        "description_body": "Ekspresowy dojazd w rejonie Ochoty. Wjeżdżamy na wąskie osiedlowe uliczki i do garaży podziemnych przy Grójeckiej i Włodarzewskiej. Płatność kartą i BLIK na miejscu."
    },
    {
        "slug": "wawer",
        "url_slug": "wymiana-akumulatora-warszawa-wawer",
        "name": "Wawer",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Wawer 24h | Dojazd z Akumulatorem",
        "desc": "Wawer, Falenica, Radość, Międzylesie, Anin: mobilne pogotowie akumulatorowe 24/7. Nowe baterie AGM i kwasowe z montażem pod domem. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Wawer 24h/7",
        "areas": "Międzylesie, Falenica, Radość, Anin, Marysin Wawerski, Zerzeń, Nadwiśle, Wał Miedzeszyński, ul. Patriotów",
        "description_body": "Obsługujemy całą dzielnicę Wawer – od Marysina po Falenicę. Dojeżdżamy na prywatne posesje, sprawdzamy upływ prądu na postoju i montujemy nową baterię bez utraty ustawień auta."
    },
    {
        "slug": "ursus",
        "url_slug": "wymiana-akumulatora-warszawa-ursus",
        "name": "Ursus",
        "eta": "20–30 min",
        "title": "Wymiana Akumulatora Warszawa Ursus 24h | Skorosze, Szamoty, Dojazd",
        "desc": "Awaria akumulatora w Ursusie? Skorosze, Szamoty, Niedźwiadek. Całodobowy dojazd w 20-30 min, profesjonalny montaż i kodowanie. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Ursus 24/7",
        "areas": "Skorosze, Szamoty, Niedźwiadek, Gołąbki, Czechowice, Al. 4 Czerwca 1989 r., ul. Dzieci Warszawy",
        "description_body": "Pomoc dla kierowców na Ursusie. Szybki dojazd na nowe osiedla na Szamotach i Skoroszach. Wjeżdżamy do podziemnych hal garażowych ze specjalnym zestawem diagnostycznym."
    },
    {
        "slug": "wilanow",
        "url_slug": "wymiana-akumulatora-warszawa-wilanow",
        "name": "Wilanów",
        "eta": "20–30 min",
        "title": "Wymiana Akumulatora Warszawa Wilanów 24h | Miasteczko Wilanów",
        "desc": "Miasteczko Wilanów, Zawady, Powsinek: pogotowie akumulatorowe 24/7. Wymiana akumulatorów AGM/EFB z kodowaniem BMS w garażach podziemnych. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Warszawa Wilanów 24/7",
        "areas": "Miasteczko Wilanów, Wilanów Królewski, Zawady, Kępa Zawadowska, Powsinek, Powsin, ul. Klimczaka, Al. Rzeczypospolitej",
        "description_body": "Specjalizujemy się w nowoczesnych samochodach z systemem Start-Stop, rekuperacją i zaawansowanym zarządzaniem energią BMS. Wjeżdżamy do garaży na Miasteczku Wilanów i kodujemy akumulatory."
    },
    {
        "slug": "wlochy",
        "url_slug": "wymiana-akumulatora-warszawa-wlochy",
        "name": "Włochy",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Włochy 24h | Okęcie, Dojazd 24/7",
        "desc": "Padł akumulator we Włochach lub w rejonie Okęcia? Dojedziemy w 20-30 minut pod dom, firmę lub parking lotniskowy. Zadzwoń: 696 556 446!",
        "h1": "Pogotowie Akumulatorowe Warszawa Włochy 24h/7",
        "areas": "Okęcie, Nowe Włochy, Stare Włochy, Salomea, Raków, Opacz Wielka, Al. Krakowska, ul. Łopuszańska",
        "description_body": "Całodobowa pomoc w dzielnicy Włochy oraz w okolicach Lotniska Chopina. Dojeżdżamy na parkingi długoterminowe, strefy biurowe i osiedla mieszkaniowe w 20–30 minut."
    },
    {
        "slug": "rembertow",
        "url_slug": "wymiana-akumulatora-warszawa-rembertow",
        "name": "Rembertów",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Rembertów 24h | Wymiana pod Domem",
        "desc": "Pomoc akumulatorowa Rembertów (Nowy i Stary Rembertów, Kawęczyn). Dojazd w 20-30 min, test instalacji i wymiana nowej baterii 24h. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Rembertów 24h/7",
        "areas": "Stary Rembertów, Nowy Rembertów, Kawęczyn, Wygoda, ul. Żołnierska, ul. Cyrulików, ul. Chruściela",
        "description_body": "Całodobowy dojazd do kierowców w Rembertowie. Wymiana akumulatora bez konieczności jazdy do stacjonarnego warsztatu – technik dobiera akumulator OEM, montuje na miejscu i rozlicza kartą/BLIK."
    },
    {
        "slug": "wesola",
        "url_slug": "wymiana-akumulatora-warszawa-wesola",
        "name": "Wesoła",
        "eta": "20–30 min",
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
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Warszawa Żoliborz 24h | Wymiana z Dojazdem",
        "desc": "Rozładowany akumulator na Żoliborzu? Plac Wilsona, Marymont, Sady Żoliborskie. Dojazd w 20-30 min, bezpieczny montaż z podtrzymaniem OBD. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Warszawa Żoliborz 24/7",
        "areas": "Plac Wilsona, Marymont-Potok, Sady Żoliborskie, Żoliborz Oficerski, Żoliborz Dziennikarski, ul. Krasińskiego, ul. Mickiewicza",
        "description_body": "Szybki dojazd na Żoliborzu – wjeżdżamy na podwórka kamienic, parkingi przy Krasińskiego i Mickiewicza oraz do podziemnych hal garażowych. Bezpieczny montaż z podtrzymaniem pamięci komputera."
    }
]

AGGLOMERATION_SUBURBS = [
    {
        "slug": "piaseczno",
        "url_slug": "wymiana-akumulatora-piaseczno",
        "name": "Piaseczno",
        "eta": "20–30 min",
        "title": "Wymiana Akumulatora z Dojazdem Piaseczno 24/7 | Pogotowie Akumulateo",
        "desc": "Padł akumulator w Piasecznie, Józefosławiu lub Lesznowoli? Całodobowe pogotowie akumulatorowe 24/7. Wymiana z dojazdem pod dom w 20-30 min, diagnostyka i kodowanie BMS. Tel: 696 556 446!",
        "h1": "Wymiana Akumulatora z Dojazdem Piaseczno i Okolice 24/7",
        "areas": "Piaseczno Centrum, Józefosław, Julianów, Lesznowola, Nowa Iwiczna, Gołków, Zalesie Dolne, Chyliczki",
        "description_body": "Awaria akumulatora w Piasecznie lub okolicznych miejscowościach? Dojeżdżamy pod domy prywatne, osiedla i do garaży podziemnych w 20–30 minut. Sprawdzamy stan starej baterii, dobieramy fabrycznie nowy akumulator AGM/EFB i kodujemy go w komputerze auta."
    },
    {
        "slug": "pruszkow",
        "url_slug": "wymiana-akumulatora-pruszkow",
        "name": "Pruszków",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Pruszków 24h | Wymiana Akumulatora z Dojazdem",
        "desc": "Samochód nie odpala w Pruszkowie (Gąsin, Żbików, Ostoja)? Mobilny serwis akumulatorów 24/7. Dojazd w 20-30 min, montaż z kodowaniem BMS. Zadzwoń: 696 556 446!",
        "h1": "Pogotowie Akumulatorowe Pruszków 24h/7 – Wymiana z Dojazdem",
        "areas": "Pruszków Centrum, Gąsin, Żbików, Ostoja, Tworki, Malichy, Bąki, trasa A2 / Al. Jerozolimskie",
        "description_body": "Szybki dojazd autostradą A2 oraz Alejami Jerozolimskimi do Pruszkowa. Nie musisz holować auta do warsztatu – technik Akumulateo przyjeżdża bezpośrednio pod wskazany adres, wykonuje test ładowania i montuje nową baterię na miejscu."
    },
    {
        "slug": "piastow",
        "url_slug": "wymiana-akumulatora-piastow",
        "name": "Piastów",
        "eta": "20–30 min",
        "title": "Wymiana Akumulatora z Dojazdem Piastów 24h | Pogotowie Akumulateo",
        "desc": "Rozładowany akumulator w Piastowie? Dojazd w 20-30 min z nową baterią Varta, Yuasa lub Bosch. Montaż, adaptacja BMS i darmowy recykling starej baterii. Tel: 696 556 446.",
        "h1": "Wymiana Akumulatora z Dojazdem Piastów 24/7",
        "areas": "Piastów Północ, Piastów Południe, Osiedle Ogińskiego, Al. Tysiąclecia, Al. Jerozolimskie",
        "description_body": "Błyskawiczny dojazd Alejami Jerozolimskimi prosto do Piastowa w 20–30 minut. Obsługujemy domy jednorodzinne, parkingi osiedlowe i firmy. Podtrzymujemy pamięć komputera przy wymianie baterii."
    },
    {
        "slug": "brwinow",
        "url_slug": "wymiana-akumulatora-brwinow",
        "name": "Brwinów",
        "eta": "25–35 min",
        "title": "Wymiana Akumulatora z Dojazdem Brwinów 24h | Pogotowie Akumulateo",
        "desc": "Awaria akumulatora w Brwinowie, Otrębusach lub Żółwinie? Mobilny serwis akumulatorów 24/7. Wymiana na posesji klienta w 25-35 min. Zadzwoń: 696 556 446!",
        "h1": "Pogotowie Akumulatorowe Brwinów i Okolice 24h",
        "areas": "Brwinów Centrum, Otrębusy, Żółwin, Owczarnia, Kotowice, Biskupice, Kanie",
        "description_body": "Szybki dojazd drogą 719 oraz autostradą A2 do Brwinowa i okolicznych miejscowości. Pełna diagnostyka instalacji, podtrzymanie pamięci sterowników i montaż markowego akumulatora na prywatnej posesji."
    },
    {
        "slug": "milanowek",
        "url_slug": "wymiana-akumulatora-milanowek",
        "name": "Milanówek",
        "eta": "25–35 min",
        "title": "Pogotowie Akumulatorowe Milanówek 24h | Wymiana Akumulatora z Dojazdem",
        "desc": "Samochód nie odpala w Milanówku lub Podkowie Leśnej? Całodobowy mobilny serwis akumulatorów z dojazdem. Markowe baterie Varta, Yuasa, Bosch. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Milanówek 24/7 – Wymiana z Dojazdem",
        "areas": "Milanówek Centrum, Grudów, Turczynek, Kazimierówka, Podkowa Leśna, Owczarnia",
        "description_body": "Dojazd do Milanówka autostradą A2 lub trasą 719. Wjeżdżamy na prywatne posesje, montujemy akumulatory AGM/EFB i kodujemy je w komputerze pokładowym pojazdu."
    },
    {
        "slug": "legionowo",
        "url_slug": "wymiana-akumulatora-legionowo",
        "name": "Legionowo",
        "eta": "25–35 min",
        "title": "Pogotowie Akumulatorowe Legionowo 24h | Wymiana Akumulatora z Dojazdem",
        "desc": "Rozładowany akumulator w Legionowie, Jabłonnie lub Wieliszewie? Całodobowe pogotowie akumulatorowe 24/7. Dojazd w 25-35 min, montaż i kodowanie BMS. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Legionowo 24h/7",
        "areas": "Legionowo Centrum, Jabłonna, Piaski, Osiedle Sobieskiego, Bukowiec, Wieliszew, Chotomów",
        "description_body": "Ekspresowy dojazd drogą DK61 z Warszawy prosto do Legionowa i Jabłonny. Pełna diagnostyka akumulatora i alternatora na miejscu, bez konieczności wizyty w warsztacie."
    },
    {
        "slug": "modlin",
        "url_slug": "wymiana-akumulatora-modlin",
        "name": "Modlin i Nowy Dwór Mazowiecki",
        "eta": "35–50 min",
        "title": "Pogotowie Akumulatorowe Lotnisko Modlin, Nowy Dwór Maz. 24h | Rozruch i Wymiana",
        "desc": "Rozładowany akumulator na parkingu przy Lotnisku Modlin lub w Nowym Dworze Mazowieckim? Całodobowa pomoc, awaryjny rozruch boosterem i montaż nowej baterii. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Lotnisko Modlin i Nowy Dwór Maz. 24h",
        "areas": "Parkingi długoterminowe Lotniska Modlin P1-P7, Twierdza Modlin, Nowy Dwór Mazowiecki Centrum, Czosnów, Zakroczym",
        "description_body": "Specjalny dyżur ratunkowy z dojazdem trasą S7 na parkingi wokół Lotniska Warszawa-Modlin oraz do Nowego Dworu Mazowieckiego. Ratunek dla kierowców powracających z podróży, których auto odmówiło posłuszeństwa po postoju."
    },
    {
        "slug": "nowy-dwor-mazowiecki",
        "url_slug": "wymiana-akumulatora-nowy-dwor-mazowiecki",
        "name": "Nowy Dwór Mazowiecki",
        "eta": "35–50 min",
        "title": "Wymiana Akumulatora Nowy Dwór Mazowiecki 24h | Pogotowie z Dojazdem",
        "desc": "Padł akumulator w Nowym Dworze Mazowieckim? Całodobowa pomoc akumulatorowa, awaryjny rozruch boosterem i montaż nowej baterii pod domem. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Nowy Dwór Mazowiecki 24h/7",
        "areas": "Nowy Dwór Centrum, Osiedle Młodych, Twierdza Modlin, Czosnów, Kazuń Nowy, Pomiechówek",
        "description_body": "Ekspresowy dojazd trasą S7 do Nowego Dworu Mazowieckiego. Nowe akumulatory Varta, Yuasa, Bosch montowane bezpośrednio pod domem klienta lub na parkingu firmowym."
    },
    {
        "slug": "minsk-mazowiecki",
        "url_slug": "wymiana-akumulatora-minsk-mazowiecki",
        "name": "Mińsk Mazowiecki",
        "eta": "35–50 min",
        "title": "Wymiana Akumulatora Mińsk Mazowiecki 24h | Pogotowie Akumulateo",
        "desc": "Pogotowie akumulatorowe Mińsk Mazowiecki, Halinów, Sulejówek. Wymiana akumulatora pod domem z kodowaniem BMS 24/7. Zadzwoń: 696 556 446!",
        "h1": "Pogotowie Akumulatorowe Mińsk Mazowiecki 24h/7",
        "areas": "Mińsk Mazowiecki Centrum, Halinów, Sulejówek, Dębe Wielkie, Stojadła, Kałuszyn",
        "description_body": "Dojazd autostradą A2 do Mińska Mazowieckiego, Halinowa i Sulejówka. Kompleksowa wymiana z podtrzymaniem pamięci OBD, dobór akumulatora wg katalogu OEM i gwarancja producenta do 3 lat."
    },
    {
        "slug": "konstancin-jeziorna",
        "url_slug": "wymiana-akumulatora-konstancin-jeziorna",
        "name": "Konstancin-Jeziorna",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Konstancin-Jeziorna 24h | Dojazd z Akumulatorem",
        "desc": "Konstancin-Jeziorna, Bielawa, Skolimów: mobilny serwis akumulatorów 24/7. Dojazd pod posesję w 20-30 min, wymiana baterii AGM i kodowanie BMS. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Konstancin-Jeziorna 24/7",
        "areas": "Konstancin Centrum, Skolimów, Bielawa, Klarysew, Chylice, Obory, Jeziorna, Borowina",
        "description_body": "Błyskawiczny dojazd od strony Wilanowa i Ursynowa do Konstancina-Jeziornej w 20–30 minut. Dojeżdżamy na prywatne posesje i do rezydencji o każdej porze. Bezpieczny montaż akumulatorów AGM w autach marek premium."
    },
    {
        "slug": "lomianki",
        "url_slug": "wymiana-akumulatora-lomianki",
        "name": "Łomianki",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Łomianki 24h | Wymiana Akumulatora z Dojazdem",
        "desc": "Rozładowany akumulator w Łomiankach, Dziekanowie lub Kiełpinie? Pogotowie akumulatorowe 24/7. Przyjedziemy w 20-30 min. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Łomianki 24h/7 – Dojazd pod Dom",
        "areas": "Łomianki Centralne, Dziekanów Leśny, Dziekanów Polski, Kiełpin, Buraków, Dąbrowa, Sadowa",
        "description_body": "Szybki dojazd trasą DK7 (Wisłostrada) z Bielan prosto do Łomianek i Dziekanowa w 20–30 minut. Wymiana akumulatora pod domem, płatność kartą i BLIK u technika oraz bezpłatny odbiór starego akumulatora."
    },
    {
        "slug": "otwock",
        "url_slug": "wymiana-akumulatora-otwock",
        "name": "Otwock i Józefów",
        "eta": "25–40 min",
        "title": "Wymiana Akumulatora z Dojazdem Otwock, Józefów 24h | Akumulateo",
        "desc": "Awaria akumulatora w Otwocku, Józefowie lub Karczewie? Pogotowie akumulatorowe 24h z dojazdem. Nowe baterie Varta, Yuasa, Bosch. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Otwock i Józefów 24/7",
        "areas": "Otwock Centrum, Józefów, Karczew, Michalin, Falenica, Świder, Świdry Wielkie",
        "description_body": "Dojazd Wałem Miedzeszyńskim oraz trasą S17 do Otwocka, Józefowa i Karczewa. Bezpieczny montaż i kodowanie akumulatorów AGM/EFB z podtrzymaniem pamięci komputera pojazdu."
    },
    {
        "slug": "marki",
        "url_slug": "wymiana-akumulatora-marki",
        "name": "Marki i Ząbki",
        "eta": "20–30 min",
        "title": "Pogotowie Akumulatorowe Marki, Ząbki 24h | Dojazd z Akumulatorem",
        "desc": "Auto nie odpala w Markach lub Ząbkach? Mobilny serwis akumulatorów 24/7. Dojazd w 20-30 min, montaż na posesji, kodowanie BMS. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Marki i Ząbki 24/7",
        "areas": "Marki Pustelnik, Marki Struga, Ząbki Centrum, Drewnica, ul. Radzymińska, Al. Piłsudskiego, trasa S8",
        "description_body": "Dojazd trasą S8 i Radzymińską do Marek i Ząbek w 20–30 minut. Wymiana na miejscu, test alternatora testerem cyfrowym i faktura VAT 23% na życzenie."
    },
    {
        "slug": "grodzisk-mazowiecki",
        "url_slug": "wymiana-akumulatora-grodzisk-mazowiecki",
        "name": "Grodzisk Mazowiecki",
        "eta": "30–45 min",
        "title": "Wymiana Akumulatora Grodzisk Mazowiecki 24h | Pogotowie z Dojazdem",
        "desc": "Mobilne pogotowie akumulatorowe Grodzisk Mazowiecki. Dowóz markowego akumulatora i profesjonalny montaż pod domem 24/7. Tel: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Grodzisk Mazowiecki 24h/7",
        "areas": "Grodzisk Mazowiecki Centrum, Osiedle Piaskowa, Osiedle Kopernika, Łąki, Książenice, Chlebnia, Natolin",
        "description_body": "Dojazd autostradą A2 lub trasą S8 do Grodziska Mazowieckiego. Wymiana akumulatorów w samochodach osobowych, hybrydowych i dostawczych bezpośrednio pod domem klienta."
    },
    {
        "slug": "wolomin",
        "url_slug": "wymiana-akumulatora-wolomin",
        "name": "Wołomin i Kobyłka",
        "eta": "25–40 min",
        "title": "Pogotowie Akumulatorowe Wołomin, Kobyłka 24h | Montaż pod Domem",
        "desc": "Auto nie odpala w Wołominie, Kobyłce lub Zielonce? Mobilny serwis akumulatorów 24/7. Dowóz, montaż i kodowanie na miejscu. Zadzwoń: 696 556 446.",
        "h1": "Pogotowie Akumulatorowe Wołomin i Kobyłka 24h/7",
        "areas": "Wołomin Centrum, Kobyłka, Zielonka, Ossów, Majdan, Duczki, Zagościniec",
        "description_body": "Obsługujemy powiat wołomiński – szybki dojazd trasą S8 i drogą 634. Pełna diagnostyka alternatora i darmowy recykling starej baterii w cenie usługi."
    }
]

def generate_local_page_html(d, is_suburb=False):
    location_label = f"Warszawa {d['name']}" if not is_suburb else f"{d['name']}"
    service_label = f"Warszawa {d['name']}" if not is_suburb else f"{d['name']} i okolice"
    prequalification_text = (
        f"Nie trać czasu na szukanie stacjonarnego sklepu ani holowanie auta. Nie prowadzimy punktu odbioru na terenie dzielnicy {d['name']} – <strong>nasz serwisant przyjeżdża pod Twój blok, dom lub do garażu podziemnego</strong> z fabrycznie nową baterią i montuje ją na miejscu."
        if not is_suburb else
        f"Nie trać czasu na holowanie pojazdu do warsztatu. Firma Akumulateo świadczy wyłącznie usługi mobilne – nie prowadzimy sklepu stacjonarnego na terenie miejscowości {d['name']}. <strong>Nasz technik dojeżdża pod wskazany adres prywatny, firmowy lub na parking</strong> z nowym akumulatorem i montuje go od ręki."
    )
    faq_garage_text = (
        f"Tak. Nasze auta serwisowe oraz przenośne zestawy rozruchowo-diagnostyczne są przystosowane do wjazdu do garaży podziemnych i hal garażowych (poziomy -1, -2, -3) na terenie całej lokalizacji {d['name']}."
    )

    schema = {
        "@context": "https://schema.org",
        "@type": "EmergencyService",
        "name": f"Akumulateo – Pogotowie Akumulatorowe {location_label}",
        "url": f"https://www.akumulateo.pl/{d['url_slug']}",
        "telephone": "+48696556446",
        "priceRange": "$$",
        "image": "https://images.squarespace-cdn.com/content/v1/685d174157b18362d5b7b0f3/7c219de6-f0cf-4151-a1a4-eac82a1de5d2/akumulateo-hero-pagespeed.jpg",
        "areaServed": {
            "@type": "AdministrativeArea",
            "name": location_label
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
            "ratingCount": "100",
            "reviewCount": "100"
        }
    }

    schema_str = json.dumps(schema, ensure_ascii=False, indent=2)

    return f"""<!-- ========================================================
     AKUMULATEO - PODSTRONA LOKALNA: {d['name'].upper()}
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
      <span>• Dojazd {d['eta']}: {location_label}</span>
    </div>
    <div style="font-weight:800;">
      ⭐ <span data-ak-cfg="ratingValue">5.0</span> w Google (<span data-ak-cfg="reviewsCount">100+</span> opinii)
    </div>
  </div>

  <!-- HERO KARTA GŁÓWNA -->
  <div style="background:linear-gradient(180deg, #0f172a 0%, #020617 100%); border:1px solid #1e293b; border-radius:20px; padding:36px 20px; text-align:center; margin-bottom:20px;">
    <span style="display:inline-block; background:rgba(245,158,11,0.15); border:1px solid rgba(245,158,11,0.35); color:#fbbf24; font-weight:900; font-size:12px; padding:6px 16px; border-radius:9999px; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:16px;">
      ⚡ Pogotowie Akumulatorowe {location_label} 24h
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
        ⏱️ Czas dojazdu w rejonie: <span style="color:#34d399;">{d['eta']}</span>
      </div>
    </div>
  </div>

  <!-- BANNER PREKWALIFIKACJI MOBILNEJ -->
  <div style="background:rgba(245,158,11,0.08); border:1px solid rgba(245,158,11,0.3); border-radius:14px; padding:16px 20px; text-align:center; margin-bottom:20px;">
    <div style="color:#fbbf24; font-weight:900; font-size:13px; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:4px;">
      ℹ️ Usługa w 100% Mobilna z Dojazdem pod Auto
    </div>
    <p style="color:#f1f5f9; font-size:15.5px; line-height:1.6; margin:0;">
      {prequalification_text}
    </p>
  </div>

  <!-- REJONY OBSŁUGI & USŁUGI -->
  <div style="background:#0f172a; border:1px solid #1e293b; border-radius:18px; padding:28px 24px; margin-bottom:20px;">
    <h2 style="font-size:22px; font-weight:900; color:#ffffff; margin:0 0 12px 0;">
      Obszar interwencji pogotowia: {service_label}
    </h2>
    <p style="color:#cbd5e1; font-size:16px; line-height:1.65; margin:0 0 20px 0;">
      Nasi technicy stacjonują mobilnie, obsługując w rejonie {d['name']} m.in.: <strong>{d['areas']}</strong>.
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

  <!-- FAQ LOKALNE -->
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
          {faq_garage_text}
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

def generate_hub_page_html(districts, suburbs):
    area_served_list = [{"@type": "AdministrativeArea", "name": f"{d['name']}, Warszawa"} for d in districts]
    for s in suburbs:
        area_served_list.append({"@type": "AdministrativeArea", "name": s['name']})

    schema = {
        "@context": "https://schema.org",
        "@type": "EmergencyService",
        "name": "Akumulateo – Pogotowie Akumulatorowe Warszawa i Aglomeracja 24h",
        "url": "https://www.akumulateo.pl/obszar-dzialania-warszawa-i-okolice",
        "telephone": "+48696556446",
        "priceRange": "$$",
        "image": "https://images.squarespace-cdn.com/content/v1/685d174157b18362d5b7b0f3/7c219de6-f0cf-4151-a1a4-eac82a1de5d2/akumulateo-hero-pagespeed.jpg",
        "areaServed": area_served_list,
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
            "ratingCount": "100",
            "reviewCount": "100"
        },
        "description": "Obszar działania mobilnego pogotowia akumulatorowego Akumulateo. Całodobowy dojazd w 20-30 min we wszystkich 18 dzielnicach Warszawy oraz szybki dojazd trasami ekspresowymi do miejscowości aglomeracji podwarszawskiej. Tel: 696 556 446."
    }

    schema_str = json.dumps(schema, ensure_ascii=False, indent=2)

    # Budujemy kafelki dzielnic
    districts_cards_html = ""
    for d in districts:
        districts_cards_html += f"""
      <a href="/{d['url_slug']}" style="display:flex; flex-direction:column; justify-content:space-between; background:#020617; border:1px solid #1e293b; border-radius:14px; padding:16px; text-decoration:none; transition:all 0.2s ease; box-shadow:0 4px 12px rgba(0,0,0,0.2);">
        <div>
          <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:6px;">
            <span style="color:#ffffff; font-weight:800; font-size:17px;">{d['name']}</span>
            <span style="color:#34d399; font-weight:700; font-size:12px; background:rgba(52,211,153,0.1); padding:2px 8px; border-radius:9999px;">{d['eta']}</span>
          </div>
          <p style="color:#94a3b8; font-size:13.5px; line-height:1.45; margin:0 0 10px 0;">
            {d['areas'].split(',')[0].strip()}, {d['areas'].split(',')[1].strip() if len(d['areas'].split(',')) > 1 else ''}
          </p>
        </div>
        <div style="color:#fbbf24; font-weight:700; font-size:13px; display:flex; align-items:center; gap:4px;">
          <span>Więcej o dojeździe</span> ➔
        </div>
      </a>"""

    # Budujemy kafelki aglomeracji
    suburbs_cards_html = ""
    for s in suburbs:
        first_area = s['areas'].split(',')[0].strip()
        second_area = s['areas'].split(',')[1].strip() if len(s['areas'].split(',')) > 1 else ''
        suburbs_cards_html += f"""
      <a href="/{s['url_slug']}" style="display:flex; flex-direction:column; justify-content:space-between; background:#020617; border:1px solid #1e293b; border-radius:14px; padding:16px; text-decoration:none; transition:all 0.2s ease; box-shadow:0 4px 12px rgba(0,0,0,0.2);">
        <div>
          <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:6px;">
            <span style="color:#ffffff; font-weight:800; font-size:17px;">{s['name']}</span>
            <span style="color:#34d399; font-weight:700; font-size:12px; background:rgba(52,211,153,0.1); padding:2px 8px; border-radius:9999px;">{s['eta']}</span>
          </div>
          <p style="color:#94a3b8; font-size:13.5px; line-height:1.45; margin:0 0 10px 0;">
            {first_area}{', ' + second_area if second_area else ''}
          </p>
        </div>
        <div style="color:#fbbf24; font-weight:700; font-size:13px; display:flex; align-items:center; gap:4px;">
          <span>Więcej o dojeździe</span> ➔
        </div>
      </a>"""

    return f"""<!-- ========================================================
     AKUMULATEO - PODSTRONA ZBIORCZA (HUB): OBSZAR DZIAŁANIA
     URL w Squarespace: /obszar-dzialania-warszawa-i-okolice
     Meta Title: Obszar Działania Pogotowia Akumulatorowego 24h | Warszawa i Aglomeracja
     Meta Description: Całodobowa wymiana akumulatora z dojazdem: wszystkie 18 dzielnic Warszawy (20-30 min) oraz kluczowe miasta aglomeracji. Sprawdź rejon i zadzwoń: 696 556 446!
     ======================================================== -->

<!-- 1. Schema.org JSON-LD (Wklej w: Page Settings -> Advanced -> Page Header Code Injection) -->
<script type="application/ld+json">
{schema_str}
</script>

<!-- 2. Treść sekcji (Wklej jako Code Block na stronie /obszar-dzialania-warszawa-i-okolice) -->
<div class="akumulateo-root bg-slate-950 text-slate-100 font-sans antialiased" style="background:#020617; color:#f8fafc; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif; max-width:1040px; margin:0 auto; padding:16px;">
  
  <!-- TOP EMERGENCY BAR -->
  <div style="background:linear-gradient(90deg, #f59e0b 0%, #fbbf24 50%, #f59e0b 100%); color:#020617; padding:8px 16px; border-radius:12px; font-size:12px; font-weight:900; margin-bottom:20px; display:flex; flex-wrap:wrap; align-items:center; justify-content:between; gap:8px;">
    <div style="display:flex; align-items:center; gap:8px;">
      <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:#020617;"></span>
      <span style="text-transform:uppercase; letter-spacing:0.5px;">Dyżur Pogotowia 24h/7</span>
      <span>• Warszawa (20–30 min) & Aglomeracja Podwarszawska</span>
    </div>
    <div style="font-weight:800;">
      ⭐ <span data-ak-cfg="ratingValue">5.0</span> w Google (<span data-ak-cfg="reviewsCount">100+</span> opinii)
    </div>
  </div>

  <!-- HERO KARTA GŁÓWNA -->
  <div style="background:linear-gradient(180deg, #0f172a 0%, #020617 100%); border:1px solid #1e293b; border-radius:20px; padding:36px 20px; text-align:center; margin-bottom:24px;">
    <span style="display:inline-block; background:rgba(245,158,11,0.15); border:1px solid rgba(245,158,11,0.35); color:#fbbf24; font-weight:900; font-size:12px; padding:6px 16px; border-radius:9999px; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:16px;">
      ⚡ Mobilny Serwis z Dojazdem 24h
    </span>
    
    <h1 style="color:#ffffff; font-size:32px; font-weight:900; line-height:1.2; margin:0 0 16px 0; letter-spacing:-0.5px;">
      Obszar Działania Pogotowia Akumulatorowego
    </h1>
    
    <p style="color:#cbd5e1; font-size:16.5px; line-height:1.65; max-width:760px; margin:0 auto 24px auto;">
      Świadczymy całodobową pomoc dla rozładowanych aut na terenie <strong>całej Warszawy (wszystkie 18 dzielnic)</strong> oraz <strong>kluczowych miejscowości aglomeracji podwarszawskiej</strong>. Nie musisz holować auta ani szukać stacjonarnych sklepów – nasz mobilny warsztat przyjeżdża bezpośrednio pod Twoje auto.
    </p>
    
    <div style="display:flex; flex-direction:column; gap:12px; align-items:center; justify-content:center;">
      <a href="tel:+48696556446" style="display:inline-flex; align-items:center; justify-content:center; gap:10px; background:linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color:#020617; font-weight:900; font-size:18px; padding:16px 36px; border-radius:14px; text-decoration:none; box-shadow:0 8px 25px -5px rgba(245,158,11,0.4); width:100%; max-width:400px;">
        <span style="font-size:22px;">📞</span>
        <span>Zadzwoń: 696 556 446</span>
      </a>
      <div style="font-size:13px; color:#94a3b8; font-weight:700;">
        ⏱️ Czas dojazdu w Warszawie: <span style="color:#34d399;">20–30 minut</span>
      </div>
    </div>
  </div>

  <!-- BANNER PREKWALIFIKACJI MOBILNEJ -->
  <div style="background:rgba(245,158,11,0.08); border:1px solid rgba(245,158,11,0.3); border-radius:14px; padding:18px 20px; text-align:center; margin-bottom:28px;">
    <div style="color:#fbbf24; font-weight:900; font-size:13px; text-transform:uppercase; letter-spacing:0.5px; margin-bottom:6px;">
      ℹ️ Usługa w 100% Mobilna z Dojazdem pod Auto
    </div>
    <p style="color:#f1f5f9; font-size:15.5px; line-height:1.6; margin:0;">
      Firma Akumulateo działa wyłącznie jako mobilny serwis ratunkowy z dojazdem. <strong>Nie prowadzimy sklepu stacjonarnego ani punktu odbioru osobistego</strong>. Każde zlecenie realizujemy bezpośrednio na miejscu awarii – pod domem, biurem, na parkingu lub w podziemnej hali garażowej.
    </p>
  </div>

  <!-- SEKCJA 1: DZIELNICE WARSZAWY (18) -->
  <div style="background:#0f172a; border:1px solid #1e293b; border-radius:20px; padding:28px 20px; margin-bottom:28px;">
    <div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:10px; margin-bottom:16px;">
      <div>
        <h2 style="font-size:24px; font-weight:900; color:#ffffff; margin:0 0 6px 0;">
          Dzielnice Warszawy (18 dzielnic)
        </h2>
        <p style="color:#cbd5e1; font-size:15.5px; margin:0;">
          Dojazd mobilnego serwisu w <strong>20–30 minut</strong> pod wskazany adres:
        </p>
      </div>
      <span style="background:rgba(245,158,11,0.15); color:#fbbf24; font-size:12px; font-weight:800; padding:4px 12px; border-radius:9999px;">
        18 Dzielnic Stolicy
      </span>
    </div>

    <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(220px, 1fr)); gap:14px;">
      {districts_cards_html}
    </div>
  </div>

  <!-- SEKCJA 2: AGLOMERACJA PODWARSZAWSKA (15) -->
  <div style="background:#0f172a; border:1px solid #1e293b; border-radius:20px; padding:28px 20px; margin-bottom:28px;">
    <div style="display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:10px; margin-bottom:16px;">
      <div>
        <h2 style="font-size:24px; font-weight:900; color:#ffffff; margin:0 0 6px 0;">
          Aglomeracja Podwarszawska
        </h2>
        <p style="color:#cbd5e1; font-size:15.5px; margin:0;">
          Szybki dojazd trasami ekspresowymi S2, S7, S8, S17 oraz autostradą A2:
        </p>
      </div>
      <span style="background:rgba(245,158,11,0.15); color:#fbbf24; font-size:12px; font-weight:800; padding:4px 12px; border-radius:9999px;">
        15 Miejscowości & Okolice
      </span>
    </div>

    <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(220px, 1fr)); gap:14px;">
      {suburbs_cards_html}
    </div>
  </div>

  <!-- SEKCJA 3: CO ZAWIERA KAŻDA INTERWENCJA -->
  <div style="background:#0f172a; border:1px solid #1e293b; border-radius:18px; padding:28px 20px; margin-bottom:28px;">
    <h3 style="font-size:20px; font-weight:900; color:#ffffff; margin:0 0 16px 0; text-align:center;">
      Co otrzymujesz w ramach każdej usługi mobilnej?
    </h3>
    
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:16px;">
      <div style="background:#020617; border:1px solid #1e293b; border-radius:14px; padding:18px;">
        <div style="font-size:22px; margin-bottom:8px;">⚡</div>
        <div style="color:#ffffff; font-weight:800; font-size:16px; margin-bottom:6px;">Dojazd & Diagnoza 24h</div>
        <p style="color:#94a3b8; font-size:14.5px; line-height:1.6; margin:0;">
          Tester obciążeniowy akumulatora oraz precyzyjny test alternatora i poboru prądu.
        </p>
      </div>

      <div style="background:#020617; border:1px solid #1e293b; border-radius:14px; padding:18px;">
        <div style="font-size:22px; margin-bottom:8px;">🔋</div>
        <div style="color:#ffffff; font-weight:800; font-size:16px; margin-bottom:6px;">Baterie OEM Premium</div>
        <p style="color:#94a3b8; font-size:14.5px; line-height:1.6; margin:0;">
          Fabryczne akumulatory <strong>Varta, Yuasa, Bosch, 4Max</strong> z gwarancją do 3 lat.
        </p>
      </div>

      <div style="background:#020617; border:1px solid #1e293b; border-radius:14px; padding:18px;">
        <div style="font-size:22px; margin-bottom:8px;">💻</div>
        <div style="color:#ffffff; font-weight:800; font-size:16px; margin-bottom:6px;">Kodowanie BMS & OBD</div>
        <p style="color:#94a3b8; font-size:14.5px; line-height:1.6; margin:0;">
          Podtrzymanie pamięci sterowników i adaptacja w autach z systemem Start-Stop.
        </p>
      </div>

      <div style="background:#020617; border:1px solid #1e293b; border-radius:14px; padding:18px;">
        <div style="font-size:22px; margin-bottom:8px;">♻️</div>
        <div style="color:#ffffff; font-weight:800; font-size:16px; margin-bottom:6px;">Darmowy Recykling BDO</div>
        <p style="color:#94a3b8; font-size:14.5px; line-height:1.6; margin:0;">
          Bezpłatny odbiór zużytego akumulatora – oszczędzasz 30 zł kaucji depozytowej.
        </p>
      </div>
    </div>
  </div>

  <!-- DOLNY CALL TO ACTION -->
  <div style="text-align:center; padding:24px; background:linear-gradient(145deg, #090e1a 0%, #0f172a 100%); border:1px solid #1e293b; border-radius:18px;">
    <div style="color:#ffffff; font-size:22px; font-weight:900; margin-bottom:8px;">
      Potrzebujesz pomocy z akumulatorem w Warszawie lub okolicach?
    </div>
    <p style="color:#cbd5e1; font-size:16px; margin:0 0 16px 0;">
      Zadzwoń do dyspozytora. Podaj model auta i adres – serwisant wyrusza natychmiast.
    </p>
    <a href="tel:+48696556446" style="display:inline-flex; align-items:center; justify-content:center; gap:10px; background:linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color:#020617; font-weight:900; font-size:18px; padding:16px 36px; border-radius:14px; text-decoration:none; box-shadow:0 8px 25px -5px rgba(245,158,11,0.4);">
      <span>📞 Zadzwoń: 696 556 446</span>
    </a>
  </div>

</div>
"""

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_pages_dir = os.path.join(base_dir, "src", "seo", "generated-pages")
    out_snippets_dir = os.path.join(base_dir, "snippets", "squarespace")
    os.makedirs(out_pages_dir, exist_ok=True)
    os.makedirs(out_snippets_dir, exist_ok=True)

    print(f"🚀 Rozpoczynam generowanie {len(WARSAW_DISTRICTS)} dzielnic Warszawy...")
    for d in WARSAW_DISTRICTS:
        html = generate_local_page_html(d, is_suburb=False)
        file_path = os.path.join(out_pages_dir, f"{d['url_slug']}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  ✅ Dzielnica: {d['name']} (/{d['url_slug']})")

    print(f"\n🚀 Rozpoczynam generowanie {len(AGGLOMERATION_SUBURBS)} miejscowości aglomeracji...")
    for s in AGGLOMERATION_SUBURBS:
        html = generate_local_page_html(s, is_suburb=True)
        file_path = os.path.join(out_pages_dir, f"{s['url_slug']}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  ✅ Aglomeracja: {s['name']} (/{s['url_slug']})")

    print(f"\n🚀 Generowanie podstrony Hub: /obszar-dzialania-warszawa-i-okolice...")
    hub_html = generate_hub_page_html(WARSAW_DISTRICTS, AGGLOMERATION_SUBURBS)
    hub_file = os.path.join(out_snippets_dir, "obszar-dzialania-hub.html")
    with open(hub_file, "w", encoding="utf-8") as f:
        f.write(hub_html)
    print(f"  ✅ Podstrona Hub zapisana w: {hub_file} ({len(hub_html)} znaków)")

    print(f"\n🎉 Pomyślnie wygenerowano komplet 33 lokalnych landing pages + 1 Hub directory!")

if __name__ == "__main__":
    main()
