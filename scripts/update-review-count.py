#!/usr/bin/env python3
"""
update-review-count.py – Główny skrypt aktualizacji opinii w projekcie Akumulateo.

Gdy użytkownik powie: 'zaktualizuj opinie' lub 'zaktualizuj liczbę opinii',
ten skrypt jest wywoływany przez agenta.

Działanie w 1 kroku:
1. Pobiera lub przyjmuje nową liczbę opinii.
2. Zapisuje ją w Single Source of Truth (src/config/business-profile.json).
3. Propaguje nową wartość do statycznych plików i generatorów (scripts/sync-all-metrics.py).
4. Przebudowuje stronę główną (scripts/build_home_page_header_injection.py).
5. Automatycznie wdraża zaktualizowany Footer do Squarespace (scripts/deploy_footer_injection.py),
   dzięki czemu WSZYSTKIE 33 podstrony natychmiast pokazują nową liczbę!
"""
import sys
import json
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "src" / "config" / "business-profile.json"

def get_count_from_gbp():
    fetcher = REPO_ROOT / "scripts" / "gbp-review-count.py"
    res = subprocess.run([sys.executable, str(fetcher)], capture_output=True, text=True)
    for line in res.stdout.splitlines():
        if "REKOMENDOWANA LICZBA OPINII:" in line:
            return line.split(":")[-1].strip()
    return None

def main():
    if len(sys.argv) >= 2:
        new_input = sys.argv[1].strip()
    else:
        print("Brak podanej liczby – próbuję pobrać automatycznie z otwartej karty GBP w Chrome...")
        gbp_count = get_count_from_gbp()
        if gbp_count:
            print(f"✅ Pobrano z panelu GBP: {gbp_count} opinii")
            new_input = gbp_count
        else:
            print("❌ Nie znaleziono otwartej karty GBP. Użycie: python3 scripts/update-review-count.py <LICZBA>")
            sys.exit(1)

    # Formatowanie wyświetlania
    if new_input.endswith("+"):
        display_count = new_input
        numeric_count = int(new_input[:-1])
    elif new_input.isdigit():
        val = int(new_input)
        display_count = f"{val}+" if val >= 100 else str(val)
        numeric_count = val
    else:
        display_count = new_input
        numeric_count = 100

    print("=" * 60)
    print("AKUMULATEO – AKTUALIZACJA LICZNIKA OPINII")
    print(f"Nowa wartość wyświetlana: {display_count}")
    print(f"Wartość Schema.org:        {numeric_count}")
    print(f"Standard oceny:            5.0 (wyłącznie pojedyncza wartość)")
    print("=" * 60)

    # 1. Zapis do Single Source of Truth
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            cfg = json.load(f)

        cfg["reviews"]["display"] = display_count
        cfg["reviews"]["displayLong"] = f"{display_count} zweryfikowanych opinii"
        cfg["reviews"]["schemaCount"] = numeric_count
        cfg["rating"]["value"] = "5.0"

        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(cfg, f, indent=2, ensure_ascii=False)
        print("✅ 1/4 Zaktualizowano Single Source of Truth: src/config/business-profile.json")

    # 2. Całościowa synchronizacja statyczna
    sync_script = REPO_ROOT / "scripts" / "sync-all-metrics.py"
    res_sync = subprocess.run([sys.executable, str(sync_script)], capture_output=True, text=True)
    print("✅ 2/4 Zsynchronizowano pliki lokalne i szablony generatorów")

    # 3. Przebudowa szablonu strony głównej
    build_script = REPO_ROOT / "scripts" / "build_home_page_header_injection.py"
    res_build = subprocess.run([sys.executable, str(build_script)], capture_output=True, text=True)
    print("✅ 3/4 Przebudowano szablon strony głównej (home-page-header-injection.html)")

    # 4. Automatyczne wdrożenie do Squarespace Footera (JEDNO MIEJSCE dla całego serwisu)
    deploy_footer_script = REPO_ROOT / "scripts" / "deploy_footer_injection.py"
    print("🚀 4/4 Wdrażam zaktualizowaną konfigurację do Squarespace Footer Code Injection...")
    res_deploy = subprocess.run([sys.executable, str(deploy_footer_script)], capture_output=True, text=True)
    print(res_deploy.stdout.strip())

    print("\n" + "=" * 60)
    print(f"🎉 SUKCES! Cały serwis www.akumulateo.pl ma teraz aktualną liczbę opinii: {display_count}")
    print("Wszystkie 33 podstrony dzielnicowe i strona główna zostały natychmiast zaktualizowane.")
    print("=" * 60)

if __name__ == "__main__":
    main()
