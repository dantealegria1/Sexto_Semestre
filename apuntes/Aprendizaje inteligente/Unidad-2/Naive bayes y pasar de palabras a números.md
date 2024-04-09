
#### Filtrar palabras

Para crear las probabilidades, se utilizo una técnica donde se calculan las probabilidades de aparecer de las palabras de la review que entre y nuestro banco de palabras filtradas. Contando las veces que aparece esa palabra + 1 una oración extra en caso de que no aparezca ninguna vez, Sobre la cantidad total de palabras 

$$\text{P(palabra)}=\frac{\text{Cantidad de veces que aparece la palabra} + 1}{\text{Total de palabras}}$$
#### Bayes 

La idea fundamental del algoritmo de Naive Bayes es calcular la probabilidad de que una instancia pertenezca a una clase particular basada en la evidencia proporcionada por sus características. En el caso de un clasificador de texto, las características son las palabras en el texto y las clases son las categorías a las que puede pertenecer el texto, por ejemplo, si una revisión es positiva o negativa.
$$\text{P(Review sea positiva)} = \frac{\text{Cantidad de reviews positivas}}{\text{Total de reviews}}$$
Esta fórmula calcula la probabilidad de que una revisión sea positiva. Para calcular esta probabilidad, simplemente se cuenta el número de revisiones que son positivas y se divide por el total de revisiones disponibles.
$$\text{Probabilidad Positiva} = P(\text{Revisión sea positiva}) \times \sum_{i=1}^{n} P(\text{Palabra sea Positiva}_i)$$
Esta fórmula calcula la probabilidad de que una revisión sea positiva utilizando las probabilidades condicionales de cada palabra en la revisión. Primero, se multiplica la probabilidad a priori de que una revisión sea positiva por el producto de las probabilidades condicionales de cada palabra en la revisión (dadas las revisiones positivas).

Se sigue un proceso similar para calcular la probabilidad de que una revisión sea negativa, utilizando las probabilidades condicionales de cada palabra en la revisión (dadas las revisiones negativas). Finalmente, el modelo selecciona la clase con la probabilidad más alta como la predicción final para la revisión.