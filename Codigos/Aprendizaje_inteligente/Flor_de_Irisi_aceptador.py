import numpy as np
import pandas as pd

iris = pd.read_csv("iris.csv", sep=';')

clases = np.array([])
for i in range(len(iris)):
    if iris.iloc[i, 4] == 'setosa':
        clases = np.append(clases, 1)
    else:
        clases = np.append(clases, 0)

# w1*x1 + w2*x2 +...+ wn*xn
def activacion(pesos, x, b):
    z = np.dot(pesos, x) + b
    if z > 0:
        # Si es 1 es setosa, si es 0 es versicolor
        return 1
    else:
        return 0

# Entrenamiento
pesos = np.random.uniform(-1, 1, size=2)
b = np.random.uniform(-1, 1)
tasa_de_aprendizaje = 0.01
epocas = 100

for epoch in range(epocas):
    error_total = 0
    for j in range(len(iris)):
        prediccion = activacion(pesos, iris.iloc[j, 0:2], b)
        error = clases[j] - prediccion
        error_total += error ** 2
        pesos[0] += tasa_de_aprendizaje * iris.iloc[j, 0] * error
        pesos[1] += tasa_de_aprendizaje * iris.iloc[j, 1] * error
        b += tasa_de_aprendizaje * error

print(activacion(pesos, [5.1, 3.5], b))
print(activacion(pesos, [7.0, 3.2], b))