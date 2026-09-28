#!/usr/bin/env python3
"""
Akumulateo – CTR Gap Analyzer
==============================
Pobiera z Google Search Console frazy z wysoką liczbą wyświetleń i niskim CTR,
a następnie generuje gotowe propozycje tytułów i opisów SERP zoptymalizowanych
pod psychologię awaryjną i intencję zakupową.

Uruchomienie:
    python3 scripts/ctr_gap_analyzer.py

Wynik: audits/ppc/ctr-gap-report-YYYY-MM-DD.md
"""

import os
import sys
import json
import time
import base64
import subprocess
import tempfile
import urllib.request
import urllib.parse
from datetime import datetime, timedelta

# ─────────────────────────────────────────────
# KONFIGURACJA
# ─────────────────────────────────────────────
CREDS_PATH    = os.path.join(os.path.dirname(__file__), '..', 'service-account.json')
SITE_URL      = "https://www.akumulateo.pl/"
PHONE         = "696 556 446"
BRAND         = "Akumulateo"
DAYS_BACK     = 28          # okno analizy
MIN_IMPR      = 15          # minimalna liczba wyświetleń, żeby fraza była rozpatrywana
MAX_CTR       = 0.04        # próg CTR – poniżej = "gap" (4%)
MIN_POSITION  = 3           # pozycja min (frazy z top 1-2 mają wysoki CTR naturalnie)
MAX_POSITION  = 25          # frazy dalej niż str. 1/2 – najpierw naprawmy te blisko top
MAX_ROWS      = 200         # ile fraz pobrać z GSC

OUTPUT_DIR    = os.path.join(os.path.dirname(__file__), '..', 'audits', 'ppc')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─────────────────────────────────────────────
# SZABLONY COPY – PSYCHOLOGIA AWARYJNA
# ─────────────────────────────────────────────
# Każdy szablon ma maksimum ~58 znaków tytułu i ~155 znaków opisu.
# Klucz "{kw}" zostanie zastąpiony wariantem frazy kluczowej.

TITLE_TEMPLATES = [
    "{kw_cap} – Dojazd 24h | {brand}",
    "{kw_cap} w Warszawie – Przyjedziemy w 45 min",
    "Awaryjny {kw} – 696 556 446 | Działa całą dobę",
]

DESC_TEMPLATES = [
    (
        "Nie odpala? Zadzwoń teraz: {phone}. Dojazd do Twojego auta w całej Warszawie "
        "i aglomeracji. Diagnostyka, wymiana, kodowanie BMS – od ręki."
    ),
    (
        "Mobilny {kw} z dojazdem 24/7. Varta, Bosch, Yuasa – montaż u Ciebie. "
        "Warszawa + okolice. Zadzwoń: {phone} – bez czekania."
    ),
    (
        "{brand}: pogotowie akumulatorowe bez sklepu stacjonarnego. Przyjeżdżamy, "
        "wymieniamy, kodujemy komputer – Twój zysk to działający samochód. {phone}."
    ),
]

# ─────────────────────────────────────────────
# OAUTH2 / JWT – bez zewnętrznych paczek
# ─────────────────────────────────────────────

def base64url(b: bytes) -> str:
    return base64.b64encode(b).decode('utf-8').rstrip('=').replace('+', '-').replace('/', '_')


def get_token(creds_path: str) -> str:
    with open(creds_path, 'r') as f:
        creds = json.load(f)

    email   = creds['client_email']
    key     = creds['private_key']
    uri     = creds.get('token_uri', 'https://oauth2.googleapis.com/token')
    now     = int(time.time())

    header  = {"alg": "RS256", "typ": "JWT"}
    payload = {
        "iss":   email,
        "scope": "https://www.googleapis.com/auth/webmasters.readonly",
        "aud":   uri,
        "exp":   now + 3600,
        "iat":   now,
    }

    unsigned = (
        f"{base64url(json.dumps(header).encode())}"
        f".{base64url(json.dumps(payload).encode())}"
    )

    with tempfile.NamedTemporaryFile('w', suffix='.pem', delete=False) as kf:
        kf.write(key)
        kf_path = kf.name

    try:
        proc = subprocess.Popen(
            ['openssl', 'dgst', '-sha256', '-sign', kf_path],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        sig, err = proc.communicate(unsigned.encode())
        if proc.returncode != 0:
            raise RuntimeError(f"OpenSSL error: {err.decode()}")
    finally:
        os.remove(kf_path)

    jwt = f"{unsigned}.{base64url(sig)}"

    data = urllib.parse.urlencode({
        'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
        'assertion':  jwt,
    }).encode()

    req = urllib.request.Request(uri, data=data,
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())['access_token']


# ─────────────────────────────────────────────
# GSC – POBIERANIE DANYCH
# ─────────────────────────────────────────────

def fetch_gsc_data(token: str) -> list[dict]:
    end   = datetime.utcnow().date()
    start = end - timedelta(days=DAYS_BACK)

    encoded = urllib.parse.quote(SITE_URL, safe='')
    url     = f"https://www.googleapis.com/webmasters/v3/sites/{encoded}/searchAnalytics/query"

    body = json.dumps({
        "startDate":  str(start),
        "endDate":    str(end),
        "dimensions": ["query", "page"],
        "rowLimit":   MAX_ROWS,
        "startRow":   0,
    }).encode()

    req = urllib.request.Request(url, data=body, headers={
        'Authorization':  f'Bearer {token}',
        'Content-Type':   'application/json',
    })

    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read()).get('rows', [])


# ─────────────────────────────────────────────
# ANALIZA GAPS
# ─────────────────────────────────────────────

def find_gaps(rows: list[dict]) -> list[dict]:
    gaps = []
    for r in rows:
        query      = r['keys'][0]
        page       = r['keys'][1]
        clicks     = r.get('clicks', 0)
        impressions= r.get('impressions', 0)
        ctr        = r.get('ctr', 0)
        position   = r.get('position', 99)

        if (impressions >= MIN_IMPR
                and ctr < MAX_CTR
                and MIN_POSITION <= position <= MAX_POSITION):
            potential_clicks = round(impressions * 0.05) - clicks  # ile dodatkowych kliknięć przy CTR 5%
            gaps.append({
                'query':      query,
                'page':       page,
                'clicks':     int(clicks),
                'impressions':int(impressions),
                'ctr_pct':    round(ctr * 100, 1),
                'position':   round(position, 1),
                'potential':  max(0, potential_clicks),
            })

    # sortuj: największy potencjał (potencjalne kliknięcia) najpierw
    return sorted(gaps, key=lambda x: x['potential'], reverse=True)


# ─────────────────────────────────────────────
# GENEROWANIE COPY
# ─────────────────────────────────────────────

def shorten(s: str, max_len: int) -> str:
    return s if len(s) <= max_len else s[:max_len - 1].rstrip() + '…'


def generate_copy(query: str) -> list[dict]:
    # Czyścimy frazę z prefiksów/sufiksów niezwiązanych z copy
    kw      = query.strip().lower()
    kw_cap  = kw.capitalize()

    variants = []
    for i, (t_tmpl, d_tmpl) in enumerate(zip(TITLE_TEMPLATES, DESC_TEMPLATES)):
        title = t_tmpl.format(kw=kw, kw_cap=kw_cap, brand=BRAND, phone=PHONE)
        desc  = d_tmpl.format(kw=kw, kw_cap=kw_cap, brand=BRAND, phone=PHONE)

        title = shorten(title, 60)
        desc  = shorten(desc, 158)

        variants.append({
            'wariant': i + 1,
            'title':   title,
            'title_len': len(title),
            'desc':    desc,
            'desc_len':  len(desc),
        })
    return variants


# ─────────────────────────────────────────────
# GENEROWANIE RAPORTU MARKDOWN
# ─────────────────────────────────────────────

def build_report(gaps: list[dict], generated_at: str) -> str:
    total_potential = sum(g['potential'] for g in gaps)
    lines = [
        f"# 🎯 Akumulateo – CTR Gap Report",
        f"",
        f"> Wygenerowano: **{generated_at}** | Okno analizy: ostatnie {DAYS_BACK} dni",
        f"> Łączny potencjał dodatkowych kliknięć organicznych (przy CTR 5%): **+{total_potential} / mies.**",
        f"",
        f"---",
        f"",
        f"## Jak używać tego raportu",
        f"",
        f"1. Wejdź w Squarespace → **Pages** → wybierz stronę z kolumny `Strona`.",
        f"2. Kliknij **⚙️ Settings** przy stronie → zakładka **SEO**.",
        f"3. Wklej wybrany wariant **Tytułu** i **Opisu** w pola `SEO Title` i `SEO Description`.",
        f"4. Zapisz. Zmiany indeksują się w Google w ciągu 1–14 dni.",
        f"",
        f"---",
        f"",
    ]

    if not gaps:
        lines.append("✅ Brak fraz z niskim CTR – wszystkie frazy powyżej progu 4%. Świetnie!")
        return "\n".join(lines)

    for idx, g in enumerate(gaps, 1):
        copy_variants = generate_copy(g['query'])

        lines += [
            f"## {idx}. `{g['query']}`",
            f"",
            f"| Metryka | Wartość |",
            f"|---|---|",
            f"| 👁 Wyświetlenia | **{g['impressions']}** |",
            f"| 🖱 Kliknięcia   | **{g['clicks']}** |",
            f"| 📊 CTR          | **{g['ctr_pct']}%** (cel: 5%) |",
            f"| 📍 Pozycja      | **{g['position']}** |",
            f"| 💡 Potencjał    | **+{g['potential']} kliknięć/mies.** przy CTR 5% |",
            f"| 🔗 Strona       | `{g['page']}` |",
            f"",
            f"### Propozycje copy SERP",
            f"",
        ]

        for v in copy_variants:
            lines += [
                f"**Wariant {v['wariant']}** ({v['title_len']} / 60 znaków tytułu, {v['desc_len']} / 158 opisu)",
                f"",
                f"- 📌 **Tytuł:** `{v['title']}`",
                f"- 📝 **Opis:** {v['desc']}",
                f"",
            ]

        lines += ["---", ""]

    return "\n".join(lines)


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  AKUMULATEO – CTR GAP ANALYZER")
    print("=" * 60)

    creds = os.path.abspath(CREDS_PATH)
    if not os.path.exists(creds):
        print(f"❌ Brak pliku service-account.json: {creds}")
        sys.exit(1)

    print("🔐 Generowanie tokena OAuth2...")
    token = get_token(creds)
    print("✅ Token OK")

    print(f"📡 Pobieranie danych GSC (ostatnie {DAYS_BACK} dni)...")
    rows = fetch_gsc_data(token)
    print(f"✅ Pobrano {len(rows)} fraz")

    print(f"🔍 Szukam gaps (CTR < {int(MAX_CTR*100)}%, wyświetlenia ≥ {MIN_IMPR}, poz. {MIN_POSITION}–{MAX_POSITION})...")
    gaps = find_gaps(rows)
    print(f"✅ Znaleziono {len(gaps)} fraz z potencjałem")

    now      = datetime.now().strftime("%Y-%m-%d %H:%M")
    date_str = datetime.now().strftime("%Y-%m-%d")
    report   = build_report(gaps, now)

    out_path = os.path.join(OUTPUT_DIR, f"ctr-gap-report-{date_str}.md")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print()
    print("=" * 60)
    print(f"✅ RAPORT ZAPISANY: {out_path}")
    total = sum(g['potential'] for g in gaps)
    print(f"💡 Łączny potencjał: +{total} kliknięć/mies. bez dodatkowego budżetu")
    print("=" * 60)


if __name__ == '__main__':
    main()
