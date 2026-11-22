# Synodic Board – a board of the inner Solar System

*[Wersja polska](board_pl.md)*

## What this board is

The board shows the inner Solar System – the space from the Sun to the asteroid belt. It is designed as a general-purpose space for hard science fiction games about space exploration: players fly ships between planets, exploit the resources of the asteroid belt and face the challenges of real orbital mechanics. The physics is real; only the ships' engines come from the future.

The name comes from the synodic frame – a frame of reference that rotates together with orbiting bodies. The whole movement mechanic of the board is built on such a frame.

The board is not tied to any particular game – it is a ready-made base on which different games can be built.

## Grid and scale

The board uses a hexagonal grid divided into concentric rings around the Sun in the centre. Each ring lies **0.5 AU** further out than the previous one (1 AU is the mean distance between the Earth and the Sun – about 150 million km).

Ring number `x` contains exactly `6x` hexes.

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

- ring 4: 1 hex forward every 3 turns,
- ring 5: 1 hex backward every 3 turns,
- ring 6: 1 hex backward every turn.

"Forward" means in the direction in which the planets move. A game can also ignore drift – details in [model.md](model.md#drift-in-play--optional).

## Frame of reference – how movement works on the board

This is the most important and most original feature of the board.

The board **is not stationary** – it rotates around the Sun. Thanks to this, objects in the asteroid belt stay practically still on the board, while the planets closer to the Sun – which really do orbit faster – visibly move around the board in one direction every turn.

### Orbital speeds

One game turn corresponds to about 87 days (a little less than a quarter of a year). Every turn, all objects on a given ring – planets, players' ships, everything – move by:

| Ring | Circumference (hexes) | Planet | Orbital movement (hexes/turn) | Angular movement |
|------|-----------------------|--------|-------------------------------|------------------|
| 1 | 6 | Mercury, Venus | 3 hexes | 180° |
| 2 | 12 | Earth | 2 hexes | 60° |
| 3 | 18 | Mars | 1 hex | 20° |
| 4–6 | 24–36 | asteroid belt | 0 hexes | 0° |

The angular movement differs from orbit to orbit because the rings have different circumferences. The Earth moves 2 hexes along a 12-hex ring, which is 60° – one sixth of a full orbit per turn. Mars moves only 20°, because its ring is larger.

Everything moves in the same direction (the real direction of motion around the Sun). Mercury and Venus are not tracked as active locations in the game.

## Ship movement

Every ship has two components of movement, which act together:

**Forced movement** – coming from the ring the ship is on (see the table above). It applies to all objects without exception.

**Powered movement** – driven by the ship's engine. Its speed (1–2 hexes per turn) is comparable to orbital speeds: orbital mechanics cannot be ignored, but active manoeuvring can use it or work against it.

### Reference model

In space you pay for changing your velocity, not for the distance travelled. The proposed flight model:

1. A ship has its own velocity: 0–2 hexes per turn in any direction (a marker on the hex the ship will reach next turn).
2. At the start of a turn a ship may change its velocity by at most 2 hexes. Each hex of velocity change costs 1 fuel unit.
3. The ship moves by its velocity and together with the ring on which it started the turn.
4. Hop: a ship may move 1 hex and stop in the same turn (cost 2).
5. Docking, landing and any other interaction require zero velocity. At planets and large asteroids the ship docks at a station in orbit, and separate shuttles run to the surface – a fusion drive is too weak to lift off from the surface. Ships can land only on small asteroids, up to a few km across.
6. Speeds above 2 hexes per turn are forbidden by regulations.
7. Ring 1 is closed to ships – it is too hot close to the Sun, and the ring moves half an orbit per turn.

A freighter's tank holds around 20 units. The flight line on the board is a schematic of a planned route: start, end, time and cost match reality, while the real path is curved. Rationale: [model.md](model.md#reference-model).

### Simplified model

Games that don't want to track ship velocities can charge for every hex of powered movement:

| Where | Ship speed | Cost |
|-------|------------|------|
| ring 1 | closed to ships | – |
| ring 2 (Earth) | max. 1 hex/turn | 3 |
| ring 3 (Mars) | max. 1 hex/turn | 2 |
| rings 4–6 (asteroid belt) | 1 or 2 hexes/turn | 1 for 1 hex, 3 for 2 hexes |

A move across a ring boundary follows the limit and cost of the ring closest to the Sun that the move touches. A freighter's tank then holds around 15 units. This model is consistent in itself but departs from physics – what exactly it loses is described in [model.md](model.md#simplified-model-cost-per-hex).

## Route planning – the heart of the mechanic

Changing orbit requires powered movement in the radial direction (closer to or further from the Sun). But getting there is only half the problem – the target moves too.

### Earth–Mars transfer

In reality the most energy-efficient flight to Mars is the so-called **Hohmann transfer**: instead of flying straight, the spacecraft makes two short engine burns and for most of the way "falls" along an ellipse without using fuel. The flight takes several months – in that time Mars moves on along its orbit. For the two to meet, Mars must be about 44° "ahead" of the spacecraft at launch. This transfer window opens only once every 26 months or so.

That is exactly how NASA's **Perseverance** mission worked: it launched in July 2020, when the planets were suitably aligned, and the rover landed on Mars in February 2021 – after exactly 7 months of flight. Had the rocket not launched in that window, the next chance would have come only in 2022.

On the board it works the same way: a ship flying from ring 2 to ring 3 needs time to change orbit. Meanwhile Mars moves along its orbit – the player has to plan the course so as to arrive on ring 3 exactly when and where Mars will be.

### Returning from the asteroid belt

Flying deep into the asteroid belt is only half of the mission. By the time a ship has reached its target, mined the resources and is ready to return, the Earth is somewhere else entirely. During the dozen or several dozen turns spent in the belt, the Earth has moved many hexes along its orbit. The return flight also takes several turns, during which the Earth does not stand still.

A player who focuses only on efficient mining in the belt and forgets to keep track of the Earth's position may face a hard choice: wait for a better return window (losing time) or cut diagonally across many rings (losing fuel). This tension between a successful mission and a smooth return is one of the key dramas of the game.

In reality the problem is the same – and even sharper. NASA's **Dawn** probe visited the asteroid Vesta (2011–2012) and the dwarf planet Ceres (2015–2018) in the asteroid belt, using almost all of its fuel on orbital manoeuvres. Returning to Earth was never an option – all the fuel went into reaching the targets and descending to low science orbits. Dawn ended its mission in 2018 exactly where it was: in orbit around Ceres, where it will stay for decades. A player who spends all their fuel exploring the belt may face the same dilemma.

---

How this model relates to reality and the design decisions behind it: [model.md](model.md).
