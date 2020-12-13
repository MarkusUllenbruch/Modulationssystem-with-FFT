#!/usr/bin/env python
# coding: utf-8

import numpy as np

# Tiefpassfilter im Zeitbereich Implementierung
def lowpass(samples, w_s, w_c, n):
    """ Tiefpassfilterung mit Verwendung von Hamming-Window
    samples -- Gesampelte Daten die gefiltert werden sollen
    w_s     -- sampling frequency w_s = 1/ T_A
    w_c     -- Grenzfrequenz, Frequenzen > w_c werden gefiltert
    n       -- Ordnung des Filters
    """
    w_c_head = 2 * w_c / w_s
    x = np.zeros(n)
    w = np.zeros(n)
    h = np.zeros(n)
    for k in range(n):
        x[k] = w_c_head * np.sinc(w_c_head * (k - 0.5*n)) # Impulsantwort
        w[k] = 0.54 - 0.46 * np.cos(2 * np.pi * k/n)      # Hamming-Window
    h = x * w
    convolved = np.convolve(samples, h) # In Test mit eigener schnellen Faltung
    return convolved



