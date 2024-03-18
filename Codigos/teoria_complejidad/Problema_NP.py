import numpy as np
import time
import random
import sys

NUMERO_ELEMENTOS = 20

Menor = np.inf
Vector_Menor = []

def Generar_Vector_U():
    Vector_U = []
    for i in range(NUMERO_ELEMENTOS+1):
        Vector_U.append(random.randint(0,10)) 
    print(Vector_U)
    return Vector_U

def Generar_Vector_G():
    Vector_G = []
    for i in range(NUMERO_ELEMENTOS+1):
        Vector_G.append(0)
    return Vector_G

def Generar_Vector_J():
    Vector_J = []
    for i in range(0, NUMERO_ELEMENTOS + 1):
        Vector_J.append(i+1)
    return Vector_J

def Suma_AyB(Vector_G, Vector_U, Menor, Vector_Menor):
    Suma_A = 0
    Suma_B = 0
    for i in range(NUMERO_ELEMENTOS - 1, -1, -1):
        if Vector_G[i] == 1:
            Suma_A += Vector_U[i]
        else:
            Suma_B += Vector_U[i]
    if Menor > abs(Suma_A-Suma_B):
        Menor = abs(Suma_A-Suma_B)
        for i in range(NUMERO_ELEMENTOS):
            Vector_Menor[i] = Vector_G[i]

    return Menor
        
def Voltear_Bit(Vector_G, i):
    if 0 <= i - 1 < len(Vector_G):
        if Vector_G[i - 1] == 0:
            Vector_G[i - 1] = 1
        else:
            Vector_G[i - 1] = 0
    else:
        print("Error: El índice está fuera de los límites del vector.")

def Vector_aYb(Vector_Menor, Vector_U):
    Vector_A = []
    Vector_B = []
    for i in range(len(Vector_Menor)):
        if Vector_Menor[i] == 1:
            Vector_A.append(Vector_U[i])
        else:
            Vector_B.append(Vector_U[i])
    print("Vector A:",Vector_A)
    print("Vector B:",Vector_B)

def Codigo_Gray(Vector_Menor):
    Vector_G = Generar_Vector_G()
    Vector_J = Generar_Vector_J()
    Vector_U = Generar_Vector_U()
    Menor = np.inf
    Vector_Menor = [0] * len(Vector_G) 
    i = 0
    while i < NUMERO_ELEMENTOS+1:
        #print(Vector_G)
        Menor = Suma_AyB(Vector_G, Vector_U, Menor, Vector_Menor)  
        i = Vector_J[0]
        if i == NUMERO_ELEMENTOS+1:
            Voltear_Bit(Vector_G, i)
            break
        Voltear_Bit(Vector_G, i)
        Vector_J[i-1] = Vector_J[i]
        Vector_J[i] = i+1
        if i != 1:
            Vector_J[0] = 1  
    print("MENOR:",Menor)
    print("MENOR:",Vector_Menor)
    Vector_aYb(Vector_Menor, Vector_U)
    return Menor

def veinte():
    print("20 Elementos")
    start_time = time.time()
    Vector_Menor = []  
    Codigo_Gray(Vector_Menor)
    Tiempo_Ejecucion = time.time() - start_time
    return Tiempo_Ejecucion

def Cincuenta():
    global NUMERO_ELEMENTOS
    print("50 Elementos")
    start_time = time.time()
    NUMERO_ELEMENTOS = 50
    Vector_Menor = []  
    Codigo_Gray(Vector_Menor)
    Tiempo_Ejecucion = time.time() - start_time
    return Tiempo_Ejecucion

def Cien():
    global NUMERO_ELEMENTOS
    print("100 Elementos")
    start_time = time.time()
    NUMERO_ELEMENTOS = 100
    Vector_Menor = []  
    Codigo_Gray(Vector_Menor)
    Tiempo_Ejecucion = time.time() - start_time
    return Tiempo_Ejecucion

def main():
    #Tiempo_20 = veinte()
    #Tiempo_50 = Cincuenta()
    Tiempo_100 = Cien()
    #print("--- %s seconds ---" % (Tiempo_20))
    #print("--- %s seconds ---" % (Tiempo_50))
    print("--- %s seconds ---" % (Tiempo_100))
    

if __name__ == "__main__":
    main()
    


