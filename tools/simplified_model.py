"""Model uproszczony (koszt za pole): kalibracja względem najtańszych tras
i porównanie kosztów przy jednakowym czasie lotu.
Dokumentacja: docs/model_pl.md, „Model uproszczony: koszt za pole”."""
import math
import numpy as np
from scipy.optimize import minimize_scalar
from orbits import *

RINGS = [2, 3, 4, 5, 6]
STEP_COST = {2: 3, 3: 2, 4: 1, 5: 1}   # przejście k <-> k+1, zasada najbliższego pierścienia


def game_cost(i, j):
    lo, hi = min(i, j), max(i, j)
    return sum(STEP_COST[k] for k in range(lo, hi))


print("== Koszt najtańszej trasy względem odległości od Słońca (pierścień 5 = 1) ==")
spiral = lambda a: v_circ(a) - v_circ(a + HEX_AU)
for k in range(1, 6):
    a = RING_AU[k]
    print(f"pierścień {k}: przejście dalej {spiral(a) / spiral(2.5):4.1f}x, "
          f"strumień ciepła {1 / a ** 2:4.2f}x ziemskiego")

print("\n== Koszt w grze | najtańsza trasa: Δv km/s (km/s na jednostkę), czas w rundach ==")
for i in RINGS:
    for j in RINGS:
        if j > i:
            dv, t = hohmann(RING_AU[i], RING_AU[j])
            c = game_cost(i, j)
            print(f"{i} -> {j}: gra {c} (czas {j - i} r.) | {dv / 1e3:4.1f} km/s ({dv / 1e3 / c:.2f}), {t / TURN:.1f} r.")


def best_dv(a1, a2, turns):
    """Najtańsza trasa a1 -> a2 trwająca dokładnie `turns` rund (najlepsze ustawienie celu)."""
    t = turns * TURN
    def f(th):
        try:
            return transfer_dv(a1, a2, th, t)
        except Exception:
            return 1e12
    starts = np.arange(0.05, 6.2, 1.0)
    return min(minimize_scalar(f, bounds=(s, s + 1.0), method="bounded").fun for s in starts)


print("\n== Przy jednakowym czasie lotu koszt nie zależy od pierścienia (Δv km/s) ==")
for i in (2, 3, 4, 5):
    a1, a2 = RING_AU[i], RING_AU[i + 1]
    dv, t = hohmann(a1, a2)
    row = "  ".join(f"{T} r.: {best_dv(a1, a2, T) / 1e3:5.1f}" for T in (1, 2, 3))
    print(f"{i} -> {i + 1}: {row}  | najtańsza {dv / 1e3:.1f} km/s w {t / TURN:.1f} r.")
