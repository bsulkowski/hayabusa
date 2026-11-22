"""Model referencyjny lotów: koszt zaplanowanych tras w tempie gry.

Trasa zaczyna się i kończy na orbicie kołowej; tor między nimi to optymalny łuk
(zagadnienie Lamberta). Cel jest tam, gdzie wskazuje gra: statek co turę przesuwa się
o swoją prędkość i razem z pierścieniem, na którym zaczął turę.
1 jednostka paliwa = zmiana prędkości o 1 pole na turę.
Dokumentacja: docs/model_pl.md, „Dlaczego model referencyjny ma sens”.
"""
import math
from orbits import *

print(f"1 pole na turę = {U / 1e3:.1f} km/s (= 1 jednostka paliwa)\n")


def along(a, hexes, turns):
    """Lot wzdłuż pierścienia o `hexes` pól w ciągu `turns` tur."""
    t = turns * TURN
    sweep = mean_motion(a) * t + hexes * HEX_AU / a
    return transfer_dv(a, a, sweep, t)


def radial(path):
    """Lot przez kolejne pierścienie, 1 pierścień na turę."""
    return transfer_dv(path[0], path[-1], game_sweep(path), (len(path) - 1) * TURN)


cases = [
    ("pas, 1 pole do przodu, prędkość 1", along(2.5, 1, 1), 2),
    ("pas, 2 pola do przodu, prędkość 1", along(2.5, 2, 2), 2),
    ("pas, 3 pola do przodu, prędkość 1", along(2.5, 3, 3), 2),
    ("pas, 4 pola do przodu, prędkość 1", along(2.5, 4, 4), 2),
    ("pierścień 4 -> 5, prędkość 1", radial([2.0, 2.5]), 2),
    ("pierścień 4 -> 6, prędkość 1", radial([2.0, 2.5, 3.0]), 2),
    ("Ziemia -> pierścień 4, prędkość 1", radial([1.0, 1.5, 2.0]), 2),
    ("Ziemia -> pierścień 5, prędkość 1", radial([1.0, 1.5, 2.0, 2.5]), 2),
    ("przeskok przy Ziemi do przodu", along(1.0, 1, 1), 2),
    ("przeskok przy Ziemi do tyłu", along(1.0, -1, 1), 2),
    ("przeskok Ziemia -> Mars", radial([1.0, 1.5]), 2),
    ("przeskok przy Marsie do przodu", along(1.5, 1, 1), 2),
    ("przeskok przy Marsie do tyłu", along(1.5, -1, 1), 2),
    ("pas, 2 pola do przodu, prędkość 2", along(2.5, 2, 1), 4),
    ("pierścień 4 -> 6 w 1 turę, prędkość 2", transfer_dv(2.0, 3.0, mean_motion(2.0) * TURN, TURN), 4),
    ("Ziemia -> pierścień 4 w 1 turę, prędkość 2", transfer_dv(1.0, 2.0, mean_motion(1.0) * TURN, TURN), 4),
]
for label, dv, model in cases:
    print(f"{label:42s} {dv / 1e3:5.1f} km/s = {dv / U:4.1f} jedn.  (model: {model})")
