  

## Tarea: Aplicar la técnica de diseño de divide y vencerás a los siguientes problemas

Aplique la técnica de diseño de divide y vencerás a los siguientes problemas:  

Piense primero cómo va será el conjunto de elementos de la solución que va a poner al inicio de manera que contemple las características del problema, luego divida ese conjunto en subconjuntos más pequeños hasta que no pueda dividirlo más. Entonces viene la parte de la "conquista", donde debe encontrar la solución para los problemas más pequeños del problema a resolver y lograr la composición de la solución que dará el algoritmo así diseñado al problema original.

### a) Problema del Clique Máximo.

1. **Dividir**:
    
    - Inicialmente, consideramos todos los vértices del grafo como un conjunto.
    - Dividimos este conjunto en dos subconjuntos de manera recursiva, hasta que tengamos conjuntos individuales de vértices.
2. **Conquistar**:
    
    - Para cada conjunto de vértices, verificamos si forman un clique. Esto se puede hacer comprobando si cada par de vértices en el conjunto está conectado por una arista.
    - Si un conjunto forma un clique, lo consideramos como una solución parcial.
3. **Combinar**:
    
    - Combinamos las soluciones parciales encontradas en la etapa de conquista para obtener el clique máximo global.

### b) Problema del camino más corto entre dos vértices de un grafo pesado. 
Sugerencia: fije los dos vértices dados por dato, por ejemplo, me dicen que el grafo tiene 8 vértices y que el camino más corto que debo encontrar es entre el vértice 3 y 6. Entonces pongo la primera solución como, 3, v1, v2, v3, v4, v5, v6, 6 (pongo los 8 vértices del grafo porque no sé en realidad con cuántos vértices voy a poder hacer el camino más corto entre 3 y 6, puede que necesite los 6 vértices restantes o menos). Este conjunto de vértices se divide a la mitad y así sucesivamente en el paso de "dividir". Luego viene la fase de resolver los problemas de forma recursiva en la fase de "conquista" o fase de "vencer" y finalmente la composición de la solución del problema original.

1. **Dividir**:
    
    - Tomamos el grafo completo y consideramos todos los caminos posibles entre los dos vértices dados.
    - Dividimos este conjunto de caminos en subconjuntos más pequeños de manera recursiva.
2. **Conquistar**:
    
    - Para cada subconjunto de caminos, calculamos la longitud de cada camino.
3. **Combinar**:
    
    - Seleccionamos el camino más corto entre todas las soluciones encontradas en la etapa de conquista.

c) Problema del coloreo de grafos.

1. **Dividir**:
    
    - Dividimos el grafo en subgrafos más pequeños, cada uno de los cuales tiene menos vértices que el grafo original.
    - Esto se puede hacer dividiendo el grafo en subconjuntos de vértices de manera recursiva.
2. **Conquistar**:
    
    - Para cada subgrafo, encontramos una solución de coloreo utilizando un algoritmo de coloreo conocido (como el algoritmo de coloreo greedy).
    - Verificamos si es posible colorear el subgrafo sin que haya conflictos de color entre los vértices.
3. **Combinar**:
    
    - Combinamos las soluciones de coloreo de cada subgrafo para obtener una solución de coloreo para el grafo original.