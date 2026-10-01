#!/usr/bin/env python3
"""
business_config.py – Pojedyncze Źródło Prawdy (Single Source of Truth)
dla danych firmy, liczby opinii i ocen w projekcie Akumulateo.

ŻELAZNE ZASADY:
1. Ocena ZAWSZE jako '5.0' – BEZWZGLĘDNY ZAKAZ '5.0/5.0' lub '5/5'.
2. Liczba opinii synchronizowana automatycznie ze skryptu scripts/update-review-count.py.
3. Wszelkie skrypty generujące podstrony i wstrzyknięcia MUSZĄ importować dane stąd.
"""
import json
import os
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parent.parent / "src" / "config" / "business-profile.json"

def load_config():
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Nie znaleziono pliku konfiguracyjnego: {CONFIG_PATH}")
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

CONFIG = load_config()

# Zmienne eksportowane dla skryptów Pythona
RATING_VALUE = CONFIG["rating"]["value"]           # Strictly "5.0"
RATING_STARS = CONFIG["rating"]["stars"]           # "★★★★★"
REVIEWS_DISPLAY = CONFIG["reviews"]["display"]     # np. "100+"
REVIEWS_DISPLAY_LONG = CONFIG["reviews"]["displayLong"] # np. "100+ zweryfikowanych opinii"
REVIEWS_SCHEMA_COUNT = str(CONFIG["reviews"]["schemaCount"]) # np. "100"
GOOGLE_MAPS_URL = CONFIG["urls"]["googleMaps"]
GOOGLE_REVIEW_URL = CONFIG["urls"]["googleReview"]
PHONE = CONFIG["phone"]
PHONE_RAW = CONFIG["phoneRaw"]
ETA = CONFIG["eta"]

def get_google_stars_badge_html():
    """Zwraca spójny HTML odznaki Google z oceną 5.0 (nigdy 5.0/5.0)."""
    return f'⭐ {RATING_VALUE} w Google ({REVIEWS_DISPLAY} opinii)'

def get_google_rating_header_html():
    """Zwraca nagłówek sekcji ocen."""
    return f'Ocena {RATING_VALUE} {RATING_STARS} w Google Maps'
