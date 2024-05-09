Unidad II. Clasificación de Problemas. 
Unidad III.- Algoritmo glotón y de fuerza bruta. 
En estas unidades lo relevante es: 

1.- Saber la relación entre los tres conjuntos de problemas, P, NP y NP- completos, para ello debe saber pintar el diagrama de Venn, donde se relacionan los conjuntos, Cual conjunto es subconjunto de otro, cuales conjuntos tienen intersección vacía. 

- NP-Completo y P son subconjuntos de los problemas P
- NP-Completo y P tienen intersección vacía

2.- Debe conocer y aplicar bien las definiciones de máquina de Turing determinística y no determinística, dibujar las máquinas señalando sus componentes, saber diferenciar una maquina determinística de una máquina no determinística. 

- Una maquina de turing Deterministica solo tiene un camino para tomar esta definido por el estado actual
- Una maquina de turing no deterministica tiene multiples caminos para tomar

3.- Saber qué problemas se resuelven con una maquina de Turing determinística y cual con una máquina de Turing no determinística. 

- Los Problemas P se resuelven con maquina de turing deterministica
- Los problemas NP con maquina de turing no deterministica

4.- Debe conocer los enunciados de los problemas NP- completos e interpretar su descripción. Los siguientes son problemas NP- completos que son de interés: 
	a) Problema del Viajante de Comercio es encontrar el recorrido cerrado con distancia total mínima. 
	b) Problema de la Mochila es encontrar aquel conjunto de objetos que se pongan en la mochila y que no sobrepase su capacidad y que además la suma total de sus valores de utilidad sea el máximo posible. 
	c) Problema del Clique Máximo es encontrar el subgrafo completo mas grande en número de vértices en un grafo dado. 
	d) Problema del cubrimiento de aristas por vértices es encontrar el subconjunto de vértices del grafo mas pequeño que cubre todas las aristas del grafo. 
	e) Problema del Pareo Perfecto Máximo (El cardinal del conjunto de vértices del grafo es un número par) es encontrar un conjunto de aristas tal que ningún par de ellas tengan vértices en común y que cubran a todos los vértices del grafo, siendo la suma total de los pesos de las aristas la mayor posible. 
	f) Problema del Coloreo de Grafos 

5.- Diseñar un algoritmo glotón y un algoritmo de fuerza bruta para dar una solución a los problemas anteriormente mencionados. Deben apoyarse en: escribir el algoritmo en pasos, o un pseudocódigo, utilizar un ejemplo (una instancia, una entrada, un juego de datos) para da

``` python

#Mochila 
mejor_combinacion = []
mejor_prioridad = 0 

for _ in range(max_iteraciones): 

	combinacion_actual = [] 
	peso_actual = 0 
	prioridad_actual = 0 
	for producto in lista_productos: 
	
		if random.randint(0, 1) == 1:
			if peso_actual + producto.peso <= peso_maximo: 
				combinacion_actual.append(producto) 
				peso_actual += producto.peso 
				prioridad_actual += producto.prioridad 
			
	if prioridad_actual > mejor_prioridad: 
		mejor_combinacion = combinacion_actual 
		mejor_prioridad = prioridad_actual 
			
return mejor_combinacion, mejor_prioridad
		
```
