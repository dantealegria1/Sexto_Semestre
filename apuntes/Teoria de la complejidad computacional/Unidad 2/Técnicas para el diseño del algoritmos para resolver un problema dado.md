
## Diseño de un algoritmo glotón

Diseñar el algoritmo glotón para el problema del viajante de comercio *En la iteración donde se encuentre el algoritmo decidir tomar la mejor pieza para encontrar la solución*

https://knuth.uca.es/moodle/mod/page/view.php?id=3417#:~:text=M%C3%A9todos%20de%20b%C3%BAsqueda%20local,criterio%20es%20conocido%20como%20greedy.

Inicio yendo a la ciudad que esta mas cerca 

El procedimiento de búsqueda o mejora local, comienza con una solución del problema y permite ir mejorando la solución actual mientras se pueda. El algoritmo se detiene cuando la solución no puede ser mejorada. A la solución encontrada se le denomina óptimo local. Este criterio es conocido como greedy.

El óptimo local alcanzado no puede mejorarse mediante el movimiento definido, pero esto no permite garantizar que sea el óptimo global del problema. Dada la miopía de la búsqueda local, es de esperar que en algunos problemas no lo sea. 

El problema del viajante de comercio (TSP, por sus siglas en inglés, Traveling Salesman Problem) es un problema combinatorio en el campo de la optimización. El objetivo es encontrar el recorrido más corto posible que visite cada ciudad exactamente una vez y regrese al punto de partida.

El algoritmo Greedy para el TSP sigue un enfoque "codicioso", es decir, en cada paso toma la decisión que parece ser la mejor en ese momento sin considerar las consecuencias a largo plazo. Aunque no garantiza la solución óptima, a menudo produce soluciones razonablemente buenas en un tiempo razonable.

Aquí está el esquema básico del algoritmo Greedy para el TSP:

1. **Inicialización**: Selecciona una ciudad inicial como punto de partida.
    
2. **Selección de la próxima ciudad**: En cada paso, selecciona la ciudad más cercana a la última ciudad visitada que aún no ha sido visitada.
    
3. **Actualización de la lista de ciudades visitadas**: Marca la ciudad seleccionada como visitada y actualiza la lista de ciudades restantes por visitar.
    
4. **Repetición**: Repite el paso 2 y 3 hasta que todas las ciudades hayan sido visitadas.
    
5. **Regreso al punto de partida**: Una vez que todas las ciudades han sido visitadas, regresa al punto de partida desde la última ciudad visitada.
    
6. **Cálculo de la distancia total**: Calcula la longitud total del recorrido obtenido.
    

El principal desafío del algoritmo Greedy para el TSP es que puede quedarse atrapado en óptimos locales, donde la solución encontrada no es necesariamente la mejor posible. Además, puede no encontrar la solución óptima para todos los casos de entrada.

Por lo tanto, aunque el algoritmo Greedy proporciona soluciones rápidas y simples, no garantiza la optimización global y puede ser necesario recurrir a algoritmos más avanzados para obtener soluciones óptimas en casos más complejos del problema del viajante de comercio.