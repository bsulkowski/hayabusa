"""Simplified model (cost per hex): calibration against the cheapest routes
and comparison of costs at equal flight time.
Documentation: docs/model.md, "Simplified model: cost per hex"."""
import math
import numpy as np
from scipy.optimize import minimize_scalar
from orbits import *

RINGS = [2, 3, 4, 5, 6]
STEP_COST = {2: 3, 3: 2, 4: 1, 5: 1}   # move k <-> k+1, closest-ring rule


def game_cost(i, j):
    lo, hi = min(i, j), max(i, j)
    return sum(STEP_COST[k] for k in range(lo, hi))


print("== Cost of the cheapest route vs distance from the Sun (ring 5 = 1) ==")
spiral = lambda a: v_circ(a) - v_circ(a + HEX_AU)
for k in range(1, 6):
    a = RING_AU[k]
    print(f"ring {k}: move outward {spiral(a) / spiral(2.5):4.1f}x, "
          f"solar heat flux {1 / a ** 2:4.2f}x Earth's")

print("\n== Game cost | cheapest route: delta-v km/s (km/s per unit), time in turns ==")
for i in RINGS:
    for j in RINGS:
        if j > i:
            dv, t = hohmann(RING_AU[i], RING_AU[j])
            c = game_cost(i, j)
            print(f"{i} -> {j}: game {c} (time {j - i} t) | {dv / 1e3:4.1f} km/s ({dv / 1e3 / c:.2f}), {t / TURN:.1f} t")


def best_dv(a1, a2, turns):
    """Cheapest route a1 -> a2 lasting exactly `turns` turns (best target alignment)."""
    t = turns * TURN
    def f(th):
        try:
            return transfer_dv(a1, a2, th, t)
        except Exception:
            return 1e12
    starts = np.arange(0.05, 6.2, 1.0)
    return min(minimize_scalar(f, bounds=(s, s + 1.0), method="bounded").fun for s in starts)


print("\n== At equal flight time the cost does not depend on the ring (delta-v km/s) ==")
for i in (2, 3, 4, 5):
    a1, a2 = RING_AU[i], RING_AU[i + 1]
    dv, t = hohmann(a1, a2)
    row = "  ".join(f"{T} t: {best_dv(a1, a2, T) / 1e3:5.1f}" for T in (1, 2, 3))
    print(f"{i} -> {i + 1}: {row}  | cheapest {dv / 1e3:.1f} km/s in {t / TURN:.1f} t")
