import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

Texto = pd.read_csv("Peliculas.csv")

Mensos = pd.get_dummies(Texto, columns=["sentiment"], drop_first=True)
