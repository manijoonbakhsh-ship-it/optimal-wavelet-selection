
import numpy as np

def sparsity(detail_coeffs):
    detail_coeffs = np.asarray(detail_coeffs)
    return np.max(np.abs(detail_coeffs)) / (np.sum(np.abs(detail_coeffs)) + 1e-12)

def sparsity_curve(coeffs_levels):
    return np.array([sparsity(c) for c in coeffs_levels])

def delta_s(s):
    return np.diff(s, prepend=s[0])

def mu_sc(s, kappa):
    if kappa <= 1:
        return 0
    return (s[kappa] - s[0]) / (kappa - 1)
