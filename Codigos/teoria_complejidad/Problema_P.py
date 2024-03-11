#Probelma P
#Alumno: Dante Alejandro Alegria Romero

import numpy as np
import time 
import sys

NUMERO_ELEMENTOS = 10

def Crear_Arreglo(Numero_Elementos):
    Arreglo = np.zeros(Numero_Elementos)
    for i in range(Numero_Elementos):
        Arreglo[i] = np.random.randint(0, 100)
    return Arreglo

Arreglo_inicial = Crear_Arreglo(NUMERO_ELEMENTOS)
Arreglo_Ordenado = np.sort(Arreglo_inicial)

def Suma_Arreglo_A(Arreglo_Ordenado):
    suma_A = 0
    for i in range(len(Arreglo_Ordenado)//2):
        suma_A += Arreglo_Ordenado[i]
    return suma_A

def Suma_Arreglo_B(Arreglo_Ordenado):
    suma_B = 0
    for i in range(len(Arreglo_Ordenado)//2):
        suma_B += Arreglo_Ordenado[i+NUMERO_ELEMENTOS//2]
    return suma_B

def Valor_Maximo(Arreglo_Ordenado):
    valor_maximo = Suma_Arreglo_A(Arreglo_Ordenado) - Suma_Arreglo_B(Arreglo_Ordenado)
    print("El valor maximo es: ", valor_maximo)

def main():
    inicio = time.time()
    Valor_Maximo(Arreglo_Ordenado)
    print("Se alcanza cuando A contiene la mitad de los elementos de U y B y la mitad de los elementos mas grandes")
    Tiempo_Ejecucion = time.time() - inicio
    Tiempo_Ejecucion = sys.float_info.max
    print("El tiempo de ejecucion es: ", Tiempo_Ejecucion)

main()