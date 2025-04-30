# H∞(20) Spectral Simulation for Riemann Zeta Function Analysis

This repository contains the numerical simulation and spectral comparison between a truncated 20×20 operator matrix \( \mathcal{H}_\infty^{(20)} \) and the imaginary parts of the first 15 nontrivial zeros of the Riemann zeta function \( \zeta(s) \).

## Contents

- `simulate_Hinfty20.py`: Python script to generate the 20×20 operator and compute eigenvalues.
- `H_infty_20_vs_zeta.csv`: CSV file comparing the computed eigenvalues to known zeta zeros.

## Purpose

This simulation supports the theoretical framework presented in the paper:

**Spectral Realization of the Nontrivial Zeros of the Riemann Zeta Function via a Hermitian Operator Framework**

It approximates the operator spectrum using components derived from:
- Discrete Geometric Quantum Gravity (DGQG)
- Multifaceted Coherence (MC)
- Infinity Algebra

## Reproducibility

To reproduce the results:

```bash
python simulate_Hinfty20.py
