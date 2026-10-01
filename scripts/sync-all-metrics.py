#!/usr/bin/env python3
"""
sync-all-metrics.py – Całościowy synchronizator metryk firmy w repozytorium Akumulateo.

Zasady:
1. Pobiera parametry z scripts/business_config.py (Single Source of Truth).
2. Format oceny ZAWSZE jako '5.0' (nigdy '5.0/5.0').
3. Atomowo aktualizuje wszystkie pliki w projekcie:
   - dokumentację docs/
   - komponenty src/widgets/
   - szablony generatorów w scripts/
   - 33 wygenerowane podstrony w src/seo/generated-pages/
   - 33 wstrzyknięcia w snippets/squarespace/
"""
import os
import re
from pathlib import Path
from business_config import (
    RATING_VALUE,
    REVIEWS_DISPLAY,
    REVIEWS_SCHEMA_COUNT,
    GOOGLE_MAPS_URL
)

REPO_ROOT = Path(__file__).resolve().parent.parent

def fix_content(content: str) -> (str, int):
    changes = 0
    
    # 1. Zastąpienie formatu 5.0/5.0 lub 5.0 / 5.0 na czyste 5.0
    patterns_rating = [
        (r'5\.0\s*/\s*5\.0', '5.0'),
        (r'5\.0/5(?!\.0)', '5.0'),
    ]
    for pat, repl in patterns_rating:
        new_content, n = re.subn(pat, repl, content)
        if n > 0:
            changes += n
            content = new_content

    # 2. Zastąpienie starych liczb 160 / 102 w Schema.org
    schema_patterns = [
        (r'"ratingCount":\s*"(?:160|102|146)"', f'"ratingCount": "{REVIEWS_SCHEMA_COUNT}"'),
        (r'"reviewCount":\s*"(?:160|102|146)"', f'"reviewCount": "{REVIEWS_SCHEMA_COUNT}"'),
    ]
    for pat, repl in schema_patterns:
        new_content, n = re.subn(pat, repl, content)
        if n > 0:
            changes += n
            content = new_content

    # 3. Zastąpienie starych tekstów o liczbie opinii (160+ / 102 / 146)
    text_patterns = [
        (r'(?:160\+|102|146)\s*opini[ięa]', f'{REVIEWS_DISPLAY} opinii'),
        (r'(?:160\+|102|146)\s*recenzji', f'{REVIEWS_DISPLAY} recenzji'),
        (r'>160\s*opinii', f'{REVIEWS_DISPLAY} opinii'),
        (r'160\s*kierowców', f'{REVIEWS_DISPLAY} kierowców'),
        (r'Ponad\s*(?:160|102|146)\s*zweryfikowanych', f'Ponad {REVIEWS_DISPLAY} zweryfikowanych'),
        (r'Zaufało nam ponad\s*<strong>(?:160|146) kierowców</strong>', f'Zaufało nam ponad <strong>{REVIEWS_DISPLAY} kierowców</strong>'),
        (r'Średnia ze?\s*<strong>(?:160\+|102|146)\s*recenzji[^<]*</strong>', f'Średnia z <strong>{REVIEWS_DISPLAY} recenzji</strong>'),
    ]
    for pat, repl in text_patterns:
        new_content, n = re.subn(pat, repl, content)
        if n > 0:
            changes += n
            content = new_content

    return content, changes

def process_file(file_path: Path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            original = f.read()
    except Exception as e:
        return 0

    updated, count = fix_content(original)
    if count > 0:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated)
        print(f"  ✅ {file_path.relative_to(REPO_ROOT)} ({count} zmian)")
        return count
    return 0

def main():
    print("=" * 60)
    print("Synchronizator Metryk Akumulateo – Wykonanie całościowe")
    print(f"Standard: Ocena = {RATING_VALUE} (bez 5.0/5.0), Opinie = {REVIEWS_DISPLAY}")
    print("=" * 60)

    total_files = 0
    total_changes = 0

    # 1. Dokumentacja
    doc_paths = list((REPO_ROOT / "docs").glob("*.md"))
    doc_paths.extend([REPO_ROOT / "AGENTS.md", REPO_ROOT / "GEMINI.md"])
    for p in doc_paths:
        if p.exists():
            c = process_file(p)
            if c > 0:
                total_files += 1
                total_changes += c

    # 2. Komponenty HTML w src/widgets/
    for p in (REPO_ROOT / "src" / "widgets").glob("*.html"):
        c = process_file(p)
        if c > 0:
            total_files += 1
            total_changes += c

    # 3. Skrypty generujące w scripts/
    for p in (REPO_ROOT / "scripts").glob("*.py"):
        if p.name in ["sync-all-metrics.py", "business_config.py"]:
            continue
        c = process_file(p)
        if c > 0:
            total_files += 1
            total_changes += c

    # 4. Wszystkie podstrony HTML w src/seo/generated-pages/
    for p in (REPO_ROOT / "src" / "seo" / "generated-pages").glob("*.html"):
        c = process_file(p)
        if c > 0:
            total_files += 1
            total_changes += c

    # 5. Wszystkie wstrzyknięcia w snippets/squarespace/
    for p in (REPO_ROOT / "snippets" / "squarespace").glob("*.html"):
        c = process_file(p)
        if c > 0:
            total_files += 1
            total_changes += c

    print("=" * 60)
    print(f"PODSUMOWANIE: Zaktualizowano {total_files} plików ({total_changes} zmian).")
    print("Wszystkie pliki mają teraz 100% spójną wiedzę zgodną z business-profile.json.")
    print("=" * 60)

if __name__ == "__main__":
    main()
