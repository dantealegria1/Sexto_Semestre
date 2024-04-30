
### Problema de la mochila

- En una mochila con capacidad de C = 11 se desea guardar los objetos mas valiosos para sobrevivir en la selva, se tiene la siguiente informacion

|  Objeto  | Valor | Capacidad |
| :------: | :---: | :-------: |
| linterna |   8   |     2     |
| Garrafon |  12   |     6     |
|  Hamaca  |   6   |     5     |
| cuchillo |  10   |     1     |
![[Pasted image 20240408114321.png]]

### Problema clique maximo

![[Pasted image 20240408114007.png]]

- Dado un grafo G=(N,A), se dice que G tiene un [clique](https://es.wikipedia.org/wiki/Clique "Clique") de tamaño k si existe un subgrafo G' = (N',A') de G tal que N' es subconjunto de N, |N'|=k y A'=N'×N', vale decir, todos sus vértices están conectados entre ellos.

- El problema del clique es un problema de decisión para determinar cuando un grafo contiene un clique al menos un tamaño k 

- Una vez que tenemos k o más vértices que forman un clique, es trivial verificar que lo son, por eso es un problema NP. El correspondiente problema de optimización, consiste en encontrar un clique de tamaño máximo en un grafo (un subgrafo completo de tamaño máximo). Este problema se puede enunciar como un problema de decisión si la pregunta que se hace es saber si existe un clique de tamaño k en el grafo

- Un ejemplo de algoritmo de [búsqueda de fuerza bruta](https://es.wikipedia.org/wiki/B%C3%BAsqueda_de_fuerza_bruta "Búsqueda de fuerza bruta") para encontrar un clique en un grafo consiste en listar todos los subconjuntos de vértices _V_ y verificar para cada uno de ellos si forma una clique. Ese algoritmo es polinomio si _k_ es una constante pero no lo es cuando se hace depender a _k_ de, por ejemplo, |_V_|/2.

