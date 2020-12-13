#!/usr/bin/env python
# coding: utf-8

import numpy as np


# Rekursive FFT, Sin/Cos terme nicht ausgelagert
def rec_FFT(f):
    """ Recursive FFT calculation of samples f """
    f = np.asarray(f)
    n = f.shape[0]
        
    if n == 1:
        return f
    else:
        f_even = f[::2]
        f_odd = f[1::2]
        g = rec_FFT(f_even)
        u = rec_FFT(f_odd)
        c = np.zeros(n, dtype=complex)
        for k in range(n//2):
            c[k] = g[k] + u[k]*np.exp(-2j*np.pi*k/n)
            c[k+n//2] = g[k] - u[k]*np.exp(-2j*np.pi*k/n)
    return c

#---------------------------------------------------------------------------
#Rekursive FFT mit Berechnung der Sin/Cos Terme ausgelagert
def rk(f):
    """Calculation of rk outside of the FFT for speed up"""
    n = f.shape[0]
    r = np.zeros(n//2, dtype=complex)
    for k in range(n//2):
        r[k] = np.exp(-2j*np.pi*k/n)
    return r

def rec_FFT2(f,r):
    """ Recursive FFT calculation of samples f with calculation of rk outside"""
    f = np.asarray(f)
    n = f.shape[0]
        
    if n == 1:
        return f
    else:
        f_even = f[::2]
        f_odd = f[1::2]
        g = rec_FFT(f_even)
        u = rec_FFT(f_odd)
        c = np.zeros(n, dtype=complex)
        for k in range(n//2):
            c[k] = g[k] + u[k]*r[k]
            c[k+n//2] = g[k] - u[k]*r[k]
    return c

# ---------------------------------------------------------------------------
# Inverse rekursive FFT
def IFFT(z):
    """Inverse Recursive FFT calculation of Fourier coefficients z"""
    n = len(z)
    f = IFFT_rec(z)
    return np.real(f)/n


def IFFT_rec(z):
    """  """
    z = np.asarray(z, dtype=complex)
    n = z.shape[0]
    z_even = z[::2]
    z_odd = z[1::2]
    
    if n == 1:
        return z
    else:
        g = IFFT_rec(z_even)
        u = IFFT_rec(z_odd)
        c = np.zeros(n, dtype=complex)
        
        for k in range(n//2):
            temp = u[k]*np.exp(2j*np.pi*k/n)
            c[k]      = g[k] + temp
            c[k+n//2] = g[k] - temp
    return c
