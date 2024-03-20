import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import pandas as pd

nltk.download('punkt')
nltk.download('stopwords')

def leer (archivo):
    texto = pd.read_csv(archivo, sep='"')
    print(texto.head())

def texto_a_vector(texto):
    palabras = word_tokenize(texto)
    stopwords_ingles = set(stopwords.words('english'))
    palabras_filtradas = [palabra.lower() for palabra in palabras 
                        if palabra.isalnum() and palabra.lower() not in 
                        stopwords_ingles]
    return palabras_filtradas


leer("Peliculas.csv")