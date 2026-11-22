"""Model planszy: punkt synchronizacji, długość rundy, ruch pierścieni, dryf pasa,
okna transferowe. Dokumentacja: docs/model_pl.md, rozdziały 2–3."""
import math
from orbits import *

print("== Punkt odniesienia i skala czasu ==")
print(f"orbita synchronizacji: {A_REF:.2f} AU, okres {T_REF:.2f} roku")
print(f"runda: {TURN / DAY:.1f} dnia, obrót planszy {W_REF * TURN / YEAR:.1f}° na rundę")
print(f"stosunek prędkości kątowych Ziemia:Mars = {W_EARTH / W_MARS:.2f} (intencja projektowa 2)")

print("\n== Ruch po orbicie kołowej na promieniu pierścienia (prawo Keplera) ==")
for k, a in RING_AU.items():
    deg = (360 / period_years(a) - W_REF) * TURN / YEAR
    print(f"pierścień {k} ({a} AU): {deg:+7.1f}° = {deg / 360 * 6 * k:+.2f} pola/rundę")
for name, a in [("Merkury", 0.387), ("Wenus", 0.723)]:
    deg = (360 / period_years(a) - W_REF) * TURN / YEAR
    print(f"{name}: {deg / 60:.2f} pola/rundę na pierścieniu 1")

print("\n== Dryf obiektów pasa względem planszy ==")
for name, a in [("Ceres", 2.767), ("wewn. krawędź (rez. 4:1)", 2.06),
                ("zewn. krawędź (rez. 2:1)", 3.27)]:
    deg = (360 / period_years(a) - W_REF) * TURN / YEAR
    print(f"{name} ({a} AU): {deg / 360 * 6 * a / HEX_AU:+.2f} pola/rundę")

print("\n== Okna transferowe: co ile rund powtarza się ustawienie ==")
syn = lambda a, b: 1 / abs(1 / period_years(a) - 1 / period_years(b)) * YEAR / TURN
print(f"Ziemia–Mars {syn(1.0, 1.5237):.1f}, Ziemia–pas {syn(1.0, A_REF):.1f}, Mars–pas {syn(1.5237, A_REF):.1f}")

print("\n== Kąt startu: o ile cel wyprzedza statek (gra vs najtańsza trasa) ==")
norm = lambda x: (x + 180) % 360 - 180
for label, path in [("Ziemia -> Mars", [1.0, 1.5]), ("Ziemia -> pierścień 4", [1.0, 1.5, 2.0]),
                    ("Mars -> pierścień 4", [1.5, 2.0]), ("Mars -> Ziemia", [1.5, 1.0]),
                    ("pierścień 4 -> Ziemia", [2.0, 1.5, 1.0]),
                    ("pierścień 5 -> Ziemia", [2.5, 2.0, 1.5, 1.0])]:
    t = (len(path) - 1) * TURN
    game = math.degrees(game_sweep(path) - mean_motion(path[-1]) * t)
    _, th = hohmann(path[0], path[-1])
    hoh = 180 - math.degrees(mean_motion(path[-1]) * th)
    print(f"{label:24s} gra {norm(game):+5.0f}°  Hohmann {norm(hoh):+5.0f}°  różnica {norm(game - hoh):+4.0f}°")
