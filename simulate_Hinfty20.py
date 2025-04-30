import numpy as np
import pandas as pd
from sympy import primerange

# 1. Discrete Laplacian on dodecahedron (mock 20-node graph)
laplacian_20 = 3 * np.identity(20)
np.random.seed(42)
adjacency = np.random.randint(0, 2, (20, 20))
adjacency = np.triu(adjacency, 1)
adjacency = adjacency + adjacency.T
np.fill_diagonal(adjacency, 0)
laplacian_20 -= adjacency

# 2. MC potential (diagonal coherence gradient)
mc_potential = np.diag(np.linspace(0.1, 1.5, 20))

# 3. Infinity Algebra operator (prime-weighted shift simulation)
primes = list(primerange(0, 80))[:20]
F_infty = np.zeros((20, 20), dtype=complex)
for i in range(20):
    F_infty[i, i] = np.log(primes[i])
    if i < 19:
        F_infty[i, i+1] = 0.1 * np.log(primes[i+1])
        F_infty[i+1, i] = 0.1 * np.log(primes[i+1])

# Build H_infty^(20)
H_infty_20 = -laplacian_20 + mc_potential + F_infty.real

# Eigenvalues
eigenvalues = np.linalg.eigvalsh(H_infty_20)
eigenvalues_sorted = np.sort(eigenvalues)

# Known first 15 zeta zeros (imaginary parts)
zeta_zeros = [14.134725, 21.022040, 25.010857, 30.424876, 32.935061,
              37.586178, 40.918719, 43.327073, 48.005150, 49.773832,
              52.970321, 56.446248, 59.347044, 60.831780, 65.112544]

# Comparison table
comparison = pd.DataFrame({
    "Index": np.arange(1, 16),
    "H_infty_20 Eigenvalues": eigenvalues_sorted[:15],
    "Im(ζ(s)) Zeta Zeros": zeta_zeros
})

# Export CSV
comparison.to_csv("H_infty_20_vs_zeta.csv", index=False)
print("CSV export complete: H_infty_20_vs_zeta.csv")
