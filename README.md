# Wavelet Selection via Sparsity Change (μsc)

## Overview
This repository implements a structured reconstruction of the IEEE Access paper:
"Optimal Wavelet Selection for Signal Denoising"

It includes:
- Wavelet decomposition pipeline (PyWavelets-based)
- Sparsity computation
- μsc metric
- Automatic wavelet ranking
- Full reproducible notebook

## Key Idea
Select wavelet that maximizes μsc:
μsc = (Sκ+1 - S1) / (κ - 1)

## Install
pip install -r requirements.txt

## Run Notebook
jupyter notebook notebooks/wavelet_full.ipynb

## Run Script
python scripts/run_all.py
