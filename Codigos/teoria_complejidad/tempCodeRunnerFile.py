def Suma_Arreglo_A(Arreglo_Ordenado):
    suma_A = 0
    i = 1
    for i in range(len(Arreglo_Ordenado)//2):
        suma_A += Arreglo_Ordenado[i]
    print("La suma de A es: ", suma_A)
    return suma_A
def Suma_Arreglo_B(Arreglo_Ordenado):
    suma_B = 0
    i = 1
    for i in range(len(Arreglo_Ordenado)//2):
        suma_B += Arreglo_Ordenado[i+(NUMERO_ELEMENTOS//2)]
    print("La suma de B es: ", suma_B)
    return suma_B

def Valor_Maximo(Arreglo_Ordenado):
    valor_maximo = Suma_Arreglo_A(Arreglo_Ordenado) - Suma_Arreglo_B(Arreglo_Ordenado)
    valor_maximo = abs(valor_maximo)
    print("El valor maximo es: ", valor_maximo)

def Veinte():
    inicio = time.time()
    print(Arreglo_inicial)
    Valor_Maximo(Arreglo_Ordenado)
    Tiempo_Ejecucion = time.time() - inicio
    print("--- %.9f seconds ---" % (Tiempo_Ejecucion))  # Cambia el número 6 según la cantidad de decimales que desees mostrar


def Cincuenta():
    global NUMERO_ELEMENTOS
    NUMERO_ELEMENTOS = 50
    Arreglo_inicial = Crear_Arreglo(NUMERO_ELEMENTOS)
    print(Arreglo_inicial)
    Arreglo_Ordenado = np.sort(Arreglo_inicial)
    inicio = time.time()
    Valor_Maximo(Arreglo_Ordenado)
    Tiempo_Ejecucion = time.time() - inicio
    print("--- %.9f seconds ---" % (Tiempo_Ejecucion))  # Cambia el número 6 según la cantidad de decimales que desees mostrar


def Cien():
    global NUMERO_ELEMENTOS
    NUMERO_ELEMENTOS = 100
    Arreglo_inicial = Crear_Arreglo(NUMERO_ELEMENTOS)
    print(Arreglo_inicial)
    Arreglo_Ordenado = np.sort(Arreglo_inicial)
    inicio = time.time()
    Valor_Maximo(Arreglo_Ordenado)
    Tiempo_Ejecucion = time.time() - inicio
    print("--- %.9f seconds ---" % (Tiempo_Ejecucion))  # Cambia el número 6 según la cantidad de decimales que desees mostrar


def main():
    print("20 Elementos")
    Veinte()
    print("50 Elementos")
    Cincuenta()
    print("100 Elementos")
    Cien()

main()