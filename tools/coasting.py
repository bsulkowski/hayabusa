"""Dlaczego linia lotu w modelu referencyjnym to schemat, a nie lot swobodny:
zakrzywienie toru przez grawitację, koszt utrzymania prostego kursu
i sprawdzenie prostej zasady zakrzywiania.
Dokumentacja: docs/model_pl.md, „Dlaczego nie prosta linia dosłownie”."""
import math
import numpy as np
from orbits import *

DIRS = [("do przodu", 0, 1), ("do tyłu", 0, -1), ("na zewnątrz", 1, 0), ("do środka", -1, 0)]
PLACES = [("Ziemia", 1.0), ("Mars", 1.5), ("pas 2,24 AU", A_REF), ("pas 3 AU", 3.0)]


def to_xy(r, th):
    return np.array([r * math.cos(th), r * math.sin(th)])


def true_coast(a, ur, ut, turns):
    """Lot swobodny z prędkością własną (ur, ut) [pola/turę] względem orbity kołowej.
    Zwraca położenie w układzie planszy (obracającym się)."""
    r0, v0 = circ_state(a, 0.0)
    v = v0 + np.array([ur * U, ut * U])
    p, _ = propagate(r0, v, turns * TURN)
    th = math.atan2(p[1], p[0]) - OMEGA_REF * turns * TURN
    return np.hypot(*p), th


def game_coast(a, ur, ut, turns, bend=False):
    """Ruch w grze: co turę ruch wymuszony pierścienia + prędkość własna po prostej.
    bend=True: dodatkowo prędkość wzdłuż orbity zamienia się w promieniową
    (pas 1, Mars 2, Ziemia 3 pola/turę na pole prędkości)."""
    r, th, u = a * AU, 0.0, [ur, ut]
    for _ in range(turns):
        if bend:
            ra = r / AU
            u[0] += (3 if ra < 1.25 else 2 if ra < 1.75 else 1) * u[1]
        th += (mean_motion(r / AU) - OMEGA_REF) * TURN
        r += u[0] * HEX
        th += u[1] * HEX / r
    return r, th


def error(a, ur, ut, turns, bend=False):
    try:
        rt, tt = true_coast(a, ur, ut, turns)
        rg, tg = game_coast(a, ur, ut, turns, bend)
        return np.linalg.norm(to_xy(rt, tt) - to_xy(rg, tg)) / HEX
    except (ValueError, ZeroDivisionError):
        return float("nan")   # trasa wpada w zamknięty pierścień 1


print("== Lot swobodny z prędkością 1 pole/turę: błąd prostej linii (pola) ==")
for name, a in PLACES:
    for turns in (1, 2, 3):
        errs = [error(a, ur, ut, turns) for _, ur, ut in DIRS]
        errs = [e for e in errs if not math.isnan(e)]
        print(f"{name:12s} po {turns} r.: {min(errs):.1f}–{max(errs):.1f}")

print("\n== Przykład: pas, 1 pole/turę do przodu, lot swobodny ==")
for turns in (1, 2, 3):
    r, th = true_coast(A_REF, 0, 1, turns)
    print(f"po {turns} r.: {(r / AU - A_REF) / HEX_AU:+.1f} pierścienia od Słońca, "
          f"{th * r / HEX:+.1f} pola wzdłuż orbity")
print(f"(prędkość orbitalna w pasie {v_circ(A_REF) / 1e3:.1f} km/s, ucieczki "
      f"{math.sqrt(2) * v_circ(A_REF) / 1e3:.1f} km/s, 1 pole/turę = {U / 1e3:.1f} km/s)")


def hold_cost(a, ur, ut, steps=4000):
    """Δv [jednostki] potrzebne, żeby przez 1 turę lecieć po prostej z gry."""
    dt = TURN / steps
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


print("\n== Koszt utrzymania prostego kursu przez 1 turę, prędkość 1 (jednostki) ==")
print(" " * 13 + "".join(f"{d:>13s}" for d, _, _ in DIRS))
for name, a in [("Ziemia", 1.0), ("Mars", 1.5), ("pas 2,24 AU", A_REF)]:
    cells = []
    for _, ur, ut in DIRS:
        cells.append("–" if a + ur * HEX_AU < 0.75 else f"{hold_cost(a, ur, ut):.1f}")
    print(f"{name:12s} " + "".join(f"{c:>13s}" for c in cells))

print("\n== Prosta zasada zakrzywiania: błąd (pola) bez zasady / z zasadą ==")
for name, a in PLACES[1:]:
    for d, ur, ut in DIRS:
        row = "  ".join(f"{t} r.: {error(a, ur, ut, t):.1f}/{error(a, ur, ut, t, True):.1f}" for t in (1, 2, 3))
        print(f"{name:12s} {d:12s} {row}")
