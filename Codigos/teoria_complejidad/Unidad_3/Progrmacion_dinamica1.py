#===============================================
#Dante Alegria Romero
#17/05/2024
#Problema de la varilla con programacion dinamica
#===============================================

import numpy as np

# Lista de los precios de los cortes de la varilla
precios = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

# Tamaño de la varilla
TAMAÑO_VARILLA = 10

# Sin programación dinámica
def cortar_varilla_SD(varilla):
    if varilla == 0:
        return 0
    else:
        maximo = -1
        for i in range(1, varilla + 1):
            maximo = max(maximo, precios[i - 1] + cortar_varilla_SD(varilla - i))
        return maximo

# Con programación dinámica
def cortar_varilla_D(varilla, memoria):
    if varilla == 0:
        return 0
    if memoria[varilla] != -1:
        return memoria[varilla]
    maximo = -1
    for i in range(1, varilla + 1):
        maximo = max(maximo, precios[i - 1] + cortar_varilla_D(varilla - i, memoria))
    memoria[varilla] = maximo
    return maximo

def cortar_varilla_iterativo(varilla):
    memoria = np.zeros(varilla + 1)
    for i in range(1, varilla + 1):
        maximo = -1
        for j in range(1, i + 1):
            maximo = max(maximo, precios[j - 1] + memoria[i - j])
        memoria[i] = maximo 
    return memoria[varilla]

def main():
    print("Sin programación dinámica")
    print(cortar_varilla_SD(TAMAÑO_VARILLA))
    print("Con programación dinámica")
    memoria = np.ones(TAMAÑO_VARILLA + 1) * -1
    print(cortar_varilla_D(TAMAÑO_VARILLA, memoria))

if __name__ == "__main__":
    main()
