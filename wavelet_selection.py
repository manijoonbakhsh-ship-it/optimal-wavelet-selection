
import numpy as np
import pywt
from .wavelet_metrics import sparsity_curve, mu_sc

def decompose(signal, wavelet, level=5):
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    # skip approximation coeffs
    return coeffs[1:]

def evaluate_wavelet(signal, wavelet):
    coeffs = decompose(signal, wavelet)
    s = sparsity_curve(coeffs)
    kappa = np.argmax(np.diff(s)) + 1
    score = mu_sc(s, kappa)
    return score, kappa
