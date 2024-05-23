El **algoritmo de Kruskal** es un [algoritmo](https://es.wikipedia.org/wiki/Algoritmo "Algoritmo") de la [teoría de grafos](https://es.wikipedia.org/wiki/Teor%C3%ADa_de_grafos "Teoría de grafos") para encontrar un [árbol recubridor mínimo](https://es.wikipedia.org/wiki/%C3%81rbol_recubridor_m%C3%ADnimo "Árbol recubridor mínimo") en un grafo conexo y ponderado. Es decir, busca un subconjunto de aristas que, formando un árbol, incluyen todos los vértices y donde el valor de la suma de todas las aristas del árbol es el mínimo.

## Descripción

El algoritmo de Kruskal es un ejemplo de [algoritmo voraz](https://es.wikipedia.org/wiki/Algoritmo_voraz "Algoritmo voraz") que funciona de la siguiente manera:

- se crea un bosque _B_ (un conjunto de árboles), donde cada vértice del grafo es un [árbol](https://es.wikipedia.org/wiki/%C3%81rbol_(teor%C3%ADa_de_grafos) "Árbol (teoría de grafos)") separado
- se crea un conjunto _C_ que contenga a todas las aristas del grafo
- mientras _C_ es _no vacío_
    - eliminar una arista de peso mínimo de _C_
    - si esa arista conecta dos árboles diferentes se añade al bosque, combinando los dos árboles en un solo árbol
    - en caso contrario, se desecha la arista

Al acabar el algoritmo, el bosque tiene un solo componente, el cual forma un árbol de expansión mínimo del grafo.

En un **árbol de expansión mínimo** se cumple:

- la cantidad de aristas del árbol es la cantidad de nodos menos uno

```
**función** Kruskal(G)
   **Para cada** v en V[G] **hacer**
     Nuevo conjunto C(v) ← {v}.
   Nuevo heap Q que contiene todas las aristas de G, ordenando por su peso
   Defino un árbol T ← Ø
   // n es el número total de vértices
   **Mientras** T tenga menos de n-1 aristas y !Q.vacío() **hacer**
     (u,v) ← Q.sacarMin()
     // previene ciclos en T. agrega (u,v) si u y v están 
     // diferentes componentes en el conjunto.
     // Nótese que C(u) devuelve la componente a la que pertenece u
     **Si** C(v) ≠ C(u) **hacer**
       Agregar arista (v,u) a  T
       Merge C(v) y C(u) en el conjunto
   **Responder** árbol T
```