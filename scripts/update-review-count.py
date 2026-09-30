#!/usr/bin/env python3
"""
update-review-count.py – Aktualizuje reviewsCount we WSZYSTKICH plikach projektu Akumulateo.

Użycie:
  python3 scripts/update-review-count.py 99
  python3 scripts/update-review-count.py "100+"

OSTRZEŻENIE: Uruchamiaj WYŁĄCZNIE po potwierdzeniu liczby z:
  python3 scripts/gbp-review-count.py
"""
import sys
import re
import subprocess

FILES_TO_UPDATE = [
    ("snippets/squarespace/footer-code-injection.html",     r'reviewsCount: "[^"]*"',        'reviewsCount: "{}"'),
    ("snippets/squarespace/homepage-content.html",          r'\d+\+ kierowców',               '{} kierowców'),
    ("snippets/squarespace/homepage-content.html",          r'content="\d+"(?=.*reviewCount)', 'content="{}"'),
    ("snippets/squarespace/homepage-content.html",          r'\d+\+? recenzji [^<"]+',        '{} recenzji w profilu Google'),
    ("snippets/squarespace/homepage-content.html",          r'Zobacz \d+\+? opinii',          'Zobacz {}+ opinii'),
    ("scripts/build_home_page_header_injection.py",         r'reviewsCount: "[^"]*"',         'reviewsCount: "{}"'),
    ("AGENTS.md",                                           r'\d+\+? opini[ię]\)',            '{} opinii)'),
]

def main():
    if len(sys.argv) < 2:
        print("Użycie: python3 scripts/update-review-count.py LICZBA")
        print("Przykład: python3 scripts/update-review-count.py 99")
        print("          python3 scripts/update-review-count.py '100+'")
        sys.exit(1)

    new_count = sys.argv[1].strip()
    print(f"\n{'='*60}")
    print(f"Aktualizacja reviewsCount → '{new_count}'")
    print(f"Źródło: Ręcznie podane po weryfikacji w GBP")
    print(f"{'='*60}\n")

    for filepath, pattern, replacement_tpl in FILES_TO_UPDATE:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            replacement = replacement_tpl.format(new_count)
            new_content, n = re.subn(pattern, replacement, content)

            if n > 0:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"  ✅  {filepath} – {n} zmiana(y)")
            else:
                print(f"  ⚠️   {filepath} – brak dopasowania dla wzorca: {pattern}")

        except FileNotFoundError:
            print(f"  ❌  {filepath} – plik nie istnieje")

    print(f"\n{'='*60}")
    print("Następne kroki:")
    print("  1. python3 scripts/build_home_page_header_injection.py")
    print("  2. python3 scripts/inject_and_save_home.py")
    print("  3. git add -u && git commit -m 'fix(cro): update review count to {}'".format(new_count))
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
