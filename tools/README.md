# Calculations

*[Wersja polska](README_pl.md)*

The scripts used to compute the numbers in the [model description](../docs/model.md). Each one prints its tables in the same form in which they appear in the documentation.

Physical model: the Sun and a ship (the two-body problem), circular and coplanar orbits. Routes between orbits are computed as optimal arcs (Lambert's problem) or as Hohmann transfers; free flight by numerical integration of the motion.

| Script | What it computes | Section of the model description |
|--------|------------------|----------------------------------|
| `orbits.py` | shared functions and board parameters (reference orbit, round length) | – |
| `board_model.py` | reference orbit, ring movement, belt drift, transfer windows and launch angles | Frame of reference, The asteroid belt, Transfer windows |
| `reference_model.py` | cost of planned routes at game pace | Why the reference model makes sense |
| `coasting.py` | path bending in free flight, cost of holding a course, test of a simple bending rule | Why not take the straight line literally |
| `simplified_model.py` | calibration of the simplified model, cost at equal flight time | Simplified model |
| `propulsion.py` | tank range, thrust and power for different drives, launching from the surface, refuelling from asteroid water | Propulsion and fuel, Launching from the surface |

## Running

You need Python 3 with the `numpy` and `scipy` libraries:

```
pip install numpy scipy
cd tools
python board_model.py
```

`coasting.py` and `simplified_model.py` take several tens of seconds to run.

## Board generator

`board_svg.py` draws the board and writes all the files in [`board/`](../board): the whole board as SVG, PDFs for printing on A4 sheets (A2 from 4, A3 from 2, butted together), previews and QR codes – in two languages and two colour versions. The board graphics are changed here, not in the files.

You need Python 3 with the `segno` library (QR codes), `rsvg-convert` (PDF and PNG; on Windows e.g. in WSL: `sudo apt install librsvg2-bin`) and the Exo 2 and Orbitron fonts (Google Fonts):

```
pip install segno
cd tools
python board_svg.py
```

Photos of the Earth, Mars and Ceres are read from `board/images/` (`earth.jpg`, `mars.jpg`, `ceres.jpg` or `.png`; square, the planet filling the frame); without them the discs are drawn in plain colours. The script also warns when a label lands on a join between sheets.

Without `rsvg-convert` the script writes the SVG files only (`--svg-only` does the same on purpose).

## Licence

The code in this folder is available under the [MIT](LICENSE) licence.
