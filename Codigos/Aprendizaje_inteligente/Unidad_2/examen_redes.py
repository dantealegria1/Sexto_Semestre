import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
import uuid
import csv

# Descargar datos necesarios para nltk
nltk.download('punkt')
nltk.download('stopwords')

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

print(DATASET.shape)
print(DATASET.head())
#ahora haremos que si comment esta vacio lo rempace por dos casos: 1. 

#Funcion para obtener las palabras de las reviews positivas y negativas
def Vectores_Palabras(dataset):
    Indices_Positivos, Indices_Negativos = Obtener_Indices()
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

#Funcion para Obtener la probabilidad de una palabra en una review
def Probabilidad_Palabra(Palabra, Review):
    if Review == "":
        return 0
    Probabilidad_Palabra = (Review.count(Palabra)+1) / len(Review)
    return Probabilidad_Palabra

#Funcion para obtener la frecuencia de las palabras en las reviews
def Frecuencia_Palabras(Palabras):
    Frecuencia = Counter(Palabras)
    print(Frecuencia.most_common(10))
    return Frecuencia

#ahora vamos a limpiar las filas  en la columna comment
def filtrar_palabra_commment(review):
    if isinstance(review, str):  # Check if the element is a string
        tokens = word_tokenize(review)
        stopwords_ingles = set(stopwords.words('spanish'))
        return ' '.join([token.lower() for token in tokens
                         if token.isalpha() and token.lower()
                         not in stopwords_ingles and token.lower() not in PROHIBIDAS])
    return review

# y maneja los valores NaN reemplazándolos con una cadena vacía
DATASET['comment'] = DATASET['comment'].fillna('').apply(str)

    #comment es 'muy buen producto excelente' lo metemos a la funcion de probabilidad
    #reemplazamos la review por la probabilidad de cada palabra
def cambio_palabra_por_probabilidad(review,palabras):
    tokens = word_tokenize(review)
    probabilidades = [Probabilidad_Palabra(token.lower(), palabras) for token in tokens]
    return ','.join([str(prob) for prob in probabilidades])

# Apply the filtrar_palabra_commment function to the 'comment' column
DATASET['comment'] = DATASET['comment'].apply(filtrar_palabra_commment)


def crear_csv_modificado(DATASET_MODIFICADO, DATASET, palabras):
    DATASET.reset_index(drop=True, inplace=True)
    DATASET_MODIFICADO.reset_index(drop=True, inplace=True)

    DATASET_MODIFICADO.update(DATASET[['rating']])
    # Correctly apply cambio_palabra_por_probabilidad with both review and palabras
    DATASET_MODIFICADO['comment'] = DATASET['comment'].apply(lambda review: cambio_palabra_por_probabilidad(review, palabras))
    DATASET_MODIFICADO.reset_index(drop=True, inplace=True)

    nombre_archivo = 'dataset_modificado.csv'
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['rating', 'comment']
        writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction='ignore')

        writer.writeheader()
        for index, row in DATASET_MODIFICADO.iterrows():
            writer.writerow(row.to_dict())

    print(f"Archivo CSV creado con comentarios procesados: {nombre_archivo}")

##comienzo con el código de redes 
#coloco el nuevo dataset
#datos=pd.read_csv('dataset_modificado.csv', delimiter=',')
#print(datos.shape)
#print(datos.head())
#eliminar variable categorica 
#X=datos.iloc[:,:1]
#print(X.head())
#variable categorica Y
#Y=datos.iloc[:,1:2]
#print(Y.head())
##se separa con el 70% de entrenamiento y 30% de prueba
#X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=0)
#se inicia la red
#instacia_red = MLPClassifier()
#print(instacia_red)
#entrenar el modelo 
#instacia_red.fit(X_train,Y_train)
def main():
    for i in range(len(DATASET)):
        if DATASET.loc[i, "comment"] == "":
            if DATASET.loc[i, "rating"] == 1:
                DATASET.loc[i, "comment"] = "bueno"
            if DATASET.loc[i, "rating"] == 0:
                DATASET.loc[i, "comment"] = "malo"
    Palabras = Vectores_Palabras(DATASET)
    Palabras = Filtar_Palabras(Palabras)

    #Palabras en nuestro banco de palabras
    #------------------------------------------------------------------------------
    #comment es 'muy buen producto excelente' lo metemos a la funcion de probabilidad
    #reemplazamos la review por la probabilidad de cada palabra


    #------------------------------------------------------------------------------
    #matriz = matriz_probabilidad(DATASET, Palabras_Positivas, Palabras_Negativas)
    #print("Matriz de probabilidad",matriz)
    # Añadir UUIDs a cada fila del DataFrame
    #DATASET['uuid'] = DATASET.apply(lambda x: uuid.uuid4(), axis=1)

    # Crear el archivo CSV
    crear_csv_modificado(DATASET, DATASET, Palabras)

if __name__ == "__main__":
    main()


