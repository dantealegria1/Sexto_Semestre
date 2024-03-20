1. Problema del viajante de comercio (TSP)
2. Problema de la mochila (Knapsack problem)
3. Problema de la partición (Partition problem)
4. Problema de la suma de subconjuntos (Subset sum problem)
5. Problema del corte mínimo (Minimum cut problem)
6. Problema del emparejamiento estable (Stable matching problem)
7. Problema de la cobertura de vértices (Vertex cover problem)
8. Problema de la coloración de grafos (Graph coloring problem)
9. Problema del conjunto independiente (Independent set problem)
10. Problema del conjunto dominante (Dominating set problem)
11. Problema del ciclo hamiltoniano (Hamiltonian cycle problem)
12. Problema del conjunto de cobertura (Set cover problem)
13. Problema de la ruta más corta en un grafo acíclico dirigido (Shortest path problem in a directed acyclic graph)
14. Problema del conjunto k-dominante (k-Dominating set problem)
15. Problema de la satisfacción de restricciones (Constraint satisfaction problem)

## Problema de la mochila 

### Definición 

Uno de los problemas más estudiados es el problema de la Mochila que es conocido como un Problema de Optimización Combinatoria de tipo NP-hard. Este problema es una generalización de los problemas donde se tiene un contenedor (mochila) con o sin restricciones, y donde la solución base es mediante la programación entera dicotómica.

El problema de la mochila (KP) puede ser definido con un conjunto de n artículos donde cada artículo es identificado por nx, con un valor entero px, y un peso wx. *El problema consiste en elegir un subconjunto de n artículos maximizando el beneficio obtenido considerando el peso total de los artículos seleccionados, sin exceder la capacidad c de la mochila*
$$maximizar \sum^{n}_{j=1}p_{j}x_{j}$$ $$sujeto \sum^{n}_{j=1}w_{j}x_{j} \leq c$$
$$x_{j}\in[0,1], j = 1\dots n$$
Donde:
$x_{}j$ -> Variables de decisión

$w_j$ -> Peso w del ítems j

$c$ -> Capacidad total del contenedor (mochila)

$n$ -> número de ítems

Este problema se puede aplicar como una forma de emular situaciones reales donde es necesario acomodar artículos de diferentes dimensiones en un espacio reducido

### Soluciones Propuestas

Para la solución del Problema de la Mochila, Fernández y Velázquez, proponen la técnica de programación dinámica, empleando cuatro tipos de visualización: árbol de recursión, grafo de dependencia, tabla de valores y tabla de decisiones.

Almeida, Giménez y López, mencionan que la experimentación es un factor clave cuando se requiere ajustar una metaheurísticas a un problema; en este caso, proponen, para la solución del Problema de la mochila, el uso de metaheurísticas parametrizadas, mediante la combinación de parámetros.

### Bibliografía 

Del Estado de Hidalgo, U. A. (s. f.). _Boletín Científico :: UAEH_. https://www.uaeh.edu.mx/scige/boletin/tlahuelilpan/n6/e2.html

## Problema de suma de subconjuntos 

### Definición

  
El problema de la suma de subconjuntos es un problema clásico en teoría de la computación y combinatoria. La pregunta básica es la siguiente: *Dado un conjunto de números enteros positivos (o no negativos), ¿existe algún subconjunto cuya suma sea igual a un número específico dado?*

Formalmente, el problema se define de la siguiente manera:

Dado un conjunto de números enteros positivos $S = [{a_{1},a_{2}\dots a_{n}}]$ 
y un número entero positivo $t$, ¿existe algún subconjunto $T \subseteq S$ tal que la suma de los elementos en $T$ sea igual a $t$?

El problema de la suma de subconjuntos tiene numerosas aplicaciones en áreas como criptografía, optimización, análisis de datos y diseño de algoritmos. Por ejemplo, se puede usar en criptografía para atacar esquemas de cifrado o para resolver problemas de optimización en la asignación de recursos.

### Soluciones propuestas 

Przydatek propone el RGLI(t) (Random Greedy con mejoramiento local–Local Improvement-) Por cada trial obtiene una solución (por ej. al azar); consideramos cada $a_{i}$ de esa solución y vemos sipodemos reemplazarlo por otro $a_{j}$ que no esté pero que haga la nueva suma más cercana a s (sinsuperarlo). 

Przydatek se refiere a esto último como el heurístico de Balas y Zemel. Se elige la mejor solución de todos los trials

### Bibliografía

Nj, T. G. (s. f.). _El subset Sum problem_. Scribd. https://es.scribd.com/document/365684561/El-Subset-Sum-Problem

## Problema del conjunto cobertura

### Definicion 

El Problema del Conjunto de Cobertura, también conocido como Set Cover Problem en inglés, es un problema de optimización combinatoria que consiste en encontrar la manera más eficiente de cubrir un conjunto de elementos con el menor número posible de subconjuntos de un conjunto dado.

Dado un conjunto finito U (llamado universo) y una colección de subconjuntos $S={S_{1​},S_{2}​,...,Sm​}$, donde cada ��Si​ es un subconjunto de U, el objetivo es encontrar el menor número posible de subconjuntos $S_{i}$​ cuya unión es igual al conjunto U.

En otras palabras, queremos seleccionar un subconjunto mínimo de S de tal manera que cada elemento en �U esté contenido en al menos uno de los subconjuntos seleccionados.

### bibliografia

colaboradores de Wikipedia. (2023, 27 septiembre). _Problema del conjunto de cobertura_. Wikipedia, la Enciclopedia Libre. https://es.wikipedia.org/wiki/Problema_del_conjunto_de_cobertura#:~:text=El%20problema%20del%20Set%20Covering,de%20los%20algoritmos%20de%20aproximaci%C3%B3n. 