# Synodic Board – a board of the inner Solar System

*[Wersja polska](board_pl.md)*

## What this board is

The board shows the inner Solar System – the space from the Sun to the asteroid belt. It is designed as a general-purpose space for hard science fiction games about space exploration: players fly ships between planets, exploit the resources of the asteroid belt and face the challenges of real orbital mechanics. The physics is real; only the ships' engines come from the future.

The name comes from the synodic frame – a frame of reference that rotates together with orbiting bodies. The whole movement mechanic of the board is built on such a frame.

The board is not tied to any particular game – it is a ready-made base on which different games can be built.

## Grid and scale

The board uses a hexagonal grid divided into concentric rings around the Sun in the centre. Each ring lies **0.5 AU** further out than the previous one (1 AU is the mean distance between the Earth and the Sun – about 150 million km).

Ring number `x` contains exactly `6x` hexes.

### Printing

The board is meant to be printed in **A2** format (the PDF and SVG files at 200% scale). A hex is then about 30 mm across the flats, and a pawn fits within one hex if it is at most about 27 mm wide. Smaller formats are too cramped for 3D pawns.

## Planetary orbits

The four planets of the inner Solar System occupy consecutive rings:

| Planet | Ring | Distance from the Sun |
|--------|------|-----------------------|
| Mercury and Venus | 1 | ~0.5 AU |
| Earth | 2 | ~1 AU |
| Mars | 3 | ~1.5 AU |

At this scale Mercury and Venus lie very close to each other and share a ring. In games built on the board they serve as background rather than active locations.

## The asteroid belt

Rings 4–6 (2–3 AU) are the asteroid belt. The popular image of the belt as a thin ring comes from the distorted proportions of popular-science drawings – in reality the dense part of the belt is hundreds of millions of kilometres wide. At this scale Jupiter would lie on ring 10–11 (5.2 AU) – almost twice as far out as the edge of the board.

### Random placement of objects

Hexes in the asteroid belt are labelled with numbers that correspond to a roll of two dice: a **d12** and a **d8**. The d12 picks a sector (12 sectors around the board), the d8 a hex within the sector. The mapping is not exactly one-to-one, so some hexes cover several results (marked e.g. `3-4`).

This makes it quick to place asteroids, resources or events at random, while keeping a distribution that matches the real belt.

### Drift (optional)

The board rotates together with one orbit in the belt; the rest of the belt circles the Sun slightly faster or slower. A game that needs to track the position of particular asteroids for longer can represent this:

- ring 4: 1 hex forward every 3 rounds,
- ring 5: 1 hex backward every 3 rounds,
- ring 6: 1 hex backward every round.

"Forward" means in the direction in which the planets move. Individual known bodies can be tracked separately: Ceres lies on the inner edge of ring 6 and moves 2 hexes backward every 3 rounds.

A game can also ignore drift – details in [model.md](model.md#drift-in-play--optional).

## Frame of reference – how movement works on the board

This is the most important and most original feature of the board.

The board **is not stationary** – it rotates around the Sun. Thanks to this, objects in the asteroid belt stay practically still on the board, while the planets closer to the Sun – which really do orbit faster – visibly move around the board in one direction every round.

### Orbital speeds

One game round corresponds to about 87 days (a little less than a quarter of a year). Every round, all objects on a given ring – planets, players' ships, everything – move by:

| Ring | Circumference (hexes) | Planet | Orbital movement (hexes/round) | Angular movement |
|------|-----------------------|--------|-------------------------------|------------------|
| 1 | 6 | Mercury, Venus | 3 hexes | 180° |
| 2 | 12 | Earth | 2 hexes | 60° |
| 3 | 18 | Mars | 1 hex | 20° |
| 4–6 | 24–36 | asteroid belt | 0 hexes | 0° |

The angular movement differs from orbit to orbit because the rings have different circumferences. The Earth moves 2 hexes along a 12-hex ring, which is 60° – one sixth of a full orbit per round. Mars moves 1 hex along an 18-hex ring, which is only 20°.

Everything moves in the same direction (the real direction of motion around the Sun). Mercury and Venus are not tracked as active locations in the game.

## Ship movement

Every ship has two components of movement:

**Orbital movement** – coming from the ring the ship is on (see the table above). It applies to all objects without exception.

**Powered movement** – driven by the ship's engine. Its speed (1–2 hexes per round) is comparable to orbital speeds: orbital mechanics cannot be ignored, but active manoeuvring can use it or work against it.

### Rounds and turns

- **A round** is the organisational unit of the game: in every round each player makes their move. It corresponds to a little under 3 months of time (about 87 days). Once per round every object on a ring moves along its orbit.
- **A turn** is a given player's – or, more generally, a side's – go within a round.

Sequence of a round:

1. **The neutral turn**, at the start of the round:
   - the Earth and Mars move along their orbits,
   - objects in the asteroid belt move according to drift (if the game tracks it),
   - the events of the round are resolved, for example interesting places in the belt appearing and disappearing.
2. **The players' turns**, one after another. In their turn a player, for each of their ships:
   1. carries out **orbital movement** – the ship moves together with the ring it stands on; the velocity marker moves with it and keeps its position relative to the ship,
   2. carries out **powered movement** – according to the flight model (below).

Orbital movement is taken from the ring the ship actually stands on – after powered movement it could already be on another ring. In their turns, players see where the planets are in this round.

Between the neutral turn and a player's turn, that player's ships briefly "lag behind" the rest of the board. In a game without direct conflict that is not a problem. For games with conflict, a better variant is to carry out the orbital movement of all ships in the neutral turn – positions are then always consistent, at the cost of moving all ships at once.

### Reference model

In space you pay for changing your velocity, not for the distance travelled.

1. A ship has its own velocity: 0–2 hexes per round in any direction. The simplest way to show it is a marker on the hex the ship will reach in its next turn, as in classic vector movement.
2. In its turn a ship may change its velocity by at most 2 hexes in total – before moving, after moving, or partly before and partly after. Each hex of velocity change costs 1 fuel unit.
3. Between changes the ship moves by its velocity. Flying at a constant velocity costs nothing.
4. Speeds above 2 hexes per round are forbidden by regulations.
5. Ring 1 is closed to ships – it is too hot close to the Sun, and the ring moves half an orbit per round.

Examples:

- **A hop** of 1 hex: +1 before moving, move, −1 after moving. Cost 2.
- **Braking on arrival**: a ship flying at speed 2 reaches its target and brakes at once (−2 after moving). Cost 2.

A freighter's tank holds around 20 units. The flight line on the board is a schematic of a planned route: start, end, time and cost match reality, while the real path is curved. Rationale: [model.md](model.md#why-the-reference-model-makes-sense).

### Docking and landing

- A ship is **docked** when it has zero velocity on the target hex – at the start of its turn, at the end of its turn, or in between. A **touch-and-go stop** is, for example: braking before moving (−1), docking, accelerating at the end of the turn (+1).
- **Short actions** – trading, transferring cargo, exchanging passengers – the ship carries out straight after docking, including during a touch-and-go stop.
- **Long actions** – mining, emergency refuelling – require **a full round of stopover**: in that turn the ship has zero velocity and does not change it at all. Accelerating and braking take time – a velocity change of 2 hexes is a whole round of engine work.
- **The Earth and Mars:** a docked ship is placed on the planet's **station space**, outside the main grid of the board. A ship on the station space moves together with the planet. When leaving, at the start of its turn it returns to the planet's hex – instead of orbital movement – and then moves normally. The station space also solves crowding at the planet.
- A fusion drive is too weak to lift off from the surface of a planet or a large asteroid:
  - at the Earth and Mars the ship docks at a station in orbit, and the station's landers run to the surface,
  - Ceres and Vesta need a lander – a local one or the freighter's own, carried on board (at the cost of range or cargo),
  - on small asteroids, up to a few km across, the freighter lands directly.

### Simplified model

Games that don't want to track ship velocities can charge for every hex of powered movement:

| Where | Ship speed | Cost |
|-------|------------|------|
| ring 1 | closed to ships | – |
| ring 2 (Earth) | max. 1 hex/round | 3 |
| ring 3 (Mars) | max. 1 hex/round | 2 |
| rings 4–6 (asteroid belt) | 1 or 2 hexes/round | 1 for 1 hex, 3 for 2 hexes |

A move across a ring boundary follows the limit and cost of the ring closest to the Sun that the move touches. The sequence of a round, docking and station spaces work the same way, except that a ship docks by ending its movement on the target hex. A freighter's tank then holds around 15 units. This model is consistent in itself but departs from physics – what exactly it loses is described in [model.md](model.md#simplified-model-cost-per-hex).

## Route planning – the heart of the mechanic

Changing orbit requires powered movement in the radial direction (closer to or further from the Sun). But getting there is only half the problem – the target moves too.

### Earth–Mars transfer

In reality the most energy-efficient flight to Mars is the so-called **Hohmann transfer**: instead of flying straight, the spacecraft makes two short engine burns and for most of the way "falls" along an ellipse without using fuel. The flight takes several months – in that time Mars moves on along its orbit. For the two to meet, Mars must be about 44° "ahead" of the spacecraft at launch. This transfer window opens only once every 26 months or so.

That is exactly how NASA's **Perseverance** mission worked: the rover launched in July 2020, when the planets were suitably aligned, and landed on Mars in February 2021 – after just under 7 months of flight. Had the rocket not launched in that window, the next chance would have come only in 2022.

On the board it works the same way: a ship flying from ring 2 to ring 3 needs time to change orbit. Meanwhile Mars moves along its orbit – the player has to plan the course so as to arrive on ring 3 exactly when and where Mars will be.

### Returning from the asteroid belt

Flying deep into the asteroid belt is only half of the mission. By the time a ship has reached its target, mined the resources and is ready to return, the Earth is somewhere else entirely. During the dozen or several dozen rounds spent in the belt, the Earth has moved many hexes along its orbit. The return flight also takes several rounds, during which the Earth does not stand still.

A player who focuses only on efficient mining in the belt and forgets to keep track of the Earth's position may face a hard choice: wait for a better return window (losing time) or fly faster (losing fuel). This tension between a successful mission and a smooth return is one of the key dramas of the game.

In reality the problem is the same – and even sharper. NASA's **Dawn** probe visited the asteroid Vesta (2011–2012) and the dwarf planet Ceres (2015–2018). Its propellant budget was planned for reaching both targets and descending to low science orbits – a return to the Earth was never part of the plan. The mission ended in 2018, when the hydrazine used to control the probe's orientation ran out, and Dawn stayed where it was: in orbit around Ceres, where it will remain for decades. A player who spends all their fuel exploring the belt may face the same dilemma.

---

How this model relates to reality and the design decisions behind it: [model.md](model.md).
