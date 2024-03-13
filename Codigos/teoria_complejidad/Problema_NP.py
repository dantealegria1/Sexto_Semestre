## Problema NP
## Alumno Dante Alejandro Alegria Romero

##Generando cadenas binarias con el codigo de Gray
import numpy as np
import time
import sys

global NUMERO_ELEMENTOS
NUMERO_ELEMENTOS = 10

Menor = -100
Arreglo_G = []
Arreglo_J = []

def Generar_Arreglos():
    Arreglo_G = np.zeros(NUMERO_ELEMENTOS)
    Arreglo_J = np.arrange(NUMERO_ELEMENTOS)
    return Arreglo_G, Arreglo_J

def Suma_AyB(Arreglo_G, Arreglo_J):
    suma_A = 0
    suma_B = 0
    for i in range(NUMERO_ELEMENTOS):
        if Arreglo_G[i] == 1:
            suma_A += Arreglo_J[i]
        else:
            suma_B += Arreglo_J[i]
    return suma_A, suma_B


