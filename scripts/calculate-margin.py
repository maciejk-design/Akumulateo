#!/usr/bin/env python3
"""
Akumulateo – Kalkulator Marży i Wyceny Zleceń (Python CLI)
Umożliwia szybkie obliczenie rentowności zlecenia pogotowia akumulatorowego 24h
z poziomu terminala bez konieczności instalowania Node.js.
"""

import sys

DEFAULT_SCRAP_PRICE_PER_KG = 3.50
MIN_ACCEPTABLE_PROFIT_PLN = 180

def estimate_scrap_weight(capacity_ah: int) -> int:
    if capacity_ah <= 50:
        return 12
    elif capacity_ah <= 65:
        return 15
    elif capacity_ah <= 80:
        return 19
    elif capacity_ah <= 100:
        return 24
    else:
        return 28

def calculate_service_fee(service_type: str, time_slot: str, zone: str, requires_bms: bool = False) -> int:
    base_fee = 0
    if service_type == 'JUMP_START':
        base_fee = 150
    elif service_type == 'DIAGNOSTIC':
        base_fee = 130
    else: # REPLACEMENT
        base_fee = 120

    if time_slot == 'NIGHT':
        base_fee += 80
    elif time_slot == 'WEEKEND':
        base_fee += 40

    if zone == 'ZONE_2': # Dalsze dzielnice Warszawy (Białołęka, Wawer, Rembertów itp.)
        base_fee += 30
    elif zone == 'ZONE_3': # Bliska aglomeracja do 20 km (Piaseczno, Pruszków, Marki, Łomianki)
        base_fee += 60
    elif zone == 'ZONE_4': # Daleka aglomeracja 20-40 km (Grodzisk Maz., Nowy Dwór Maz., Mińsk Maz., Wołomin)
        base_fee += 110

    if requires_bms:
        base_fee += 60

    return base_fee

def calculate_quote(
    service_type: str = 'REPLACEMENT',
    capacity_ah: int = 70,
    wholesale_cost: float = 350.0,
    customer_battery_price: float = None,
    time_slot: str = 'DAY',
    zone: str = 'ZONE_1',
    requires_bms: bool = False,
    scrap_price_per_kg: float = DEFAULT_SCRAP_PRICE_PER_KG
):
    service_fee = calculate_service_fee(service_type, time_slot, zone, requires_bms)
    
    if service_type == 'REPLACEMENT':
        if customer_battery_price is None:
            customer_battery_price = round(wholesale_cost * 1.35)
        battery_margin = max(0.0, customer_battery_price - wholesale_cost)
        scrap_weight = estimate_scrap_weight(capacity_ah)
        scrap_profit = round(scrap_weight * scrap_price_per_kg)
    else:
        wholesale_cost = 0.0
        customer_battery_price = 0.0
        battery_margin = 0.0
        scrap_profit = 0.0

    total_quote = customer_battery_price + service_fee
    total_net_profit = battery_margin + service_fee + scrap_profit
    margin_pct = round((total_net_profit / total_quote) * 100) if total_quote > 0 else 100

    return {
        'total_quote': round(total_quote),
        'wholesale_cost': round(wholesale_cost),
        'battery_margin': round(battery_margin),
        'service_fee': round(service_fee),
        'scrap_profit': round(scrap_profit),
        'total_net_profit': round(total_net_profit),
        'margin_pct': margin_pct,
        'is_profitable': total_net_profit >= MIN_ACCEPTABLE_PROFIT_PLN
    }

def print_quote_summary(q):
    print("=" * 55)
    print("  AKUMULATEO – KALKULACJA RENTOWNOŚCI ZLECENIA")
    print("=" * 55)
    print(f" CENA DLA KLIENTA (Brutto):        {q['total_quote']:>6} PLN")
    print("-" * 55)
    print(f" Koszt zakupu baterii w hurtowni:  {q['wholesale_cost']:>6} PLN")
    print(f" Marża handlowa na baterii:        {q['battery_margin']:>6} PLN")
    print(f" Opłata za usługę (dojazd+montaż): {q['service_fee']:>6} PLN")
    print(f" Czysty zysk ze złomu ołowianego:  {q['scrap_profit']:>6} PLN")
    print("-" * 55)
    print(f" CAŁKOWITY ZYSK NETTO NA ZLECENIU: {q['total_net_profit']:>6} PLN")
    print(f" Rentowność zlecenia:              {q['margin_pct']:>6} %")
    status = "TAK (OPŁACALNE)" if q['is_profitable'] else "NIE (ZBYT NISKA MARŻA!)"
    print(f" Spełnia próg rentowności (>=180):  {status}")
    print("=" * 55)

if __name__ == '__main__':
    # Domyślny przykład kalkulacji:
    example = calculate_quote(
        service_type='REPLACEMENT',
        capacity_ah=75,
        wholesale_cost=420.0,
        customer_battery_price=590.0,
        time_slot='DAY',
        zone='ZONE_1',
        requires_bms=True
    )
    print_quote_summary(example)
