"""Shared functions: motion on orbits around the Sun and board parameters.

Model: two bodies (Sun + ship), circular and coplanar orbits.
SI units unless the name says otherwise (AU, turns, hexes).
"""
import math
import numpy as np
from scipy.integrate import solve_ivp

MU = 1.32712e20          # gravitational parameter of the Sun [m^3/s^2]
AU = 1.495979e11         # [m]
DAY = 86400.0
YEAR = 365.25 * DAY

# --- board parameters -------------------------------------------------------------
HEX_AU = 0.5                                  # grid step
T_EARTH, T_MARS = 1.0, 1.8809                 # orbital periods [years]
W_EARTH, W_MARS = 360 / T_EARTH, 360 / T_MARS # angular velocities [deg/year]
# The board rotates so that on the board the Earth is exactly 3x faster than Mars:
# (W_EARTH - W_REF) = 3 (W_MARS - W_REF)
W_REF = (3 * W_MARS - W_EARTH) / 2            # [deg/year]
T_REF = 360 / W_REF                           # [years]
A_REF = T_REF ** (2 / 3)                      # [AU], Kepler's law
TURN = 60 / (W_EARTH - W_REF) * YEAR          # Earth: 60 deg on the board per turn [s]
OMEGA_REF = math.radians(W_REF) / YEAR        # [rad/s]
HEX = HEX_AU * AU                             # [m]
U = HEX / TURN                                # 1 hex per turn [m/s]

RING_AU = {k: HEX_AU * k for k in range(1, 7)}


def period_years(a_au):
    return a_au ** 1.5


def mean_motion(a_au):
    """Angular velocity of a circular orbit [rad/s]."""
    return math.sqrt(MU / (a_au * AU) ** 3)


def v_circ(a_au):
    """Speed on a circular orbit [m/s]."""
    return math.sqrt(MU / (a_au * AU))


def circ_state(a_au, theta):
    """Position and velocity on a circular orbit of radius a_au at angle theta [rad]."""
    r, v = a_au * AU, v_circ(a_au)
    return (np.array([r * math.cos(theta), r * math.sin(theta)]),
            np.array([-v * math.sin(theta), v * math.cos(theta)]))


def hohmann(a1_au, a2_au):
    """Hohmann transfer: (delta-v [m/s], time [s])."""
    r1, r2 = a1_au * AU, a2_au * AU
    dv1 = math.sqrt(MU / r1) * (math.sqrt(2 * r2 / (r1 + r2)) - 1)
    dv2 = math.sqrt(MU / r2) * (1 - math.sqrt(2 * r1 / (r1 + r2)))
    t = math.pi * math.sqrt(((r1 + r2) / 2) ** 3 / MU)
    return abs(dv1) + abs(dv2), t


def _stumpff(z):
    if z > 1e-8:
        s = math.sqrt(z)
        return (s - math.sin(s)) / s ** 3, (1 - math.cos(s)) / z
    if z < -1e-8:
        s = math.sqrt(-z)
        return (math.sinh(s) - s) / s ** 3, (math.cosh(s) - 1) / (-z)
    return 1 / 6, 1 / 2


def lambert(r1, r2, t):
    """Lambert's problem (prograde, no full revolutions).

    Returns the velocity at the start and at the end of the arc from r1 to r2 in time t.
    """
    R1, R2 = np.linalg.norm(r1), np.linalg.norm(r2)
    cross = r1[0] * r2[1] - r1[1] * r2[0]
    dth = math.acos(np.clip(np.dot(r1, r2) / R1 / R2, -1, 1))
    if cross < 0:
        dth = 2 * math.pi - dth
    A = math.sin(dth) * math.sqrt(R1 * R2 / (1 - math.cos(dth)))

    def y(z):
        S, C = _stumpff(z)
        return R1 + R2 + A * (z * S - 1) / math.sqrt(C)

    def F(z):
        S, C = _stumpff(z)
        yy = y(z)
        if yy < 0:
            return -1e30
        return (yy / C) ** 1.5 * S + A * math.sqrt(yy) - math.sqrt(MU) * t

    lo, hi = -4 * math.pi ** 2, 4 * math.pi ** 2 * 0.999
    while y(lo) < 0:
        lo += 0.1
    for _ in range(200):
        m = (lo + hi) / 2
        lo, hi = (lo, m) if F(m) > 0 else (m, hi)
    yy = y((lo + hi) / 2)
    f, g, gd = 1 - yy / R1, A * math.sqrt(yy / MU), 1 - yy / R2
    return (r2 - f * r1) / g, (gd * r2 - r1) / g


def transfer_dv(a1_au, a2_au, sweep_rad, t):
    """Delta-v [m/s] of a route starting and ending on circular orbits.

    Start: orbit a1 at angle 0. Target: orbit a2 at angle sweep_rad, reached after time t.
    """
    r1, v1 = circ_state(a1_au, 0.0)
    r2, v2 = circ_state(a2_au, sweep_rad)
    vd, va = lambert(r1, r2, t)
    return np.linalg.norm(vd - v1) + np.linalg.norm(v2 - va)


def game_sweep(rings_au):
    """Angle (inertial) swept by a ship in the game: every turn the forced movement of
    the ring on which the ship starts the turn. rings_au - radii of the successive hexes."""
    return sum(mean_motion(a) * TURN for a in rings_au[:-1])


def propagate(r, v, t):
    """Free flight in the gravity field of the Sun."""
    f = lambda _, s: [s[2], s[3], *(-MU * np.array(s[:2]) / np.hypot(*s[:2]) ** 3)]
    sol = solve_ivp(f, [0, t], [*r, *v], rtol=1e-10, atol=1)
    return sol.y[:2, -1], sol.y[2:, -1]
