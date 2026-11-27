# Hayabusa – design philosophy

*[Wersja polska](design_pl.md)*

This document collects the principles the board is designed by – what it is meant to be and what comes first when goals conflict. How the individual elements relate to reality is described in [the board's model](model.md).

## A board, not a game

The board is not tied to a single game – it is a space on which different games can be built. The goal of the game, resources, events and the rest of the rules belong to a particular game.

Three things follow from this:

- The board provides physics and a flight model, not a story. The setting is the early days of space exploration and the resources of the asteroid belt, but the world around it is built by the game.
- The [3D pawns](../models/README.md) are general-purpose – a transport ship and an outpost, not the heroes of a particular game.
- The [ideas for games](ideas.md) are material to use, not rules.

## Hard science fiction

The physics is real; only the ships' engines come from the future. Distances and orbital speeds keep their real proportions, transfer windows come round as often as in reality, and ships pay for changing their velocity, not for the distance travelled.

The principle holds all the way down, details included: the ships are large freighters, not light probes, and every element of the pawns is justified by the physics and technology described in the model.

## A point of reference, loosened knowingly

The reference model keeps as close to physics as play on a board allows. It is a point of reference: a game can simplify it, but knowingly – aware of what it loses.

An example is the [simplified model](board.md#simplified-model): a cost for every hex of movement instead of tracking velocity. It is consistent in itself, but it loosens the hard science fiction, and [the model](model.md#simplified-model-cost-per-hex) describes exactly what is lost.

## Playability

In the end the result should be something simple that is enjoyable to play. The physics is rounded to numbers you can play with: distances and speeds are chosen to fit the grid, and the length of a round follows from them rather than being assumed.

## Accuracy where it affects decisions

The Earth and Mars move on the board as they do in reality. The biggest simplifications – the shared ring of Mercury and Venus and the simplified or ignored drift in the asteroid belt – concern places where accuracy doesn't affect the player's decisions.

When faithfulness to physics conflicts with practicality, practicality wins and the departure is documented. This is the case with the drift of the asteroid belt (optional and rounded) and with the pawns (the outpost's reactor radiators are marked only symbolically).

## Convenience at the table

The board should be convenient to use without special equipment: printable at home and played with ordinary dice.

### Dice for random placement

Positions in the asteroid belt are rolled with a pair of dice, **d12 + d8**, rather than more standard combinations. The decision has two practical reasons.

First, a d12 and a d8 are easy to tell apart at a glance – they differ in shape and size. There is no need to roll them one after another or colour-code them: it is immediately clear which result is which (d12 → sector, d8 → hex within the sector).

Second, the asteroid belt has 90 hexes (rings 4–6, in total `6×4 + 6×5 + 6×6 = 90`). With standard d6s, rolling among 90 hexes would take three rolls and a non-trivial mapping of the result. A d12 × d8 pair gives 96 combinations, which covers 90 hexes with a minimal surplus and a simple scheme: one roll, two results, one position on the board. The surplus – a 4 on the d8 in an odd sector – means rolling again, on average once in 16 rolls; in return every hex has the same chance. The d8 result also tells the ring at once: 1–2, 3–5, 6–8.

### Printing on home equipment

The board can be printed on an ordinary printer – in parts, on A4 sheets that make up an A2 board.

### Two colour versions

The board comes in two colour versions: a dark one, more like space, and a light, printer-friendly one that uses less ink. The dark one also comes on a black background, where space doesn't end at the edge of the board.

## Educational value

Despite the simplifications, the model conveys things that popular visualisations of the Solar System don't show at all:

- Planets move at different speeds – and the difference is felt during play.
- Transfers between orbits require planning in time: you have to predict where the target will be when you arrive.
- The asteroid belt is wide, not thin.
- An inertial frame is not the only way to describe motion – the choice of a frame of reference has consequences.
- In space you pay for changing velocity, not for the distance travelled.

A player without astronomical knowledge will find the model consistent and intuitive. A player with that knowledge will recognise that the mechanic is real – just rounded to numbers you can play with.

## Openness

The board, the documentation and the pawns are licensed under CC BY 4.0, and the scripts under MIT. Not only how the board works is open, but also why: the rationale for every decision is in the documentation, and the numbers come from [scripts](../tools/README.md) that anyone can use to check them and recompute them for a modified board.

## What is where

- [How the board works](board.md) – the rules, without the rationale.
- [The model and design decisions](model.md) – the rationale: how the board relates to physics.
- [Ideas for games](ideas.md) – material to use.
- This document – the principles the rest is built by.
