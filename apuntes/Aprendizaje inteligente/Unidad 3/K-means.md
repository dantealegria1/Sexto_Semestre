### Clustering

- Se utilizan para agrupar datos existentes de los que desconocemos sus características en común o queremos descubrirlas.  Estos métodos intentan crear “puntos centrales” y jerarquías para diferenciar grupos y descubrir características comunes por cercanía.
## k means

- Es un algoritmo no supervisado de clustering. El objetivo es el de encontrar “k” grupos entre los datos crudos.
#### Como funciona

-  El algoritmo trabaja iterativamente para asignar a cada “punto” (las filas de nuestro conjunto de entrada forman una coordenada) uno de los “K” grupos basado en sus características. Son agrupados en base a la similitud de sus features (las columnas). Como resultado de ejecutar el algoritmo tendremos:

- Los “centroids” de cada grupo que serán unas “coordenadas” de cada uno de los K conjuntos que se utilizarán para poder etiquetar nuevas muestras.
- Etiquetas para el conjunto de datos de entrenamiento. Cada etiqueta perteneciente a uno de los K grupos formados.

- Los grupos se van definiendo de manera “orgánica”, es decir que se va ajustando su posición en cada iteración del proceso, hasta que converge el algoritmo. Una vez hallados los centroids deberemos analizarlos para ver cuales son sus características únicas, frente a la de los otros grupos. Estos grupos son las etiquetas que genera el algoritmo.
#### Datos de entrada

- Las “features” o características que utilizaremos como entradas para aplicar el algoritmo k-means deberán ser de valores numéricos, continuos en lo posible. En caso de valores categóricos (por ej. Hombre/Mujer o Ciencia Ficción, Terror, Novela,etc) se puede intentar pasarlo a valor numérico, pero no es recomendable pues no hay una “distancia real” -como en el caso de géneros de película o libros 

- Además es recomendable que los valores utilizados estén normalizados, manteniendo una misma escala. En algunos casos también funcionan mejor datos porcentuales en vez de absolutos. No conviene utilizar features que estén correlacionados o que sean escalares de otros
#### Algoritmo 

- El algoritmo utiliza una proceso iterativo en el que se van ajustando los grupos para producir el resultado final. Para ejecutar el algoritmo deberemos pasar como entrada el conjunto de datos y un valor de K. El conjunto de datos serán las características o features para cada punto. Las posiciones iniciales de los K centroids serán asignadas de manera aleatoria de cualquier punto del conjunto de datos de entrada. Luego se itera en dos pasos
	1.  Asignación de datos
		- Cada fila de nuestro conjunto de datos se asigna al centroide más cercano  basado en la distancia cuadrada euclideana
	2. Actualización de centroid
		- en este paso el centoid de cada grupo son re calculados. Esto se hace tomando una media de todos los puntos asignados en el also anterior 
	
- Este proceso acaba cuando: 
	- No hay cambios en los miembros de cada grupo 
	- Si la suma de las distancias se minimiza
	- Se alcanza el número maximo de iteraciones

#### Elegir valor de k 

- Este algoritmo funciona pre-seleccionando un valor de K. Para encontrar el número de clusters en los datos, deberemos ejecutar el algoritmo para un rango de valores K, ver los resultados y comparar características de los grupos obtenidos. En general no hay un modo exacto de determinar el valor K, pero se puede estimar con aceptable precisión siguiendo la siguiente técnica:

- Una de las métricas usada para comparar resultados es la **distancia media entre los puntos de datos y su centroid**. Como el valor de la media diminuirá a medida de aumentemos el valor de K, deberemos utilizar la distancia media al centroide en función de K y entontrar el “punto codo”, donde la tasa de descenso se “afila”. Aquí vemos una gráfica a modo de ejemplo:

![](https://www.aprendemachinelearning.com/wp-content/uploads/2018/03/ejemplo-elbow.png)
#### Información
https://www.aprendemachinelearning.com/k-means-en-python-paso-a-paso/