/**
 * Akumulateo – Local SEO & Warsaw Districts Database
 * Kompletna baza danych pod pozycjonowanie lokalne pogotowia akumulatorowego 24h
 * dla wszystkich 18 dzielnic Warszawy oraz kluczowych miast aglomeracji.
 */

export interface DistrictSeoData {
  slug: string;
  name: string;
  isSuburbs: boolean;
  etaMinutes: string;
  metaTitle: string;
  metaDescription: string;
  h1: string;
  h2: string;
  popularAreas: string[];
  serviceScopeText: string;
}

export const WARSAW_DISTRICTS: DistrictSeoData[] = [
  {
    slug: 'mokotow',
    name: 'Mokotów',
    isSuburbs: false,
    etaMinutes: '15-25 min',
    metaTitle: 'Pogotowie Akumulatorowe Warszawa Mokotów 24/7 | Dojazd w 20 min',
    metaDescription: 'Auto nie odpala na Mokotowie? Całodobowa wymiana akumulatora z dojazdem, awaryjny rozruch i kodowanie BMS. Dojeżdżamy w 15-25 min. Zadzwoń: 696 556 446!',
    h1: 'Pogotowie Akumulatorowe Warszawa Mokotów 24h/7',
    h2: 'Mobilna wymiana i awaryjny rozruch akumulatora na Mokotowie',
    popularAreas: ['Służew', 'Służewiec', 'Stegny', 'Sadyba', 'Wierzbno', 'Ksawerów', 'Sielce', 'Mordor (Domaniewska)'],
    serviceScopeText: 'Obsługujemy cały Mokotów – dojeżdżamy pod domy, biurowce na Domaniewskiej oraz garaże podziemne. Pełna diagnostyka alternatora i montaż nowego akumulatora na miejscu.'
  },
  {
    slug: 'ursynow',
    name: 'Ursynów',
    isSuburbs: false,
    etaMinutes: '15-25 min',
    metaTitle: 'Wymiana Akumulatora z Dojazdem Warszawa Ursynów 24h | Akumulateo',
    metaDescription: 'Mobilny serwis akumulatorów na Ursynowie (Kabaty, Imielin, Stokłosy, Natolin). Awaryjne uruchamianie auta i montaż akumulatora 24/7. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Ursynów 24/7 – Wymiana z Dojazdem',
    h2: 'Szybki dojazd do rozładowanego auta na Ursynowie',
    popularAreas: ['Kabaty', 'Natolin', 'Imielin', 'Stokłosy', 'Dąbrówka', 'Grabów', 'Pyry'],
    serviceScopeText: 'Brak sklepu stacjonarnego – przyjeżdżamy bezpośrednio pod Twój adres na Ursynowie. Dowóz baterii, wymiana z podtrzymaniem pamięci i kodowanie komputerem.'
  },
  {
    slug: 'wola',
    name: 'Wola',
    isSuburbs: false,
    etaMinutes: '15-25 min',
    metaTitle: 'Pogotowie Akumulatorowe Warszawa Wola 24/7 | Rozruch i Wymiana',
    metaDescription: 'Rozładowany akumulator na Woli? Przyjedziemy w 20 minut pod Twój dom lub firmę. Awaryjny rozruch i nowa bateria z montażem 24h. Zadzwoń: 696 556 446!',
    h1: 'Pogotowie Akumulatorowe Warszawa Wola 24h',
    h2: 'Całodobowy mobilny serwis akumulatorów na Woli',
    popularAreas: ['Czyste', 'Mirów', 'Młynów', 'Koło', 'Ulrychów', 'Odolany', 'Rondo Daszyńskiego'],
    serviceScopeText: 'Błyskawiczna pomoc przy awarii akumulatora na Odolanach, Kole, Mirowie i w centrum biznesowym przy Rondzie Daszyńskiego.'
  },
  {
    slug: 'srodmiescie',
    name: 'Śródmieście',
    isSuburbs: false,
    etaMinutes: '15-25 min',
    metaTitle: 'Awaryjne Odpalanie Auta i Wymiana Akumulatora Śródmieście 24h',
    metaDescription: 'Śródmieście Warszawa: pogotowie akumulatorowe 24/7. Wjazd do stref i garaży podziemnych. Diagnostyka, montaż i kodowanie akumulatora. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Warszawa Śródmieście 24/7',
    h2: 'Pomoc z akumulatorem w centrum Warszawy o każdej porze',
    popularAreas: ['Muranów', 'Powiśle', 'Solec', 'Ujazdów', 'Stare Miasto', 'Plac Zbawiciela', 'Dworzec Centralny'],
    serviceScopeText: 'Wjeżdżamy do garaży podziemnych i stref ograniczonego ruchu w centrum Warszawy. Sprzęt rozruchowy i nowe akumulatory dostępne od ręki 24/7.'
  },
  {
    slug: 'praga-poludnie',
    name: 'Praga-Południe',
    isSuburbs: false,
    etaMinutes: '15-25 min',
    metaTitle: 'Wymiana Akumulatora z Dojazdem Praga-Południe (Saska Kępa, Grochów)',
    metaDescription: 'Pogotowie akumulatorowe Praga-Południe: Grochów, Saska Kępa, Gocław. Dojazd w 20 min, diagnostyka ładowania i wymiana na miejscu 24h. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Praga-Południe 24h',
    h2: 'Wymiana baterii i awaryjny rozruch: Gocław, Grochów, Saska Kępa',
    popularAreas: ['Gocław', 'Grochów', 'Saska Kępa', 'Kamionek', 'Gocławek', 'Przyczółek Grochowski'],
    serviceScopeText: 'Nie musisz szukać sklepów na Zamienieckiej – przywieziemy dobrany akumulator i zamontujemy go pod Twoim blokiem lub na trasie.'
  },
  {
    slug: 'bielany',
    name: 'Bielany',
    isSuburbs: false,
    etaMinutes: '20-30 min',
    metaTitle: 'Pogotowie Akumulatorowe Bielany 24/7 | Wymiana Akumulatora z Dojazdem',
    metaDescription: 'Pomoc z akumulatorem Warszawa Bielany: Chomiczówka, Wrzeciono, Młociny, Słodowiec. Sprawdzenie prądu i nowy akumulator u klienta. Zadzwoń: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Warszawa Bielany 24h',
    h2: 'Mobilny montaż akumulatora z dojazdem na Bielanach',
    popularAreas: ['Chomiczówka', 'Wrzeciono', 'Młociny', 'Wawrzyszew', 'Słodowiec', 'Stare Bielany'],
    serviceScopeText: 'Całodobowy dojazd do kierowców na terenie całych Bielan. Zabieramy zużyty akumulator, testujemy instalację i kodujemy nowy akumulator w systemie auta.'
  },
  {
    slug: 'bemowo',
    name: 'Bemowo',
    isSuburbs: false,
    etaMinutes: '20-30 min',
    metaTitle: 'Wymiana Akumulatora z Dojazdem Warszawa Bemowo 24h | Akumulateo',
    metaDescription: 'Auto nie odpala na Bemowie? Jelonki, Górce, Chrzanów, Boernerowo. Dojazd z nowym akumulatorem w 20-30 min. Sprawdź cennik: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Warszawa Bemowo 24/7',
    h2: 'Awaryjny rozruch i wymiana baterii samochodowej na Bemowie',
    popularAreas: ['Jelonki', 'Górce', 'Chrzanów', 'Boernerowo', 'Fort Bema', 'Nowe Bemowo'],
    serviceScopeText: 'Błyskawiczny dojazd na Bemowie pod domy jednorodzinne i nowe osiedla na Chrzanowie oraz Jelonkach.'
  },
  {
    slug: 'bialoleka',
    name: 'Białołęka',
    isSuburbs: false,
    etaMinutes: '25-35 min',
    metaTitle: 'Pogotowie Akumulatorowe Białołęka 24h | Dojazd z Akumulatorem Tarchomin',
    metaDescription: 'Pogotowie akumulatorowe Białołęka (Tarchomin, Nowodwory, Derby, Brzeziny). Rozruch auta z kabli/boostera i montaż akumulatora 24/7. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Warszawa Białołęka 24h',
    h2: 'Wymiana akumulatora u klienta: Tarchomin, Nowodwory, Zielona Białołęka',
    popularAreas: ['Tarchomin', 'Nowodwory', 'Żerań', 'Dąbrówka Szlachecka', 'Brzeziny', 'Grodzisk / Derby'],
    serviceScopeText: 'Dojazd na całą Białołękę. Wymiana akumulatora bez stania w korkach – technik przyjeżdża z właściwym akumulatorem pod Twoje drzwi.'
  },
  {
    slug: 'ochota',
    name: 'Ochota',
    isSuburbs: false,
    etaMinutes: '15-25 min',
    metaTitle: 'Wymiana Akumulatora Ochota 24h | Dojazd, Diagnostyka i Kodowanie',
    metaDescription: 'Ochota (Szczęśliwice, Rakowiec, Stara Ochota): natychmiastowa pomoc z rozładowanym akumulatorem. Dojazd 24/7, test ładowania. Zadzwoń: 696 556 446!',
    h1: 'Pogotowie Akumulatorowe Warszawa Ochota 24/7',
    h2: 'Awaryjne uruchamianie auta i montaż akumulatora na Ochocie',
    popularAreas: ['Szczęśliwice', 'Rakowiec', 'Stara Ochota', 'Filtry', 'Plac Narutowicza'],
    serviceScopeText: 'Obsługa rejonu Szczęśliwic, Rakowca i Starej Ochoty. Dojazd w 20 minut z pełnym asortymentem akumulatorów AGM, EFB i standardowych.'
  },
  {
    slug: 'targowek',
    name: 'Targówek',
    isSuburbs: false,
    etaMinutes: '20-30 min',
    metaTitle: 'Pogotowie Akumulatorowe Targówek 24h | Bródno, Zacisze – Dojazd',
    metaDescription: 'Wymiana akumulatora Targówek (Bródno, Zacisze, Targówek Mieszkaniowy/Fabryczny). Mobilny serwis z dojazdem i kodowaniem 24/7. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Warszawa Targówek 24h',
    h2: 'Szybki dojazd do rozładowanego auta: Bródno, Zacisze, Targówek',
    popularAreas: ['Bródno', 'Zacisze', 'Targówek Mieszkaniowy', 'Targówek Fabryczny', 'Elsnerów'],
    serviceScopeText: 'Całodobowy dojazd na Bródno i Zacisze. Awaryjny rozruch samochodów osobowych i dostawczych.'
  },
  {
    slug: 'wilanow',
    name: 'Wilanów',
    isSuburbs: false,
    etaMinutes: '15-25 min',
    metaTitle: 'Wymiana Akumulatora Miasteczko Wilanów 24h | Kodowanie AGM Akumulateo',
    metaDescription: 'Pogotowie akumulatorowe Miasteczko Wilanów, Zawady, Powsinek. Akumulatory AGM/EFB z montażem i kodowaniem w garażach podziemnych 24/7. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Warszawa Wilanów 24/7',
    h2: 'Montaż akumulatorów AGM/EFB i kodowanie BMS w Miasteczku Wilanów',
    popularAreas: ['Miasteczko Wilanów', 'Zawady', 'Powsinek', 'Kępa Zawadowska', 'Wilanów Wysoki'],
    serviceScopeText: 'Specjalizujemy się w nowoczesnych autach z systemem Start-Stop wymagających kodowania w Miasteczku Wilanów i na Zawadach. Wjazd do garaży podziemnych.'
  },
  {
    slug: 'piaseczno',
    name: 'Piaseczno',
    isSuburbs: true,
    etaMinutes: '20-30 min',
    metaTitle: 'Pogotowie Akumulatorowe Piaseczno 24h | Wymiana Akumulatora z Dojazdem',
    metaDescription: 'Rozładowany akumulator w Piasecznie lub Józefosławiu? Mobilny serwis akumulatorów 24/7. Przyjedziemy i wymienimy na miejscu. Zadzwoń: 696 556 446!',
    h1: 'Pogotowie Akumulatorowe Piaseczno i Okolice 24h',
    h2: 'Dojazd z nowym akumulatorem: Piaseczno, Józefosław, Julianów, Lesznowola',
    popularAreas: ['Piaseczno Centrum', 'Józefosław', 'Julianów', 'Zalesie Dolne', 'Lesznowola', 'Nowa Iwiczna'],
    serviceScopeText: 'Obsługujemy całą gminę Piaseczno i Lesznowolę. Szybki dojazd drogą S79/Puławską o każdej porze dnia i nocy.'
  },
  {
    slug: 'pruszkow',
    name: 'Pruszków',
    isSuburbs: true,
    etaMinutes: '20-30 min',
    metaTitle: 'Wymiana Akumulatora z Dojazdem Pruszków 24h | Pogotowie Akumulateo',
    metaDescription: 'Pruszków, Michałowice, Raszyn: pogotowie akumulatorowe 24/7. Wymiana pod domem, awaryjne odpalanie boosterem. Zadzwoń: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Pruszków 24/7',
    h2: 'Mobilny serwis akumulatorów w Pruszkowie',
    popularAreas: ['Pruszków Centrum', 'Gąsin', 'Żbików', 'Ostoja', 'Bąki', 'Michałowice'],
    serviceScopeText: 'Ekspresowy dojazd autostradą A2 i Alejami Jerozolimskimi do Pruszkowa z nowym akumulatorem.'
  },
  {
    slug: 'piastow',
    name: 'Piastów',
    isSuburbs: true,
    etaMinutes: '20-30 min',
    metaTitle: 'Pogotowie Akumulatorowe Piastów 24h | Wymiana Akumulatora z Dojazdem',
    metaDescription: 'Rozładowany akumulator w Piastowie? Całodobowa wymiana z dojazdem pod dom lub firmę. Diagnostyka, montaż i kodowanie BMS. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Piastów 24/7',
    h2: 'Szybki dojazd z nowym akumulatorem na terenie Piastowa',
    popularAreas: ['Piastów Północ', 'Piastów Południe', 'Osiedle Ogińskiego', 'Al. Tysiąclecia', 'Dworzec PKP Piastów'],
    serviceScopeText: 'Błyskawiczny dojazd Alejami Jerozolimskimi prosto do Piastowa. Wymieniamy akumulatory pod domem, blokiem lub firmą o każdej porze.'
  },
  {
    slug: 'marki',
    name: 'Marki i Ząbki',
    isSuburbs: true,
    etaMinutes: '20-30 min',
    metaTitle: 'Pogotowie Akumulatorowe Marki, Ząbki 24h | Dojazd z Akumulatorem',
    metaDescription: 'Padł akumulator w Markach lub Ząbkach? Mobilna wymiana z montażem na miejscu 24/7. Dojazd w 20-30 min. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Marki i Ząbki 24h',
    h2: 'Awaryjny rozruch i wymiana akumulatora u klienta w Markach',
    popularAreas: ['Marki Pustelnik', 'Marki Struga', 'Ząbki Centrum', 'Drewnica'],
    serviceScopeText: 'Dojazd trasą S8 i Radzymińską do Marek i Ząbek. Wymiana na miejscu bez potrzeby holowania auta do warsztatu.'
  },
  {
    slug: 'legionowo',
    name: 'Legionowo',
    isSuburbs: true,
    etaMinutes: '25-35 min',
    metaTitle: 'Pogotowie Akumulatorowe Legionowo 24h | Wymiana Akumulatora z Dojazdem',
    metaDescription: 'Rozładowany akumulator w Legionowie lub Jabłonnie? Całodobowa wymiana z dojazdem pod dom. Diagnostyka, montaż i kodowanie BMS. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Legionowo i Jabłonna 24/7',
    h2: 'Mobilny serwis akumulatorów u klienta w Legionowie',
    popularAreas: ['Legionowo Centrum', 'Jabłonna', 'Piaski', 'Osiedle Sobieskiego', 'Bukowiec', 'Chotomów'],
    serviceScopeText: 'Ekspresowy dojazd drogą DK61 z Warszawy do Legionowa i Jabłonny. Wymiana akumulatora pod domem lub firmą 24/7.'
  },
  {
    slug: 'otwock',
    name: 'Otwock i Józefów',
    isSuburbs: true,
    etaMinutes: '25-40 min',
    metaTitle: 'Wymiana Akumulatora z Dojazdem Otwock, Józefów 24h | Akumulateo',
    metaDescription: 'Awaria akumulatora w Otwocku, Józefowie lub Karczewie? Pogotowie akumulatorowe 24h z dojazdem. Nowe baterie Varta, Yuasa, Bosch. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Otwock i Józefów 24h',
    h2: 'Całodobowa wymiana i awaryjny rozruch w powiecie otwockim',
    popularAreas: ['Otwock Centrum', 'Józefów', 'Świdry Wielkie', 'Karczew', 'Michalin', 'Falenica'],
    serviceScopeText: 'Dojazd Wałem Miedzeszyńskim oraz trasą S17 do Otwocka, Józefowa i Karczewa. Bezpieczny montaż i kodowanie akumulatorów AGM/EFB.'
  },
  {
    slug: 'wolomin',
    name: 'Wołomin i Kobyłka',
    isSuburbs: true,
    etaMinutes: '25-40 min',
    metaTitle: 'Pogotowie Akumulatorowe Wołomin, Kobyłka 24h | Montaż pod Domem',
    metaDescription: 'Auto nie odpala w Wołominie, Kobyłce lub Zielonce? Mobilny serwis akumulatorów 24/7. Dowóz, montaż i kodowanie na miejscu. Zadzwoń: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Wołomin i Kobyłka 24h',
    h2: 'Szybki dojazd z nowym akumulatorem: Wołomin, Kobyłka, Zielonka',
    popularAreas: ['Wołomin Centrum', 'Kobyłka', 'Zielonka', 'Ossów', 'Majdan', 'Duczki'],
    serviceScopeText: 'Obsługujemy powiat wołomiński – szybki dojazd trasą S8 i drogą 634. Pełna diagnostyka alternatora i darmowy recykling starej baterii.'
  },
  {
    slug: 'grodzisk-mazowiecki',
    name: 'Grodzisk Mazowiecki',
    isSuburbs: true,
    etaMinutes: '30-45 min',
    metaTitle: 'Wymiana Akumulatora Grodzisk Mazowiecki 24h | Pogotowie z Dojazdem',
    metaDescription: 'Mobilne pogotowie akumulatorowe Grodzisk Mazowiecki. Dowóz markowego akumulatora i profesjonalny montaż pod domem 24/7. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Grodzisk Mazowiecki 24h',
    h2: 'Montaż akumulatora z dojazdem: Grodzisk Mazowiecki i okolice',
    popularAreas: ['Grodzisk Mazowiecki Centrum', 'Łąki', 'Piaskowa', 'Książenice', 'Chlebnia'],
    serviceScopeText: 'Dojazd autostradą A2 lub trasą S8 do Grodziska Mazowieckiego. Wymiana akumulatorów w autach osobowych i dostawczych pod domem klienta.'
  },
  {
    slug: 'brwinow',
    name: 'Brwinów',
    isSuburbs: true,
    etaMinutes: '25-35 min',
    metaTitle: 'Wymiana Akumulatora z Dojazdem Brwinów 24h | Pogotowie Akumulateo',
    metaDescription: 'Awaria akumulatora w Brwinowie, Otrębusach lub Żółwinie? Mobilny serwis akumulatorów 24/7. Wymiana na posesji klienta. Zadzwoń: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Brwinów i Okolice 24h',
    h2: 'Mobilny montaż akumulatora: Brwinów, Otrębusy, Żółwin, Owczarnia',
    popularAreas: ['Brwinów Centrum', 'Otrębusy', 'Żółwin', 'Owczarnia', 'Kotowice', 'Biskupice'],
    serviceScopeText: 'Szybki dojazd drogą 719 oraz A2 do Brwinowa i okolicznych miejscowości. Pełna diagnostyka instalacji i podtrzymanie pamięci sterowników.'
  },
  {
    slug: 'milanowek',
    name: 'Milanówek',
    isSuburbs: true,
    etaMinutes: '25-35 min',
    metaTitle: 'Pogotowie Akumulatorowe Milanówek 24h | Wymiana Akumulatora z Dojazdem',
    metaDescription: 'Samochód nie odpala w Milanówku? Całodobowy mobilny serwis akumulatorów z dojazdem. Markowe baterie Varta, Yuasa, Bosch. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Milanówek 24/7',
    h2: 'Wymiana i awaryjny rozruch akumulatora w Milanówku i Podkowie Leśnej',
    popularAreas: ['Milanówek Centrum', 'Grudów', 'Turczynek', 'Kazimierówka', 'Podkowa Leśna'],
    serviceScopeText: 'Dojazd do Milanówka autostradą A2 lub trasą 719. Wjeżdżamy na prywatne posesje, montujemy akumulatory AGM i kodujemy w komputerze pojazdu.'
  },
  {
    slug: 'lomianki',
    name: 'Łomianki',
    isSuburbs: true,
    etaMinutes: '20-30 min',
    metaTitle: 'Pogotowie Akumulatorowe Łomianki 24h | Wymiana Akumulatora z Dojazdem',
    metaDescription: 'Rozładowany akumulator w Łomiankach, Dziekanowie lub Kiełpinie? Pogotowie akumulatorowe 24/7. Przyjedziemy w 20-30 min. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Łomianki 24/7',
    h2: 'Wymiana akumulatora u klienta: Łomianki, Dziekanów Leśny, Kiełpin',
    popularAreas: ['Łomianki Centralne', 'Dziekanów Leśny', 'Dziekanów Polski', 'Kiełpin', 'Buraków', 'Dąbrowa'],
    serviceScopeText: 'Szybki dojazd trasą DK7 (Wisłostrada) z Bielan prosto do Łomianek i Dziekanowa. Płatność kartą i BLIK u technika.'
  },
  {
    slug: 'modlin',
    name: 'Modlin i Nowy Dwór Mazowiecki',
    isSuburbs: true,
    etaMinutes: '35-50 min',
    metaTitle: 'Pogotowie Akumulatorowe Lotnisko Modlin, Nowy Dwór Maz. 24h | Rozruch i Wymiana',
    metaDescription: 'Rozładowany akumulator na parkingu przy Lotnisku Modlin lub w Nowym Dworze Mazowieckim? Całodobowa pomoc, awaryjny rozruch boosterem i montaż nowej baterii. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Modlin i Nowy Dwór Mazowiecki 24h',
    h2: 'Ekspresowy rozruch i wymiana na parkingach Lotniska Modlin oraz w Nowym Dworze',
    popularAreas: ['Parkingi Lotnisko Modlin P1-P7', 'Modlin Twierdza', 'Nowy Dwór Centrum', 'Czosnów', 'Zakroczym'],
    serviceScopeText: 'Specjalny dyżur z dojazdem trasą S7 na parkingi długoterminowe wokół Lotniska Warszawa-Modlin oraz do Nowego Dworu Mazowieckiego. Ratunek dla podróżnych powracających z lotów.'
  },
  {
    slug: 'nowy-dwor-mazowiecki',
    name: 'Nowy Dwór Mazowiecki',
    isSuburbs: true,
    etaMinutes: '35-50 min',
    metaTitle: 'Pogotowie Akumulatorowe Nowy Dwór Mazowiecki 24h | Dojazd z Akumulatorem',
    metaDescription: 'Padł akumulator w Nowym Dworze Mazowieckim? Całodobowa pomoc akumulatorowa, rozruch boosterem i wymiana. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Nowy Dwór Mazowiecki 24h',
    h2: 'Ratunek dla rozładowanych aut w Nowym Dworze Mazowieckim i okolicach',
    popularAreas: ['Nowy Dwór Centrum', 'Osiedle Młodych', 'Twierdza Modlin', 'Czosnów', 'Kazuń Nowy'],
    serviceScopeText: 'Dojazd trasą S7 do Nowego Dworu Mazowieckiego. Awaryjny rozruch i wymiana akumulatora od ręki pod domem lub na parkingu.'
  },
  {
    slug: 'minsk-mazowiecki',
    name: 'Mińsk Mazowiecki',
    isSuburbs: true,
    etaMinutes: '35-50 min',
    metaTitle: 'Wymiana Akumulatora Mińsk Mazowiecki 24h | Pogotowie Akumulateo',
    metaDescription: 'Pogotowie akumulatorowe Mińsk Mazowiecki, Halinów, Sulejówek. Wymiana akumulatora pod domem z kodowaniem BMS 24/7. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Mińsk Mazowiecki 24h',
    h2: 'Mobilny montaż akumulatora: Mińsk Mazowiecki, Halinów, Dębe Wielkie',
    popularAreas: ['Mińsk Mazowiecki Centrum', 'Halinów', 'Sulejówek', 'Dębe Wielkie', 'Stojadła'],
    serviceScopeText: 'Dojazd autostradą A2 do Mińska Mazowieckiego i Halinowa. Kompleksowa wymiana z podtrzymaniem pamięci OBD i gwarancją do 3 lat.'
  },
  {
    slug: 'konstancin-jeziorna',
    name: 'Konstancin-Jeziorna',
    isSuburbs: true,
    etaMinutes: '20-30 min',
    metaTitle: 'Pogotowie Akumulatorowe Konstancin-Jeziorna 24h | Dojazd z Akumulatorem',
    metaDescription: 'Konstancin-Jeziorna, Bielawa, Skolimów: mobilny serwis akumulatorów 24/7. Dojazd pod posesję, wymiana baterii AGM i kodowanie. Tel: 696 556 446.',
    h1: 'Pogotowie Akumulatorowe Konstancin-Jeziorna 24h',
    h2: 'Montaż akumulatora z dojazdem: Konstancin, Bielawa, Skolimów, Klarysew',
    popularAreas: ['Konstancin Centrum', 'Skolimów', 'Bielawa', 'Klarysew', 'Chylice', 'Obory'],
    serviceScopeText: 'Błyskawiczny dojazd od strony Wilanowa i Ursynowa do Konstancina-Jeziornej. Dojeżdżamy na posesje prywatne i do rezydencji o każdej porze.'
  }
];

export class DistrictSeoHelper {
  public static getAllDistricts(): DistrictSeoData[] {
    return WARSAW_DISTRICTS;
  }

  public static getBySlug(slug: string): DistrictSeoData | undefined {
    return WARSAW_DISTRICTS.find(d => d.slug.toLowerCase() === slug.toLowerCase());
  }

  /**
   * Generuje ustrukturyzowane dane Schema.org (JSON-LD) dla danej dzielnicy
   */
  public static generateSchemaOrgJsonLd(district: DistrictSeoData): string {
    const schema = {
      "@context": "https://schema.org",
      "@type": "EmergencyService",
      "name": `Akumulateo – Pogotowie Akumulatorowe Warszawa ${district.name}`,
      "image": "https://www.akumulateo.pl/static/logo.png",
      "url": `https://www.akumulateo.pl/obszar-dzialania/${district.slug}`,
      "telephone": "+48696556446",
      "priceRange": "$$",
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
          ],
          "opens": "00:00",
          "closes": "23:59"
        }
      ],
      "areaServed": {
        "@type": "AdministrativeArea",
        "name": `Warszawa ${district.name}`
      },
      "description": district.metaDescription
    };

    return JSON.stringify(schema, null, 2);
  }
}
