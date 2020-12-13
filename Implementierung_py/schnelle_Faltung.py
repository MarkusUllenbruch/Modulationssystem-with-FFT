#!/usr/bin/env python
# coding: utf-8

import numpy as np


# Schnelle Faltung Implementierung
def schnelle_faltung(f_arg, g_arg):
    """ Berechne schnelle Faltung von 2 Inputsignalen
    f_arg  --  Inputsignal 1
    g_arg  --  Inputsignal 2
    """
    if f_arg.size >= g_arg.size: # Bezeichne längeres Signal als f
        f = f_arg                # Bezeichne kürzeres Signal als g
        g = g_arg
    else:
        f = g_arg
        g = f_arg
        
    G = g.shape[0]               # Länge "Impulsantwort"       
    F = 8*G                      # Länge Fenster --> grobe Festlegung, Daumenregel aus Vorlesung
    F = 2**(int(np.log2(F)) + 1) # F>G UND 2er-Potenz, es wird die nächste 2-er Potenz berechnet zu 8*G
    
    g = np.pad(g, (0, F-G), 'constant', constant_values=(0,0)) # Füge F-G Nullen ans Ende von g ein
    f = np.pad(f, (G-1, 0), 'constant', constant_values=(0,0)) # Füge G-1 Nullen an Anfang von f ein
    len_F = len(f)         # Länge des zero gepaddeten Signals f
    h = [];                # Initialisiere leeren Array h  
    delta = F - G + 1
    s = 0                  # Shift-Index       
    while True: 
        f_block = [];
        if s+F-1 >= len_F: #Abbruchbedingung der while-Schleife Vor "break" muss noch  verbleibendes Signal verarbeitet werden
            signal_remaining = f[s:]  
            part_for_FFT = np.concatenate((signal_remaining, np.zeros(F-len(signal_remaining))) )
            cyc = np.fft.ifft(np.fft.fft(part_for_FFT)*np.fft.fft(g))   # Zyklische Faltung
            h = np.concatenate((h, cyc[G-1: G+len(signal_remaining)-1]))
            break
        else:
            f_block = f[s:s+F]
            z =  np.fft.ifft( np.fft.fft(f_block) * np.fft.fft(g) )  #Zyklische Faltung
            h = np.concatenate((h, z[G-1: F]))
            s = s + delta
        
    h = np.array(h, dtype=np.float64)    
    return h
# In Test mit eigener FFT implementiert