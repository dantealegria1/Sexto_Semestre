import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
import numpy as np

#Importamos las librerias necesarias
nltk.download('punkt')
nltk.download('stopwords')

#Creamos nuestras variables globales
global PROHIBIDAS
PROHIBIDAS = [""]
global ARCHIVO
ARCHIVO = "comments.csv"
global DATASET
DATASET = pd.read_csv(ARCHIVO)

def Quitar_Valores_Nulos():
    for i in range(len(DATASET)):
        if DATASET.loc[i, "comment"] == "":
            if DATASET.loc[i, "rating"] == 1:
                DATASET.loc[i, "comment"] = "bueno"
            if DATASET.loc[i, "rating"] == 0:
                DATASET.loc[i, "comment"] = "malo"

def Vectores_Palabras(dataset):
    Palabras = []
    Largo = len(dataset)
    for i in range(Largo):
        Palabras.append(DATASET["comment"][i])
    return Palabras

def Filtar_Palabras(Palabras):
    Palabras_Filtradas = []
    for review in Palabras:
        if isinstance(review, str):  # Check if the element is a string
            tokens = word_tokenize(review)
            stopwords_ingles = set(stopwords.words('spanish'))
            Palabras_Filtradas.extend([Palabra.lower() for Palabra in tokens
                                        if Palabra.isalpha() and Palabra.lower()
                                        not in stopwords_ingles and Palabra.lower() not in PROHIBIDAS])
    return Palabras_Filtradas

def Probabilidad_Palabra(Palabra, Review):
    Probabilidad_Palabra = (Review.count(Palabra)+1) / len(Review)
    return Probabilidad_Palabra

def Probabilidad_Review(Review, Palabras):
    Probabilidades = []
    Review = Filtar_Palabras([Review])
    for Palabra in Review:
        Probabilidades.append(Probabilidad_Palabra(Palabra, Palabras))
    return np.array(Probabilidades)

def main_Redes():
    Quitar_Valores_Nulos()
    X = DATASET["comment"]
    Y = DATASET["rating"]
    df_Test, df_Train, Res_Test, Res_Train = train_test_split(X,Y, test_size=0.5, random_state=42)
    Palabras_Entrenamiento = Vectores_Palabras(df_Train)
    Palabras_EnFiltradas = Filtar_Palabras(Palabras_Entrenamiento)
    Matriz_Entrenamiento = []
    max_length = 0 # Initialize a variable to keep track of the maximum length
    for review in Palabras_Entrenamiento:
        prob_review = Probabilidad_Review(review, Palabras_EnFiltradas)
        Matriz_Entrenamiento.append(prob_review)
        max_length = max(max_length, len(prob_review)) # Update max_length if necessary

    for i in range(len(Matriz_Entrenamiento)):
        if len(Matriz_Entrenamiento[i]) < max_length:
            Matriz_Entrenamiento[i] = np.pad(Matriz_Entrenamiento[i], (0, max_length - len(Matriz_Entrenamiento[i])), 'constant', constant_values=0)
    
    Matriz_Entrenamiento = np.array(Matriz_Entrenamiento, dtype=float)
    Res_Train = np.array(Res_Train)
    #--------------------------------------------------------------------------------
    instancia_red = MLPClassifier(hidden_layer_sizes=(50, 50, 50), max_iter=1000)
    instancia_red.fit(Matriz_Entrenamiento, Res_Train)
    #--------------------------------------------------------------------------------
    Palabras_Test = Vectores_Palabras(df_Test)
    Palabras_Test_Filtradas = Filtar_Palabras(Palabras_Test)
    Matriz_Test = []
    max_length = 0
    for review in Palabras_Test:
        prob_review = Probabilidad_Review(review, Palabras_Test_Filtradas)
        Matriz_Test.append(prob_review)
        max_length = max(max_length, len(prob_review))

    for i in range(len(Matriz_Test)):
        if len(Matriz_Test[i]) < max_length:
            Matriz_Test[i] = np.pad(Matriz_Test[i], (0, max_length - len(Matriz_Test[i])), 'constant', constant_values=0)
    
    Matriz_Test = np.array(Matriz_Test, dtype=float)
    Res_Test = np.array(Res_Test)

    #--------------------------------------------------------------------------------
    Predicciones = instancia_red.predict(Matriz_Test)
    Matriz_Confusion = confusion_matrix(Res_Test, Predicciones)
    #print(Matriz_Confusion)
    #--------------------------------------------------------------------------------
    #Forma de la 5ta practica
    precision = np.sum(np.diag(Matriz_Confusion)) / np.sum(Matriz_Confusion)
    print('presicion global',precision)
    print('presicion negativa',Matriz_Confusion[0][0]/np.sum(Matriz_Confusion[0]))
    print('presicion positiva',Matriz_Confusion[1][1]/np.sum(Matriz_Confusion[1]))
    print('error',1-precision)

#--------------------------------------------------------------------------------
#mi forma que es de la presentacion del profe
    tn, fp, fn, tp = confusion_matrix(Res_Test, Predicciones).ravel()
    precision = (tn+tp)/(tn+fp+fn+tp)
    FalsosPositivos = fp/(tn+fp)
    FalsosNegativos = fn/(fn+tp)
    Error = 1-precision
    AcertividadPositiva = tp/(fp+tp)
    if tn + fn == 0:
        AcertividadNegativa = 0 # or 1, depending on your preference
    else:
        AcertividadNegativa = tn / (tn + fn)
    print('precision',precision)
    print('falsos positivos',FalsosPositivos)
    print('falsos negativos',FalsosNegativos)
    print('error',Error)
    print('acertividad positiva',AcertividadPositiva)
    print('acertividad negativa',AcertividadNegativa)


main_Redes()



