#!/usr/bin/env python3
"""
Automatyczny skrypt do sekwencyjnego wdrożenia pozostałych 13 miejscowości aglomeracji:
Piastów, Brwinów, Milanówek, Legionowo, Modlin, Nowy Dwór Mazowiecki,
Mińsk Mazowiecki, Konstancin-Jeziorna, Łomianki, Otwock, Marki,
Grodzisk Mazowiecki, Wołomin.

Po wdrożeniu aktualizuje stronę Hub z wszystkimi 33 odnośnikami.
"""

import os
import sys
import time
import subprocess

from deploy_district import deploy_district, get_chrome_sqs_tab, ensure_pages_panel, run_js
from build_agglomeration_snippets import AGGLOMERATION_TOWNS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPETS_DIR = os.path.join(BASE_DIR, "snippets", "squarespace")

def main():
    # Pomijamy Pruszków, który już został wdrożony
    towns_to_deploy = [t for t in AGGLOMERATION_TOWNS if t["slug"] != "pruszkow"]

    print("==================================================================")
    print("🚀 ROZPOCZYNAM AUTOMATYCZNE WDROŻENIE 13 MIEJSCOWOŚCI AGLOMERACJI")
    print(f"Liczba miejscowości w kolejce: {len(towns_to_deploy)}")
    print("==================================================================")

    results = {}
    
    for idx, t in enumerate(towns_to_deploy, 1):
        name = t["name"]
        slug = t["url_slug"]
        page_title = t["title"]
        snippet_path = os.path.join(SNIPPETS_DIR, f"{t['slug']}-page-header-injection.html")

        print(f"\n[{idx}/{len(towns_to_deploy)}] Rozpoczynam wdrożenie dla: {name} (/{slug})...")
        
        success = False
        for attempt in range(2):
            try:
                success = deploy_district(name, page_title, slug, snippet_path)
                if success:
                    break
                print(f"⚠️ Próba {attempt+1} nie powiodła się, ponawiam za 5s...")
                time.sleep(5)
            except Exception as e:
                print(f"❌ Wyjątek podczas wdrażania {name}: {e}")
                time.sleep(5)

        results[name] = {
            "success": success,
            "url": f"https://www.akumulateo.pl/{slug}"
        }
        
        print(f"[{idx}/{len(towns_to_deploy)}] Wynik dla {name}: {'✅ SUKCES' if success else '❌ BŁĄD'}")
        time.sleep(3)

    print("\n==================================================================")
    print("📊 PODSUMOWANIE WDROŻENIA AGLOMERACJI:")
    for name, res in results.items():
        status_icon = "✅" if res["success"] else "❌"
        print(f"  {status_icon} {name:<28}: {res['url']}")
    print("==================================================================")

    # Aktualizacja Hub Page
    print("\n🔄 Aktualizuję stronę Hub (/obszar-dzialania-warszawa-i-okolice)...")
    update_hub_script = os.path.join(BASE_DIR, "scripts", "update_hub_page.py")
    subprocess.run(["python3", update_hub_script])

if __name__ == "__main__":
    main()
