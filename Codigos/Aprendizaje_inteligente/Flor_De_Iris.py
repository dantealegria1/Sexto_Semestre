#Importamos las librerias necesarias
import numpy as np

#Pandas es para cargar los datos de las flores de iris
import pandas as pd

#Esta es para el perceptron
from sklearn.linear_model import Perceptron

#Cargamos los datos de las flores de iris
iris = pd.read_csv("iris.csv", sep=';')

#Cargamos los datos de las flores a clases, esto lo usa para comprar con las predicciones
#Si es setosa es 1, si no es 0 
clases = np.array([])
for i in range(len(iris)):
    if iris.iloc[i, 4] == 'setosa':
        clases = np.append(clases, 1)
    else:
        clases = np.append(clases, 0)

#Entrenamos el perceptron
perceptron = Perceptron().fit(iris.iloc[:, 0:2], clases)

# Predicciones
#Setosa, la otra, setosa
predicciones = perceptron.predict([[5.1, 3.5], [6.1, 2.8], [5.0, 3.3]])
print("Predicciones:", predicciones)
