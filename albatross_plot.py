import numpy as np
import matplotlib.pyplot as plt

# Data the 14 mortality studies
studies = [
    "Periselneris", "Nabavi", "Moazzami", "Haskologlu", "Goussault", 
    "Collet", "Chandesris", "Chalmers", "Carrabba", "Brent", 
    "Bintalib", "Bayrak-Durmaz", "Aykan", "Ameratunga '25"
]
sample_sizes = [153, 98, 66, 11, 20, 20, 39, 55, 30, 801, 129, 45, 116, 108]
# Approximated p-values calculated from then study standard errors
p_values = [0.0003, 0.0001, 0.0001, 0.294, 0.136, 0.304, 0.035, 0.002, 0.068, 0.0001, 0.0001, 0.148, 0.0001, 0.0001]

# Plot grid
plt.figure(figsize=(9, 6))
plt.scatter(p_values, sample_sizes, color='teal', edgecolor='black', s=80, zorder=5)

# Add label 
for i, txt in enumerate(studies):
    plt.annotate(txt, (p_values[i], sample_sizes[i]), xytext=(5, 5), textcoords='offset points', fontsize=8)

# Format axes for standard Albatross layouts
plt.xscale('log')
plt.xlim(1, 1e-5)
plt.xlabel('Two-sided P-value (Log Scale)')
plt.ylabel('Total Sample Size (N)')
plt.title('Albatross Plot Matrix for Baseline Cohort Mortality')
plt.grid(True, which="both", ls="--", alpha=0.5)

# Render output 
plt.tight_layout()
plt.show()