#!/usr/bin/env python3
"""
gbp-review-count.py – Pobiera PRAWDZIWĄ liczbę opinii z otwartego profilu GBP w Chrome.

ZASADA: Ten skrypt jest JEDYNYM dozwolonym źródłem danych o liczbie opinii
przed aktualizacją reviewsCount w projekcie Akumulateo.

Uruchom: python3 scripts/gbp-review-count.py
Wymaganie: W Chrome musi być otwarty profil GBP lub wyniki wyszukiwania Akumulateo.
"""
import subprocess
import json
import re
import sys

GBP_URL_KEYWORDS = [
    "Pogotowie%20Akumulatorowe%2024h",
    "Pogotowie+Akumulatorowe+24h",
    "akumulateo",
    "CXjN9llopHR_EBM",
]

JS_EXTRACT = r"""(() => {
    const text = document.body.innerText;

    // Metoda 1: Szukaj wzorca "N,N NUMER opinii" lub "NUMER\xa0opinii" w otoczeniu słów kluczowych firmy
    const firmMarkers = ["akumulateo", "Pogotowie Akumulatorowe"];
    const allFirmPositions = [];
    for (const marker of firmMarkers) {
        let idx = 0;
        while ((idx = text.toLowerCase().indexOf(marker.toLowerCase(), idx)) !== -1) {
            allFirmPositions.push(idx);
            idx++;
        }
    }

    if (allFirmPositions.length === 0) {
        return JSON.stringify({ error: "Nie znaleziono nazwy firmy na stronie", rawSnippet: text.slice(0, 300) });
    }

    // Szukaj liczby opinii w oknie ±300 znaków od każdego wystąpienia nazwy firmy
    const opinionPattern = /(\d+)\s*(?:\u00a0)?\s*opini/gi;
    const candidates = [];

    for (const pos of allFirmPositions) {
        const window = text.slice(Math.max(0, pos - 50), pos + 300);
        let m;
        const re = /(\d+)\s*(?:\u00a0)?\s*opini/gi;
        while ((m = re.exec(window)) !== null) {
            const count = parseInt(m[1], 10);
            const ctx = window.slice(Math.max(0, m.index - 60), m.index + 60).replace(/\n/g, " ");
            candidates.push({ count, ctx });
        }
    }

    // Deduplicate i posortuj
    const seen = new Set();
    const unique = candidates.filter(c => {
        if (seen.has(c.count)) return false;
        seen.add(c.count);
        return true;
    });

    return JSON.stringify({ candidates: unique, firmPositionsFound: allFirmPositions.length });
})()"""


def run_js_in_tab(url_keyword):
    script = f'''tell application "Google Chrome"
    repeat with w in windows
        repeat with t in tabs of w
            if (URL of t) contains "{url_keyword}" then
                tell t
                    return (execute javascript {json.dumps(JS_EXTRACT)})
                end tell
            end if
        end repeat
    end repeat
    return "NOT_FOUND"
end tell'''
    res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return res.stdout.strip()


def main():
    print("=" * 60)
    print("GBP Review Count Fetcher – Akumulateo")
    print("Źródło: Otwarty profil Google Business Profile w Chrome")
    print("=" * 60)

    raw_result = None
    matched_keyword = None

    for keyword in GBP_URL_KEYWORDS:
        result = run_js_in_tab(keyword)
        if result and result != "NOT_FOUND":
            raw_result = result
            matched_keyword = keyword
            break

    if not raw_result or raw_result == "NOT_FOUND":
        print("\n❌ BŁĄD: Nie znaleziono żadnej karty przeglądarki z profilem GBP Akumulateo.")
        print("\nOtwórz jedną z poniższych stron w Chrome i uruchom ponownie:")
        print("  https://www.google.com/search?q=Pogotowie+Akumulatorowe+24h+Akumulateo")
        print("  https://g.page/r/CXjN9llopHR_EBM/")
        sys.exit(1)

    print(f"\n✅ Znaleziono kartę z URL zawierającym: '{matched_keyword}'")

    try:
        data = json.loads(raw_result)
    except json.JSONDecodeError:
        print(f"\n❌ Błąd parsowania odpowiedzi JS: {raw_result[:200]}")
        sys.exit(1)

    if "error" in data:
        print(f"\n❌ {data['error']}")
        if "rawSnippet" in data:
            print(f"Fragment strony: {data['rawSnippet']}")
        sys.exit(1)

    candidates = data.get("candidates", [])
    if not candidates:
        print("\n❌ Nie znaleziono żadnej liczby opinii w okolicach nazwy firmy.")
        print("Upewnij się, że strona jest w pełni załadowana i widoczna jest sekcja opinii.")
        sys.exit(1)

    print(f"\nZnalezione kandydatury (posortowane wg odległości od nazwy firmy):\n")
    for i, c in enumerate(candidates):
        print(f"  [{i+1}] LICZBA: {c['count']:>5}   KONTEKST: ...{c['ctx'].strip()}...")

    # Rekomendacja: wybierz kandydata z najniższą wartością (pomija fałszywe trafienia z reklam)
    # GBP pokazuje dokładną liczbę, nie zaokrągloną
    best = candidates[0]
    print(f"\n{'=' * 60}")
    print(f"✅ REKOMENDOWANA LICZBA OPINII: {best['count']}")
    print(f"{'=' * 60}")
    print(f"\nJeśli ta liczba jest poprawna, zaktualizuj projekt komendą:")
    print(f"  python3 scripts/update-review-count.py {best['count']}")
    print(f"\nLub wpisz dokładną liczbę ręcznie, jeśli widzisz inną wartość na stronie GBP.")

    return best["count"]


if __name__ == "__main__":
    main()
