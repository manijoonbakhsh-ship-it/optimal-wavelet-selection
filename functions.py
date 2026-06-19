import numpy as np
import matplotlib.pyplot as plt

# =========================
# 1. Wavelet-like filter response (approximation)
# =========================
x = np.linspace(0, 1, 200)

lp = np.exp(-((x - 0.5)**2) / 0.02)
hp = 1 - lp

plt.figure()
plt.plot(x, lp, label="Low-pass")
plt.plot(x, hp, label="High-pass")
plt.title("Wavelet Filter Response (Approx.)")
plt.legend()
plt.savefig("fig1_wavelet_filters.png")

# =========================
# 2. Sparsity across decomposition levels
# =========================
levels = np.arange(1, 11)

sparsity = np.array([0.10, 0.12, 0.15, 0.22, 0.35, 0.52, 0.68, 0.74, 0.78, 0.80])

plt.figure()
plt.plot(levels, sparsity, marker='o')
plt.title("Sparsity vs Decomposition Level")
plt.xlabel("Level")
plt.ylabel("Sparsity S_j")
plt.savefig("fig2_sparsity_curve.png")

# =========================
# 3. Sparsity change ΔS (core paper metric)
# =========================
delta_s = np.diff(sparsity, prepend=sparsity[0])

plt.figure()
plt.stem(levels, delta_s)
plt.title("Sparsity Change ΔS")
plt.xlabel("Level")
plt.savefig("fig3_delta_s.png")

# =========================
# 4. Signal vs Noise (SNR example)
# =========================
t = np.linspace(0, 1, 500)

clean = np.sin(8 * np.pi * t)
noise = np.random.normal(0, 0.3, len(t))
noisy = clean + noise

plt.figure()
plt.plot(t, clean, label="Clean")
plt.plot(t, noisy, label="Noisy", alpha=0.7)
plt.title("Clean vs Noisy Signal")
plt.legend()
plt.savefig("fig4_signal_noise.png")

# =========================
# 5. μsc wavelet ranking (from paper-style table)
# =========================
wavelets = ["db4", "sym4", "coif3", "bior1.3", "rbio1.5"]
mus = [0.126, 0.096, 0.152, 0.093, 0.089]

plt.figure()
plt.bar(wavelets, mus)
plt.title("Wavelet Ranking by μsc")
plt.ylabel("μsc")
plt.savefig("fig5_musc_ranking.png")

# =========================
# 6. SNR vs μsc trend
# =========================
snr = [5, 10, 30, 50]
musc = [0.09, 0.11, 0.14, 0.16]

plt.figure()
plt.plot(snr, musc, marker='o')
plt.title("SNR vs μsc")
plt.xlabel("SNR")
plt.ylabel("μsc")
plt.savefig("fig6_snr_vs_musc.png")

print("All figures generated.")