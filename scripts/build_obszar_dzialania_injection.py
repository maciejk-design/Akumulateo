#!/usr/bin/env python3
"""
Buduje snippets/squarespace/obszar-dzialania-page-header-injection.html
dla strony /obszar-dzialania-warszawa-i-okolice (Squarespace 7.1).
Wdraża standard Brandbook v2.2:
- Pełny Schema.org EmergencyService JSON-LD
- Style scoped (#collection-6a8c92622180ae5dca0135cf)
- Szablon <template id="akumulateo-obszar-template"> z 33 kafelkami (18 dzielnic + 15 miast)
- Natychmiastowy skrypt montażu (zero opóźnienia DOM)
"""

import os
import re

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    hub_file = os.path.join(base_dir, "snippets", "squarespace", "obszar-dzialania-hub.html")
    out_file = os.path.join(base_dir, "snippets", "squarespace", "obszar-dzialania-page-header-injection.html")

    with open(hub_file, "r", encoding="utf-8") as f:
        hub_raw = f.read()

    schema_match = re.search(r'(<script type="application/ld\+json">[\s\S]*?</script>)', hub_raw)
    if not schema_match:
        raise ValueError("Nie znaleziono tagu Schema.org JSON-LD w pliku hub_raw")
    schema_part = schema_match.group(1).strip()

    html_match = re.search(r'(<div class="akumulateo-root[\s\S]*?</div>)\s*$', hub_raw.strip())
    if not html_match:
        raise ValueError("Nie znaleziono sekcji div.akumulateo-root w pliku hub_raw")
    html_part = html_match.group(1).strip()

    styles_part = """<style id="akumulateo-obszar-custom-styles">
#collection-6a8c92622180ae5dca0135cf {
  background-color: #020617 !important;
}

/* Ukrycie przestarzałej sekcji z surowym tekstem w Squarespace */
#collection-6a8c92622180ae5dca0135cf section[data-section-id="6a8c9270e600463300572a53"],
#collection-6a8c92622180ae5dca0135cf .fe-6a8c9270c7617d7cc5094ae8 {
  display: none !important;
}

/* Eliminacja nadmiarowych paddingów szablonu */
#collection-6a8c92622180ae5dca0135cf #page-regions,
#collection-6a8c92622180ae5dca0135cf main#page,
#collection-6a8c92622180ae5dca0135cf section.page-section:first-child {
  padding-top: 15px !important;
  padding-bottom: 20px !important;
}

#collection-6a8c92622180ae5dca0135cf .content-wrapper {
  padding: 0 !important;
  max-width: 100% !important;
}

/* Responsywność kafelków */
#akumulateo-obszar-wrapper a:hover {
  border-color: #f59e0b !important;
  transform: translateY(-2px);
}
</style>"""

    mounting_script = """<script>
(function() {
  function mountAkumulateoObszar() {
    if (document.getElementById('akumulateo-obszar-wrapper')) return true;
    
    var tpl = document.getElementById('akumulateo-obszar-template');
    if (!tpl) return false;
    
    var targetSection = document.querySelector('section[data-section-id="6a8c9270e600463300572a53"]');
    var parent = targetSection ? targetSection.parentNode : 
                 (document.querySelector('#sections') || 
                  document.querySelector('main#page') || 
                  document.querySelector('#page') || 
                  document.body);
    if (!parent) return false;
    
    var wrapper = document.createElement('div');
    wrapper.id = 'akumulateo-obszar-wrapper';
    wrapper.appendChild(tpl.content.cloneNode(true));
    
    if (targetSection) {
      parent.insertBefore(wrapper, targetSection);
    } else if (parent.firstChild) {
      parent.insertBefore(wrapper, parent.firstChild);
    } else {
      parent.appendChild(wrapper);
    }
    return true;
  }

  // 1. Natychmiastowa próba montażu
  if (!mountAkumulateoObszar()) {
    // 2. MutationObserver montujący treść natychmiast gdy powstaje DOM
    if (window.MutationObserver) {
      var obs = new MutationObserver(function() {
        if (mountAkumulateoObszar()) {
          obs.disconnect();
        }
      });
      obs.observe(document.documentElement, { childList: true, subtree: true });
    }
    // 3. Fallback DOMContentLoaded / load
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', mountAkumulateoObszar);
    }
    window.addEventListener('load', mountAkumulateoObszar);
  }
})();
</script>"""

    injection_code = f"""<!-- ========================================================
     AKUMULATEO – OBSZAR DZIAŁANIA PAGE HEADER INJECTION (SQUARESPACE 7.1)
     Dedykowany dla: /obszar-dzialania-warszawa-i-okolice (collection-6a8c92622180ae5dca0135cf)
     ======================================================== -->

<!-- 1. USTRUKTURYZOWANE DANE SCHEMA.ORG EMERGENCY SERVICE (5.0★) -->
{schema_part}

<!-- 2. STYLE IZOLUJĄCE I UKRYWAJĄCE PRZESTARZAŁĄ SEKCJĘ FLUID ENGINE -->
{styles_part}

<!-- 3. TEMPLATE DZIELNIC I AGLOMERACJI AKUMULATEO -->
<template id="akumulateo-obszar-template">
{html_part}
</template>

<!-- 4. NATYCHMIASTOWY SKRYPT MONTAŻU (HIGH SPEED SSR EMULATION) -->
{mounting_script}
"""

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(injection_code)

    print(f"✅ Zbudowano: {out_file} ({len(injection_code)} znaków)")

if __name__ == "__main__":
    main()
