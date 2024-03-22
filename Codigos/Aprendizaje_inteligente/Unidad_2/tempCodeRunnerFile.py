import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Texto = pd.read_csv("Peliculas.csv")
print(Texto.info())

Mensos = pd.get_dummies(Texto, columns=["sentiment"], drop_first=True)
Mensos.head()