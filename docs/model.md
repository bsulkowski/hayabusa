# Synodic Board – the model and design decisions

*[Wersja polska](model_pl.md)*

## Who this document is for

This document is for people interested in how the board relates to the real physics of the Solar System: what is modelled faithfully, what is simplified and why. It may be useful both for game designers who want to modify the board or draw inspiration from it for their own, and for players curious about the astronomical background.

## Distance scale

A grid step of 0.5 AU per ring gives a very good approximation for the planets that are active in play:

| Object | Reality | Model | Error |
|--------|---------|-------|-------|
| Earth | 1.00 AU | ring 2 (1.0 AU) | 0% |
| Mars | 1.52 AU | ring 3 (1.5 AU) | −2% |

### The asteroid belt

A ring is not a line but a band one hex wide – from −0.25 to +0.25 AU around its nominal distance. Rings 4–6 therefore cover the region **1.75–3.25 AU**.

The main asteroid belt lies between two Kirkwood gaps – empty bands cleared by resonances with Jupiter: 4:1 (2.06 AU) and 2:1 (3.27 AU). The outer edge of the belt on the board matches it practically perfectly. The inner edge reaches about 0.3 AU closer to the Sun, but that region (1.78–2.0 AU) is occupied by the Hungaria group – the innermost dense concentration of asteroids in the Solar System.

Ceres (2.77 AU) falls on the boundary between rings 5 and 6.

### Mercury and Venus

Mercury actually lies at 0.39 AU, Venus at 0.72 AU. In the model both planets land on ring 1 (0.5 AU) – neither comes out well. This is a deliberate decision: both planets are background in games, not active locations, so the accuracy of their positions doesn't matter for play.

## Frame of reference and orbital speeds

### Where the 3/2/1/0 hexes per round come from

When designing the orbital speeds, the goal was to find whole numbers that best capture the proportions of real angular velocities. The angular velocities of the Earth, Mars and the asteroid belt are roughly in the proportion **4 : 2 : 1**.

The board rotates in the direction of planetary motion at a speed corresponding to that unit "1". After subtracting the board's rotation, the visible speeds are **3 : 1 : 0** – exactly what the movement table shows. In astrodynamics such a rotating frame of reference is called a synodic frame – hence the board's name. On the board the Earth moves 60° per round (2 hexes on a 12-hex ring), and Mars 20° (1 hex on an 18-hex ring).

### Reference orbit and time scale

The 4:2:1 proportion is only a starting point – the real ratio of the angular velocities of the Earth and Mars is 1.88, not 2. Even so, the **3:1 proportion on the board can be exact**: it is enough to choose the board's rotation speed so that, after subtracting it, the Earth moves exactly three times faster than Mars.

Two values follow from this condition:

- the board is synchronised with an orbit of radius **2.24 AU** and an orbital period of **3.36 years** – in the inner part of the asteroid belt, closer to the Sun than Ceres,
- one round lasts about **87 days** (a little under a quarter of a year).

Thanks to this, the Earth and Mars move on the board as they do in reality – with an accuracy limited only by the rounding of the round length. Neither the reference orbit nor the round length was assumed in advance; both are the result of the fitting. The price is that the board rotates together with the inner part of the belt, not with its middle – the further parts of the belt drift (see below).

Synchronising with Ceres would give a round closer to an exact quarter of a year, but the Earth:Mars proportion on the board would then be about 2.5:1 instead of 3:1. A quarter of a year is a convenient figure to communicate, but it slightly overstates the real length of a round.

### Ring 1

By Kepler's law a circular orbit at 0.5 AU would move about 3.6 hexes per round on the board – the model rounds this to 3. The real planets of this ring diverge in both directions: Venus would move about 1.9 hexes per round, Mercury about 5.5. One ring with one speed can't represent both – which doesn't matter, since both planets are background.

## The asteroid belt – drift and randomness

### An unavoidable simplification

The asteroid belt is not a disc rotating at a constant speed – each asteroid orbits at its own speed, determined by its orbit. Objects closer to the Sun orbit faster, objects further out slower. The board is synchronised with only one orbit (2.24 AU), so objects on the other rings of the belt would drift relative to the board:

| Ring | Distance | Drift relative to the board |
|------|----------|-----------------------------|
| 4 | 2.0 AU | +0.3 hexes/round (forward) |
| – | 2.24 AU (reference orbit) | 0 |
| 5 | 2.5 AU | −0.3 hexes/round (backward) |
| 6 | 3.0 AU | −0.9 hexes/round (backward) |

Ceres would drift by about −0.6 hexes/round. Over a typical game (30–50 rounds) it would move by a dozen to several dozen hexes, and objects on the outer ring even more.

### Drift in play – optional

Drift can be tracked simply by rounding it to whole hexes:

| Ring | Drift | Simplification |
|------|-------|----------------|
| 4 | +0.3 hexes/round | 1 hex forward every 3 rounds |
| 5 | −0.3 hexes/round | 1 hex backward every 3 rounds |
| 6 | −0.9 hexes/round | 1 hex backward every round |

"Forward" means in the direction in which the planets move. The arithmetic is simple; the trouble may be the number of objects to move – every third round all objects on rings 4 and 5, and every round those on ring 6.

So a game can either ignore drift or apply it, depending on its needs:

- **Ignoring it** is enough when objects in the belt appear at random and their exact position doesn't need to be tracked for long. The asteroid belt consists of millions of bodies on slightly different orbits, so random placement with dice represents it well – drift is absorbed by the randomness.
- **Tracking it** makes sense when a game needs to know the position of a particular asteroid more precisely over a longer time.

Individual known bodies can be tracked separately, even when a game ignores the drift of the rest of the belt. Ceres (2.77 AU) lies on the inner edge of ring 6, but orbits faster than the rest of that ring: it drifts by about −0.6 hexes/round, that is **2 hexes backward every 3 rounds**. Combined with the need for a lander (see "Launching from the surface"), this makes a trip to Ceres something to plan: the target moves, and a lander is needed on arrival.

## Ship movement and physics

A ship's movement on the board consists of orbital movement (together with the ring) and powered movement, driven by the engine. The board proposes two flight models:

- **the reference model** – as faithful to physics as possible, a point of reference for hard science fiction,
- **the simplified model** – simpler to play, at the cost of a few deliberate departures from physics.

Any game can loosen the flight model further. This chapter shows what is lost when it does.

### Orbital movement is inertia

A ship without thrust on a given ring flies on a circular orbit – that is, freely, without using fuel. So the model has inertia; its natural state is not standing still but orbiting.

### In space you pay for changing velocity

In reality fuel is spent on changing velocity: on leaving the departure orbit and on matching the target's orbit. In between, the ship flies freely, along an arc shaped by gravity. So the length of the route doesn't matter much – what counts is how fast you have to accelerate and how much you then have to brake.

The unit on the board is a speed of 1 hex per round – about **10 km/s** relative to the local orbit. That is a lot: the orbital speed in the asteroid belt is about 20 km/s.

### Reference model

The full rules of the reference model – the sequence of a round, movement, docking – are in the [board description](board.md#reference-model). In short: a ship has its own velocity of 0–2 hexes per round, each hex of velocity change costs 1 fuel unit (at most 2 per turn), flying at constant velocity is free, and docking requires zero velocity. This chapter explains why the rules are the way they are.

### Why the reference model makes sense

The cheapest planned route at game pace – starting and ending in orbit, along an arbitrarily curved path – costs:

| Route | Δv | In the reference model |
|-------|----|------------------------|
| asteroid belt, 1–4 hexes forward at speed 1 | 19–21 km/s | 2 |
| asteroid belt, 1–2 rings outward at speed 1 | 20–21 km/s | 2 |
| Earth → ring 4 or 5 at speed 1 | 20–21 km/s | 2 |
| 1-hex hop near the Earth or Mars | 20–26 km/s | 2 |
| routes at speed 2 | 40–48 km/s | 4 |

The model is accurate to about ±25% across the whole board: the cost depends neither on the length of the route nor on the location, only on acceleration and braking – exactly as in the model.

A real ship, however, doesn't fly in a straight line but along an arc. **The flight line on the board is a schematic of a planned route**: start, end, time and cost are real; the position during flight is nominal. This matters only if a game lets players do something with a ship in flight (for example intercept it). A change of plan mid-flight is also counted by the same rules – a fair approximation.

### Why not take the straight line literally

If the straight line were taken literally, as free flight, the model would diverge from physics. At game speeds gravity bends the path very strongly: in the asteroid belt, 1 hex per round forward (+10 km/s) is enough to escape the Solar System, and 2 hexes per round backward (−20 km/s) almost stop the ship relative to the Sun, so it starts falling towards it.

Position error of a ship coasting at 1 hex per round, compared with the straight line in the game (in hexes):

| Where | after 1 round | after 2 rounds | after 3 rounds |
|-------|--------------|---------------|---------------|
| near the Earth | 1.1–1.9 | 2–6 | 2–8 |
| near Mars | 0.7–1.0 | 1.6–4 | 2–8 |
| asteroid belt (2.24 AU) | 0.3–0.6 | 1.0–2.3 | 1.6–5 |
| asteroid belt (3 AU) | 0.2–0.4 | 0.7–1.5 | 1.1–3.4 |

The main mechanism is one of the most counter-intuitive phenomena of orbital mechanics: accelerating forward along the orbit raises the orbit. A ship flying forward in the belt is, after 3 rounds, about 3 rings further from the Sun and has not moved forward at all.

A straight course can be held with thrust, but the cost depends strongly on direction. Cost per round at a speed of 1 hex per round:

| Where | forward | backward | outward | inward |
|-------|---------|----------|---------|--------|
| near the Earth | 3.5 | 2.5 | 0.5 | – |
| near Mars | 2.0 | 1.3 | 0.3 | 0.5 |
| asteroid belt | 1.1 | 0.7 | 0.2 | 0.3 |

Flying away from or towards the Sun is almost free; flying along the orbit is expensive. A simple path-bending rule was also tested (forward velocity rounds into outward velocity: 1 hex per round in the belt, 2 near Mars, 3 near the Earth). It improves forward flight but makes backward flight worse – not worth an extra rule. Treating the flight line as a schematic of a planned route is simpler and gives correct costs.

### Round sequence and docking

**Orbital movement at the start of the turn.** Orbital movement is taken from the ring the ship actually stands on; after powered movement the ship could already be on another ring, where a hex means a different angle. The planets move in the neutral turn, at the start of the round, so in their turns players aim at current positions.

**Station spaces at the Earth and Mars.** A ship docked at a planet moves together with it. If it stood on the grid, it would briefly "lag behind" the planet between the neutral turn and its own turn. A station space outside the grid removes this problem, and crowding at the planet too.

**Docking needs only stabilisation.** Approach and docking take hours, at most days, while a round is about 87 days. So it is enough for the ship to have zero velocity on the target hex at any moment of its turn. Long actions are different: a velocity change of 2 hexes is a whole round of engine work (about 0.27 milli-g for 87 days). A touch-and-go stop – braking and accelerating again in the same turn – leaves time only for short actions, while mining or emergency refuelling need a turn with no velocity change at all.

**Velocity change before and after moving.** The engine works through the whole round, and 2 hexes of velocity change is what it can do in that time. With constant thrust, the distance a ship covers in a round corresponds to its average velocity – the velocity at the middle of the round. That is why the change is split into two halves of at most 1 hex each: before moving and after moving. The movement between them happens at the mid-round velocity, just as with continuous engine work. It is the same method (the so-called leapfrog) used in numerical simulations of orbital motion. Changing the whole velocity before moving would overstate the distance, and after moving – understate it. A hop, accelerating and braking then need no separate rules.

### Transfer windows

**The frequency of windows is exact.** The planets move on the board as they do in reality, so favourable alignments repeat every same number of rounds as in reality: Earth–Mars every 9 rounds (about 26 months), Earth–asteroid belt every 6 rounds, Mars–asteroid belt every 18 rounds.

**The planets' alignment at launch depends on the flight pace.** In the reference model ships really do fly at game pace, so the launch alignments on the board are real for such flights. They differ from the alignments for the cheapest, slow routes (the Hohmann transfer). The table shows by how many degrees the target must lead the ship at launch (minus – the target is behind):

| Route | At game pace | Cheapest route | Difference |
|-------|--------------|----------------|------------|
| Earth → Mars | +39° | +43° | −4° |
| Earth → ring 4 | +72° | +63° | +8° |
| Mars → ring 4 | +16° | +33° | −16° |
| Mars → Earth | −39° | −72° | +33° |
| ring 4 → Earth | −94° | −151° | +57° |
| ring 5 → Earth | −158° | +123° | +79° |

An Earth → Mars flight at game pace needs almost the same alignment as the cheapest route. For returns to the Earth the difference is large: on the cheapest route the ship travels half way around the Sun, and during the long flight the fast Earth moves much further. In the simplified model (below), which assumes the cheapest routes in shortened time, launch angles are therefore only approximate.

In both models the player learns a true principle: aim where the target will be, and wait for the window.

### Ring 1 – no-fly zone

By default ships do not enter ring 1. There are three reasons:

- **Heat** – the solar radiation flux there is four times higher than near the Earth, and almost seven times higher near Mercury.
- **Control** – the ring moves half an orbit per round, and gravity bends the path even more strongly than near the Earth. A ship with an own speed of 1–2 hexes per round practically loses control over where it ends up.
- **Cost of economical routes** – they are 8–11 times more expensive there than in the asteroid belt. In reality missions to Mercury take years and need many planetary flybys: the MESSENGER probe launched in 2004 and entered Mercury orbit only in 2011, after six such flybys.

The rule fits the role of Mercury and Venus as background. A game that wants to fly there can lift it.

### Propulsion and fuel

The reference model requires a **fusion drive**: with a unit of 10 km/s, other drives cannot carry enough propellant.

**Thrust.** A velocity change of 2 hexes within a round is about 20 km/s in 87 days – a constant acceleration of about 0.27 milli-g. With an exhaust velocity of about 300 km/s this requires a power of the order of 0.7 MW per tonne of ship. That is the distant future, but the physics stays honest: accelerations are of the order of milli-g, not a full g as in less restrained science fiction.

**Tank.** The velocity change a full tank provides depends only on the exhaust velocity and on the ratio of the ship's mass with propellant to its mass without – not on the size of the ship. For a freighter the cargo counts too, since it is part of the mass. Example: structure of mass 1, cargo 1 (or 2), full tank of mass 2, exhaust velocity about 300 km/s:

| Freighter state | Mass ratio | Δv | Game units |
|-----------------|------------|----|------------|
| empty | 3 | about 330 km/s | about 33 |
| loaded | 2 | about 210 km/s | about 21 |
| heavily loaded | 1.7 | about 155 km/s | about 15 |

For a game a single value is enough: **a tank of around 20 units**. A hop costs 2, and a whole route with acceleration, corrections and braking about 3–6, so fuel is a real constraint – ships have to refuel. A game that wants to represent the effect of cargo can let an empty ship fly further – about 1.5 times. Lighter passenger ships have a higher mass ratio, and so a longer range.

Other drives are not enough. A nuclear-electric drive (exhaust velocity about 40 km/s) would give a tank of about 3 units, a nuclear thermal one (about 9 km/s) – less than 1.

**Refuelling in the asteroid belt.** Propellant – water – can be extracted from the asteroids themselves. To do so, the ship has to stop: land on a small asteroid or go into orbit around it.

- **How much water is a unit.** One unit is about 1/20 of a tank. For a freighter with a 1000 t structure, 1000 t of cargo and a 2000 t tank, that is about 100 t of water.
- **How much rock has to be processed.** Carbonaceous asteroids usually contain about 5–20% water, bound in minerals; it is recovered by heating the excavated material to a few hundred degrees. At 10% water, one unit takes about 1000 t of rock.
- **What limits the rate.** Not energy: the freighter's reactor has a power of the order of several gigawatts, and recovering 100 t of water per day takes about 12 MW. What limits it is equipment – how much material can be dug up and processed in microgravity. There is no real data, because nobody has done it yet.

Proposed values:

| Method | Rate | Full tank |
|--------|------|-----------|
| emergency kit carried by the freighter (about 1–2.5 t of rock per hour) | about 3 units per round of stopover | about 7 rounds |
| mining station | the whole tank | 1 round |

The emergency kit is slow enough to really be an emergency solution – during the stopover the Earth and the transfer windows slip away. Like a lander, the kit has mass and reduces the ship's range.

There is more water in the outer part of the belt: stony, water-poor asteroids dominate the inner part, carbonaceous ones the outer part. On the board, rings 5–6 can therefore yield more water than ring 4.

Water is propellant, not fusion fuel. Fusion fuel, for example deuterium, is a negligible part of the mass – and deuterium can also be recovered from water.

These values – extraction rate, water content, availability of stations – are good dials for configuring different game scenarios.

### Launching from the surface

Fuel is not the problem here: getting from the Earth's surface to low orbit takes about 9.4 km/s (an orbital speed of 7.9 km/s plus losses to gravity and air drag) – less than one unit. The problem is thrust. To lift off, an engine has to provide an acceleration greater than the surface gravity, in practice about 1.2–1.5 g. The fusion drive of the reference model provides about 0.27 milli-g:

| Body | Surface gravity | Ship thrust relative to weight | Orbital speed at the surface |
|------|-----------------|--------------------------------|------------------------------|
| Earth | 9.8 m/s² | 1/3700 | 7.9 km/s |
| Mars | 3.7 m/s² | 1/1400 | 3.6 km/s |
| Ceres | 0.28 m/s² | 1/106 | 0.37 km/s |
| Vesta | 0.25 m/s² | 1/94 | 0.26 km/s |
| 1 km asteroid | 0.0003 m/s² | 9.5 | about 0 |

At a typical asteroid density (about 2 g/cm³) the ship can lift off from a body up to about 6–10 km across.

A stronger engine won't solve this: for a given power, a higher exhaust velocity means less thrust, so a fuel-efficient drive is by nature a weak one. Launching from the Earth needs a chemical rocket with an exhaust velocity of about 4 km/s. Besides, the exhaust of a fusion drive in the atmosphere would be a jet of hot plasma.

Three things follow:

- Fusion freighters fly from orbit to orbit. At the Earth and Mars they dock at orbital stations, and separate landers – chemical ones, for example – run to the surface and back. Most of today's concepts of transport in the Solar System look similar: rockets to low orbit, then separate space tugs.
- Getting to orbit from Mars (about 4 km/s) is much cheaper than from the Earth (about 9.4 km/s), so a station at Mars is easier to supply from the surface.
- Ceres and Vesta also need landers, but cheap ones – the escape velocity of Ceres is about 0.5 km/s. On small asteroids a freighter lands directly.

**A lander carried by the freighter.** At Ceres and Vesta a lander needs little: from low orbit to the surface and back is about 0.8 km/s at Ceres and about 0.6 km/s at Vesta, with no atmosphere and weak gravity. A small chemical lander that the freighter can carry with it is enough. Its fuel – hydrogen and oxygen from split water – can be produced in the asteroid belt. The lander's mass, however, counts towards the ship's mass without propellant, so a freighter with a lander has a shorter range or carries less cargo.

At Mars an own lander is possible but heavy (about 5 km/s for landing and returning to orbit) and needs fuel on the surface. At the Earth just getting to orbit takes a large rocket with ground infrastructure – a freighter can't carry that.

Where a permanent settlement has grown up, it is natural to keep landers on site, as at the Earth and Mars. A freighter's own lander is the solution for places without infrastructure – that is, for the early days of asteroid belt exploration.

### Manoeuvres in the asteroid belt

The asteroid belt is very empty – the average distance between asteroids is about a million km, and probes fly through it without any manoeuvres. Avoiding obstacles is therefore not what costs. What costs is matching the target: to land on a particular asteroid you have to get onto its orbit, and every asteroid has its own. This is also the real-world counterpart of drift – when a game ignores drift, its cost is included in the cost of manoeuvres.

### Simplified model: cost per hex

The simplified model doesn't track ship velocity – you pay for every hex of powered movement, more the closer to the Sun. The rules are in the [board description](board.md#simplified-model).

**Interpretation.** The simplified model corresponds to freighters flying the cheapest routes (the Hohmann transfer) with travel times shortened for playability. One unit is then about 1.8 km/s, and a nuclear-electric drive is enough (exhaust velocity about 40 km/s) – a loaded freighter's tank holds about 15 units.

**Where the multipliers come from.** The cheapest routes are more expensive the closer they are to the Sun – the cost falls roughly as distance to the power of 1.5:

| Ring | Move to the next ring out (cheapest route) | Solar heat flux |
|------|--------------------------------------------|-----------------|
| 1 (0.5 AU) | 7.5× | 4× Earth's |
| 2 (Earth) | 3.3× | 1× |
| 3 (Mars) | 2× | 0.4× |
| 4 | 1.4× | 0.25× |
| 5 | 1 | 0.16× |

A multiplier of ×3 on ring 2, ×2 on ring 3 and ×1 in the asteroid belt captures this well.

**Calibration.** Cost in the game (with the closest-ring rule) and the cheapest route:

| from \ to | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| **2** (Earth) | – | 3 | 5 | 6 | 7 |
| **3** (Mars) | 3 | – | 2 | 3 | 4 |
| **4** | 5 | 2 | – | 1 | 2 |
| **5** | 6 | 3 | 1 | – | 1 |
| **6** | 7 | 4 | 2 | 1 | – |

| from \ to | 3 | 4 | 5 | 6 |
|---|---|---|---|---|
| **2** | 5.4 km/s (1.80) | 8.5 km/s (1.69) | 10.4 km/s (1.74) | 11.7 km/s (1.68) |
| **3** | | 3.2 km/s (1.62) | 5.4 km/s (1.80) | 6.9 km/s (1.73) |
| **4** | | | 2.2 km/s (2.22) | 3.8 km/s (1.91) |
| **5** | | | | 1.6 km/s (1.64) |

In brackets – km/s per unit of game cost. All pairs fall within 1.6–2.2 km/s per unit, so the cost table is consistent with the cheapest routes.

**Speed limits** follow from the assumption that a ship can spend at most about 3 units in one round: near the Earth that is 1 hex, near Mars also 1 (2 hexes would cost 4), in the belt 2 hexes. **The speed penalty** (2 hexes for 3) is a surcharge for haste. **The closest-ring rule** makes a flight there and back cost the same, as in reality.

**What the simplified model loses:**

- **You pay for distance, not for changing velocity.** Long flights cost several times too much: a 4-hex route physically costs as much as a 1-hex one, while in the model it costs 4 times more. The speed penalty, on the other hand, is too small – physically a flight twice as fast costs twice as much.
- **Time is shortened unevenly.** The cheapest Earth → Mars route takes about 3 rounds, and between neighbouring rings of the belt 7–10 rounds; in the game each takes one round. So the game shortens time in the belt several times more than near the Earth – and that is where the multipliers come from. At the same pace the cost practically doesn't depend on the ring:

| Flight time (rounds) | 1 | 2 | 3 | Cheapest route |
|---------------------|---|---|---|----------------|
| 2 → 3 (Earth → Mars) | 19 km/s | 7.9 km/s | 5.4 km/s | 5.4 km/s in 2.9 rounds |
| 3 → 4 | 20 km/s | 9.1 km/s | 5.5 km/s | 3.2 km/s in 4.9 rounds |
| 4 → 5 | 20 km/s | 9.6 km/s | 6.0 km/s | 2.2 km/s in 7.1 rounds |
| 5 → 6 | 20 km/s | 9.8 km/s | 6.3 km/s | 1.6 km/s in 9.6 rounds |

- **Launch angles in transfer windows are approximate** (see "Transfer windows").

The simplified model is consistent in itself and works well for games that don't want to track ship velocities. Further simplifications – for example a constant cost per hex across the whole board – are possible, but move the model even further from physics.

**Board geometry.** Neither model builds costs into the board itself – for example through hexes that get smaller closer to the Sun. The board would then show cost instead of space and lose what is its main value: real distances and proportions of orbital motion. Maps built from manoeuvre costs do exist (the game High Frontier has one, for example), but they lose the sense of where things really are.

All the numbers in this chapter come from the scripts in the [tools](../tools/README.md) folder – anyone can check them and recompute them for a modified board.

## Choice of dice for placement in the asteroid belt

Positions in the asteroid belt are rolled with a pair of dice, **d12 + d8**, rather than more standard combinations. The decision has two practical reasons.

First, a d12 and a d8 are easy to tell apart at a glance – they differ in shape and size. There is no need to roll them one after another or colour-code them: it is immediately clear which result is which (d12 → sector, d8 → hex within the sector).

Second, the asteroid belt has 90 hexes (rings 4–6, in total `6×4 + 6×5 + 6×6 = 90`). With standard d6s, rolling among 90 hexes would take three rolls and a non-trivial mapping of the result. A d12 × d8 pair gives 96 combinations, which covers 90 hexes with a minimal surplus and a simple scheme: one roll, two results, one position on the board.

## Educational value

Despite the simplifications, the model conveys things that popular visualisations of the Solar System don't show at all:

- Planets move at different speeds – and the difference is felt during play.
- Transfers between orbits require planning in time: you have to predict where the target will be when you arrive.
- The asteroid belt is wide, not thin.
- An inertial frame is not the only way to describe motion – the choice of a frame of reference has consequences.
- In space you pay for changing velocity, not for the distance travelled.

The Earth and Mars move on the board as they do in reality. The biggest simplifications – the shared ring of Mercury and Venus and the simplified or ignored drift in the belt – concern places where accuracy doesn't affect the player's decisions. A player without astronomical knowledge will find the model consistent and intuitive. A player with that knowledge will recognise that the mechanic is real – just rounded to numbers you can play with.
