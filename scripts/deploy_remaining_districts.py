#!/usr/bin/env python3
"""
Automatyczny skrypt do sekwencyjnego wdrożenia pozostałych 12 dzielnic Warszawy:
Białołęka, Targówek, Praga-Południe, Praga-Północ, Ochota, Włochy,
Ursus, Wilanów, Wawer, Rembertów, Wesoła, Żoliborz.

Po wdrożeniu aktualizuje stronę Hub ze wszystkimi 18 linkami.
"""

import os
import sys
import time
import subprocess

from deploy_district import deploy_district, get_chrome_sqs_tab, ensure_pages_panel, run_js
from build_remaining_12_districts import REMAINING_12_DISTRICTS

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPETS_DIR = os.path.join(BASE_DIR, "snippets", "squarespace")

def main():
    print("==================================================================")
    print("🚀 ROZPOCZYNAM AUTOMATYCZNE WDROŻENIE 12 DZIELNIC WARSZAWY")
    print(f"Liczba dzielnic w kolejce: {len(REMAINING_12_DISTRICTS)}")
    print("==================================================================")

    results = {}
    
    for idx, d in enumerate(REMAINING_12_DISTRICTS, 1):
        name = d["name"]
        slug = d["url_slug"]
        page_title = d["title"]
        snippet_path = os.path.join(SNIPPETS_DIR, f"{d['slug']}-page-header-injection.html")

        print(f"\n[{idx}/{len(REMAINING_12_DISTRICTS)}] Rozpoczynam wdrożenie dla: {name} (/{slug})...")
        
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
        
        print(f"[{idx}/{len(REMAINING_12_DISTRICTS)}] Wynik dla {name}: {'✅ SUKCES' if success else '❌ BŁĄD'}")
        time.sleep(3)

    print("\n==================================================================")
    print("📊 PODSUMOWANIE WDROŻENIA 12 DZIELNIC:")
    for name, res in results.items():
        status_icon = "✅" if res["success"] else "❌"
        print(f"  {status_icon} {name:<16}: {res['url']}")
    print("==================================================================")

    # Aktualizacja Hub Page
    print("\n🔄 Aktualizuję stronę Hub (/obszar-dzialania-warszawa-i-okolice)...")
    update_hub_script = os.path.join(BASE_DIR, "scripts", "update_hub_page.py")
    subprocess.run(["python3", update_hub_script])

if __name__ == "__main__":
    main()
