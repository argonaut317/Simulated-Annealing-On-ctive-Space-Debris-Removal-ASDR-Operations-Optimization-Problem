# Simulated-Annealing-On-ctive-Space-Debris-Removal-ASDR-Operations-Optimization-Problem


# Active Space Debris Removal (ASDR) Optimization using Simulated Annealing

## Overview

This project presents a simplified **research-level implementation** of the **Active Space Debris Removal (ASDR)** optimization problem using the **Simulated Annealing (SA)** metaheuristic.

The objective is to determine an efficient sequence for removing space debris while minimizing mission resources (fuel, time, and cost) and maximizing the reduction in collision risk.

Although this implementation uses simplified orbital transfer models, it demonstrates the optimization framework commonly used in Operations Research before integrating high-fidelity astrodynamics tools such as Orekit or Poliastro.

---

# Why is this an NP-Hard Problem?

The ASDR mission planning problem is considered an **NP-hard combinatorial optimization problem** because it combines several difficult optimization tasks:

- Selecting which debris objects to remove.
- Determining the optimal removal sequence.
- Minimizing fuel consumption (ΔV).
- Satisfying mission constraints such as fuel and mission duration.

If there are **N debris objects**, the number of possible visit sequences is:

N!

For example:

| Number of Debris | Possible Sequences |
|-----------------:|-------------------:|
| 5 | 120 |
| 8 | 40,320 |
| 10 | 3,628,800 |
| 20 | 2.43 × 10¹⁸ |

An exhaustive search quickly becomes computationally infeasible.

The ASDR problem is closely related to several classical NP-hard problems:

- Traveling Salesman Problem (optimal visit sequence)
- Vehicle Routing Problem
- Orienteering Problem
- Knapsack Problem
- Scheduling Problem

Because ASDR generalizes these problems while adding orbital mechanics constraints, exact optimization methods become impractical for large instances. Metaheuristic algorithms such as Simulated Annealing, Genetic Algorithms, and Ant Colony Optimization are therefore widely used to obtain high-quality near-optimal solutions.

---

# Problem Formulation

## Decision Variables

The optimizer determines:

- x₁ : Sequence of debris removal
- x₂ : Next debris object to visit
- x₃ : Orbital transfer between debris
- x₄ : Total fuel (ΔV) allocation
- x₅ : Mission schedule

---

## Objective Function

The optimization minimizes the weighted objective:

J = w₁(ΔV)
  + w₂(Mission Time)
  + w₃(Operational Cost)
  - w₄(Collision Risk Removed)

where:

- ΔV = Total fuel consumption
- Mission Time = Total transfer time
- Operational Cost = Time × hourly mission cost
- Collision Risk Removed = Sum of debris risk scores

A large penalty is added whenever the fuel constraint is violated.

---

# Constraints

The optimization is subject to:

- Fuel capacity limit
- Mission duration
- One visit per debris object
- Valid orbital transfers
- Single spacecraft mission
- No duplicate debris removal

Penalty functions are used to discourage infeasible solutions.

---

# Example Dataset

Each debris object contains:

| Attribute | Description |
|-----------|-------------|
| ID | Debris identifier |
| Altitude | Orbital altitude (km) |
| Inclination | Orbital inclination (degrees) |
| Mass | Estimated object mass (kg) |
| Risk | Collision risk score |

The program automatically computes simplified transfer ΔV and mission time matrices from orbital altitude and inclination differences.

---

# Algorithm

The project implements **Simulated Annealing** using:

1. Random initial mission sequence
2. Neighbor generation (swap, reverse, insert)
3. Objective function evaluation
4. Acceptance using the Metropolis criterion
5. Gradual cooling schedule
6. Best solution tracking until convergence

---

# Project Structure

```text
.
├── asdr_simulated_annealing.py
├── README.md
```

---

# Requirements

- Python 3.10+
- NumPy
- Pandas
- Matplotlib

Install dependencies:

```bash
pip install numpy pandas matplotlib
```

---

# Running the Project

Execute:

```bash
python asdr_simulated_annealing.py
```

The program will:

1. Load the example debris dataset.
2. Build the transfer ΔV and mission time matrices.
3. Run the Simulated Annealing optimizer.
4. Print the optimized debris removal sequence.
5. Display mission statistics.
6. Plot the convergence history.

---

# Simulated Annealing Parameters

| Parameter | Value |
|-----------|------:|
| Initial Temperature | 1000 |
| Cooling Rate | 0.995 |
| Minimum Temperature | 0.01 |

---

# Current Assumptions

This implementation is intended for Operations Research coursework and makes several simplifying assumptions:

- Estimated ΔV from altitude and inclination differences.
- Simplified mission time model.
- Single-spacecraft mission.
- Single weighted objective function.
- Static debris positions.
- No atmospheric drag or orbital perturbations.

---


# Sample Program Output

> **Note:** Simulated Annealing is a stochastic (randomized) optimization algorithm. Therefore, the exact output may vary each time the program is executed unless a fixed random seed is used.

## Example Console Output

```text
====================================================
Active Space Debris Removal Optimization
Simulated Annealing
====================================================

Building transfer cost matrices...

Running Simulated Annealing...

Optimization Complete!

Best Objective Score: 24396.87

Optimized Removal Order

D5 -> D2 -> D1 -> D6 -> D8 -> D7 -> D4 -> D3

Mission Summary
-----------------------------------
Total ΔV         : 381.40 m/s
Mission Time     : 52.80 hr
Operational Cost : $264,000.00
Risk Removed     : 6.64

Fuel Constraint  : Satisfied
```

---

## Expected Convergence Trend

The objective function typically decreases rapidly during the early iterations before gradually converging toward a stable near-optimal solution.

```text
Objective
25000 |\
      | \
24000 |  \
      |    \_____
23000 |          \_____
      |                \____
22000 |                     \_____
      |
      +------------------------------------>
          Iterations
```

---

## Example Dataset

| Debris | Altitude (km) | Inclination (°) | Mass (kg) | Risk |
|---------|--------------:|----------------:|----------:|-----:|
| D1 | 700 | 98.2 | 1200 | 0.82 |
| D2 | 720 | 97.8 | 900 | 0.65 |
| D3 | 680 | 98.6 | 1400 | 0.91 |
| D4 | 750 | 99.1 | 1600 | 0.93 |
| D5 | 690 | 97.9 | 850 | 0.72 |
| D6 | 710 | 98.4 | 1000 | 0.79 |
| D7 | 740 | 99.4 | 1500 | 0.95 |
| D8 | 730 | 98.7 | 1300 | 0.87 |

---

## Reproducible Results

To obtain the same output every time, initialize the random number generators before running the algorithm:

```python
import random
import numpy as np

random.seed(42)
np.random.seed(42)
```

This ensures that the initial solution and the optimization process are deterministic, making the results reproducible for coursework, reports, and research documentation.


# Future Improvements

Possible extensions include:

- Real orbital elements (Keplerian or TLE)
- Hohmann and Lambert transfer calculations
- Integration with Orekit or Poliastro
- Multi-spacecraft mission planning
- Ant Colony Optimization (ACO)
- NSGA-II multi-objective optimization
- Particle Swarm Optimization (PSO)
- Real ESA DISCOS or Space-Track debris catalog
- Statistical comparison of multiple metaheuristics

---



# Mathematical Formulation

> **Note:** The equations below are written in GitHub-compatible Markdown using LaTeX. GitHub may display them as plain text unless MathJax is enabled (e.g., GitHub Pages, VS Code Markdown Preview, Jupyter, or Typora).

---

# 1. Transfer ΔV Model

The estimated transfer cost between debris object \(i\) and debris object \(j\) is

```math
\Delta V_{ij}
=
0.4\left|Altitude_i-Altitude_j\right|
+
25\left|Inclination_i-Inclination_j\right|
```

### Explanation

- \(\Delta V_{ij}\) = estimated fuel required to transfer from debris \(i\) to debris \(j\)
- \(|Altitude_i-Altitude_j|\) = orbital altitude difference (km)
- \(|Inclination_i-Inclination_j|\) = orbital inclination difference (degrees)

The coefficients (0.4 and 25) are simplified weighting factors. In a real mission, these values would be computed using orbital mechanics (e.g., Hohmann or Lambert transfers).

---

# 2. Mission Time Model

Mission transfer time is estimated as

```math
Time_{ij}
=
\frac{|Altitude_i-Altitude_j|}{25}
+
4|Inclination_i-Inclination_j|
```

### Explanation

- Every 25 km of altitude change contributes approximately one hour.
- Every degree of inclination change contributes four hours.
- This provides a simple approximation of transfer duration.

---

# 3. Operational Cost

The mission operating cost is

```math
Operational\ Cost
=
Mission\ Time
\times
Cost_{hour}
```

where

```math
Cost_{hour}=5000
```

This assumes a constant operating cost of \$5,000 per mission hour.

---

# 4. Collision Risk Removed

The total collision risk removed is

```math
Risk_{removed}
=
\sum_{i=1}^{n} Risk_i
```

where \(Risk_i\) is the risk score of debris object \(i\).

Higher values indicate that more hazardous debris has been removed.

---

# 5. Fuel Constraint

The total mission ΔV must satisfy

```math
\sum \Delta V \le Fuel_{limit}
```

For this project,

```math
Fuel_{limit}=450
```

Any solution exceeding this limit is considered infeasible.

---

# 6. Penalty Function

Constraint violations are handled using a penalty function.

```math
Penalty=
\begin{cases}
100000,& \text{if } \sum\Delta V > Fuel_{limit} \\
0,& \text{otherwise}
\end{cases}
```

The large penalty discourages infeasible solutions while still allowing Simulated Annealing to explore the search space.

---

# 7. Objective Function

The optimization minimizes

```math
J
=
w_1(\Delta V)
+
w_2(Time)
+
w_3(Cost)
-
w_4(Risk_{removed})
+
Penalty
```

where

- \(w_1 = 0.4\)
- \(w_2 = 0.2\)
- \(w_3 = 0.2\)
- \(w_4 = 0.2\)

### Interpretation

- Minimize fuel consumption.
- Minimize mission duration.
- Minimize operational cost.
- Maximize collision risk removed (therefore the risk term is subtracted).
- Penalize infeasible missions.

---

# 8. Simulated Annealing Acceptance Rule

The change in objective value is

```math
\Delta = J_{new} - J_{current}
```

If

```math
\Delta < 0
```

the new solution is accepted because it is better.

Otherwise, it is accepted with probability

```math
P=e^{-\Delta/T}
```

where

- \(P\) = acceptance probability
- \(T\) = current temperature

This mechanism helps the algorithm escape local optima during the early stages of the search.

---

# 9. Cooling Schedule

The temperature is reduced after every iteration using geometric cooling.

```math
T_{new}
=
\alpha T_{old}
```

where

- Initial temperature = 1000
- Cooling factor \(\alpha = 0.995\)
- Minimum temperature = 0.01

The algorithm terminates when the temperature falls below the minimum threshold.

---

# Overall Optimization Model

The project combines:

1. Simplified orbital transfer estimation.
2. A weighted multi-objective optimization function.
3. Constraint handling using penalty functions.
4. Simulated Annealing with the Metropolis acceptance criterion.
5. A geometric cooling schedule.

This formulation is appropriate for an Operations Research demonstration and can later be extended by replacing the simplified transfer equations with physically accurate orbital mechanics models.

---

## Summary

The project combines:

- A simplified orbital transfer model
- A weighted multi-objective optimization function
- Constraint handling using penalty functions
- Simulated Annealing with Metropolis acceptance
- Geometric cooling schedule

Although simplified, this formulation reflects the optimization workflow commonly used in Operations Research studies and can later be extended with real orbital mechanics libraries such as Orekit or Poliastro.


# References

1. Kirkpatrick, S., Gelatt, C. D., & Vecchi, M. P. (1983). *Optimization by Simulated Annealing*. Science.
2. NASA Orbital Debris Program Office.
3. ESA Space Debris Office.
4. Talbi, E.-G. (2009). *Metaheuristics: From Design to Implementation*.

---

# License

This project is intended for educational, academic, and research purposes.

