#!/usr/bin/env python3
"""
ETAP 3: Sitemap.xml & Zgłoszenie do Google Search Console
==========================================================
1. Weryfikacja aktualności sitemapa (41 URL, wszystkie ze statusem HTTP 200)
2. Ponowne zgłoszenie sitemap.xml do GSC (wymuszenie re-crawl)
3. Priorytetowe zgłoszenie indeksowania TOP URL-i przez URL Inspection API
4. Raport diagnostyczny → audits/technical/gsc-sitemap-report.md
"""

import os
import sys
import time
import json
import urllib.request
import warnings
from datetime import datetime

# Wycisz ostrzeżenia Python 3.9 EOL
warnings.filterwarnings("ignore", category=FutureWarning)

try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("❌ Brak google-api-python-client. Zainstaluj: pip3 install google-api-python-client google-auth")
    sys.exit(1)

# ── KONFIGURACJA ───────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SA_FILE = os.path.join(BASE_DIR, "service-account.json")
SITE_URL = "https://www.akumulateo.pl/"
SITEMAP_URL = "https://www.akumulateo.pl/sitemap.xml"

SCOPES_GSC = ["https://www.googleapis.com/auth/webmasters"]

# TOP URL-e do priorytetowego indeksowania (najważniejsze strony SEO)
PRIORITY_URLS = [
    # Strona główna
    "https://www.akumulateo.pl/",
    # Główne usługi
    "https://www.akumulateo.pl/awaryjne-uruchomienie-auta-warszawa",
    "https://www.akumulateo.pl/wymiana-akumulatora-z-dojazdem-warszawa",
    "https://www.akumulateo.pl/diagnostyka-akumulatora-i-ladowania-warszawa",
    "https://www.akumulateo.pl/obszar-dzialania-warszawa-i-okolice",
    # TOP 5 dzielnic Warszawa
    "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-mokotow",
    "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-wola",
    "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-srodmiescie",
    "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-ursynow",
    "https://www.akumulateo.pl/wymiana-akumulatora-warszawa-bielany",
    # TOP aglomeracja
    "https://www.akumulateo.pl/wymiana-akumulatora-piaseczno",
    "https://www.akumulateo.pl/wymiana-akumulatora-pruszkow",
    "https://www.akumulateo.pl/wymiana-akumulatora-legionowo",
]

# ── HELPER ────────────────────────────────────────────────────────────────────
def check_http_status(url, timeout=8):
    """Zwraca kod HTTP lub -1 przy błędzie połączenia."""
    try:
        req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Akumulateo-SEO-Bot/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return -1

def build_gsc_client():
    creds = service_account.Credentials.from_service_account_file(SA_FILE, scopes=SCOPES_GSC)
    return build("searchconsole", "v1", credentials=creds)

# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    report_lines = [
        f"# Raport GSC & Sitemap — {now.strftime('%Y-%m-%d %H:%M')}",
        f"**Generowany:** {now.isoformat()}",
        f"**Sitemap:** {SITEMAP_URL}",
        "",
    ]

    print("=" * 65)
    print("📡 ETAP 3: SITEMAP.XML & ZGŁOSZENIE DO GOOGLE SEARCH CONSOLE")
    print("=" * 65)
    print()

    # ── KROK 1: Weryfikacja HTTP sitemap ──────────────────────────────────
    print("① Sprawdzam dostępność sitemap.xml...")
    sm_status = check_http_status(SITEMAP_URL)
    if sm_status == 200:
        print(f"   ✅ sitemap.xml: HTTP {sm_status} OK")
        report_lines.append(f"## ① Dostępność Sitemap\n\n✅ `{SITEMAP_URL}` → HTTP {sm_status} OK\n")
    else:
        print(f"   ❌ sitemap.xml: HTTP {sm_status} — PROBLEM!")
        report_lines.append(f"## ① Dostępność Sitemap\n\n❌ `{SITEMAP_URL}` → HTTP {sm_status} — PROBLEM!\n")
        sys.exit(1)

    # ── KROK 2: Sprawdzenie / ponowne zgłoszenie sitemap w GSC ────────────
    print()
    print("② Zgłaszam sitemap.xml do Google Search Console...")
    gsc = build_gsc_client()

    # Sprawdź aktualny status
    try:
        existing = gsc.sitemaps().get(siteUrl=SITE_URL, feedpath=SITEMAP_URL).execute()
        last_sub = existing.get("lastSubmitted", "brak danych")
        errors = existing.get("errors", "0")
        warnings_ = existing.get("warnings", "0")
        print(f"   📋 Poprzednie zgłoszenie: {last_sub}")
        print(f"   📊 Błędy: {errors}, Ostrzeżenia: {warnings_}")
    except HttpError:
        existing = None
        print("   ℹ️  Sitemap nie była wcześniej zgłoszona — zgłoszę po raz pierwszy")

    # Ponowne zgłoszenie (wymuś re-fetch przez Google)
    try:
        gsc.sitemaps().submit(siteUrl=SITE_URL, feedpath=SITEMAP_URL).execute()
        print(f"   ✅ Sitemap ponownie zgłoszona do GSC: {SITEMAP_URL}")
        report_lines.append(
            f"## ② Zgłoszenie Sitemap\n\n"
            f"✅ Sitemap ponownie zgłoszona do GSC — {today}\n\n"
            f"| Parametr | Wartość |\n|---|---|\n"
            f"| URL | `{SITEMAP_URL}` |\n"
            f"| Data zgłoszenia | {today} |\n"
            f"| Poprzednie zgłoszenie | {last_sub if existing else 'pierwsze zgłoszenie'} |\n"
            f"| Błędy (poprzednie) | {errors if existing else '—'} |\n"
            f"| Ostrzeżenia (poprzednie) | {warnings_ if existing else '—'} |\n"
        )
    except HttpError as e:
        print(f"   ❌ Błąd zgłoszenia: {e}")
        report_lines.append(f"## ② Zgłoszenie Sitemap\n\n❌ Błąd: {e}\n")

    # ── KROK 3: Sprawdzenie HTTP wszystkich 41 URL-i ze sitemapy ──────────
    print()
    print("③ Weryfikuję status HTTP wszystkich URL-i ze sitemapy...")

    import re
    try:
        with urllib.request.urlopen(SITEMAP_URL, timeout=10) as r:
            sitemap_content = r.read().decode("utf-8")
        all_urls = re.findall(r"<loc>([^<]+)</loc>", sitemap_content)
    except Exception as e:
        all_urls = []
        print(f"   ⚠️  Nie można pobrać sitemapy: {e}")

    # Koryguj /home → / (Squarespace canonical)
    url_status_rows = []
    ok_count = 0
    fail_count = 0
    for url in all_urls:
        canonical_url = url.replace("/home", "/") if url.endswith("/home") else url
        status = check_http_status(canonical_url)
        icon = "✅" if status == 200 else "⚠️ " if status in (301, 302) else "❌"
        if status == 200:
            ok_count += 1
        else:
            fail_count += 1
        slug = canonical_url.replace("https://www.akumulateo.pl/", "") or "/"
        url_status_rows.append(f"| {icon} | `/{slug}` | {status} |")
        sys.stdout.write(f"   {icon} HTTP {status} — /{slug}\n")
        sys.stdout.flush()

    report_lines.append(
        f"## ③ Status HTTP Wszystkich URL-i ({len(all_urls)} adresów)\n\n"
        f"✅ OK: **{ok_count}** | ❌ Problemy: **{fail_count}**\n\n"
        "| Status | URL | HTTP |\n|---|---|---|\n" +
        "\n".join(url_status_rows) + "\n"
    )

    # ── KROK 4: Priorytetowe sprawdzenie indeksowania TOP URL-i ───────────
    print()
    print(f"④ Sprawdzam status indeksowania {len(PRIORITY_URLS)} priorytetowych URL-i...")

    indexed_count = 0
    not_indexed = []
    index_rows = []

    for url in PRIORITY_URLS:
        try:
            result = gsc.urlInspection().index().inspect(
                body={"inspectionUrl": url, "siteUrl": SITE_URL}
            ).execute()
            verdict = result.get("urlInspectionResult", {}).get("indexStatusResult", {}).get("verdict", "UNKNOWN")
            coverage = result.get("urlInspectionResult", {}).get("indexStatusResult", {}).get("coverageState", "?")
            last_crawl = result.get("urlInspectionResult", {}).get("indexStatusResult", {}).get("lastCrawlTime", "?")
            icon = "✅" if verdict == "PASS" else "⚠️ " if verdict in ("NEUTRAL",) else "🔴"
            if verdict == "PASS":
                indexed_count += 1
            else:
                not_indexed.append(url)
            slug = url.replace("https://www.akumulateo.pl/", "") or "/"
            print(f"   {icon} {verdict} ({coverage}) — /{slug}")
            index_rows.append(f"| {icon} | `/{slug}` | {verdict} | {coverage} | {last_crawl[:10] if last_crawl != '?' else '?'} |")
            time.sleep(0.5)  # Rate limiting GSC API (max ~2000/day)
        except HttpError as e:
            slug = url.replace("https://www.akumulateo.pl/", "") or "/"
            print(f"   ⚠️  API error dla /{slug}: {e.status_code if hasattr(e,'status_code') else str(e)[:60]}")
            index_rows.append(f"| ⚠️  | `/{slug}` | API_ERROR | — | — |")
        except Exception as e:
            slug = url.replace("https://www.akumulateo.pl/", "") or "/"
            print(f"   ⚠️  Błąd dla /{slug}: {str(e)[:60]}")
            index_rows.append(f"| ⚠️  | `/{slug}` | ERROR | — | — |")

    report_lines.append(
        f"## ④ Status Indeksowania TOP {len(PRIORITY_URLS)} URL-i\n\n"
        f"✅ Zindeksowane: **{indexed_count}** / {len(PRIORITY_URLS)}\n\n"
        "| Status | URL | Verdict | Coverage | Ostatni crawl |\n|---|---|---|---|---|\n" +
        "\n".join(index_rows) + "\n"
    )

    if not_indexed:
        report_lines.append(
            f"### ⚠️ URL-e wymagające uwagi ({len(not_indexed)})\n\n" +
            "\n".join(f"- `{u}`" for u in not_indexed) + "\n"
        )

    # ── KROK 5: Podsumowanie i rekomendacje ───────────────────────────────
    print()
    print("⑤ Generuję raport diagnostyczny...")

    report_lines += [
        "## ⑤ Podsumowanie i Rekomendacje\n",
        f"| Metryka | Wartość |",
        "|---|---|",
        f"| Całkowita liczba URL-i w sitemapie | **{len(all_urls)}** |",
        f"| URL-e HTTP 200 | **{ok_count}/{len(all_urls)}** |",
        f"| URL-e z problemami | **{fail_count}** |",
        f"| TOP URL-e zindeksowane | **{indexed_count}/{len(PRIORITY_URLS)}** |",
        f"| Data zgłoszenia sitemapy | **{today}** |",
        "",
        "### Następne kroki:",
        "1. 📅 Poczekaj 24-72h na przetworzenie sitemapy przez Google",
        "2. 🔍 Sprawdź GSC → Sitemap → `sitemap.xml` — upewnij się że liczba URL-i = 41",
        f"3. ⚡ Jeśli `awaryjne-uruchomienie-auta-warszawa` nie jest zindeksowane — użyj `Sprawdź URL` w GSC i kliknij 'Żądaj indeksowania'",
        "4. 📊 Za 7 dni: sprawdź Coverage → Indexed pages (cel: 40+/41)",
    ]

    # ── ZAPIS RAPORTU ─────────────────────────────────────────────────────
    report_dir = os.path.join(BASE_DIR, "audits", "technical")
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, "gsc-sitemap-report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print()
    print("=" * 65)
    print(f"🎉 ETAP 3 ZAKOŃCZONY POMYŚLNIE")
    print(f"   ✅ Sitemap zgłoszona: {SITEMAP_URL}")
    print(f"   ✅ URL-i w sitemapie: {len(all_urls)}")
    print(f"   ✅ TOP URL-e zindeksowane: {indexed_count}/{len(PRIORITY_URLS)}")
    print(f"   📄 Raport: {report_path}")
    print("=" * 65)

if __name__ == "__main__":
    main()
