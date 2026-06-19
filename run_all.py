
import numpy as np
import matplotlib.pyplot as plt

from src.wavelet_selection import evaluate_wavelet

signal = np.sin(np.linspace(0, 10*np.pi, 1000)) + 0.3*np.random.randn(1000)

wavelets = ["db2","db4","sym4","coif3","bior1.3"]

scores = []
for w in wavelets:
    s, k = evaluate_wavelet(signal, w)
    scores.append(s)

plt.bar(wavelets, scores)
plt.title("Wavelet Ranking (μsc)")
plt.show()
