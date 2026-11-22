# 3D pawns

*[Wersja polska](README_pl.md)*

General-purpose 3D-printable pawns for any game on this board.

![Model preview](preview.png)

| File | Model | Size |
|------|-------|------|
| [ship.stl](ship.stl) | transport ship – modular hull on a spine, with nozzles at the bottom; indirectly inspired by the Eagle 1 from "Space: 1999" | 26 × 26 × 36 mm |
| [outpost.stl](outpost.stl) | outpost on an asteroid, with a long-range communication antenna | 30 × 30 × 24 mm |

## Ship – design intent

From bottom to top:

- **Tanks and nozzles.** At the bottom are the tanks for "fuel" – really propellant, expelled by the engine – and the nozzles of the fusion engines.
- **Cargo hold.** The elongated hull is the cargo hold.
- **Habitat.** The three modules above it carry people and other living beings. Three independent modules provide redundancy for safety. Spinning the ship around its axis creates artificial gravity in them.
- **Bridge.** The bridge (control room) is at the bow.

The faceted shape of the bow and of the tanks by the nozzles is not meant to be streamlined – in a vacuum that doesn't matter – but to give a clear view from the bridge: visually, and for antennas and sensors.

**Ship scale.** Spinning around the axis along which the thrust acts doesn't interfere with flight. Artificial gravity, however, needs a large radius, because faster rotation makes people motion-sick – the safe limit is usually about 2–4 revolutions per minute:

| Artificial gravity | at 4 rpm | at 2 rpm |
|--------------------|----------|----------|
| 0.3 g | about 17 m from the axis | about 67 m from the axis |
| 1 g | about 56 m from the axis | about 220 m from the axis |

On the model the habitat modules lie about 1/4 of the ship's length from the axis. A real ship would therefore be from about 70 m long (0.3 g at fast rotation) to nearly a kilometre (1 g at slow rotation). The "floor" in the habitat is on the side facing away from the ship's axis.

## Size

The board is meant to be printed in A2 format. A hex is then about 30 mm across the flats, and a pawn fits within one hex if it is at most about 27 mm wide.

- **The ship** fits without scaling. It has no base – it is meant to be turned freely in the hand, and a base would hide the nozzles. It also stands well on its side.
- **The outpost** takes up almost the whole hex – it is worth printing at about 0.9 scale.

## Printing

- The ship needs supports under its lower modules (tree supports work best); the outpost prints without supports.
- The ship stands on the print bed on three small nozzles – a brim may help.

## To fix

- The ship file is saved in metres, the outpost in millimetres. Some slicers will load the ship at the wrong scale – it has to be scaled ×1000 or re-exported in millimetres.
- Both models consist of overlapping bodies. Slicers usually cope, but before publishing it is worth merging them (Boolean Union or "Make Manifold" in Blender). The ship also contains a stray double triangle of zero thickness.
- The outpost's antenna has parts 0.1–0.5 mm thick – to be thickened to at least about 1 mm at the final scale.
