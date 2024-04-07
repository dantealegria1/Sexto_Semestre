#--------------------------------------------
# Dante Alejandro Alegria Romero
# Agente Viajero con Fuerza Bruta
#--------------------------------------------

import itertools
import math

def distancia(ciudad1, ciudad2):
    return math.sqrt((ciudad1[0] - ciudad2[0])**2 + (ciudad1[1] - ciudad2[1])**2)

def Distancia_total(camino, ciudades):
    distancia_total = 0
    for i in range(len(camino) - 1):
        distancia_total += distancia(ciudades[camino[i]], ciudades[camino[i + 1]])
    return distancia_total

def agente_viajero_fuerza_bruta(ciudades):
    camino_mas_corto = None
    distancia_mas_corta = float('inf')
    for camino in itertools.permutations(range(len(ciudades))):
        distancia = Distancia_total(camino, ciudades)
        if distancia < distancia_mas_corta:
            distancia_mas_corta = distancia
            camino_mas_corto = camino
    return camino_mas_corto, distancia_mas_corta

def main():
    ciudades = [(0, 0), (1, 5), (2, 3), (5, 2), (7, 1)]
    camino_mas_corto, distancia_mas_corta = agente_viajero_fuerza_bruta(ciudades)
    print("El camino más corto es: ", camino_mas_corto)
    print("La distancia más corta es: ", distancia_mas_corta)

if __name__ == '__main__':
    main()
