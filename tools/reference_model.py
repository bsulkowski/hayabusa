"""Reference flight model: cost of planned routes at game pace.

A route starts and ends on a circular orbit; the path between is the optimal arc
(Lambert's problem). The target is where the game puts it: every round the ship moves
by its velocity and together with the ring on which it started the round.
1 fuel unit = a velocity change of 1 hex per round.
Documentation: docs/model.md, "Why the reference model makes sense".
"""
import math
from orbits import *

print(f"1 hex per round = {U / 1e3:.1f} km/s (= 1 fuel unit)\n")


def along(a, hexes, rounds):
    """Flight along a ring by `hexes` hexes in `rounds` rounds."""
    t = rounds * ROUND
    sweep = mean_motion(a) * t + hexes * HEX_AU / a
    return transfer_dv(a, a, sweep, t)


def radial(path):
    """Flight across successive rings, 1 ring per round."""
    return transfer_dv(path[0], path[-1], game_sweep(path), (len(path) - 1) * ROUND)


cases = [
    ("belt, 1 hex forward, speed 1", along(2.5, 1, 1), 2),
    ("belt, 2 hexes forward, speed 1", along(2.5, 2, 2), 2),
    ("belt, 3 hexes forward, speed 1", along(2.5, 3, 3), 2),
    ("belt, 4 hexes forward, speed 1", along(2.5, 4, 4), 2),
    ("ring 4 -> 5, speed 1", radial([2.0, 2.5]), 2),
    ("ring 4 -> 6, speed 1", radial([2.0, 2.5, 3.0]), 2),
    ("Earth -> ring 4, speed 1", radial([1.0, 1.5, 2.0]), 2),
    ("Earth -> ring 5, speed 1", radial([1.0, 1.5, 2.0, 2.5]), 2),
    ("hop near the Earth, forward", along(1.0, 1, 1), 2),
    ("hop near the Earth, backward", along(1.0, -1, 1), 2),
    ("hop Earth -> Mars", radial([1.0, 1.5]), 2),
    ("hop near Mars, forward", along(1.5, 1, 1), 2),
    ("hop near Mars, backward", along(1.5, -1, 1), 2),
    ("belt, 2 hexes forward, speed 2", along(2.5, 2, 1), 4),
    ("ring 4 -> 6 in 1 round, speed 2", transfer_dv(2.0, 3.0, mean_motion(2.0) * ROUND, ROUND), 4),
    ("Earth -> ring 4 in 1 round, speed 2", transfer_dv(1.0, 2.0, mean_motion(1.0) * ROUND, ROUND), 4),
]
for label, dv, model in cases:
    print(f"{label:36s} {dv / 1e3:5.1f} km/s = {dv / U:4.1f} units  (model: {model})")
