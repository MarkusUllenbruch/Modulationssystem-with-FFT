#!/usr/bin/env python
# coding: utf-8

import numpy as np

#  Overall System Implementation
def overall_system(sig1, sig2, fs, fc, n, w1_mod, w2_mod):
    """ Funktion führt die Kette:  ----Tiefpass -> Modulation -> Demodulation -> Tiefpass---- durch
    sig1   --  zu modulierendes Inputsignal 1
    sig2   --  zu modulierendes Inputsignal 2
    fs     --  Abstastfrequenz
    fc     --  Cutoff-Frequenz des Tiefpassfilter
    n      --  Ordnung des Tiefpassfilter
    w1_mod --  Modulationsfrequenz 1 in Hz angewendet auf Signal 1
    w2_mod --  Modulationsfrequenz 2 in Hz angewendet auf Signal 2
    """
    s1 = lowpass(sig1, fs, fc, n) 
    s2 = lowpass(sig2, fs, fc, n)

    smod1 = modulation(s1, w1_mod, fs)
    smod2 = modulation(s2, w2_mod, fs)
    
    s_mod = smod1 + smod2
    
    s1_demod = demodulation(s_mod, w1_mod, fs)
    s2_demod = demodulation(s_mod, w2_mod, fs)

    s11 = lowpass(s1_demod, fs, fc, n)
    s22 = lowpass(s2_demod, fs, fc, n)

    return s11, s22
