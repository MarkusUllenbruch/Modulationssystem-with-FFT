#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# DFT und IDFT Implementierung

def DFT(f):
    """Diskrete Fourier Transformation
    f  --  Input Samples
    """
    n = len(f)
    B = np.zeros( (n,n), dtype=complex )
    for k in range(0,n):
        for l in range(0,n):
            B[k,l] = np.exp(2j*np.pi*k*l/n)
    B_ad = np.conjugate(np.transpose(B))
    return np.dot(B_ad, f)

#------------------------------------------------------------------------


def IDFT(z):
    """Inverse Diskrete Fourier Transformation
    z  --  Input Fourier Coefficients
    """
    z = np.asarray(z, dtype=complex)
    n = z.shape[0]
    B = np.zeros( (n,n), dtype=complex )
    for k in range(0,n):
        for l in range(0,n):
            B[k,l] = np.exp(2j*np.pi*k*l/n)
    return np.real(np.dot(B,z))/n

