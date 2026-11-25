# Badminton shuttlecock trajectories: feather vs plastic

Physical and numerical study of the "parachute" trajectory of badminton shuttlecocks, comparing feather, plastic and damaged shuttlecocks: drag forces, flipping oscillations and the effect of the material.

TIPE (research project of the French *classes préparatoires*), Mathéo Cail, PSI, 2023–2024. Final grade: **18.6/20**.

## Method

- **Experiments**: shots filmed and tracked frame by frame with Tracker, which gives the position of the shuttlecock over time, and its angle during the flip that follows the racket impact.
- **Models**: the measured trajectories are compared with two projectile models:
  - linear drag: analytic trajectory, landing point found by bisection;
  - quadratic drag: equations of motion integrated numerically with SciPy.
- **Oscillations**: the flip of the shuttlecock is modelled by a non-linear second-order equation, solved numerically and compared with the measured angle.

## Results

Distance between the predicted and the measured landing point:

| Shuttlecock | Linear drag | Quadratic drag |
|---|---:|---:|
| Feather | 2.20 m | **0.20 m** |
| Plastic | **0.35 m** | 1.17 m |
| Damaged | **0.72 m** | 1.54 m |

Quadratic drag describes the feather shuttlecock best, and linear drag the plastic one, in line with the literature cited in the MCOT.

## Contents

- `shuttlecock_analysis.py`: comparison of experiments and models (plots and landing-point errors)
- `data/feather.txt`, `data/plastic.txt`, `data/damaged.txt`: tracked positions (t, x, y)
- `data/oscillation_angles.txt`: tracked angle during the flip (t, θ)
- `docs/MCOT.pdf`: objectives and annotated bibliography (French)
- `docs/presentation.pdf`: slides of the final presentation (French)

## Getting started

```bash
pip install numpy scipy matplotlib
python shuttlecock_analysis.py
```

## Tech

Python (NumPy, SciPy, Matplotlib), Tracker video analysis.
