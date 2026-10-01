#!/usr/bin/env python3
"""
update-review-count.py – Atomowa aktualizacja liczby opinii w całym projekcie Akumulateo.

ZASADA PROJEKTOWA:
1. Aktualizuje Single Source of Truth (src/config/business-profile.json).
2. Format oceny ZAWSZE jako '5.0' (BEZWZGLĘDNY ZAKAZ '5.0').
3. Atomowo propaguje nową wartość do WSZYSTKICH plików w projekcie przez scripts/sync-all-metrics.py.
4. Przebudowuje główny plik wstrzyknięcia strony domowej (home-page-header-injection.html).

Użycie:
  python3 scripts/update-review-count.py 99
  python3 scripts/update-review-count.py "100+"

Wymóg: Przed uruchomieniem potwierdź liczbę przez python3 scripts/gbp-review-count.py.
"""
import sys
import json
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / "src" / "config" / "business-profile.json"

def main():
    if len(sys.argv) < 2:
        print("Użycie: python3 scripts/update-review-count.py <LICZBA_LUB_FORMAT>")
        print("Przykłady:")
        print("  python3 scripts/update-review-count.py '100+'")
        print("  python3 scripts/update-review-count.py 99")
        sys.exit(1)

    new_input = sys.argv[1].strip()
    
    # Rozpoznanie czy to format z plusem (np. 100+) czy czysta liczba (np. 99)
    if new_input.endswith("+"):
        display_count = new_input
        numeric_count = int(new_input[:-1])
    elif new_input.isdigit():
        display_count = f"{new_input}+" if int(new_input) >= 100 else new_input
        numeric_count = int(new_input)
    else:
        display_count = new_input
        numeric_count = 100

    print("=" * 60)
    print(f"AKUMULATEO – AKTUALIZACJA LICZNIKA OPINII")
    print(f"Nowa wartość wyświetlana: {display_count}")
    print(f"Wartość Schema.org:        {numeric_count}")
    print(f"Standard oceny:            5.0 (pojedyncza wartość, bez 5.0)")
    print("=" * 60)

    # 1. Aktualizacja src/config/business-profile.json
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            cfg = json.load(f)

        cfg["reviews"]["display"] = display_count
        cfg["reviews"]["displayLong"] = f"{display_count} zweryfikowanych opinii"
        cfg["reviews"]["schemaCount"] = numeric_count
        cfg["rating"]["value"] = "5.0"

        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(cfg, f, indent=2, ensure_ascii=False)
        print("✅ Zaktualizowano src/config/business-profile.json (Single Source of Truth)")

    # 2. Uruchomienie całościowej synchronizacji
    sync_script = REPO_ROOT / "scripts" / "sync-all-metrics.py"
    print("\nUruchamiam synchronizację wszystkich plików w projekcie...")
    res = subprocess.run([sys.executable, str(sync_script)], capture_output=True, text=True)
    print(res.stdout)
    if res.returncode != 0:
        print("❌ Błąd synchronizacji:", res.stderr)
        sys.exit(res.returncode)

    # 3. Przebudowa strony głównej
    build_script = REPO_ROOT / "scripts" / "build_home_page_header_injection.py"
    print("\nPrzebudowuję szablon strony głównej...")
    res_build = subprocess.run([sys.executable, str(build_script)], capture_output=True, text=True)
    print(res_build.stdout.strip())

    print("\n" + "=" * 60)
    print("✅ GOTOWE! Wszystkie pliki projektu mają w 100% zsynchronizowaną wiedzę.")
    print("Aby wdrożyć zmiany na żywo na Squarespace, uruchom:")
    print("  python3 scripts/inject_and_save_home.py")
    print("=" * 60)

if __name__ == "__main__":
    main()
