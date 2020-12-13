#!/usr/bin/env python
# coding: utf-8

import numpy as np

# Iterative FFT
def FFT_ITER(f, rk):
    """Iterative FFT
    f   --  Samples, Input
    rk  --  Sin/Cos Koeffizienten die ausserhalb berechnet werden
    """
    
    n = f.shape[0]                     
    IND = Bitflip(f)                     
    len_Offset = 1                                
    exponent = int(np.log2(n))                  
                                         
    zk = np.zeros(n, dtype=complex)      
    zk_temp = zk                              
    ZK_K = 0          
    ZK_Offset = 0
    count = 0
    for i in range (exponent):
        count = 0
        for k in range(n//2):
            if i == 0:
                a = int(IND[2*k])
                b = int(IND[2*k + len_Offset])
                temp = f[b] * rk[2*k, i+1]
                zk[2*k] = f[a] + temp
                zk[2*k + len_Offset] = f[a] - temp
            else: 
                if k >= len_Offset: 
                    if k % len_Offset == 0:
                        count +=1    
                    k = int(count*len_Offset + k)
                    
                temp = zk_temp[k + len_Offset] * rk[k, i+1]
                ZK_K = zk_temp[k] + temp 
                ZK_Offset = zk_temp[k] - temp
                zk[k] = ZK_K
                zk[k + len_Offset] = ZK_Offset
                
        zk_temp = zk       
        len_Offset = int(len_Offset*2)
    
    return zk


# rk --> Ausgelagerte Sin/Cos Terme
def calc_rk(f):
    """Calculate sin/cos coefficients
    f  --  Samples to Fourier Transform
    """
    n = 2*f.shape[0]                  
    n_HALF = int(f.shape[0])              
    Expo = int(np.log2(n))               
    rk = np.zeros([n_HALF, Expo], dtype = complex)     
    for k in range(n_HALF): 
        for i in range(Expo):
            rk[k, i] = np.exp(-2j*np.pi*(k) / (2**i))
    return rk


#----------------------------------------------------------------------------
# Inverse iterative FFT

def Bitflip(f):
    n = f.shape[0]                          
    exponent = int(np.log2(n))                     
    Ind_in = np.linspace(0, n-1, n)              
    Ind_output = np.linspace(0, n-1, n)              
    for k in range(n):                                 
        Binary = bin(int(Ind_in[k]))        
        d  = np.zeros(exponent)           
        Str_BIT  = ''
        j = len(Binary) - 1
        for i in range(0, len(Binary) - 2):              
            d[i] = Binary[j]
            j -= 1                              
        for i in range(0, len(d)):
            Str_BIT += str(int(d[i]))   
        Ind_output[k] = int(binary_2_decimal(Str_BIT))      
    return Ind_output



def binary_2_decimal(Seq):
    """Convert Binary Number to a Decimal Number"""
    summe = 0
    for k in enumerate(reversed(str(Seq))):
        summe += int(k[1]) * 2**(k[0])
    return summe

# IFFT
def IFFT_ITER(zk, rk):
    """
    zk  --  Koeffizienten
    rk  --  Ausgelagerte Matrix, gleiches rk wie bei FFT
    """
    rk = rk**(-1)
    n = zk.shape[0]
    index = Bitflip(zk)
    length_offset = 1
    exponent = int(np.log2(n))
    f = np.zeros(n, dtype=complex)
    f_temp = zk
    f_k = 0
    f_k_offset = 0
    count = 0
    
    for i in range(exponent):
        count = 0
        for k in range(n//2):
            if i == 0:
                a = int(index[2*k])
                b = int(index[2*k + length_offset])
                temp = zk[b] * rk[2*k,i+1]
                f[2*k] = zk[a] + temp
                f[2*k + length_offset] = zk[a] - temp
            else:
                if k >= length_offset:   
                    if k % length_offset == 0:
                        count += 1
                    k = int(count*length_offset + k)
                    
                temp = f_temp[k+length_offset] * rk[k, i+1]
                f_k = f_temp[k] + temp 
                f_k_offset = f_temp[k] - temp
                f[k] = f_k
                f[k + length_offset] = f_k_offset
        f_temp = f       
        length_offset = int(length_offset*2)
                
    return f/n

