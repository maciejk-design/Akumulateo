# Akumulateo – Brand Kit & UI Design System (v2.2)

Kompletny zestaw komponentów interfejsu (UI Kit), tokenów projektowych oraz gotowych do skopiowania szablonów HTML/CSS dla witryny **[https://www.akumulateo.pl](https://www.akumulateo.pl)** oraz wszystkich dedykowanych podstron dzielnicowych i aglomeracyjnych (np. Ursynów, Mokotów, Wola, Piastów, Brwinów, Milanówek, Legionowo, Modlin, Mińsk Mazowiecki).

Każdy komponent w tym zestawie został przetestowany pod kątem **zerowego przesunięcia układu (CLS = 0.00)**, pełnej responsywności na ekranach od **320px do 4K** oraz zgodności z wytycznymi WCAG AAA.

---

## 1. Tokeny Projektowe (Design Tokens)

### 1.1. Kolory (Color Tokens):
```css
/* Tła i Powierzchnie */
--akumulateo-bg-canvas: #020617;       /* Slate 950 - Główne tło witryny */
--akumulateo-bg-surface: #0f172a;      /* Slate 900 - Tło sekcji, nagłówek */
--akumulateo-bg-card: #1e293b;         /* Slate 800 - Standardowe karty cennika */
--akumulateo-bg-card-featured: #090e1a;/* Slate 950 głęboki - Karta wyróżniona */

/* Barwy Markowe i Akcenty */
--akumulateo-amber-primary: #f59e0b;  /* Główny bursztyn CTA, błyskawica, gwiazdki */
--akumulateo-amber-light: #fbbf24;    /* Bursztyn hover, gradient paska dyżuru */
--akumulateo-amber-dark: #d97706;     /* Ciemny bursztyn, obramowanie karty */
--akumulateo-emerald-live: #10b981;   /* Zielona pulsująca dioda dyżuru 24/7 */
--akumulateo-red-emergency: #ef4444;  /* Czerwień bieguna dodatniego (+), awarie */

/* Typografia i Kontrast (WCAG AAA) */
--akumulateo-text-white: #f8fafc;     /* Slate 50 - Nagłówki H1, H2, H3, ceny */
--akumulateo-text-body: #f1f5f9;      /* Slate 100 - GŁÓWNY TEKST OPISÓW I AKAPITÓW */
--akumulateo-text-muted: #cbd5e1;     /* Slate 300 - Dopiski techniczne */
--akumulateo-text-dark: #020617;      /* Ciemny tekst na żółtych/bursztynowych tłach */

/* Obramowania i Linie Podziału */
--akumulateo-border-subtle: #334155;  /* Slate 700 - Obramowanie kart standardowych */
--akumulateo-border-amber: #f59e0b;   /* Obramowanie karty wyróżnionej */

/* Cienie i Efekty Glow */
--akumulateo-shadow-amber: 0 10px 30px -10px rgba(245, 158, 11, 0.35);
--akumulateo-shadow-card: 0 10px 25px -5px rgba(0, 0, 0, 0.5);

/* Hierarchia Z-Index (Zabezpieczenie przed kolizjami) */
--akumulateo-z-header: 50;
--akumulateo-z-sticky-bar: 9999;
--akumulateo-z-cookie-banner: 10000005; /* ZAWSZE PONAD PASKIEM TELEFONICZNYM! */
```

### 1.2. Żelazne Reguły Wielkości Fontów (Typography Rules):
1. **Opisy usług i akapity (`<p>`):**
   * Mobile (<=640px): **15.5px !important**, line-height: **1.65 !important**, color: `#f1f5f9 !important`.
   * Desktop (>640px): **16.5px !important**, line-height: **1.70 !important**, color: `#f1f5f9 !important`.
   * ❌ **ZAKAZ:** fontów 11–12px w opisach ofertowych.
2. **Nagłówki H1:** 30–36px mobile / 44–50px desktop, font-black (900).
3. **Nagłówki H2:** 22–26px mobile / 30–36px desktop, font-bold (800).
4. **Nagłówki H3 (Karty):** 18–20px mobile / 20–22px desktop, font-bold (800).
5. **Ceny:** 22–26px mobile / 24–28px desktop, font-black (900), kolor `#f59e0b`.
6. **Tagi / Metki:** 13–13.5px, font-bold (700).

---

## 2. Biblioteka Wzorcowych Komponentów HTML/CSS

### 2.1. Komponent 1: Top Emergency Bar (Pasek Dyżuru 24h)
Gwarantuje brak ucinania tekstu nawet na wąskich smartfonach (320px).

```html
<!-- TOP EMERGENCY BAR 24H -->
<div class="akumulateo-top-bar bg-gradient-to-r from-amber-500 via-amber-400 to-amber-500 text-slate-950 py-1.5 px-3 sm:px-4 text-xs font-black tracking-wide shadow-sm">
  <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-x-2.5 gap-y-1">
    
    <!-- Status Dyżuru -->
    <div class="flex items-center space-x-1.5">
      <span class="inline-block w-2.5 h-2.5 bg-emerald-700 rounded-full animate-pulse shadow-sm"></span>
      <span class="uppercase tracking-wider">DYŻUR POGOTOWIA 24H/7</span>
      <span class="hidden xs:inline text-slate-800 font-bold">• Warszawa i okolice</span>
    </div>

    <!-- Dowód Społeczny / Język -->
    <div class="flex items-center space-x-3 text-slate-950 text-right">
      <span class="hidden sm:inline font-bold">🇬🇧 We speak English</span>
      <a href="https://g.page/r/CXjN9llopHR_EBM/" target="_blank" rel="noopener noreferrer" 
         class="inline-flex items-center font-black hover:underline transition-all">
        ⭐ 5.0 w Google (100+ opinii) ↗
      </a>
    </div>

  </div>
</div>
```

---

### 2.2. Komponent 2: Mobility Notice Banner (Brak Odbioru Osobistego)
Chroni budżet reklamowy i natychmiast uświadamia klienta o dojeździe.

```html
<!-- MOBILITY NOTICE BANNER -->
<div class="max-w-5xl mx-auto mb-8 px-4">
  <div class="bg-gradient-to-r from-amber-500/10 via-slate-900 to-amber-500/10 border-2 border-amber-500/40 rounded-2xl p-4 sm:p-5 text-center shadow-lg">
    <div class="inline-flex items-center space-x-2 text-amber-400 font-black text-sm uppercase tracking-wider mb-1">
      <svg class="w-5 h-5 text-amber-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>
      </svg>
      <span>WAŻNA INFORMACJA DLA KLIENTÓW</span>
    </div>
    <p class="text-[15.5px] sm:text-base font-medium text-slate-100 leading-relaxed max-w-3xl mx-auto">
      Akumulateo jest <strong>w 100% mobilnym pogotowiem akumulatorowym</strong>. Nie prowadzimy sklepu stacjonarnego ani punktu odbioru osobistego – 
      <strong class="text-amber-400">dojeżdżamy bezpośrednio pod wskazany adres</strong> w Warszawie oraz okolicach z pełnym wyposażeniem diagnostycznym i nową baterią.
    </p>
  </div>
</div>
```

---

### 2.3. Komponent 3: Karta Standardowa Cennika (np. Awaryjny Rozruch / Diagnostyka)

```html
<!-- STANDARD PRICING CARD -->
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-5 sm:p-6 shadow-lg flex flex-col justify-between hover:border-slate-700 transition-all">
  <div>
    <!-- Nagłówek i Cena -->
    <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-1 sm:gap-4 mb-2.5">
      <h3 class="text-lg sm:text-xl font-bold text-white tracking-tight">Awaryjny Rozruch z Dojazdem</h3>
      <div class="text-xl sm:text-2xl font-black text-amber-400 whitespace-nowrap">od 100 zł</div>
    </div>
    
    <!-- Opis Usługi (Ścisły standard typografii: min 15.5px mobile / 16.5px desktop) -->
    <p class="text-[15.5px] sm:text-[16.5px] text-slate-100 font-normal leading-relaxed mb-4">
      Dojazd technika, bezpieczne uruchomienie profesjonalnym boosterem mikroprocesorowym (12V/24V) oraz komputerowy test parametrów ładowania alternatora.
    </p>
  </div>

  <div>
    <!-- Tagi Korzyści -->
    <div class="flex flex-wrap gap-2 pt-2 border-t border-slate-800/80">
      <span class="inline-flex items-center bg-slate-800/80 border border-slate-700/60 text-slate-200 text-xs sm:text-[13px] font-bold px-3 py-1.5 rounded-lg">
        ⏱️ Czas dojazdu: 20-30 min
      </span>
      <span class="inline-flex items-center bg-slate-800/80 border border-slate-700/60 text-slate-200 text-xs sm:text-[13px] font-bold px-3 py-1.5 rounded-lg">
        ⚡ Bezpieczne dla elektroniki
      </span>
    </div>
  </div>
</div>
```

---

### 2.4. Komponent 4: Karta Wyróżniona („Najczęściej Wybierana Usługa”)
Wzorzec dla najważniejszej usługi generującej najwyższy zysk netto (Wymiana Akumulatora z Montażem i Kodowaniem).

```html
<!-- FEATURED PRICING CARD (NAJCZĘŚCIEJ WYBIERANA USŁUGA) -->
<div class="bg-slate-950 border-2 border-amber-500 rounded-2xl p-5 sm:p-6 shadow-xl relative flex flex-col justify-between akumulateo-featured-card">
  <div>
    <!-- Wyróżniająca Pigułka Statusowa -->
    <div class="inline-flex items-center bg-amber-500 text-slate-950 text-xs font-black uppercase tracking-wider px-3.5 py-1 rounded-full mb-3 shadow-md">
      ★ Najczęściej Wybierana Usługa
    </div>

    <!-- Tytuł i Cena (Elastyczny układ kolumna/wiersz zapobiegający ucinaniu) -->
    <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-1 sm:gap-4 mb-2.5">
      <h3 class="text-xl sm:text-2xl font-black text-white tracking-tight">Wymiana Akumulatora + Kodowanie BMS</h3>
      <div class="text-xl sm:text-2xl font-black text-amber-400 whitespace-nowrap">od 150 zł <span class="text-xs font-normal text-slate-300">+ koszt baterii</span></div>
    </div>

    <!-- Opis Usługi (Wysoki kontrast, min 15.5px) -->
    <p class="text-[15.5px] sm:text-[16.5px] text-slate-100 font-normal leading-relaxed mb-4">
      Dowóz fabrycznie nowego akumulatora (Varta, Yuasa, Bosch), demontaż starego, podtrzymanie zasilania OBD, montaż oraz elektroniczna adaptacja komputerowa BMS dla systemów Start-Stop.
    </p>
  </div>

  <div>
    <!-- Tagi Korzyści (Wyrazisty bursztynowy akcent) -->
    <div class="flex flex-wrap gap-2 pt-2 border-t border-amber-500/20">
      <span class="inline-flex items-center bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs sm:text-[13px] font-bold px-3 py-1.5 rounded-lg">
        ✓ Podtrzymanie pamięci OBD
      </span>
      <span class="inline-flex items-center bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs sm:text-[13px] font-bold px-3 py-1.5 rounded-lg">
        ✓ Adaptacja komputerowa BMS
      </span>
      <span class="inline-flex items-center bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs sm:text-[13px] font-bold px-3 py-1.5 rounded-lg">
        ✓ Bezpłatny odbiór starej baterii
      </span>
    </div>
  </div>
</div>
```

---

### 2.5. Komponent 5: Pasek Zaufania w Hero (Social Proof Grid 2x2 na Mobile)

```html
<!-- TRUST BADGES 2X2 MOBILE / 4X1 DESKTOP -->
<div class="grid grid-cols-2 lg:grid-cols-4 gap-2.5 sm:gap-4 max-w-5xl mx-auto my-6">
  
  <div class="bg-slate-900/90 border border-slate-800 p-3 sm:p-4 rounded-xl text-center">
    <div class="text-amber-400 font-black text-base sm:text-lg">⭐ 5.0 w Google</div>
    <div class="text-slate-300 text-xs sm:text-sm font-medium">Ponad 100 autentycznych opinii</div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 p-3 sm:p-4 rounded-xl text-center">
    <div class="text-amber-400 font-black text-base sm:text-lg">⚡ 20–30 minut</div>
    <div class="text-slate-300 text-xs sm:text-sm font-medium">Średni czas dojazdu w Warszawie</div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 p-3 sm:p-4 rounded-xl text-center">
    <div class="text-amber-400 font-black text-base sm:text-lg">💳 Karta / BLIK</div>
    <div class="text-slate-300 text-xs sm:text-sm font-medium">Mobilny terminal u technika</div>
  </div>

  <div class="bg-slate-900/90 border border-slate-800 p-3 sm:p-4 rounded-xl text-center">
    <div class="text-amber-400 font-black text-base sm:text-lg">🛡️ Gwarancja do 3 lat</div>
    <div class="text-slate-300 text-xs sm:text-sm font-medium">Faktura VAT 23% + karta gwarancyjna</div>
  </div>

</div>
```

---

### 2.6. Komponent 6: Sticky Call Bar & GDPR Cookie Banner Sync
Wklejany w **Footer Code Injection** witryny.

```html
<!-- FOOTER CODE INJECTION – STICKY BAR + COOKIE BANNER SYNC -->
<style>
  #akumulateo-sticky-call-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 9999;
    padding: 10px 12px calc(10px + env(safe-area-inset-bottom, 0px)) 12px;
    background: linear-gradient(180deg, rgba(2, 6, 23, 0) 0%, rgba(2, 6, 23, 0.95) 25%, #020617 100%);
    pointer-events: none;
    display: none;
  }
  @media (max-width: 768px) {
    #akumulateo-sticky-call-bar {
      display: block;
    }
  }
  #akumulateo-sticky-call-bar a {
    pointer-events: auto;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    width: 100%;
    min-height: 54px;
    background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
    color: #020617;
    font-size: 16px;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-radius: 14px;
    text-decoration: none;
    box-shadow: 0 4px 20px rgba(245, 158, 11, 0.45);
  }
  .akumulateo-pulse-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: #10b981;
    box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7);
    animation: akumulateo-pulse 1.8s infinite;
  }
  @keyframes akumulateo-pulse {
    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
    70% { transform: scale(1); box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
  }

  /* KRYTYCZNA REGUŁA: Z-INDEX DLA BANERA GDPR SQUARESPACE */
  .gdpr-cookie-banner,
  .cookie-banner-mount-point,
  .sqs-cookie-banner-v2,
  .sqs-cookie-banner-v2-container,
  [data-cookie-banner] {
    z-index: 10000005 !important;
  }
</style>

<div id="akumulateo-sticky-call-bar">
  <a href="tel:+48696556446">
    <span class="akumulateo-pulse-dot"></span>
    <span>Zadzwoń: 696 556 446</span>
    <span style="font-size: 11px; opacity: 0.85; font-weight: 700; margin-left: 2px;">• 24H</span>
  </a>
</div>

<script>
(function() {
  function syncCookieBannerWithStickyBar() {
    var banner = document.querySelector('.gdpr-cookie-banner, .cookie-banner-mount-point, .sqs-cookie-banner-v2, [data-cookie-banner], .manage-cookies-bar');
    var bar = document.getElementById('akumulateo-sticky-call-bar');
    if (!bar) return;
    
    var isBannerActive = banner && (banner.offsetHeight > 0 || (banner.children && banner.children.length > 0)) && window.getComputedStyle(banner).display !== 'none' && window.getComputedStyle(banner).visibility !== 'hidden';
    
    if (isBannerActive) {
      bar.style.setProperty('display', 'none', 'important');
      document.body.style.setProperty('padding-bottom', '0px', 'important');
    } else {
      if (window.innerWidth <= 768) {
        bar.style.removeProperty('display');
        document.body.style.setProperty('padding-bottom', '74px', 'important');
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', syncCookieBannerWithStickyBar);
  } else {
    syncCookieBannerWithStickyBar();
  }
  window.addEventListener('load', syncCookieBannerWithStickyBar);
  setInterval(syncCookieBannerWithStickyBar, 250);
})();
</script>
```

---

## 3. Żelazne Wytyczne Anty-Błędowe (Anti-Error Rules dla Dewelopera)

1. **Nigdy nie wklejaj czystego CSS do Header Code Injection:**
   * Style globalne wklejaj wyłącznie do **Website Tools -> Custom CSS**.
   * Jeśli wstrzykujesz styl do strony w nagłówku, **ZAWSZE zamykaj go w znacznikach `<style>...</style>`**.
2. **Zachowuj minimalne wielkości fontów:**
   * Żaden akapit nie może spaść poniżej `15.5px` na telefonie. Stosuj klasę `text-[15.5px] sm:text-[16.5px] text-slate-100 leading-relaxed`.
3. **Zawsze stosuj flex-wrap na paskach statusowych:**
   * Wąskie ekrany (iPhone SE, Galaxy Z Flip w trybie pionowym – 320–360px) wymagają zawijania elementów lub ukrywania opcjonalnych dopisków (`hidden xs:inline`).
4. **Weryfikuj tryb Incognito:**
   * Każde wdrożenie sprawdzaj w nowym oknie incognito, aby zweryfikować czy baner ciasteczek nie nakłada się na przyciski mobilne.
5. **Cenzura marek Centra i Banner:**
   * Wszelkie wzmianki o akumulatorach zastępuj markami: **Yuasa, Varta, Bosch, 4Max**.

---
*Akumulateo Brand Kit & Design System v2.2 | Wrzesień 2026*
