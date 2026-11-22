"""Board model: reference orbit, turn length, ring movement, belt drift,
transfer windows. Documentation: docs/model.md, chapters 2-3."""
import math
from orbits import *

print("== Reference orbit and time scale ==")
print(f"reference orbit: {A_REF:.2f} AU, period {T_REF:.2f} years")
print(f"turn: {TURN / DAY:.1f} days, board rotation {W_REF * TURN / YEAR:.1f} deg per turn")
print(f"Earth:Mars angular velocity ratio = {W_EARTH / W_MARS:.2f} (design intent 2)")

print("\n== Circular orbit at the ring's radius (Kepler's law) ==")
for k, a in RING_AU.items():
    deg = (360 / period_years(a) - W_REF) * TURN / YEAR
    print(f"ring {k} ({a} AU): {deg:+7.1f} deg = {deg / 360 * 6 * k:+.2f} hexes/turn")
for name, a in [("Mercury", 0.387), ("Venus", 0.723)]:
    deg = (360 / period_years(a) - W_REF) * TURN / YEAR
    print(f"{name}: {deg / 60:.2f} hexes/turn on ring 1")

print("\n== Drift of belt objects relative to the board ==")
for name, a in [("Ceres", 2.767), ("inner edge (4:1 resonance)", 2.06),
                ("outer edge (2:1 resonance)", 3.27)]:
    deg = (360 / period_years(a) - W_REF) * TURN / YEAR
    print(f"{name} ({a} AU): {deg / 360 * 6 * a / HEX_AU:+.2f} hexes/turn")

print("\n== Transfer windows: alignment repeats every N turns ==")
syn = lambda a, b: 1 / abs(1 / period_years(a) - 1 / period_years(b)) * YEAR / TURN
print(f"Earth-Mars {syn(1.0, 1.5237):.1f}, Earth-belt {syn(1.0, A_REF):.1f}, Mars-belt {syn(1.5237, A_REF):.1f}")

print("\n== Launch angle: how far the target leads the ship (game vs cheapest route) ==")
norm = lambda x: (x + 180) % 360 - 180
for label, path in [("Earth -> Mars", [1.0, 1.5]), ("Earth -> ring 4", [1.0, 1.5, 2.0]),
                    ("Mars -> ring 4", [1.5, 2.0]), ("Mars -> Earth", [1.5, 1.0]),
                    ("ring 4 -> Earth", [2.0, 1.5, 1.0]),
                    ("ring 5 -> Earth", [2.5, 2.0, 1.5, 1.0])]:
    t = (len(path) - 1) * TURN
    game = math.degrees(game_sweep(path) - mean_motion(path[-1]) * t)
    _, th = hohmann(path[0], path[-1])
    hoh = 180 - math.degrees(mean_motion(path[-1]) * th)
    print(f"{label:18s} game {norm(game):+5.0f} deg  Hohmann {norm(hoh):+5.0f} deg  difference {norm(game - hoh):+4.0f} deg")
