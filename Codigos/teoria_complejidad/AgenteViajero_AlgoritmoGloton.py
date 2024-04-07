#--------------------------------------------
# Dante Alejandro Alegria Romero
# Agente Viajero con Fuerza Bruta
#--------------------------------------------
import numpy as np
import math

def distancia(ciudad1, ciudad2):
    return math.sqrt((ciudad1[0] - ciudad2[0])**2 + (ciudad1[1] - ciudad2[1])**2)

def Distancia_Total(ruta, ciudades):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += distancia(ciudades[ruta[i]], ciudades[ruta[i + 1]])
    return distancia_total

def agente_viajero_greedy(ciudades):
    num_ciudades = len(ciudades)
    ruta = [0]
    visitadas = set([0])
    for i in range(num_ciudades - 1):
        ciudad_actual = ruta[-1]
        distancia_minima = float('inf')
        ciudad_mas_cercana = None
        for siguiente_ciudad in range(num_ciudades):
            if siguiente_ciudad not in visitadas:
                dist = distancia(ciudades[ciudad_actual], ciudades[siguiente_ciudad])
                if dist < distancia_minima:
                    distancia_minima = dist
                    ciudad_mas_cercana = siguiente_ciudad
        ruta.append(ciudad_mas_cercana)
        visitadas.add(ciudad_mas_cercana)
    ruta.append(0)
    return ruta

def main():
    ciudades = np.array([(0, 0), (1, 5), (2, 3), (5, 2), (7, 1)])
    ruta = agente_viajero_greedy(ciudades)
    print("La ruta más corta es: ", ruta)
    print("La distancia más corta es: ", Distancia_Total(ruta, ciudades))

if __name__ == "__main__":
    main()
