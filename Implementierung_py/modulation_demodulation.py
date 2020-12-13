#!/usr/bin/env python
# coding: utf-8

import numpy as np

# Modulation Implementierung
def modulation(signal, f, fs):
    """ Erzeugt moduliertes Signal
        time   -- Zeitvektor
        signal -- Signal das zu modulieren ist
        f      -- Modulationsfrequenz
        fs     -- Samplingfrequenz
    """
    t_end = len(signal)/fs
    time = np.linspace(0, t_end, t_end * fs, endpoint=True)
    s = np.cos(2*np.pi*f*time)
    return signal*s

# --------------------------------------------------------------------------
# Demodulation Implementierung
def demodulation(signal, f, fs):
    """ Erzeugt demoduliertes Signal aus dem Trägersignal
        time   -- Zeitvektor
        signal -- Trägersignal das zu demodulieren ist
        f      -- Modulationsfrequenz
        fs     -- Samplingfrequenz
    """
    t_end = len(signal)/fs
    time = np.linspace(0, t_end, t_end * fs, endpoint=True)
    s = 2*np.cos(2*np.pi*f*time)
    return signal*s
