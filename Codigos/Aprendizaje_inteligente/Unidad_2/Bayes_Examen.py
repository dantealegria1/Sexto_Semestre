import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

# Descargar datos necesarios para nltk
#nltk.download('punkt')
#nltk.download('stopwords')

global PROHIBIDAS
PROHIBIDAS = [""]
global ARCHIVO
ARCHIVO = "comments.csv"
global DATASET
DATASET = pd.read_csv(ARCHIVO)

def Probabilidades_Iniciales(dataset):
    Numero_Reviews_Positivas = 0
    Numero_Reviews_Negativas = 0
    for i in range(len(dataset)):
        if dataset["comment"].iloc[i] != "":
            if dataset["rating"].iloc[i] == 1:
                Numero_Reviews_Positivas += 1
            if dataset["rating"].iloc[i] == 0:
                Numero_Reviews_Negativas += 1
    Probabilaidad_Negativa = Numero_Reviews_Negativas/len(dataset)
    Probabilidad_Positiva = Numero_Reviews_Positivas/len(dataset)
    return Probabilaidad_Negativa, Probabilidad_Positiva

#Funcion para obtener las palabras de las reviews positivas y negativas
def Vectores_Palabras(dataset):
    Palabras_Positivas = []
    Palabras_Negativas = []
    Largo = len(dataset)
    for i in range(Largo):
        if dataset["comment"].iloc[i] != "": 
            if dataset["rating"].iloc[i] == 1 : 
                Palabras_Positivas.append(dataset["comment"].iloc[i])
            if dataset["rating"].iloc[i] == 0: 
                Palabras_Negativas.append(dataset["comment"].iloc[i])
    return Palabras_Positivas, Palabras_Negativas

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

#Funcion para Obtener la probabilidad de una palabra en una review
def Probabilidad_Palabra(Palabra, Review):
    Probabilidad_Palabra = (Review.count(Palabra)+1) / len(Review)
    return Probabilidad_Palabra

#Funcion para obtener la frecuencia de las palabras en las reviews
def Frecuencia_Palabras(Palabras):
    Frecuencia = Counter(Palabras)
    print(Frecuencia.most_common(10))
    return Frecuencia

#Funcion para obtener la probabilidad de que una review sea positiva o negativa
def Naive_Bayes(Review, Palabras):
    Probabilidad = 1
    Probabilidades = []
    # Ensure Review is a string
    if not isinstance(Review, str):
        Review = str(Review)
    Review_Filtrada = Filtar_Palabras([Review])
    Review_Token = word_tokenize(Review)
    for Palabra in Review_Token:
        if Palabra not in Palabras:
            Probabilidad = Probabilidad * 1.
        else:
            Probabilidad = Probabilidad + Probabilidad_Palabra(Palabra, Palabras)
    return Probabilidad



#Funcion para hacer pruebas
def Pruebas(Palabras_Positivas, Palabras_Negativas,Review_Prueba,dataset):
    Probabilidad_Inicial_Negativa, Probabilidad_Inicial_Positiva = Probabilidades_Iniciales(dataset)
    Probabilidad_De_Ser_Positiva = Naive_Bayes(Review_Prueba, Palabras_Positivas)
    Probabilidad_De_Ser_Positiva *= Probabilidad_Inicial_Positiva
    Probabilidad_De_Ser_Negativa = Naive_Bayes(Review_Prueba, Palabras_Negativas)
    Probabilidad_De_Ser_Negativa *= Probabilidad_Inicial_Negativa
    Resultado = 0
    if Probabilidad_De_Ser_Positiva > Probabilidad_De_Ser_Negativa:
        Resultado = 1
    if Probabilidad_De_Ser_Positiva and Probabilidad_De_Ser_Negativa == 0:
        Resultado = -1
    if Resultado == 0:
        print(Probabilidad_De_Ser_Negativa, Probabilidad_De_Ser_Positiva)
    return Resultado

def Matriz_Confusion(dataset, Palabras_Positivas, Palabras_Negativas):
    y_true = []
    y_pred = []
    for i in range(len(dataset)):
        if dataset["comment"].iloc[i] != "":
            if dataset["rating"].iloc[i] == 1:
                y_true.append(1)
            if dataset["rating"].iloc[i] == 0:
                y_true.append(0)
    for i in range(len(dataset)):
        if Pruebas(Palabras_Positivas, Palabras_Negativas, dataset["comment"].iloc[i],dataset) == 1:
            y_pred.append(1)
        if Pruebas(Palabras_Positivas, Palabras_Negativas, dataset["comment"].iloc[i],dataset) == 0:
            y_pred.append(0)
            print("Comentario")
            print(dataset["comment"].iloc[i] + "\n")
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    Presicion = (tn+tp)/(tn+fp+fn+tp)
    FalsosPositivos = fp/(tn+fp)
    FalsosNegativos = fn/(fn+tp)
    Error = 1-Presicion
    AcertividadPositiva = tp/(fp+tp)
    if tn + fn == 0:
        AcertividadNegativa = 0 # or 1, depending on your preference
    else:
        AcertividadNegativa = tn / (tn + fn)

    return Presicion, FalsosPositivos, FalsosNegativos, Error, AcertividadPositiva, AcertividadNegativa

def main():
    # Dividir el conjunto de datos en entrenamiento y prueba (70% entrenamiento, 30% prueba)
    df_train, df_test = train_test_split(DATASET, test_size=0.2, random_state=0)
    #print(df_test.head(100))
    #print(df_train.head(100))

    # Obtener palabras de los conjuntos de entrenamiento y prueba
    Palabras_Positivas_train, Palabras_Negativas_train = Vectores_Palabras(df_train)
    #Palabras_Positivas_test, Palabras_Negativas_test = Vectores_Palabras(df_test)

    # Filtrar palabras
    Palabras_Positivas_train = Filtar_Palabras(Palabras_Positivas_train)
    Palabras_Negativas_train = Filtar_Palabras(Palabras_Negativas_train)

    #print('Cantidad de palabras positivas en el conjunto de entrenamiento:', len(Palabras_Positivas_train))
    #print('Cantidad de palabras negativas en el conjunto de entrenamiento:', len(Palabras_Negativas_train))
    #print('Cantidad de palabras positivas en el conjunto de prueba:', len(Palabras_Positivas_test))
    #print('Cantidad de palabras negativas en el conjunto de prueba:', len(Palabras_Negativas_test))

    #print("Frecuencia de las palabras positivas y negativas en el conjunto de entrenamiento :)")
    Frecuencia_Palabras(Palabras_Positivas_train)
    Frecuencia_Palabras(Palabras_Negativas_train)
    print()

    print("Precision Global, Falsos Positivos, Falsos Negativos, Error Global, Acertividad Positiva, Acertividad Negativa\n")
    print(Matriz_Confusion(df_test, Palabras_Positivas_train, Palabras_Negativas_train))

if __name__ == "__main__":
    main()
