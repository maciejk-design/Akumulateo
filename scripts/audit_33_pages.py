#!/usr/bin/env python3
"""
Kompleksowy audyt 33 podstron lokalnych Akumulateo:
18 dzielnic Warszawy + 15 miejscowości aglomeracji.
Sprawdza: HTTP Status, brak wycieku CSS, aktywny link logo, przycisk MENU oraz czystość marek (Centra/Banner ban).
"""

import urllib.request
import sys
import re

URLS = [
    # 18 Dzielnic Warszawy
    ("Mokotów", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-mokotow"),
    ("Bemowo", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-bemowo"),
    ("Wola", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-wola"),
    ("Ursynów", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-ursynow"),
    ("Śródmieście", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-srodmiescie"),
    ("Bielany", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-bielany"),
    ("Białołęka", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-bialoleka"),
    ("Targówek", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-targowek"),
    ("Praga-Południe", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-praga-poludnie"),
    ("Praga-Północ", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-praga-polnoc"),
    ("Ochota", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-ochota"),
    ("Włochy", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-wlochy"),
    ("Ursus", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-ursus"),
    ("Wilanów", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-wilanow"),
    ("Wawer", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-wawer"),
    ("Rembertów", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-rembertow"),
    ("Wesoła", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-wesola"),
    ("Żoliborz", "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-zoliborz"),
    # 15 Miejscowości Aglomeracji
    ("Piaseczno", "https://www.akumulateo.pl/wymiana-akumulatora-piaseczno"),
    ("Pruszków", "https://www.akumulateo.pl/wymiana-akumulatora-pruszkow"),
    ("Piastów", "https://www.akumulateo.pl/wymiana-akumulatora-piastow"),
    ("Brwinów", "https://www.akumulateo.pl/wymiana-akumulatora-brwinow"),
    ("Milanówek", "https://www.akumulateo.pl/wymiana-akumulatora-milanowek"),
    ("Legionowo", "https://www.akumulateo.pl/wymiana-akumulatora-legionowo"),
    ("Modlin", "https://www.akumulateo.pl/wymiana-akumulatora-modlin"),
    ("Nowy Dwór Maz.", "https://www.akumulateo.pl/wymiana-akumulatora-nowy-dwor-mazowiecki"),
    ("Mińsk Maz.", "https://www.akumulateo.pl/wymiana-akumulatora-minsk-mazowiecki"),
    ("Konstancin-Jez.", "https://www.akumulateo.pl/wymiana-akumulatora-konstancin-jeziorna"),
    ("Łomianki", "https://www.akumulateo.pl/wymiana-akumulatora-lomianki"),
    ("Otwock", "https://www.akumulateo.pl/wymiana-akumulatora-otwock"),
    ("Marki", "https://www.akumulateo.pl/wymiana-akumulatora-marki"),
    ("Grodzisk Maz.", "https://www.akumulateo.pl/wymiana-akumulatora-grodzisk-mazowiecki"),
    ("Wołomin", "https://www.akumulateo.pl/wymiana-akumulatora-wolomin"),
]

def main():
    print(f"Rozpoczynam audyt {len(URLS)} podstron na żywo...")
    results = []
    all_passed = True

    header = f"{'LOKALIZACJA':<18} | {'STATUS':<6} | {'ROZMIAR':<8} | {'CSS LEAK':<8} | {'LOGO':<6} | {'MENU':<6} | {'BRAND':<6}"
    print(header)
    print("-" * len(header))

    for name, url in URLS:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"})
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                status = resp.status
                raw = resp.read().decode("utf-8", errors="ignore")
                size = len(raw)
                css_leak = "GLOBAL CUSTOM CSS" in raw
                logo_ok = 'href="/"' in raw or "href='/'" in raw
                menu_ok = "ak-mobile-menu-btn" in raw or "MENU" in raw
                # Weryfikacja marek: Centra (jako pojedyncze słowo) oraz marka akumulatorów Banner
                centra_matches = re.findall(r"\bcentra\b", raw, re.IGNORECASE)
                banner_brand_matches = re.findall(r"\b(akumulator[a-z]*\s+banner|banner\s+bull|banner\s+batter[a-z]*|mark[a-z]*\s+banner)\b", raw, re.IGNORECASE)
                brand_ok = (len(centra_matches) == 0) and (len(banner_brand_matches) == 0)

                passed = (status == 200) and (not css_leak) and logo_ok and menu_ok and brand_ok
                if not passed:
                    all_passed = False

                row = f"{name:<18} | {status:<6} | {size:<8} | {'NIE (OK)' if not css_leak else 'TAK (BŁĄD)':<8} | {'OK' if logo_ok else 'BŁĄD':<6} | {'OK' if menu_ok else 'BŁĄD':<6} | {'OK' if brand_ok else 'BŁĄD':<6}"
                print(row)
                results.append((name, passed))
        except Exception as e:
            all_passed = False
            row = f"{name:<18} | {'BŁĄD':<6} | {0:<8} | {'-':<8} | {'-':<6} | {'-':<6} | {str(e)[:15]}"
            print(row)
            results.append((name, False))

    print("-" * len(header))
    passed_count = sum(1 for _, p in results if p)
    print(f"WYNIK: {passed_count}/{len(URLS)} podstron w 100% poprawnych.")
    if all_passed:
        print("🎉 WSZYSTKIE 33 PODSTRONY DZIAŁAJĄ PERFEKCYJNIE NA PRODUKCJI!")
    else:
        print("⚠️ Wykryto nieprawidłowości na niektórych podstronach.")
        sys.exit(1)

if __name__ == "__main__":
    main()
