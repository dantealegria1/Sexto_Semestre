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
global INITAL_GUESS_POSITIVA
INITAL_GUESS_POSITIVA  = 0.8847474
global INITAL_GUESS_NEGATIVA
INITAL_GUESS_NEGATIVA = 0.1152526

Review_Prueba = "Excelente producto, de la mejor calidad, la pantalla es amoled, funciona bastante bien, las cámaras tienen una excelente definición, me deja satisfecho. 👌🏻😎."

#Funcion para obtener los indices de las reviews positivas y negativas
def Obtener_Indices():
    Indices_Positivos = []
    Indices_Negativos = []
    for i in range(len(DATASET)):
        if DATASET["rating"][i] == 1:
            Indices_Positivos.append(i)
        else:
            Indices_Negativos.append(i)
    return Indices_Positivos, Indices_Negativos

#Funcion para obtener las palabras de las reviews positivas y negativas
def Vectores_Palabras(dataset):
    Indices_Positivos, Indices_Negativos = Obtener_Indices()
    Palabras_Positivas = []
    Palabras_Negativas = []
    Largo = len(dataset)
    for i in range(Largo):
        if i in Indices_Positivos:
            Palabras_Positivas.append(DATASET["comment"][i])
        else: 
            Palabras_Negativas.append(DATASET["comment"][i])
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
    Review_Filtrada = Filtar_Palabras([Review])
    for Palabra in Review_Filtrada:
        Probabilidad_Individual = Probabilidad_Palabra(Palabra, Palabras)
        Probabilidades.append(Probabilidad_Individual)
        Probabilidad *= Probabilidad_Individual
    #print(Probabilidades)
    return Probabilidad

#Funcion para hacer pruebas
def Pruebas(Palabras_Positivas, Palabras_Negativas,Review_Prueba):
    Probabilidad_De_Ser_Positiva = Naive_Bayes(Review_Prueba, Palabras_Positivas)
    Probabilidad_De_Ser_Positiva *= INITAL_GUESS_POSITIVA
    Probabilidad_De_Ser_Negativa = Naive_Bayes(Review_Prueba, Palabras_Negativas)
    Probabilidad_De_Ser_Negativa *= INITAL_GUESS_NEGATIVA
    Resultado = 0
    if Probabilidad_De_Ser_Positiva > Probabilidad_De_Ser_Negativa:
        Resultado = 1
    return Resultado

def Matriz_Confusion(dataset, Palabras_Positivas, Palabras_Negativas):
    y_true = []
    y_pred = []
    for i in range(len(dataset)):
        if dataset["rating"].iloc[i] == 1:  # Accede a la columna "rating" usando iloc
            y_true.append(1)
        else:
            y_true.append(0)
    for i in range(len(dataset)):
        if Pruebas(Palabras_Positivas, Palabras_Negativas, dataset["comment"].iloc[i]) == 1:
            y_pred.append(1)
        else:
            y_pred.append(0)
            #print("-",dataset["comment"].iloc[i])
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
    Presicion = (tn+tp)/(tn+fp+fn+tp)
    FalsosPositivos = fp/(tn+fp)
    FalsosNegativos = fn/(fn+tp)
    Error = 1-Presicion
    AcertividadPositiva = tp/(fp+tp)
    AcertividadNegativa = tn/(tn+fn)
    return Presicion, FalsosPositivos, FalsosNegativos, Error, AcertividadPositiva, AcertividadNegativa

def main():
    # Dividir el conjunto de datos en entrenamiento y prueba (70% entrenamiento, 30% prueba)
    df_train, df_test = train_test_split(DATASET, test_size=0.3, random_state=42)
    #print(df_test.head(100))
    #print(df_train.head(100))

    # Obtener palabras de los conjuntos de entrenamiento y prueba
    Palabras_Positivas_train, Palabras_Negativas_train = Vectores_Palabras(df_train)
    #Palabras_Positivas_test, Palabras_Negativas_test = Vectores_Palabras(df_test)

    # Filtrar palabras
    Palabras_Positivas_train = Filtar_Palabras(Palabras_Positivas_train)
    Palabras_Negativas_train = Filtar_Palabras(Palabras_Negativas_train)
    #Palabras_Positivas_test = Filtar_Palabras(Palabras_Positivas_test)
    #Palabras_Negativas_test = Filtar_Palabras(Palabras_Negativas_test)

    #print('Cantidad de palabras positivas en el conjunto de entrenamiento:', len(Palabras_Positivas_train))
    #print('Cantidad de palabras negativas en el conjunto de entrenamiento:', len(Palabras_Negativas_train))
    #print('Cantidad de palabras positivas en el conjunto de prueba:', len(Palabras_Positivas_test))
    #print('Cantidad de palabras negativas en el conjunto de prueba:', len(Palabras_Negativas_test))

    #print("Frecuencia de las palabras positivas y negativas en el conjunto de entrenamiento :)")
    #Frecuencia_Palabras(Palabras_Positivas_train)
    #Frecuencia_Palabras(Palabras_Negativas_train)
    print()

    print("Precision Global, Falsos Positivos, Falsos Negativos, Error Global, Acertividad Positiva, Acertividad Negativa\n")
    print(Matriz_Confusion(df_test, Palabras_Positivas_train, Palabras_Negativas_train))

if __name__ == "__main__":
    main()
