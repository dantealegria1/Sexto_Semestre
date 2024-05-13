### Introducción
El Problema del Agente Viajero (TSP, por sus siglas en inglés) es uno de los problemas de optimización más estudiados en la ciencia de la computación. 

El problema consiste en encontrar la ruta más corta para un vendedor que visite una lista de ciudades exactamente una vez y regrese a la ciudad de origen. Normalmente, se representa el esquema de ciudades como un grafo completo, donde cada arista tiene un peso asociado que representa la distancia entre ciudades. El TSP se relaciona con los ciclos hamiltonianos, que son caminos cíclicos en grafos que pasan por cada nodo una única vez y tienen el mismo punto de llegada y salida. A pesar de ser un problema estudiado, encontrar la solución óptima para el TSP en grafos grandes puede ser muy costoso en términos de tiempo y recursos computacionales. 

El TSP pertenece a la clase NP, lo que significa que es un problema cuya complejidad es muy alta y se requiere mucho tiempo y muchos pasos para encontrar la solución correcta.

### Planteamiento del problema
Nuestro problema elegido se centra en el recorrido que debe realizar un repartidor alrededor de la ciudad de Aguascalientes, partiendo desde su centro de distribución y visitando siete casas para entregar pedidos. El objetivo es encontrar la ruta más corta que permita al repartidor visitar cada casa exactamente una vez y luego regresar al centro de distribución, minimizando así la distancia total recorrida y optimizando la eficiencia del reparto.

Este escenario es un ejemplo clásico del Problema del Viajante (TSP), que tiene aplicaciones prácticas en la gestión logística y la planificación de rutas. En este contexto, resolver el TSP para el repartidor en Aguascalientes permitirá optimizar la distribución de pedidos, reducir los costos operativos y mejorar la puntualidad de las entregas.

Para abordar este problema, exploraremos diferentes enfoques algorítmicos. Evaluaremos la eficacia y la eficiencia de cada enfoque en función del tamaño del conjunto de datos y los recursos computacionales disponibles, con el objetivo final de encontrar una solución óptima o aproximada que satisfaga las necesidades del repartidor y de la empresa de distribución.

Todo considerando distancia neta, no tomaremos en cuenta el flujo de trafico ni otros factores externos

![[Pasted image 20240511170856.png]]

### Algoritmo Fuerza Bruta
El algoritmo de fuerza bruta utilizado para resolver el Problema del Agente Viajero (TSP) tiene una complejidad de tiempo factorial, lo que significa que su tiempo de ejecución aumenta de manera exponencial con el número de ciudades a visitar. Veamos por qué:

1. **Generación de permutaciones:** En el algoritmo de fuerza bruta, se generan todas las posibles permutaciones de las ciudades a visitar. Para un conjunto de 𝑛n ciudades, el número total de permutaciones es 𝑛!n! (factorial de 𝑛n). Esto significa que se deben explorar todas estas permutaciones para encontrar la ruta más corta.
    
2. **Cálculo de la distancia:** Para cada permutación generada, se calcula la distancia total de la ruta. Esto implica sumar las distancias entre cada par de ciudades consecutivas en la permutación. En el peor de los casos, se deben realizar 𝑛n operaciones de suma para una permutación de 𝑛n ciudades.
    

Por lo tanto, el tiempo total de ejecución del algoritmo de fuerza bruta es proporcional al producto del número de permutaciones (𝑛!n!) y el tiempo necesario para calcular la distancia para cada permutación (𝑂(𝑛)O(n)). En resumen, la complejidad de tiempo del algoritmo de fuerza bruta para el TSP es 𝑂(𝑛⋅𝑛!)O(n⋅n!), lo que lo hace prohibitivamente lento para un número grande de ciudades debido al crecimiento factorial del número de permutaciones

#### Solución dada
![[Pasted image 20240511170728.png]]


Camino más corto encontrado: ['Centro de Distribución', 'Casa 1', 'Casa 3', 'Casa 5', 'Casa 6', 'Casa 4', 'Casa 7', 'Casa 2', 'Centro de Distribución']
Distancia del camino más corto: 0.36590335125091994

![[Pasted image 20240511171426.png]]