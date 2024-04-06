import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd

nltk.download('punkt')
nltk.download('stopwords')

global PROHIBIDAS
PROHIBIDAS = ["hola"]
global ARCHIVO
ARCHIVO = "comments.csv"

df = pd.read_csv(ARCHIVO)
print(df.head())

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(data=df,x='comment',hue='rating')
plt.xticks(rotation=45, ha='right');

pre_df = pd.get_dummies(df,columns=['comment'],drop_first=True)
pre_df.head()

from sklearn.model_selection import train_test_split

X = pre_df.drop('rating', axis=1)
y = pre_df['rating']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=125
)

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

model.fit(X_train, y_train);

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    classification_report,
)

y_pred = model.predict(X_test)

accuray = accuracy_score(y_pred, y_test)
f1 = f1_score(y_pred, y_test, average="weighted")

print("Accuracy:", accuray)
print("F1 Score:", f1)

labels = ["Positivo", "Nehativo"]
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
disp.plot();