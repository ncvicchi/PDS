#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@autor: Norberto Vicchi

@descripcion:
Generadores de señal parametrizables
-----------
"""

#%% Imports
from scipy import signal as sig
import numpy as np


#%% Generadores

def senoidal(vmax = 1, off = 0, f=10, ph = 0, n = 1000, fs = 1000.0):
    """
    ```
    * Genera una señal senoidal
    
    * Parametros:
    * Valor maximo              vmax = 1
    * Offset                    off  = 0
    * Frecuencia de la señal    f    = 10
    * Fase de la señal          ph   = 0
    * Cantidad de muestras      n    = 1000         
    * Frecuencia de muestreo    fs   = 1000       [Hz]    
    ``` 
    """
    
    # Definimos el tiempo entre muestras
    ts = 1/fs 

    # Creamos el eje temporal
    tt = np.linspace(0, (n-1)*ts, n).flatten()
    
    # Generamos la señal
    ss = vmax * np.sin(2*np.pi*f*tt + ph) + off

    return tt, ss

def diente_sierra(vmax = 1, cd = 5, off = 0, n = 1000, fs = 1000.0):
    """
    ```
    * Genera una señal diente de sierra
    
    * Parametros: 
    * Valor maximo            vmax  = 1
    * cantidad de dientes     cd    = 5   
    * Offset                  off   = 0
    * Cantidad de muestras    n     = 1000            
    * Frecuencia de muestreo  fs    = 1000      [Hz]    
    ``` 
    """

    # Definimos el tiempo entre muestras
    ts = 1/fs 

    # Creamos el eje temporal
    tt = np.linspace(0, (n-1)*ts, n).flatten()
    
    # Generamos la señal
    ss = vmax * sig.sawtooth(2 * np.pi * cd * tt) + off

    return tt, ss

