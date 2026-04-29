# Multi-Agent Path Finding (MAPF) Simulation

This repository contains a full MAPF solver built for CS 57200, including a decoupled A\* baseline, standard Conflict-Based Search (CBS), a custom h-CBS heuristic, and State Hashing optimizations.

## Setup Instructions

1. Ensure Python 3.x is installed.
2. Install the required visualization dependencies:
   `pip install -r requirements.txt`

## Running the Code

- **Baseline A\* \*\***test*\*\*:* `python baseline_astar.py`
- **Standard CBS vs h-CBS test:** `python cbs_enhancement.py`
- **Experiment 1 & 2 (Scaling):** `python run_experiments.py`
- **Experiment 3 (Density):** `python run_density_exp.py`
- **Experiment 4 (Heuristic Impact):** `python run_heuristic_exp.py`
- **Experiment 5 (Hashing Impact):** `python run_hashing_exp.py`
- **Generate Data Charts:** `python generate_heuristic_chart.py` and `python generate_hashing_chart.py`
