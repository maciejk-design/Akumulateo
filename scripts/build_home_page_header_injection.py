#!/usr/bin/env python3
"""
Rebuilds snippets/squarespace/home-page-header-injection.html
from snippets/squarespace/homepage-content.html and the optimized, inlined Tailwind CSS.
Eliminates external render-blocking CDN requests (was 2.86MB -> now 20KB).
Uses instant MutationObserver mounting instead of waiting for DOMContentLoaded (zero LCP delay).
"""
import os

def main():
    with open('snippets/squarespace/homepage-content.html', 'r', encoding='utf-8') as f:
        homepage_content = f.read().strip()

    with open('snippets/squarespace/compiled-tailwind.min.css', 'r', encoding='utf-8') as f:
        compiled_tailwind = f.read().strip()

    header_wrapper = f"""<!-- 1. ZOPTYMALIZOWANY WEWNĘTRZNY TAILWIND CSS (ZERO ZEWNĘTRZNYCH ZAPYTAŃ CDN, ZERO RENDER-BLOCKING) -->
<style id="akumulateo-optimized-tailwind">
{compiled_tailwind}
</style>

<!-- 2. DESIGN SYSTEM AKUMULATEO – GLOBALNE STYLE STRONY GŁÓWNEJ -->
<style id="akumulateo-home-custom-styles">
/* ========================================================
   AKUMULATEO – HOMEPAGE ISOLATION & DESIGN SYSTEM (SQUARESPACE 7.1)
   ======================================================== */

/* 1. Ukrycie szablonu Squarespace na stronie głównej */
body.homepage #header,
body.homepage footer.sections,
body.homepage #footer-sections,
body.homepage #page-regions > section.region > section[data-test="page-section"],
body.homepage #sections > section {{
  display: none !important;
}}

/* 2. Pełna szerokość i eliminacja marginesów Squarespace */
body.homepage #page,
body.homepage #page-regions,
body.homepage section.region,
body.homepage main#page {{
  padding: 0 !important;
  margin: 0 !important;
  max-width: 100% !important;
  width: 100% !important;
}}

#akumulateo-home-wrapper {{
  display: block !important;
  width: 100% !important;
  margin: 0 !important;
  padding: 0 !important;
  background-color: #020617 !important;
}}

/* 3. Główny Reset Kontenera */
.akumulateo-root {{
  background-color: #030712 !important;
  color: #f8fafc !important;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
  line-height: 1.5 !important;
}}

/* 4. Ścisłe wymiary logo (eliminacja rozciągnięcia SVG) */
.akumulateo-root .w-9,
.akumulateo-root svg[viewBox="0 0 68 68"] {{
  width: 36px !important;
  height: 36px !important;
  min-width: 36px !important;
  min-height: 36px !important;
  max-width: 36px !important;
  max-height: 36px !important;
}}

/* 5. TOP EMERGENCY BAR (PASEK DYŻURU 24H) */
.akumulateo-root > div:first-child,
.akumulateo-top-bar {{
  background: linear-gradient(90deg, #f59e0b 0%, #fbbf24 50%, #f59e0b 100%) !important;
  color: #020617 !important;
}}
.akumulateo-root > div:first-child *,
.akumulateo-top-bar * {{
  color: #020617 !important;
}}

/* 6. NAWIGACJA & PRZYCISKI CALL-TO-ACTION */
.akumulateo-root header {{
  background-color: rgba(15, 23, 42, 0.95) !important;
  backdrop-filter: blur(12px) !important;
  border-bottom: 1px solid #1e293b !important;
}}

.akumulateo-root a[href^="tel:"].bg-gradient-to-r,
.akumulateo-root a.bg-gradient-to-r,
.akumulateo-btn-call,
.akumulateo-btn-primary {{
  background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%) !important;
  color: #020617 !important;
  font-weight: 900 !important;
  text-decoration: none !important;
  box-shadow: 0 4px 15px rgba(245, 158, 11, 0.35) !important;
  border: none !important;
}}

.akumulateo-root a[href^="tel:"].bg-gradient-to-r *,
.akumulateo-root a.bg-gradient-to-r *,
.akumulateo-btn-call *,
.akumulateo-btn-primary * {{
  color: #020617 !important;
}}

/* 7. TYPOGRAFIA I KONTRAST TEKSTÓW (ŻELAZNY STANDARD BRANDBOOK v2.2) */
.akumulateo-root h1,
.akumulateo-root h2,
.akumulateo-root h3,
.akumulateo-root .text-white {{
  color: #ffffff !important;
}}

.akumulateo-root p {{
  color: #f1f5f9 !important;
  font-size: 15.5px !important;
  line-height: 1.65 !important;
}}
@media (min-width: 640px) {{
  .akumulateo-root p {{
    font-size: 16.5px !important;
    line-height: 1.7 !important;
  }}
}}

.akumulateo-root .text-slate-100 {{ color: #f8fafc !important; }}
.akumulateo-root .text-slate-200 {{ color: #f1f5f9 !important; }}
.akumulateo-root .text-slate-300 {{ color: #e2e8f0 !important; }}
.akumulateo-root .text-slate-400 {{ color: #94a3b8 !important; }}
.akumulateo-root .text-slate-500 {{ color: #64748b !important; }}
.akumulateo-root .text-slate-900 {{ color: #0f172a !important; }}
.akumulateo-root .text-slate-950 {{ color: #020617 !important; }}

.akumulateo-root .text-amber-300 {{ color: #fcd34d !important; }}
.akumulateo-root .text-amber-400 {{ color: #fbbf24 !important; }}
.akumulateo-root .text-amber-500 {{ color: #f59e0b !important; }}
.akumulateo-root .text-amber-600 {{ color: #d97706 !important; }}
.akumulateo-root .text-emerald-400 {{ color: #34d399 !important; }}
.akumulateo-root .text-emerald-500 {{ color: #10b981 !important; }}
.akumulateo-root .text-blue-400 {{ color: #60a5fa !important; }}
.akumulateo-root .text-red-400 {{ color: #f87171 !important; }}

/* 8. TŁA, KARTY I BORDERY */
.akumulateo-root .bg-slate-900 {{ background-color: #0f172a !important; }}
.akumulateo-root .bg-slate-900\\/95 {{ background-color: rgba(15, 23, 42, 0.95) !important; }}
.akumulateo-root .bg-slate-800 {{ background-color: #1e293b !important; }}
.akumulateo-root .bg-slate-800\\/80 {{ background-color: rgba(30, 41, 59, 0.8) !important; }}
.akumulateo-root .bg-slate-800\\/50 {{ background-color: rgba(30, 41, 59, 0.5) !important; }}
.akumulateo-root .bg-slate-950 {{ background-color: #020617 !important; }}
.akumulateo-root .bg-slate-950\\/80 {{ background-color: rgba(2, 6, 23, 0.8) !important; }}

.akumulateo-root .bg-amber-500\\/10 {{ background-color: rgba(245, 158, 11, 0.1) !important; }}
.akumulateo-root .bg-amber-500\\/20 {{ background-color: rgba(245, 158, 11, 0.2) !important; }}
.akumulateo-root .bg-emerald-500\\/20 {{ background-color: rgba(16, 185, 129, 0.2) !important; }}
.akumulateo-root .bg-blue-500\\/20 {{ background-color: rgba(59, 130, 246, 0.2) !important; }}
.akumulateo-root .bg-red-500\\/20 {{ background-color: rgba(239, 68, 68, 0.2) !important; }}

.akumulateo-root .border-slate-800 {{ border-color: #1e293b !important; }}
.akumulateo-root .border-slate-700 {{ border-color: #334155 !important; }}
.akumulateo-root .border-slate-700\\/60 {{ border-color: rgba(51, 65, 85, 0.6) !important; }}
.akumulateo-root .border-slate-700\\/70 {{ border-color: rgba(51, 65, 85, 0.7) !important; }}
.akumulateo-root .border-amber-500\\/30 {{ border-color: rgba(245, 158, 11, 0.3) !important; }}
.akumulateo-root .border-amber-500\\/20 {{ border-color: rgba(245, 158, 11, 0.2) !important; }}

.akumulateo-root .bg-gradient-to-b.from-slate-900 {{
  background: linear-gradient(180deg, #0f172a 0%, #0b1120 50%, #020617 100%) !important;
}}

/* 9. KARTA WYRÓŻNIONA (NAJCZĘŚCIEJ WYBIERANA USŁUGA) */
.akumulateo-root .akumulateo-featured-card {{
  border: 2px solid #f59e0b !important;
  box-shadow: 0 10px 30px -10px rgba(245, 158, 11, 0.35) !important;
  background: linear-gradient(145deg, #090e1a 0%, #0f172a 100%) !important;
}}

.akumulateo-root .akumulateo-featured-card .bg-amber-500,
.akumulateo-root .bg-amber-500 {{
  background-color: #f59e0b !important;
  color: #020617 !important;
}}

.akumulateo-root .akumulateo-featured-card .bg-amber-500 *,
.akumulateo-root .bg-amber-500 * {{
  color: #020617 !important;
}}

/* 10. KARTY ZAUFANIA (TRUST BAR) */
.akumulateo-root .grid.grid-cols-2 > div {{
  background-color: #0f172a !important;
  border: 1px solid #1e293b !important;
  color: #f1f5f9 !important;
}}
.akumulateo-root .grid.grid-cols-2 > div * {{
  color: inherit;
}}
.akumulateo-root .grid.grid-cols-2 > div .text-amber-400 {{
  color: #fbbf24 !important;
}}
.akumulateo-root .grid.grid-cols-2 > div .text-slate-400 {{
  color: #94a3b8 !important;
}}

/* 11. SUBTELNA ANIMACJA DIODY STATUSOWEJ */
@keyframes akumulateo-pulse {{
  0% {{ transform: scale(0.95); opacity: 0.85; }}
  50% {{ transform: scale(1.15); opacity: 1; }}
  100% {{ transform: scale(0.95); opacity: 0.85; }}
}}
.akumulateo-pulse-dot {{
  animation: akumulateo-pulse 2s infinite ease-in-out;
}}

/* 12. WYMUSZENIE WIDOCZNOŚCI I BRAKU PRZESUNIĘĆ (CLS = 0) */
#akumulateo-home-wrapper {{
  contain: content;
}}
</style>

<!-- 3. TEMPLATE STRONY GŁÓWNEJ (NATYCHMIASTOWE RENDEROWANIE) -->
<template id="akumulateo-home-template">
"""

    footer_wrapper = """</template>

<!-- 4. NATYCHMIASTOWY SKRYPT MONTAŻU (ZERO OPÓŹNIENIA DOMCONTENTLOADED / HIGH SPEED SSR EMULATION) -->
<script>
(function() {
  function mountAkumulateoHome() {
    if (document.getElementById('akumulateo-home-wrapper')) return true;
    
    var tpl = document.getElementById('akumulateo-home-template');
    if (!tpl) return false;
    
    var parent = document.querySelector('#page-regions > section.region') || 
                 document.querySelector('#page-regions') || 
                 document.querySelector('main#page') || 
                 document.body;
    if (!parent) return false;
    
    var wrapper = document.createElement('div');
    wrapper.id = 'akumulateo-home-wrapper';
    wrapper.appendChild(tpl.content.cloneNode(true));
    
    if (parent.firstChild) {
      parent.insertBefore(wrapper, parent.firstChild);
    } else {
      parent.appendChild(wrapper);
    }
    
    // Zastosuj centralną konfigurację ocen i linków do opinii Google
    try {
      var cfg = window.AKUMULATEO_CONFIG || {
        reviewsCount: "100+",
        ratingValue: "5.0",
        googleMapsUrl: "https://g.page/r/CXjN9llopHR_EBM/"
      };
      var elements = wrapper.querySelectorAll('[data-ak-cfg]');
      for (var i = 0; i < elements.length; i++) {
        var el = elements[i];
        var key = el.getAttribute('data-ak-cfg');
        if (key === 'googleMapsUrl' && el.tagName === 'A') {
          if (cfg.googleMapsUrl) el.href = cfg.googleMapsUrl;
        } else if (cfg[key]) {
          el.textContent = cfg[key];
        }
      }
    } catch(e) {
      console.warn('Config error:', e);
    }
    return true;
  }

  // 1. Natychmiastowa próba montażu
  if (!mountAkumulateoHome()) {
    // 2. Błyskawiczny MutationObserver montujący treść natychmiast gdy powstaje <body> (bez czekania na DOMContentLoaded)
    if (window.MutationObserver) {
      var obs = new MutationObserver(function() {
        if (mountAkumulateoHome()) {
          obs.disconnect();
        }
      });
      obs.observe(document.documentElement, { childList: true, subtree: true });
    }
    // 3. Fallback dla pełnego bezpieczeństwa
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', mountAkumulateoHome);
    }
    window.addEventListener('load', mountAkumulateoHome);
  }
})();
</script>
"""

    full_content = header_wrapper + homepage_content + footer_wrapper
    with open('snippets/squarespace/home-page-header-injection.html', 'w', encoding='utf-8') as f:
        f.write(full_content)

    print(f"Successfully generated home-page-header-injection.html ({len(full_content)} chars)")

if __name__ == '__main__':
    main()
