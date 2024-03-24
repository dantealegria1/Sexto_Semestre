import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd

# Si lo corres por primera vez descomenta las siguientes líneas
nltk.download('punkt')
nltk.download('stopwords')

global PROHIBIDAS
PROHIBIDAS = ["br","movie"]
global ARCHIVO
ARCHIVO = "Peliculas.csv"

def leer_texto():
    texto = pd.read_csv(ARCHIVO)
    return texto

def probabilidad_sentimiento():
    texto = leer_texto()
    positivos = texto["sentiment"].value_counts()
    positivos = positivos[1]
    negativos = texto["sentiment"].value_counts()
    negativos = negativos[0]
    total = len(texto)
    probabilidad_positiva = positivos / total
    probabilidad_negativa = negativos / total
    return probabilidad_positiva, probabilidad_negativa

def texto_a_vector():
    texto = leer_texto()
    texto = texto.head(100)
    texto = texto.to_string()
    palabras = word_tokenize(texto)
    stopwords_ingles = set(stopwords.words('english'))
    palabras_filtradas = [palabra.lower() for palabra in palabras 
                        if palabra.isalpha() and palabra.lower() 
                        not in stopwords_ingles and palabra.lower() not in PROHIBIDAS
                        and palabra.lower()]
    palabras_filtradas = list(set(palabras_filtradas))
    return palabras_filtradas

def procesar_texto():
    palabras = texto_a_vector()
    return palabras

def Calculo_Probabilidad(palabra, palabras):
    Probabilidad_Palabra = palabras.count(palabra) / len(palabras)
    print("Probabilidad de la palabra:", palabra, "es:", Probabilidad_Palabra)
    return Probabilidad_Palabra

def main():
    palabras = procesar_texto()
    print(palabras)
    print(probabilidad_sentimiento())

if __name__ == "__main__":
    main()
