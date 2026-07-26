
"""
Research-Level Active Space Debris Removal (ASDR)
Simulated Annealing Example

This example demonstrates a simplified research-style optimization model
for sequencing debris removal missions using Simulated Annealing.

Author: ChatGPT
"""

import random
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Example Debris Dataset
# -----------------------------
debris = pd.DataFrame({
    "ID": ["D1","D2","D3","D4","D5","D6","D7","D8"],
    "Altitude": [700,720,680,750,690,710,740,730],      # km
    "Inclination": [98.2,97.8,98.6,99.1,97.9,98.4,99.4,98.7],  # deg
    "Mass": [1200,900,1400,1600,850,1000,1500,1300],    # kg
    "Risk": [0.82,0.65,0.91,0.93,0.72,0.79,0.95,0.87]
})

# -----------------------------
# Transfer Matrices
# -----------------------------
n = len(debris)
delta_v = np.zeros((n, n))
mission_time = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        altitude_diff = abs(debris.iloc[i]["Altitude"] - debris.iloc[j]["Altitude"])
        inc_diff = abs(debris.iloc[i]["Inclination"] - debris.iloc[j]["Inclination"])

        # Simplified estimates
        delta_v[i, j] = 0.4 * altitude_diff + 25 * inc_diff
        mission_time[i, j] = altitude_diff / 25 + inc_diff * 4

SPACECRAFT_COST_PER_HOUR = 5000
FUEL_LIMIT = 450

weights = {
    "dv": 0.4,
    "time": 0.2,
    "cost": 0.2,
    "risk": 0.2
}

def objective(route):
    total_dv = 0
    total_time = 0
    total_risk = 0

    for i in range(len(route)-1):
        a = route[i]
        b = route[i+1]
        total_dv += delta_v[a, b]
        total_time += mission_time[a, b]

    for node in route:
        total_risk += debris.iloc[node]["Risk"]

    total_cost = total_time * SPACECRAFT_COST_PER_HOUR
    penalty = 100000 if total_dv > FUEL_LIMIT else 0

    score = (
        weights["dv"] * total_dv +
        weights["time"] * total_time +
        weights["cost"] * total_cost -
        weights["risk"] * 1000 * total_risk +
        penalty
    )

    return score

def neighbour(route):
    new = route.copy()
    move = random.choice(["swap", "reverse", "insert"])

    if move == "swap":
        i, j = random.sample(range(len(new)), 2)
        new[i], new[j] = new[j], new[i]

    elif move == "reverse":
        i, j = sorted(random.sample(range(len(new)), 2))
        new[i:j] = reversed(new[i:j])

    else:
        i, j = random.sample(range(len(new)), 2)
        city = new.pop(i)
        new.insert(j, city)

    return new

def simulated_annealing():
    route = list(range(len(debris)))
    random.shuffle(route)

    best_route = route.copy()
    current_score = objective(route)
    best_score = current_score

    T = 1000
    Tmin = 0.01
    alpha = 0.995

    history = []

    while T > Tmin:
        candidate = neighbour(route)
        candidate_score = objective(candidate)
        delta = candidate_score - current_score

        if delta < 0 or random.random() < math.exp(-delta / T):
            route = candidate
            current_score = candidate_score

        if current_score < best_score:
            best_score = current_score
            best_route = route.copy()

        history.append(best_score)
        T *= alpha

    return best_route, best_score, history

def mission_statistics(route):
    dv = 0
    time = 0
    risk = 0

    for i in range(len(route)-1):
        dv += delta_v[route[i], route[i+1]]
        time += mission_time[route[i], route[i+1]]

    for node in route:
        risk += debris.iloc[node]["Risk"]

    cost = time * SPACECRAFT_COST_PER_HOUR

    print("\nMission Summary")
    print("-" * 35)
    print(f"Total ΔV         : {dv:.2f} m/s")
    print(f"Mission Time     : {time:.2f} hr")
    print(f"Operational Cost : ${cost:,.2f}")
    print(f"Risk Removed     : {risk:.2f}")

if __name__ == "__main__":
    best_route, best_score, history = simulated_annealing()

    print("Best Objective Score:", round(best_score, 2))
    print("\nOptimized Removal Order:")
    print(" -> ".join(debris.iloc[i]["ID"] for i in best_route))

    mission_statistics(best_route)

    plt.figure(figsize=(8,5))
    plt.plot(history)
    plt.xlabel("Iteration")
    plt.ylabel("Best Objective Value")
    plt.title("Simulated Annealing Convergence")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
