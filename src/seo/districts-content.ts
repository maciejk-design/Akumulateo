/**
 * Akumulateo – Kompleksowa paczka gotowych treści pod lokalne strony dzielnicowe (Warszawa i okolice)
 * Gotowe teksty do skopiowania do bloków Squarespace (Text, Accordion/FAQ, Code Block)
 * Zoptymalizowane pod konwersję (Click-to-Call 696 556 446), prekwalifikację (usługa mobilna 24h) oraz SEO.
 */

export interface DistrictFaqItem {
  question: string;
  answer: string;
}

export interface DistrictContentPage {
  slug: string;
  districtName: string;
  isWarsawDistrict: boolean;
  eta: string;
  urlPath: string;
  meta: {
    title: string;
    description: string;
  };
  hero: {
    badge: string;
    h1: string;
    lead: string;
    ctaButtonText: string;
    phoneNumber: string;
    trustNote: string;
  };
  whyMobileSection: {
    h2: string;
    paragraphs: string[];
    localLandmarks: string[];
  };
  servicesSection: {
    h2: string;
    services: {
      title: string;
      description: string;
    }[];
  };
  pricingAndEtaSection: {
    h2: string;
    etaText: string;
    pricingItems: {
      service: string;
      price: string;
      details: string;
    }[];
  };
  faqSection: {
    h2: string;
    items: DistrictFaqItem[];
  };
  schemaJsonLd: string;
}

export const DISTRICTS_CONTENT: DistrictContentPage[] = [
  {
    slug: 'mokotow',
    districtName: 'Mokotów',
    isWarsawDistrict: true,
    eta: '15-25 minut',
    urlPath: '/wymiana-akumulatora-warszawa-mokotow',
    meta: {
      title: 'Wymiana Akumulatora z Dojazdem Warszawa Mokotów 24/7 | Akumulateo',
      description: 'Padł akumulator na Mokotowie? Całodobowa wymiana z dojazdem w 15-25 min (Mordor, Służew, Stegny, Sadyba). Dobór, montaż, kodowanie BMS. Zadzwoń: 696 556 446!'
    },
    hero: {
      badge: '⚡ Pogotowie Akumulatorowe 24h – Dojazd w 15-25 min na Mokotów',
      h1: 'Wymiana Akumulatora z Dojazdem Warszawa Mokotów (24/7)',
      lead: 'Auto nie odpala na Mokotowie? Nie musisz holować auta ani szukać stacjonarnego sklepu. Przyjeżdżamy bezpośrednio pod Twój blok, dom, biurowiec lub do garażu podziemnego z nowym, dobranym akumulatorem.',
      ctaButtonText: 'Zadzwoń po pomoc: 696 556 446',
      phoneNumber: '696 556 446',
      trustNote: '⭐ 5.0 w Google | Wjazd do garaży podziemnych | Płatność kartą i BLIK na miejscu'
    },
    whyMobileSection: {
      h2: 'Mobilny serwis akumulatorów na Mokotowie – Dlaczego to najlepszy wybór?',
      paragraphs: [
        'Mokotów to jedna z najbardziej zatłoczonych dzielnic Warszawy. W godzinach szczytu holowanie unieruchomionego samochodu z osiedli na Służewie, Stegnach czy z zagłębia biurowego na Domaniewskiej (Mordor) do warsztatu to strata kilku godzin i setek złotych.',
        'Akumulateo działa w 100% mobilnie. Nasze mobilne warsztaty stacjonują w strategicznych punktach Warszawy, dzięki czemu na terenie Górnego i Dolnego Mokotowa meldujemy się zazwyczaj w 15 do 25 minut od zgłoszenia telefonicznego.',
        'Dysponujemy sprzętem o niskim profilu, co pozwala nam bez problemu wjechać do ciasnych garaży podziemnych (np. przy Galerii Mokotów, w nowych apartamentowcach na Sadybie czy przy ul. Konstruktorskiej).'
      ],
      localLandmarks: [
        'Służewiec / Mordor (Domaniewska, Wołoska, Konstruktorska)',
        'Sadyba i Stegny (św. Bonifacego, Sobieskiego, Powsińska)',
        'Służew nad Dolinką i Ksawerów',
        'Wierzbno, Mokotów Górny (Puławska, Niepodległości, Madalińskiego)',
        'Sielce i Czerniaków (Gagarina, Czerniakowska)'
      ]
    },
    servicesSection: {
      h2: 'Pełen zakres pomocy akumulatorowej na Mokotowie',
      services: [
        {
          title: 'Kompleksowa Wymiana Akumulatora',
          description: 'Dowozimy akumulator renomowanej marki (Varta, Yuasa, Bosch itp.), demontujemy stary i profesjonalnie montujemy nowy. Zabieramy zużytą baterię do legalnej utylizacji bez opłaty depozytowej.'
        },
        {
          title: 'Podtrzymanie Pamięci i Kodowanie BMS',
          description: 'Prace prowadzimy z podtrzymaniem zasilania, aby nie zresetować ustawień radia, szyb i komputera pokładowego. W autach z systemem Start-Stop przeprowadzamy adaptację akumulatora w sterowniku silnika.'
        },
        {
          title: 'Awaryjny Rozruch Boosterem 12V / 24V',
          description: 'Gdy akumulator jest sprawny, ale rozładowany (np. przez zostawione światła), odpalamy auto bezpiecznym boosterem mikroprocesorowym chroniącym czułą elektronikę.'
        },
        {
          title: 'Komputerowy Test Alternatora i Poboru Prądu',
          description: 'Przed montażem badamy stan ładowania alternatora oraz prąd rozruchowy, dając 100% pewności, że problem leży w baterii, a nie w instalacji pojazdu.'
        }
      ]
    },
    pricingAndEtaSection: {
      h2: 'Cennik usług z dojazdem – Warszawa Mokotów',
      etaText: 'Średni czas dojazdu technika na Mokotów: 15–25 minut (dostępność 24h / 7 dni w tygodniu).',
      pricingItems: [
        {
          service: 'Awaryjny rozruch auta (Booster)',
          price: 'od 150 zł',
          details: 'Dojazd technika, test ładowania alternatora, bezpieczny rozruch.'
        },
        {
          service: 'Kompleksowa wymiana akumulatora',
          price: 'od 150 zł + cena akumulatora',
          details: 'Dojazd, montaż, podtrzymanie napięcia, kodowanie BMS, utylizacja starej baterii.'
        },
        {
          service: 'Diagnostyka instalacji i test baterii',
          price: 'w cenie wymiany (lub 100 zł solo)',
          details: 'Cyfrowy wydruk parametrów akumulatora i napięcia ładowania.'
        }
      ]
    },
    faqSection: {
      h2: 'Często zadawane pytania (FAQ) – Mokotów',
      items: [
        {
          question: 'Czy posiadacie sklep stacjonarny na Mokotowie, gdzie mogę odebrać akumulator?',
          answer: 'Nie prowadzimy sklepu stacjonarnego ani odbiorów osobistych. Działamy wyłącznie jako mobilny serwis z dojazdem i montażem na miejscu u klienta – dzięki temu nie tracisz czasu na wyjazdy i transport ciężkiego akumulatora.'
        },
        {
          question: 'Czy wjedziecie do garażu podziemnego o niskim stropie?',
          answer: 'Tak. Nasze auta serwisowe oraz przenośny sprzęt diagnostyczno-rozruchowy są dostosowane do wjazdu do parkingów podziemnych o wysokości nawet poniżej 1,9 m na terenie całego Mokotowa.'
        },
        {
          question: 'Jak mogę zapłacić technikowi po skończonej usłudze?',
          answer: 'Każdy nasz serwisant posiada terminal płatniczy. Akceptujemy płatności kartą, BLIK-iem oraz gotówką. Na życzenie wystawiamy fakturę VAT 23% dla firm.'
        }
      ]
    },
    schemaJsonLd: `{
  "@context": "https://schema.org",
  "@type": "EmergencyService",
  "name": "Akumulateo – Pogotowie Akumulatorowe Warszawa Mokotów",
  "image": "https://www.akumulateo.pl/static/logo.png",
  "url": "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-mokotow",
  "telephone": "+48696556446",
  "priceRange": "$$",
  "areaServed": {
    "@type": "AdministrativeArea",
    "name": "Mokotów, Warszawa"
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "opens": "00:00",
    "closes": "23:59"
  },
  "description": "Całodobowa wymiana akumulatora z dojazdem Warszawa Mokotów. Szybki dojazd w 15-25 min, diagnostyka, montaż i kodowanie BMS."
}`
  },
  {
    slug: 'ursynow',
    districtName: 'Ursynów',
    isWarsawDistrict: true,
    eta: '15-25 minut',
    urlPath: '/wymiana-akumulatora-warszawa-ursynow',
    meta: {
      title: 'Wymiana Akumulatora z Dojazdem Warszawa Ursynów 24h | Akumulateo',
      description: 'Mobilne pogotowie akumulatorowe Warszawa Ursynów (Kabaty, Natolin, Imielin, Stokłosy). Dojazd w 20 min, montaż z kodowaniem BMS pod domem 24/7. Tel: 696 556 446.'
    },
    hero: {
      badge: '⚡ Mobilny Serwis Akumulatorów 24/7 – Ursynów w 20 minut',
      h1: 'Wymiana Akumulatora z Dojazdem Warszawa Ursynów 24h',
      lead: 'Zaskoczył Cię rozładowany akumulator na Ursynowie? Dojeżdżamy na Kabaty, Natolin, Imielin, Stokłosy oraz Zielony Ursynów. Wymieniamy akumulator na miejscu postoju auta o każdej porze dnia i nocy.',
      ctaButtonText: 'Zamów wymianę z dojazdem: 696 556 446',
      phoneNumber: '696 556 446',
      trustNote: '⭐ 5.0 w Google | Parkingi podziemne | Gwarancja do 3 lat'
    },
    whyMobileSection: {
      h2: 'Pogotowie akumulatorowe na Ursynowie – Dlaczego Akumulateo?',
      paragraphs: [
        'Duże osiedla mieszkaniowe na Ursynowie charakteryzują się setkami podziemnych hal garażowych oraz rozległymi parkingami wzdłuż al. KEN i ul. Rosoła. Awaria akumulatora w takim miejscu uniemożliwia tradycyjne holowanie.',
        'Akumulateo eliminuje ten problem. Przyjeżdżamy bezpośrednio pod Twój blok na Ursynowie, diagnozujemy układ ładowania i montujemy nowy, fabrycznie naładowany akumulator marek premium.',
        'Zapewniamy pełne wsparcie dla aut nowoczesnych wyposażonych w inteligentny sensor akumulatora (IBS) – kodujemy nowy akumulator testerem diagnostycznym na miejscu.'
      ],
      localLandmarks: [
        'Kabaty (Wąwozowa, Rosoła, al. KEN)',
        'Natolin (Belgradzka, Przy Bażantarni)',
        'Imielin i Stokłosy (Ciszewskiego, Jastrzębowskiego, Puławska)',
        'Zielony Ursynów, Grabów, Pyry, Dąbrówka',
        'Okolice Lasu Kabackiego i Centrum Onkologii'
      ]
    },
    servicesSection: {
      h2: 'Usługi akumulatorowe z dojazdem na Ursynowie',
      services: [
        {
          title: 'Wymiana Akumulatorów AGM i EFB (Start-Stop)',
          description: 'Dobór i profesjonalny montaż akumulatorów z technologią AGM/EFB dedykowanych do nowoczesnych aut z rekuperacją energii.'
        },
        {
          title: 'Awaryjny Rozruch Auta w Garażu Podziemnym',
          description: 'Bezpieczny rozruch profesjonalnymi boosterami litowo-jonowymi bez ryzyka przepięcia w instalacji elektronicznej.'
        },
        {
          title: 'Adaptacja Komputerowa BMS',
          description: 'Reset licznika cykli ładowania w sterowniku samochodu – gwarancja długiej żywotności nowej baterii.'
        },
        {
          title: 'Bezpłatna Utylizacja Starego Akumulatora',
          description: 'Zabieramy zużyty akumulator, wypełniamy kartę przekazania odpadu – brak konieczności płacenia 30 zł kaucji.'
        }
      ]
    },
    pricingAndEtaSection: {
      h2: 'Cennik pogotowia akumulatorowego – Ursynów',
      etaText: 'Średni czas dojazdu na Ursynowie: 15–25 minut, 24 godziny na dobę.',
      pricingItems: [
        {
          service: 'Awaryjny rozruch 12V',
          price: 'od 150 zł',
          details: 'Dojazd, bezpieczne odpalenie, test alternatora.'
        },
        {
          service: 'Wymiana baterii z montażem',
          price: 'od 150 zł + bateria',
          details: 'Dojazd, profesjonalny montaż, podtrzymanie zasilania, adaptacja BMS.'
        },
        {
          service: 'Kodowanie BMS / Adaptacja',
          price: 'w cenie wymiany',
          details: 'Komputerowa rejestracja akumulatora w sterowniku silnika.'
        }
      ]
    },
    faqSection: {
      h2: 'Pytania kierowców z Ursynowa (FAQ)',
      items: [
        {
          question: 'Czy muszę znać dokładny model akumulatora przed telefonem?',
          answer: 'Nie! Wystarczy, że podasz dyspozytorowi markę, model, rok produkcji auta i wersję silnikową. Nasz technik dobierze fabryczny rozmiar, pojemność (Ah), prąd rozruchowy (CCA) oraz właściwą technologię (AGM/EFB/kwasowy).'
        },
        {
          question: 'Czy dojeżdżacie w nocy na Ursynowie?',
          answer: 'Tak, działamy w trybie pogotowia 24h/7, również w niedziele i dni świąteczne. Dojeżdżamy na Kabaty, Imielin i w okolice Puławskiej o dowolnej porze.'
        },
        {
          question: 'Czy po wymianie akumulatora nie zresetują się zegary i radio?',
          answer: 'Prace wykonujemy z podłączeniem zasilania awaryjnego przez gniazdo OBD, dzięki czemu wszystkie ustawienia komfortu, stacje radiowe i pamięć szyb pozostają nienaruszone.'
        }
      ]
    },
    schemaJsonLd: `{
  "@context": "https://schema.org",
  "@type": "EmergencyService",
  "name": "Akumulateo – Pogotowie Akumulatorowe Warszawa Ursynów",
  "image": "https://www.akumulateo.pl/static/logo.png",
  "url": "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-ursynow",
  "telephone": "+48696556446",
  "priceRange": "$$",
  "areaServed": {
    "@type": "AdministrativeArea",
    "name": "Ursynów, Warszawa"
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "opens": "00:00",
    "closes": "23:59"
  },
  "description": "Pogotowie akumulatorowe Ursynów 24/7. Szybki dojazd z nowym akumulatorem, montaż, kodowanie BMS pod domem klienta."
}`
  },
  {
    slug: 'wola',
    districtName: 'Wola',
    isWarsawDistrict: true,
    eta: '15-25 minut',
    urlPath: '/wymiana-akumulatora-warszawa-wola',
    meta: {
      title: 'Pogotowie Akumulatorowe Warszawa Wola 24/7 – Wymiana z Dojazdem',
      description: 'Rozładowany akumulator na Woli (Odolany, Mirów, Koło, Czyste)? Wymiana akumulatora u klienta w 20 min. Diagnostyka, montaż i kodowanie 24h. Tel: 696 556 446.'
    },
    hero: {
      badge: '⚡ Pogotowie Akumulatorowe Wola 24h – Dojazd w 20 min',
      h1: 'Pogotowie Akumulatorowe Warszawa Wola 24/7',
      lead: 'Auto uwięzione na podziemnym parkingu na Odolanach lub pod biurowcem przy Rondzie Daszyńskiego? Przyjedziemy z nowym akumulatorem, zamontujemy go na miejscu i bezpiecznie uruchomimy Twój samochód.',
      ctaButtonText: 'Wezwij technika na Wolę: 696 556 446',
      phoneNumber: '696 556 446',
      trustNote: '⭐ 5.0 w Google | Parkingi podziemne | Szybki dojazd trasą Kasprzaka / Wolską'
    },
    whyMobileSection: {
      h2: 'Mobilny montaż akumulatora na Woli – Bez stania w korkach',
      paragraphs: [
        'Wola dynamicznie rośnie – nowe osiedla na Odolanach oraz centra biznesowe wokół Ronda Daszyńskiego i Towarowej generują ogromny ruch. Gdy w samochodzie pada akumulator, transport lawetą przez zatłoczoną Kasprzaka lub Wolską jest czasochłonny i kosztowny.',
        'Akumulateo to najwygodniejsze rozwiązanie. Technik przyjeżdża z dobranym akumulatorem prosto pod Twój blok, biurowiec lub na parking podziemny. Sprawdza instalację, zakłada nową baterię i zabiera zużytą.',
        'Nie prowadzimy sklepu stacjonarnego – jesteśmy pogotowiem mobilnym, dlatego oszczędzasz czas i nerwy.'
      ],
      localLandmarks: [
        'Odolany (Jana Kazimierza, Ordona, Kasprzaka)',
        'Centrum biznesowe Wola (Rondo Daszyńskiego, Towarowa, Prosta)',
        'Mirów i Czyste (Żelazna, Chłodna, Grzybowska)',
        'Koło i Młynów (Obozowa, Górczewska, Młynarska)',
        'Ulrychów (okolice Wola Park, Powstańców Śląskich)'
      ]
    },
    servicesSection: {
      h2: 'Zakres usług pogotowia akumulatorowego na Woli',
      services: [
        {
          title: 'Awaryjny Rozruch Samochodu',
          description: 'Uruchamianie aut benzynowych, diesli oraz hybryd przy użyciu bezpiecznych boosterów rozruchowych.'
        },
        {
          title: 'Montaż Akumulatora z Kodowaniem BMS',
          description: 'Wymiana akumulatorów kwasowo-ołowiowych, EFB oraz AGM z komputerową adaptacją w systemie pojazdu.'
        },
        {
          title: 'Pomiary Instalacji Elektrycznej',
          description: 'Diagnostyka alternatora, napięcia ładowania i prądu spoczynkowego (wykrywanie złodziei prądu).'
        },
        {
          title: 'Złomowanie i Utylizacja Starej Baterii',
          description: 'Odbiór zużytego akumulatora zgodnie z normami ochrony środowiska.'
        }
      ]
    },
    pricingAndEtaSection: {
      h2: 'Cennik i orientacyjny czas reakcji – Warszawa Wola',
      etaText: 'Średni czas dojazdu na terenie Woli: 15–25 minut (24/7).',
      pricingItems: [
        {
          service: 'Awaryjne odpalanie z boostera',
          price: 'od 150 zł',
          details: 'Bezpieczny rozruch 12V, test ładowania.'
        },
        {
          service: 'Wymiana akumulatora u klienta',
          price: 'od 150 zł + bateria',
          details: 'Dojazd, montaż, kodowanie komputerem, utylizacja.'
        },
        {
          service: 'Diagnostyka akumulatora',
          price: 'w cenie wymiany',
          details: 'Cyfrowy test stanu baterii i układu ładowania.'
        }
      ]
    },
    faqSection: {
      h2: 'Pytania mieszkańców Woli (FAQ)',
      items: [
        {
          question: 'Czy dojedziecie na nowe osiedla na Odolanach?',
          answer: 'Oczywiście. Regularnie obsługujemy klientów przy ul. Jana Kazimierza, Ordona, Kasprzaka i Wschowskiej, wjeżdżając do garaży podziemnych.'
        },
        {
          question: 'Ile trwa cała usługa na miejscu?',
          answer: 'Standardowa wymiana akumulatora wraz z diagnostyką i adaptacją komputerową zajmuje technikowi od 15 do 25 minut.'
        },
        {
          question: 'Czy otrzymam gwarancję na nowy akumulator?',
          answer: 'Tak, każdy akumulator posiada pełną gwarancję producenta (od 24 do 36 miesięcy) oraz kartę gwarancyjną podstemplowaną przez technika.'
        }
      ]
    },
    schemaJsonLd: `{
  "@context": "https://schema.org",
  "@type": "EmergencyService",
  "name": "Akumulateo – Pogotowie Akumulatorowe Warszawa Wola",
  "image": "https://www.akumulateo.pl/static/logo.png",
  "url": "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-wola",
  "telephone": "+48696556446",
  "priceRange": "$$",
  "areaServed": {
    "@type": "AdministrativeArea",
    "name": "Wola, Warszawa"
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "opens": "00:00",
    "closes": "23:59"
  },
  "description": "Mobilna wymiana akumulatora z dojazdem Warszawa Wola. Awaryjny rozruch, montaż i kodowanie akumulatorów 24/7."
}`
  },
  {
    slug: 'piaseczno',
    districtName: 'Piaseczno i Okolice',
    isWarsawDistrict: false,
    eta: '20-30 minut',
    urlPath: '/pogotowie-akumulatorowe-piaseczno',
    meta: {
      title: 'Pogotowie Akumulatorowe Piaseczno 24h | Wymiana Akumulatora z Dojazdem',
      description: 'Padł akumulator w Piasecznie, Józefosławiu lub Lesznowoli? Mobilny serwis 24/7. Przyjedziemy i wymienimy akumulator pod domem w 20-30 min. Tel: 696 556 446.'
    },
    hero: {
      badge: '⚡ Mobilny Serwis Akumulatorów 24h – Piaseczno i Powiat Piaseczyński',
      h1: 'Pogotowie Akumulatorowe Piaseczno 24/7 – Wymiana z Dojazdem',
      lead: 'Samochód nie chce odpalić w Piasecznie, Józefosławiu, Julianowie lub Zalesiu? Nie musisz organizować holowania do Warszawy. Nasz mobilny technik przyjedzie pod Twój adres z dobranym akumulatorem.',
      ctaButtonText: 'Zadzwoń po pomoc w Piasecznie: 696 556 446',
      phoneNumber: '696 556 446',
      trustNote: '⭐ 5.0 w Google | Szybki dojazd Puławską / trasą S79 | Płatność kartą i BLIK'
    },
    whyMobileSection: {
      h2: 'Dlaczego warto wezwać Akumulateo w Piasecznie i okolicach?',
      paragraphs: [
        'Piaseczno i przyległe miejscowości (Józefosław, Julianów, Mysiadło, Nowa Iwiczna, Lesznowola) to rejon o intensywnej zabudowie jednorodzinnej i apartamentowej. Kierowcy codziennie dojeżdżają stąd do centrum Warszawy.',
        'Poranny brak prądu w akumulatorze paraliżuje plany całego dnia. Zamiast szukać otwartego sklepu i wozić ciężką baterię w bagażniku innego auta, wystarczy jeden telefon do Akumulateo.',
        'Dzięki bliskości trasy ekspresowej S79 i ul. Puławskiej docieramy do Piaseczna i okolic zazwyczaj w 20–30 minut o każdej porze dnia i nocy.'
      ],
      localLandmarks: [
        'Piaseczno Centrum, Zalesie Dolne i Zalesie Górne',
        'Józefosław i Julianów (ul. Geodetów, Wilanowska, Cyraneczki)',
        'Nowa Iwiczna, Stara Iwiczna, Mysiadło',
        'Lesznowola, Nowa Wola, Zgorzała',
        'Konstancin-Jeziorna i Bielawa'
      ]
    },
    servicesSection: {
      h2: 'Kompletne usługi akumulatorowe – Piaseczno i aglomeracja',
      services: [
        {
          title: 'Dobór i Montaż Akumulatora pod Domem',
          description: 'Akumulatory AGM, EFB i standardowe z pełną gwarancją. Montaż bez wychodzenia z domu.'
        },
        {
          title: 'Kodowanie BMS i Adaptacja w Komputerze',
          description: 'Konieczne w nowszych autach (BMW, Audi, Mercedes, VW, Volvo) dla poprawnego ładowania akumulatora.'
        },
        {
          title: 'Awaryjny Rozruch na Posesji i w Garażu',
          description: 'Uruchamianie silników benzynowych i wysokoprężnych boosterem rozruchowym.'
        },
        {
          title: 'Odbiór i Utylizacja Zużytego Akumulatora',
          description: 'Odbieramy starą baterię, eliminując konieczność opłaty kaucji 30 zł w sklepie.'
        }
      ]
    },
    pricingAndEtaSection: {
      h2: 'Cennik usług pogotowia – Piaseczno i okolice',
      etaText: 'Średni czas dojazdu do Piaseczna: 20–30 minut (całodobowo).',
      pricingItems: [
        {
          service: 'Awaryjny rozruch boosterem',
          price: 'od 150 zł',
          details: 'Dojazd do Piaseczna/Józefosławia, odpalenie, test alternatora.'
        },
        {
          service: 'Wymiana z dojazdem i montażem',
          price: 'od 150 zł + akumulator',
          details: 'Dojazd, profesjonalny montaż, podtrzymanie pamięci, kodowanie BMS.'
        },
        {
          service: 'Diagnostyka instalacji',
          price: 'w cenie wymiany',
          details: 'Cyfrowy test akumulatora i układu ładowania.'
        }
      ]
    },
    faqSection: {
      h2: 'Najczęstsze pytania kierowców z Piaseczna (FAQ)',
      items: [
        {
          question: 'Czy pobieracie dodatkowe opłaty za dojazd poza granice Warszawy?',
          answer: 'Nasz koszt usługi jest w pełni transparentny i podawany z góry przez telefon przed wyjazdem technika. Nie ma żadnych ukrytych opłat za kilometry.'
        },
        {
          question: 'Czy obsługujecie również Józefosław i Konstancin-Jeziorną?',
          answer: 'Tak, obsługujemy cały powiat piaseczyński, w tym Józefosław, Julianów, Lesznowolę, Konstancin-Jeziorną i Górę Kalwarię.'
        },
        {
          question: 'Czy technik wystawia fakturę VAT?',
          answer: 'Tak, na każdą usługę oraz akumulator wystawiamy paragon lub fakturę VAT 23% na firmę.'
        }
      ]
    },
    schemaJsonLd: `{
  "@context": "https://schema.org",
  "@type": "EmergencyService",
  "name": "Akumulateo – Pogotowie Akumulatorowe Piaseczno",
  "image": "https://www.akumulateo.pl/static/logo.png",
  "url": "https://www.akumulateo.pl/pogotowie-akumulatorowe-piaseczno",
  "telephone": "+48696556446",
  "priceRange": "$$",
  "areaServed": {
    "@type": "AdministrativeArea",
    "name": "Piaseczno, powiat piaseczyński"
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "opens": "00:00",
    "closes": "23:59"
  },
  "description": "Całodobowe pogotowie akumulatorowe Piaseczno i okolice (Józefosław, Lesznowola). Wymiana akumulatora z dojazdem pod dom 24/7."
}`
  }
];

export class DistrictContentHelper {
  public static getAll(): DistrictContentPage[] {
    return DISTRICTS_CONTENT;
  }

  public static getBySlug(slug: string): DistrictContentPage | undefined {
    return DISTRICTS_CONTENT.find(d => d.slug.toLowerCase() === slug.toLowerCase());
  }

  /**
   * Zwraca gotowy kod HTML dla sekcji Hero danej dzielnicy do wklejenia w Code Block w Squarespace
   */
  public static renderHeroHtml(district: DistrictContentPage): string {
    return `
<div class="akumulateo-district-hero" style="background:#111; color:#fff; padding:40px 20px; text-align:center; border-radius:12px; margin-bottom:30px;">
  <span style="display:inline-block; background:#f59e0b; color:#000; font-weight:700; font-size:13px; padding:6px 14px; border-radius:20px; margin-bottom:16px;">
    ${district.hero.badge}
  </span>
  <h1 style="font-size:32px; font-weight:800; line-height:1.2; margin-bottom:16px; color:#ffffff;">
    ${district.hero.h1}
  </h1>
  <p style="font-size:16px; color:#d1d5db; max-width:700px; margin:0 auto 24px auto; line-height:1.5;">
    ${district.hero.lead}
  </p>
  <a href="tel:+48${district.hero.phoneNumber.replace(/\\s+/g, '')}" style="display:inline-flex; align-items:center; gap:10px; background:linear-gradient(135deg, #eab308 0%, #ca8a04 100%); color:#000; font-weight:800; font-size:18px; padding:16px 28px; border-radius:8px; text-decoration:none; box-shadow:0 4px 15px rgba(234,179,8,0.4);">
    📞 ${district.hero.ctaButtonText}
  </a>
  <div style="font-size:13px; color:#9ca3af; margin-top:14px;">
    ${district.hero.trustNote}
  </div>
</div>
`.trim();
  }
}
