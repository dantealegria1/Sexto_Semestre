import numpy as np
import timeit

NUMERO_ELEMENTOS = 20

def Crear_Arreglo(Numero_Elementos):
    Arreglo = np.zeros(Numero_Elementos)
    for i in range(Numero_Elementos):
        Arreglo[i] = np.random.randint(1, 10)
    return Arreglo

def Suma_Arreglo_A(Arreglo_Ordenado):
    suma_A = sum(Arreglo_Ordenado[:len(Arreglo_Ordenado)//2])
    return suma_A

def Suma_Arreglo_B(Arreglo_Ordenado):
    suma_B = sum(Arreglo_Ordenado[len(Arreglo_Ordenado)//2:])
    return suma_B

def Valor_Maximo(Arreglo_Ordenado):
    suma_A = Suma_Arreglo_A(Arreglo_Ordenado)
    suma_B = Suma_Arreglo_B(Arreglo_Ordenado)
    valor_maximo = abs(suma_A - suma_B)
    return valor_maximo

def Veinte():
    Arreglo_inicial = Crear_Arreglo(NUMERO_ELEMENTOS)
    Arreglo_Ordenado = np.sort(Arreglo_inicial)
    print(Arreglo_Ordenado)
    for _ in range(1000):
        Valor_Maximo(Arreglo_Ordenado)
    
    suma_A = Suma_Arreglo_A(Arreglo_Ordenado)
    suma_B = Suma_Arreglo_B(Arreglo_Ordenado)
    maximo = Valor_Maximo(Arreglo_Ordenado)
    
    print("Suma de A:", suma_A)
    print("Suma de B:", suma_B)
    print("Valor máximo:", maximo)
    
    timer = timeit.Timer(lambda: Valor_Maximo(Arreglo_Ordenado))
    tiempo_ejecucion = timer.timeit(number=1000)
    print("Tiempo de ejecución para 20 elementos:", tiempo_ejecucion, "segundos")

# Repite la misma lógica para las funciones Cincuenta() y Cien()

def Cincuenta():
    global NUMERO_ELEMENTOS
    NUMERO_ELEMENTOS = 50
    Arreglo_inicial = Crear_Arreglo(NUMERO_ELEMENTOS)
    Arreglo_Ordenado = np.sort(Arreglo_inicial)
    print(Arreglo_Ordenado)
    for _ in range(1000):
        Valor_Maximo(Arreglo_Ordenado)
    
    suma_A = Suma_Arreglo_A(Arreglo_Ordenado)
    suma_B = Suma_Arreglo_B(Arreglo_Ordenado)
    maximo = Valor_Maximo(Arreglo_Ordenado)
    
    print("Suma de A:", suma_A)
    print("Suma de B:", suma_B)
    print("Valor máximo:", maximo)
    
    timer = timeit.Timer(lambda: Valor_Maximo(Arreglo_Ordenado))
    tiempo_ejecucion = timer.timeit(number=1000)
    print("Tiempo de ejecución para 50 elementos:", tiempo_ejecucion, "segundos")

def Cien():
    global NUMERO_ELEMENTOS
    NUMERO_ELEMENTOS = 100
    Arreglo_inicial = Crear_Arreglo(NUMERO_ELEMENTOS)
    Arreglo_Ordenado = np.sort(Arreglo_inicial)
    print(Arreglo_Ordenado)
    for _ in range(1000):
        Valor_Maximo(Arreglo_Ordenado)
    
    suma_A = Suma_Arreglo_A(Arreglo_Ordenado)
    suma_B = Suma_Arreglo_B(Arreglo_Ordenado)
    maximo = Valor_Maximo(Arreglo_Ordenado)
    
    print("Suma de A:", suma_A)
    print("Suma de B:", suma_B)
    print("Valor máximo:", maximo)
    
    timer = timeit.Timer(lambda: Valor_Maximo(Arreglo_Ordenado))
    tiempo_ejecucion = timer.timeit(number=1000)
    print("Tiempo de ejecución para 100 elementos:", tiempo_ejecucion, "segundos")

def main():
    print("20 Elementos")
    Veinte()
    print("\n50 Elementos")
    Cincuenta()
    print("\n100 Elementos")
    Cien()

main()
