#!/usr/bin/env python
# coding: utf-8

import numpy as np

## Convolution in Time Domain Implementation
def convolution(f, g):
    """Faltung im Zeitbereich
    f, g  --  Input: Diskrete Funktionen, die gefalten werden
    Gefaltetes Signal hat Länge F+G-1
    """
    n = len(f)
    m = len(g)
    
    f = np.concatenate((np.zeros(m-1), np.asarray(f,dtype=float)))
    f = np.concatenate((f,  np.zeros(m-1)))
    
    result = np.zeros(n+m-1)
    for i in range(0, n+m-1):
        summe = 0
        for j in range(0,m):
            summe = summe + f[i+m-j-1]*g[j]
        result[i] = summe
    return result


def convolution2(f, g):
    """Gefaltetes Signal hat Länge F"""
    Falt = np.zeros(len(f))
    
    for i in range(len(f)):
        for j in range(len(g)):
            if i-j >= 0:
                Falt[i] = Falt[i] + f[i-j]*g[j]
            else:
                Falt[i] = Falt[i] + 0
    return Falt
