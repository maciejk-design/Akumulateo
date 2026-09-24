#!/usr/bin/env python3
"""
Akumulateo – Mobilny Audytor Wydajności PageSpeed Insights (CLI)
Pozwala błyskawicznie sprawdzić Core Web Vitals strony akumulateo.pl lub podstron dzielnicowych
bez instalowania dodatkowych pakietów npm.
"""

import sys
import json
import os
import ssl
import urllib.request
import urllib.parse
import argparse
from typing import Dict, Any

DEFAULT_TARGET_URL = "https://www.akumulateo.pl/"

def load_env_pagespeed_key() -> str:
    """Odczytuje klucz GOOGLE_PAGESPEED_API_KEY z pliku .env w projekcie."""
    env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
    if not os.path.exists(env_path):
        return ""
    try:
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and 'GOOGLE_PAGESPEED_API_KEY=' in line:
                    val = line.split('=', 1)[1].strip()
                    return val.strip('"\'')
    except Exception:
        pass
    return ""

def run_pagespeed_audit(url: str, strategy: str = "mobile", api_key: str = None) -> Dict[str, Any]:
    if not api_key:
        api_key = load_env_pagespeed_key() or os.environ.get("GOOGLE_PAGESPEED_API_KEY")

    endpoint = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    params = [
        ("url", url),
        ("strategy", strategy),
        ("category", "performance"),
        ("category", "seo"),
        ("category", "accessibility"),
        ("category", "best-practices")
    ]
    if api_key:
        params.append(("key", api_key))

    query_str = urllib.parse.urlencode(params)
    full_url = f"{endpoint}?{query_str}"

    req = urllib.request.Request(
        full_url,
        headers={"User-Agent": "Akumulateo-PageSpeed-CLI/1.0"}
    )

    # SSL context with graceful fallback for macOS environments
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except ssl.SSLCertVerificationError:
        ctx_unverified = ssl._create_unverified_context()
        with urllib.request.urlopen(req, context=ctx_unverified, timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
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

    a11y_score_raw = categories.get("accessibility", {}).get("score")
    a11y_score = round(a11y_score_raw * 100) if a11y_score_raw is not None else None

    bp_score_raw = categories.get("best-practices", {}).get("score")
    bp_score = round(bp_score_raw * 100) if bp_score_raw is not None else None

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
    if a11y_score is not None:
        print(f" Dostępność (A11y):{a11y_score:>4} / 100")
    if bp_score is not None:
        print(f" Dobre Praktyki:   {bp_score:>4} / 100")
    print("-" * 65)
    print(" METRYKI CORE WEB VITALS:")
    print(f" • LCP (Czas głównej treści / telefonu):  {lcp_ms:>5} ms  (Cel: <= 2500 ms)")
    print(f" • FCP (Pierwsze wyrenderowanie strony):  {fcp_ms:>5} ms  (Cel: <= 1800 ms)")
    print(f" • TBT (Blokowanie wątku głównego przez JS):{tbt_ms:>4} ms  (Cel: <= 200 ms)")
    print(f" • CLS (Przesunięcia elementów layoutu):   {cls:>5}     (Cel: <= 0.1)")
    print("-" * 65)

    # Szukanie głównych wąskich gardeł (opportunities)
    opps = []
    for k, a in audits.items():
        if a.get("details", {}).get("type") == "opportunity" and a.get("score") is not None and a.get("score") < 0.9:
            savings = a.get("displayValue", "")
            opps.append((a.get("title", k), savings, a.get("score", 1)))

    if opps:
        print(" GŁÓWNE MOŻLIWOŚCI PRZYSPIESZENIA (SQUARESPACE):")
        for title, savings, _ in sorted(opps, key=lambda x: x[2])[:5]:
            print(f" • {title}: {savings}")
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
    parser.add_argument("--save-json", default=None, help="Ścieżka do zapisu pełnego wyniku JSON")
    args = parser.parse_args()

    key = args.key
    if not key:
        # Odczytaj z .env jeśli istnieje
        env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
        if os.path.exists(env_path):
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("GOOGLE_PAGESPEED_API_KEY="):
                        key = line.split("=", 1)[1].strip().strip('"').strip("'")
                        break
        if not key:
            key = os.environ.get("GOOGLE_PAGESPEED_API_KEY")

    print(f"⏳ Pobieranie audytu PageSpeed dla {args.url} [{args.strategy}]...")
    data = run_pagespeed_audit(args.url, args.strategy, key)
    print_audit_report(args.url, args.strategy, data)
    if args.save_json:
        with open(args.save_json, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"💾 Zapisano pełne dane do {args.save_json}")

if __name__ == "__main__":
    main()
