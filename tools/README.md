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

## Licence

The code in this folder is available under the [MIT](LICENSE) licence.
