# 3D pawns

*[Wersja polska](README_pl.md)*

General-purpose 3D-printable pawns for any game on this board.

![Model preview](preview.png)

| File | Model | Size |
|------|-------|------|
| [ship.stl](ship.stl) | transport ship – modular hull on a spine, with nozzles at the bottom; indirectly inspired by the Eagle 1 from "Space: 1999" | 26 × 26 × 36 mm |
| [outpost.stl](outpost.stl) | outpost on an asteroid – the industrial part: reactor, processing and storage, long-range antenna, spaceport | 30 × 30 × 24 mm |

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

## Outpost – design intent

The pawn shows **the industrial part of the outpost**. The living quarters stand separately, away from it – ideally on the other side of the asteroid.

- **Reactor.** In the asteroid belt sunlight has only 1/5–1/9 of its strength at the Earth, and mining and processing take a lot of energy. Recovering water is mostly a matter of heating rock, so a reactor next to the processing plant can supply heat directly. A reactor needs large radiators – in a vacuum there is nothing to cool it with; about 500 m² for every 1 MW of electrical power.

  On the pawn the reactor sits in a recess – as in NASA concepts for lunar bases, where the reactor stands in a pit and the ground shields against radiation. The cross on the reactor stands for the radiators. In reality they would be large, thin panels standing high above the pit, because a radiator gives off heat only when it "sees" the open sky. On the pawn they are marked symbolically and solidly – small fins would be awkward to print and to keep clean.
- **The domes partly dug into the ground** are processing plants and stores of water and propellant. Burying them keeps the temperature stable (ice does not sublimate) and shields them from micrometeoroids.
- **The antenna** stands on top of the rock for better visibility. Next to the reactor it has power at hand for the transmitter.
- **Spaceport.** Ships refuel and load where water and propellant are produced. Dust and debris from engines at launch and landing travel far in such weak gravity, so the spaceport should be away from people.

**The habitat stands apart.** Distance protects the inhabitants from the reactor's radiation (on the other side of the asteroid the rock itself shields them), from the effects of industrial accidents and from dust from the spaceport and mining. The industrial part should be largely automated and operated from the habitat – over a kilometre the delay is negligible, unlike control from the Earth. People come mainly for repairs, so a small radiation-shielded shelter is useful in case of a solar flare.

**Communication with the Earth.** An antenna a few metres across, powered by the reactor, theoretically gives from several to several tens of Mb/s even at the greatest distance from the Earth (about 3.2 AU); in practice losses reduce this several times. The limits lie elsewhere:

- the signal takes 10–27 minutes one way – messages can be exchanged, but not conversations,
- when the outpost is behind the Sun, contact is lost for about 13 days; this happens about every 1.4 years, i.e. every 6 turns,
- a small asteroid rotates in a few hours, so from any point on the surface the Earth is visible only during part of each rotation – continuous contact needs antennas on several sides or a relay satellite in orbit.

**Weak gravity.** The escape velocity of a 1 km asteroid is about 0.5 m/s. Everything – the antenna mast, the modules, the people – has to be anchored. Regolith on the domes shields them but holds nothing down: 3 m of regolith presses with about 1 Pa, while the pressure inside a module is about 100,000 Pa. The domes have to withstand the pressure on their own.

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
- Optionally, at the next edit: raise the radiator cross higher above the rim of the recess, keeping its thickness.
