#!/usr/bin/env python3
"""
Akumulateo – Mobilny Audytor Wydajności PageSpeed Insights (CLI)
Pozwala błyskawicznie sprawdzić Core Web Vitals strony akumulateo.pl lub podstron dzielnicowych
bez instalowania dodatkowych pakietów npm.
"""

import sys
import json
import urllib.request
import urllib.parse
import argparse
from typing import Dict, Any

DEFAULT_TARGET_URL = "https://www.akumulateo.pl/"

def run_pagespeed_audit(url: str, strategy: str = "mobile", api_key: str = None) -> Dict[str, Any]:
    endpoint = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    params = {
        "url": url,
        "strategy": strategy,
        "category": ["performance", "seo"]
    }
    if api_key:
        params["key"] = api_key

    query_str = urllib.parse.urlencode(params, doseq=True)
    full_url = f"{endpoint}?{query_str}"

    req = urllib.request.Request(
        full_url,
        headers={"User-Agent": "Akumulateo-PageSpeed-CLI/1.0"}
    )

    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data
    except urllib.error.HTTPError as e:
        print(f"❌ Błąd HTTP API [{e.code}]: {e.reason}", file=sys.stderr)
        err_body = e.read().decode("utf-8", errors="ignore")
        print(f"Szczegóły: {err_body}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Nie udało się połączyć z API PageSpeed: {e}", file=sys.stderr)
        sys.exit(1)

def print_audit_report(url: str, strategy: str, data: Dict[str, Any]):
    lighthouse = data.get("lighthouseResult", {})
    categories = lighthouse.get("categories", {})
    audits = lighthouse.get("audits", {})

    perf_score_raw = categories.get("performance", {}).get("score")
    perf_score = round(perf_score_raw * 100) if perf_score_raw is not None else 0

    seo_score_raw = categories.get("seo", {}).get("score")
    seo_score = round(seo_score_raw * 100) if seo_score_raw is not None else None

    lcp_ms = round(audits.get("largest-contentful-paint", {}).get("numericValue", 0))
    fcp_ms = round(audits.get("first-contentful-paint", {}).get("numericValue", 0))
    cls = round(audits.get("cumulative-layout-shift", {}).get("numericValue", 0), 3)
    tbt_ms = round(audits.get("total-blocking-time", {}).get("numericValue", 0))

    print("\n" + "=" * 65)
    print("   AKUMULATEO – AUDYT WYDAJNOŚCI STRONY (PAGESPEED INSIGHTS)")
    print("=" * 65)
    print(f" Badany URL:       {url}")
    print(f" Strategia:        {strategy.upper()} (Priorytet dla pogotowia 24h: MOBILE)")
    print(f" Wynik Performance:{perf_score:>4} / 100")
    if seo_score is not None:
        print(f" Wynik SEO:        {seo_score:>4} / 100")
    print("-" * 65)
    print(" METRYKI CORE WEB VITALS:")
    print(f" • LCP (Czas głównej treści / telefonu):  {lcp_ms:>5} ms  (Cel: <= 2500 ms)")
    print(f" • FCP (Pierwsze wyrenderowanie strony):  {fcp_ms:>5} ms  (Cel: <= 1800 ms)")
    print(f" • TBT (Blokowanie wątku głównego przez JS):{tbt_ms:>4} ms  (Cel: <= 200 ms)")
    print(f" • CLS (Przesunięcia elementów layoutu):   {cls:>5}     (Cel: <= 0.1)")
    print("-" * 65)

    print(" OCENA BIZNESOWA DLA POGOTOWIA AKUMULATOROWEGO:")
    if lcp_ms <= 2500 and perf_score >= 80:
        print("  Wzorowa gotowość alarmowa!")
        print("   Kierowca widzi numer telefonu 696 556 446 w mniej niż 2.5s.")
        print("   Maksymalna ochrona budżetu Google Ads (wysoki Wynik Jakości, niskie CPC).")
    elif lcp_ms <= 4000:
        print(" ⚠️  Wydajność akceptowalna, ale wymaga optymalizacji.")
        print("   Kierowca czeka ponad 2.5s. Część użytkowników może zadzwonić do konkurencji.")
        print("   Zoptymalizuj obrazy i odchudź skrypty w Squarespace Code Injection.")
    else:
        print(" ❌ Krytyczne ryzyko utraty klientów!")
        print("   Strona ładuje się zbyt wolno (>4.0s na mobile).")
        print("   Google Ads zawyża koszty za kliknięcie ze względu na słabe doświadczenie strony docelowej.")

    print("=" * 65 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Audytor PageSpeed Insights dla Akumulateo")
    parser.add_argument("url", nargs="?", default=DEFAULT_TARGET_URL, help="URL strony do zbadania")
    parser.add_argument("--strategy", choices=["mobile", "desktop"], default="mobile", help="mobile lub desktop")
    parser.add_argument("--key", default=None, help="Opcjonalny klucz Google API")
    args = parser.parse_args()

    print(f"⏳ Pobieranie audytu PageSpeed dla {args.url} [{args.strategy}]...")
    data = run_pagespeed_audit(args.url, args.strategy, args.key)
    print_audit_report(args.url, args.strategy, data)

if __name__ == "__main__":
    main()
