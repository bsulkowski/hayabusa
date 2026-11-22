"""Napęd i paliwo: zasięg zbiornika z równania rakietowego, ciąg i moc.
Dokumentacja: docs/model_pl.md, „Napęd i paliwo” i „Model uproszczony”."""
import math
from orbits import *

UNIT_REF = U            # model referencyjny: 1 jednostka = 1 pole/turę (~10 km/s)
UNIT_SIMPLE = 1.8e3     # model uproszczony: 1 jednostka ~ 1,8 km/s (kalibracja)
DRIVES = [("jądrowy termiczny", 9e3), ("jądrowo-elektryczny", 40e3), ("fuzyjny", 300e3)]
# frachtowiec: konstrukcja 1, ładunek 0/1/2, pełny zbiornik 2
STATES = [("pusty", 3.0), ("z ładunkiem", 2.0), ("mocno obciążony", 5 / 3)]

for unit_name, unit in [("model referencyjny", UNIT_REF), ("model uproszczony", UNIT_SIMPLE)]:
    print(f"== Zasięg zbiornika frachtowca, {unit_name} (1 jedn. = {unit / 1e3:.1f} km/s) ==")
    for drive, ve in DRIVES:
        cells = [f"{state} {ve * math.log(R) / 1e3:5.0f} km/s = {ve * math.log(R) / unit:5.1f} jedn."
                 for state, R in STATES]
        print(f"{drive:20s} " + " | ".join(cells))
    print()

print("== Ciąg i moc ==")
for label, dv_per_turn, ve in [("referencyjny: zmiana o 2 pola w turze, fuzja", 2 * U, 300e3),
                               ("uproszczony: 3 jednostki w turze, jądrowo-elektryczny", 3 * UNIT_SIMPLE, 40e3)]:
    a = dv_per_turn / TURN
    power = a * ve / (2 * 0.6)     # moc na kg masy statku przy sprawności 60%
    print(f"{label}: {a / 9.81 * 1e3:.2f} milli-g, moc ok. {power:.0f} W/kg ({power / 1e3:.2f} MW/t)")
dawn = 0.091 / 1220
print(f"dla porównania sonda Dawn: {dawn / 9.81 * 1e3:.4f} milli-g")
