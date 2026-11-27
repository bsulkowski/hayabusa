"""Why the flight line in the reference model is a schematic, not free flight:
path bending by gravity, cost of holding a straight course and a test
of a simple bending rule.
Documentation: docs/model.md, "Why not take the straight line literally"."""
import math
import numpy as np
from orbits import *

DIRS = [("forward", 0, 1), ("backward", 0, -1), ("outward", 1, 0), ("inward", -1, 0)]
PLACES = [("Earth", 1.0), ("Mars", 1.5), ("belt 2.24 AU", A_REF), ("belt 3 AU", 3.0)]


def to_xy(r, th):
    return np.array([r * math.cos(th), r * math.sin(th)])


def true_coast(a, ur, ut, rounds):
    """Free flight with own velocity (ur, ut) [hexes/round] relative to a circular orbit.
    Returns the position in the (rotating) board frame."""
    r0, v0 = circ_state(a, 0.0)
    v = v0 + np.array([ur * U, ut * U])
    p, _ = propagate(r0, v, rounds * ROUND)
    th = math.atan2(p[1], p[0]) - OMEGA_REF * rounds * ROUND
    return np.hypot(*p), th


def game_coast(a, ur, ut, rounds, bend=False):
    """Movement in the game: every round the ring's forced movement + own velocity in a straight line.
    bend=True: in addition, velocity along the orbit converts into radial velocity
    (belt 1, Mars 2, Earth 3 hexes/round per hex of velocity)."""
    r, th, u = a * AU, 0.0, [ur, ut]
    for _ in range(rounds):
        if bend:
            ra = r / AU
            u[0] += (3 if ra < 1.25 else 2 if ra < 1.75 else 1) * u[1]
        th += (mean_motion(r / AU) - OMEGA_REF) * ROUND
        r += u[0] * HEX
        th += u[1] * HEX / r
    return r, th


def error(a, ur, ut, rounds, bend=False):
    try:
        rt, tt = true_coast(a, ur, ut, rounds)
        rg, tg = game_coast(a, ur, ut, rounds, bend)
        return np.linalg.norm(to_xy(rt, tt) - to_xy(rg, tg)) / HEX
    except (ValueError, ZeroDivisionError):
        return float("nan")   # the route falls into the closed ring 1


print("== Free flight at 1 hex/round: error of the straight line (hexes) ==")
for name, a in PLACES:
    for rounds in (1, 2, 3):
        errs = [error(a, ur, ut, rounds) for _, ur, ut in DIRS]
        errs = [e for e in errs if not math.isnan(e)]
        print(f"{name:12s} after {rounds} rounds: {min(errs):.1f}-{max(errs):.1f}")

print("\n== Example: belt, 1 hex/round forward, free flight ==")
for rounds in (1, 2, 3):
    r, th = true_coast(A_REF, 0, 1, rounds)
    print(f"after {rounds} rounds: {(r / AU - A_REF) / HEX_AU:+.1f} rings away from the Sun, "
          f"{th * r / HEX:+.1f} hexes along the orbit")
print(f"(orbital speed in the belt {v_circ(A_REF) / 1e3:.1f} km/s, escape "
      f"{math.sqrt(2) * v_circ(A_REF) / 1e3:.1f} km/s, 1 hex/round = {U / 1e3:.1f} km/s)")


def hold_cost(a, ur, ut, steps=4000):
    """Delta-v [units] needed to fly the game's straight line for 1 round."""
    dt = ROUND / steps
    r, thb, pts = a * AU, 0.0, []
    for i in range(steps + 1):
        th = thb + OMEGA_REF * i * dt
        pts.append(to_xy(r, th))
        thb += (mean_motion(r / AU) - OMEGA_REF + ut * U / r) * dt
        r += ur * U * dt
    P = np.array(pts)
    acc = np.gradient(np.gradient(P, dt, axis=0), dt, axis=0)
    g = -MU * P / np.linalg.norm(P, axis=1)[:, None] ** 3
    return np.linalg.norm(acc - g, axis=1)[5:-5].sum() * dt / U


print("\n== Cost of holding a straight course for 1 round, speed 1 (units) ==")
print(" " * 13 + "".join(f"{d:>13s}" for d, _, _ in DIRS))
for name, a in [("Earth", 1.0), ("Mars", 1.5), ("belt 2.24 AU", A_REF)]:
    cells = []
    for _, ur, ut in DIRS:
        cells.append("–" if a + ur * HEX_AU < 0.75 else f"{hold_cost(a, ur, ut):.1f}")
    print(f"{name:12s} " + "".join(f"{c:>13s}" for c in cells))

print("\n== Simple bending rule: error (hexes) without rule / with rule ==")
for name, a in PLACES[1:]:
    for d, ur, ut in DIRS:
        row = "  ".join(f"{t} t: {error(a, ur, ut, t):.1f}/{error(a, ur, ut, t, True):.1f}" for t in (1, 2, 3))
        print(f"{name:12s} {d:12s} {row}")
