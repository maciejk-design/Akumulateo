#!/usr/bin/env python3
"""
Akumulateo – Tester Połączenia z Google Search Console i GA4
Używa wbudowanego w macOS LibreSSL/OpenSSL do wygenerowania podpisu RSA-SHA256 JWT,
dzięki czemu działa bezpośrednio w systemie bez instalacji jakichkolwiek paczek!
"""

import sys
import os
import json
import time
import base64
import subprocess
import urllib.request
import urllib.parse

def base64url(b: bytes) -> str:
    return base64.b64encode(b).decode('utf-8').rstrip('=').replace('+', '-').replace('/', '_')

def get_oauth2_token(creds_path: str, scopes: list) -> str:
    with open(creds_path, 'r', encoding='utf-8') as f:
        creds = json.load(f)

    client_email = creds['client_email']
    private_key = creds['private_key']
    token_uri = creds.get('token_uri', 'https://oauth2.googleapis.com/token')

    now = int(time.time())
    header = {"alg": "RS256", "typ": "JWT"}
    payload = {
        "iss": client_email,
        "scope": " ".join(scopes),
        "aud": token_uri,
        "exp": now + 3600,
        "iat": now
    }

    unsigned_jwt = f"{base64url(json.dumps(header).encode('utf-8'))}.{base64url(json.dumps(payload).encode('utf-8'))}"

    # Podpisujemy kluczem RSA za pomocą wbudowanego w macOS openssl dgst
    p = subprocess.Popen(
        ['openssl', 'dgst', '-sha256', '-sign', '-'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    # Przekazujemy klucz prywatny jako wejście i podpisujemy unsigned_jwt
    # Zapiszmy tymczasowo klucz prywatny lub przekażmy go
    # openssl dgst -sign przyjmuje ścieżkę do pliku z kluczem
    import tempfile
    with tempfile.NamedTemporaryFile('w', delete=False) as key_file:
        key_file.write(private_key)
        key_file_path = key_file.name

    try:
        sign_proc = subprocess.Popen(
            ['openssl', 'dgst', '-sha256', '-sign', key_file_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        signature, err = sign_proc.communicate(input=unsigned_jwt.encode('utf-8'))
        if sign_proc.returncode != 0:
            raise RuntimeError(f"Błąd OpenSSL przy podpisywaniu: {err.decode('utf-8')}")
    finally:
        if os.path.exists(key_file_path):
            os.remove(key_file_path)

    signed_jwt = f"{unsigned_jwt}.{base64url(signature)}"

    post_data = urllib.parse.urlencode({
        'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
        'assertion': signed_jwt
    }).encode('utf-8')

    req = urllib.request.Request(token_uri, data=post_data, headers={
        'Content-Type': 'application/x-www-form-urlencoded'
    })

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data['access_token']
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8', errors='ignore')
        raise RuntimeError(f"Błąd pobierania tokena OAuth2 [{e.code}]: {err_msg}")

def test_gsc(token: str, site_url: str):
    print(f"\n🔍 [1/2] Testowanie Google Search Console dla {site_url}...")
    encoded_site = urllib.parse.quote(site_url, safe='')
    endpoint = f"https://www.googleapis.com/webmasters/v3/sites/{encoded_site}/searchAnalytics/query"

    body = json.dumps({
        "startDate": "2026-09-01",
        "endDate": "2026-09-20",
        "dimensions": ["query"],
        "rowLimit": 5
    }).encode('utf-8')

    req = urllib.request.Request(endpoint, data=body, headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    })

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            rows = data.get('rows', [])
            print(f"✅ POŁĄCZENIE Z GSC DZIAŁA! Pobrano {len(rows)} wierszy.")
            if rows:
                print("   Przykładowe frazy:")
                for r in rows[:3]:
                    print(f"   • {r['keys'][0]}: {r.get('clicks', 0)} kliknięć, {r.get('impressions', 0)} wyświetleń")
            return True
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8', errors='ignore')
        print(f"❌ Błąd GSC [{e.code}]: {err_msg}")
        return False

def test_ga4(token: str, property_id: str):
    print(f"\n📊 [2/2] Testowanie Google Analytics 4 dla usługi {property_id}...")
    endpoint = f"https://analyticsdata.googleapis.com/v1beta/properties/{property_id}:runReport"

    body = json.dumps({
        "dateRanges": [{"startDate": "30daysAgo", "endDate": "today"}],
        "metrics": [{"name": "sessions"}]
    }).encode('utf-8')

    req = urllib.request.Request(endpoint, data=body, headers={
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    })

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            rows = data.get('rows', [])
            sessions = rows[0]['metricValues'][0]['value'] if rows else '0'
            print(f"✅ POŁĄCZENIE Z GA4 DZIAŁA! Sesji w ostatnich 30 dniach: {sessions}")
            return True
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode('utf-8', errors='ignore')
        print(f"❌ Błąd GA4 [{e.code}]: {err_msg}")
        return False

def main():
    print("=" * 60)
    print("  AKUMULATEO – TEST POŁĄCZENIA API (GOOGLE CLOUD SERVICE ACCOUNT)")
    print("=" * 60)

    creds_path = os.path.abspath("service-account.json")
    if not os.path.exists(creds_path):
        print(f"❌ Brak pliku: {creds_path}")
        sys.exit(1)

    scopes = [
        "https://www.googleapis.com/auth/webmasters.readonly",
        "https://www.googleapis.com/auth/analytics.readonly"
    ]

    print("🔐 1. Generowanie tokena OAuth2 JWT...")
    try:
        token = get_oauth2_token(creds_path, scopes)
        print("✅ Token OAuth2 wygenerowany pomyślnie!")
    except Exception as e:
        print(f"❌ Błąd generowania tokena: {e}")
        sys.exit(1)

    site_url = "https://www.akumulateo.pl/"
    property_id = "475492247"

    gsc_ok = test_gsc(token, site_url)
    ga4_ok = test_ga4(token, property_id)

    print("\n" + "=" * 60)
    print(f"PODSUMOWANIE: GSC={'✅ OK' if gsc_ok else '❌ OCZEKUJE NA UPRAWNIENIA'} | GA4={'✅ OK' if ga4_ok else '❌ OCZEKUJE NA UPRAWNIENIA'}")
    print("=" * 60)

if __name__ == '__main__':
    main()
