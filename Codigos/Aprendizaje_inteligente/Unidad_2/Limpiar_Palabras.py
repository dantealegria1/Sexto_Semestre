import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd

nltk.download('punkt')
nltk.download('stopwords')
global PROHIBIDAS
PROHIBIDAS = ["br"]

def leer(archivo):
    texto = pd.read_csv(archivo, sep=',')
    print(texto.head())

def texto_a_vector(texto):
    palabras = word_tokenize(texto)
    stopwords_ingles = set(stopwords.words('english'))
    palabras_filtradas = [palabra.lower() for palabra in palabras 
                          if palabra.isalpha() and palabra.lower() 
                          not in stopwords_ingles and palabra.lower() not in PROHIBIDAS]
    return palabras_filtradas


def procesar_texto(archivo):
    texto = pd.read_csv(archivo)
    #Solo leer la primer fila
    texto = texto.iloc[0,0]
    palabras = texto_a_vector(texto)
    print(palabras)


procesar_texto("Peliculas.csv")