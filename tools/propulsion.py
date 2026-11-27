"""Propulsion and fuel: tank range from the rocket equation, thrust and power,
launching from the surface.
Documentation: docs/model.md, "Propulsion and fuel", "Launching from the surface"
and "Simplified model"."""
import math
from orbits import *

G = 6.674e-11
UNIT_REF = U            # reference model: 1 unit = 1 hex/round (~10 km/s)
UNIT_SIMPLE = 1.8e3     # simplified model: 1 unit ~ 1.8 km/s (calibration)
DRIVES = [("nuclear thermal", 9e3), ("nuclear-electric", 40e3), ("fusion", 300e3)]
# freighter: structure 1, cargo 0/1/2, full tank 2
STATES = [("empty", 3.0), ("loaded", 2.0), ("heavily loaded", 5 / 3)]

for unit_name, unit in [("reference model", UNIT_REF), ("simplified model", UNIT_SIMPLE)]:
    print(f"== Freighter tank range, {unit_name} (1 unit = {unit / 1e3:.1f} km/s) ==")
    for drive, ve in DRIVES:
        cells = [f"{state} {ve * math.log(R) / 1e3:4.0f} km/s = {ve * math.log(R) / unit:5.1f} u."
                 for state, R in STATES]
        print(f"{drive:17s} " + " | ".join(cells))
    print()

print("== Thrust and power ==")
for label, dv_per_round, ve in [("reference: 2 hexes of change per round, fusion", 2 * U, 300e3),
                               ("simplified: 3 units per round, nuclear-electric", 3 * UNIT_SIMPLE, 40e3)]:
    a = dv_per_round / ROUND
    power = a * ve / (2 * 0.6)     # power per kg of ship at 60% efficiency
    print(f"{label}: {a / 9.81 * 1e3:.2f} milli-g, power about {power:.0f} W/kg ({power / 1e3:.2f} MW/t)")
dawn = 0.091 / 1220
print(f"for comparison, the Dawn probe: {dawn / 9.81 * 1e3:.4f} milli-g")

print("\n== Launching from the surface with the reference fusion drive ==")
A_SHIP = 2 * U / ROUND
BODIES = [("Earth", 3.986e14, 6371e3), ("Mars", 4.2828e13, 3389.5e3),
          ("Ceres", 6.26e10, 470e3), ("Vesta", 1.73e10, 262.7e3)]
rho = 2000.0   # typical asteroid density [kg/m^3]
BODIES.append(("1 km asteroid", G * 4 / 3 * math.pi * 500 ** 3 * rho, 500.0))
for name, gm, r in BODIES:
    g = gm / r ** 2
    tw = A_SHIP / g
    tw_text = f"{tw:.1f}" if tw >= 1 else f"1/{1 / tw:.0f}"
    print(f"{name:14s} gravity {g:8.5f} m/s2, ship thrust/weight {tw_text:>7s}, "
          f"orbital speed at the surface {math.sqrt(gm / r):5.0f} m/s, escape {math.sqrt(2 * gm / r):5.0f} m/s")
r_max = A_SHIP / (4 / 3 * math.pi * G * rho)
print(f"largest asteroid the ship can lift off from (density {rho:.0f} kg/m3): "
      f"diameter {2 * r_max / 1e3:.1f} km at thrust/weight 1, {2 * r_max / 1.5 / 1e3:.1f} km at 1.5")

print("\n== Refuelling from asteroid water (fusion drive, exhaust velocity 300 km/s) ==")
VE = 300e3
STRUCT, CARGO, TANK = 1000e3, 1000e3, 2000e3      # example freighter [kg]
units_full = VE * math.log((STRUCT + CARGO + TANK) / (STRUCT + CARGO)) / UNIT_REF
per_unit = TANK / units_full
print(f"example freighter: structure {STRUCT / 1e3:.0f} t, cargo {CARGO / 1e3:.0f} t, tank {TANK / 1e3:.0f} t "
      f"= {units_full:.1f} units, about {per_unit / 1e3:.0f} t of water per unit")
WATER_FRACTION = 0.10                              # carbonaceous asteroids: about 5-20%
print(f"regolith per unit at {WATER_FRACTION:.0%} water: about {per_unit / WATER_FRACTION / 1e3:.0f} t")
for rate in (1.0, 2.5):                            # processed regolith [t/h]
    water = rate * 1e3 * 24 * ROUND / DAY * WATER_FRACTION
    print(f"kit processing {rate} t/h of regolith: {water / 1e3:.0f} t of water per round = {water / per_unit:.1f} units/round")
reactor = 2 * U / ROUND * VE / (2 * 0.6) * (STRUCT + CARGO + TANK)
heat = 100e3 * 10e6 / DAY                          # 100 t of water per day at 10 MJ/kg
print(f"reactor power about {reactor / 1e9:.1f} GW; extracting 100 t of water per day needs about {heat / 1e6:.0f} MW")
