#### Memoria Caché

Es una memoria de alta velocidad, es más rápida y costosa que las demás. Los programas antes de ser ejecutados pasan de la memoria principal a la memoria caché.

Al utilizar la memoria caché, se espera que:
- La sobrecarga en el traspaso de una memoria a otra sea mucho menor que la mejora en el rendimiento obtenida por usar la memoria caché

Los objetivos al utilizar la memoria caché son:
- Reducir el ancho de banda entre la memoria principal y el procesador
- Reducir el tiempo de acceso promedio a la memoria

La frecuencia en la que el procesador puede ejecutar las instrucciones se encuentra limitada por el tiempo de ciclo de memoria (suma de los tiempos de acceso y de los tiempos de carga/traslado). Estos tiempos se miden en nanosegundos

La caché contiene una copia de una parte de la memoria principal. Cuando el procesador intenta leer algún dato de la memoria comprueba si este no existe en la memoria caché, si está se envía al procesador y listo. Pero si no se encuentra un bloque de la memoria principal se mueve a la memoria caché y se devuelve al procesador.
#### Tipos de caché

Clasificación 1

1. *Caché de disco.* Se trata de utilizar una porción de memoria RAM asociada a un disco particular, en la que se almacenan los datos de reciente acceso para agilizar su carga.
2. *Caché de pista.* Es un tipo de memoria caché sólida, es similar a la RAM y se encuentra en supercomputadoras.
3. *Caché de web.* Es la memoria caché que se ocupa de guardar los datos de las páginas web que hemos visitado de manera reciente.

Clasificación 2

1. *Caché nivel 1.* Es la caché que se encuentra más cercana al procesador (más rápida). Llamada caché interna
2. *Caché nivel 2 y 3.* Es una caché que se encuentra incluida en la placa madre. Es más grande que la de nivel 1 pero un poco más lenta. Es una caché de tipo externa.
