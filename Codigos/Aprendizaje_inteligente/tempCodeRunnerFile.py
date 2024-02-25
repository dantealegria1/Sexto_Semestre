# Importamos las librerias necesarias
import numpy as np

# Agregamos los valores de los pesos
W14 = 0.2
W24 = 0.4
W34 = -0.5
W15 = -0.3
W25 = 0.1
W35 = 0.2
W46 = -0.3
W56 = -0.2

# Agregamos los valores de las thetas
T4 = -0.4
T5 = 0.2
T6 = 0.1

# Tasa de aprendizaje
L = 0.5

# Agregamos los valores de las entradas
X1 = 1
X2 = 0
X3 = 1

# Salida deseada
D = 1

# Funcion de activacion
def activacion(x):
    return 1 / (1 + np.exp(-x))

# Funcion Neuronas
def Neuronas():
    global W14, W24, W34, T4, W15, W25, W35, T5, W46, W56, T6  # Agrega esta línea
    # Calculamos la salida de la red
    V4 = W14 * X1 + W24 * X2 + W34 * X3 + T4
    Y4 = activacion(V4)

    V5 = W15 * X1 + W25 * X2 + W35 * X3 + T5
    Y5 = activacion(V5)

    V6 = W46 * Y4 + W56 * Y5 + T6
    Y6 = activacion(V6)
    return Y4, Y5, Y6

def Entrenamientos():
    # Calculamos el error de salida
    Y4 = Neuronas()[0]
    Y5 = Neuronas()[1]
    Y6 = Neuronas()[2]
    global D

    Error_Salida = Y6 * (1 - Y6) * (D - Y6)

    # Calculamos el error de la capa oculta
    Error_Oculta4 = Y4 * (1 - Y4) * W46 * Error_Salida
    Error_Oculta5 = Y5 * (1 - Y5) * W56 * Error_Salida

    # Calculamos los nuevos pesos y thetas
    W14 = W14 + L * Error_Oculta4 * X1
    W24 = W24 + L * Error_Oculta4 * X2
    W34 = W34 + L * Error_Oculta4 * X3
    T4 = T4 + L * Error_Oculta4

    W15 = W15 + L * Error_Oculta5 * X1
    W25 = W25 + L * Error_Oculta5 * X2
    W35 = W35 + L * Error_Oculta5 * X3
    T5 = T5 + L * Error_Oculta5

    W46 = W46 + L * Error_Salida * Y4
    W56 = W56 + L * Error_Salida * Y5
    T6 = T6 + L * Error_Salida


# Creamos una función main para ejecutar el programa
def main():
    for i in range(10):
        Neuronas()
        Entrenamientos()

if __name__ == "__main__":
    main()
    #Verificamos que los valores de los pesos y thetas sean los correctos
    #Esto lo hacemos 
