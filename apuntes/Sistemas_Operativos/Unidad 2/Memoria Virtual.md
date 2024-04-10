## Reemplazo de paginas

- Es necesario encontrar una forma justa y adecuada de llevar a cabo un reemplazo de paginas

- Si todos los marcos están ocupados, el sistema deberá encontrar una pagina que pueda liberar y llevarla al espacio de intercambio en el disco

- Para esto se debe implementar un algoritmo de reemplazo de paginas, La característica que busca en este algoritmo es que para un patrón de acceso dado, permita obtener el menor numero de fallos de paginas

- Ante un fallo de pagina hay que localizar la pagina solicitada en el disco, cargarla en memoria y reiniciar la instrucción

- El fallo de pagina es cuando cargo en la memoria RAM desde el disco duro 

## Asignación de Macros

- Tenemos un sistema con 1,024 kb de memoria, compuesta por 256 paginas de 4096 bytes cada uno basado en paginación

- Si el sistema usa 248 kb, el primer paso será reservar 62 paginas y destinar 194 paginas restantes a la ejecución de programas

- Conforme comienzan a ejecutarse los procesos y cada uno genere un fallo de pagina, se le ira asignando uno de los macros disponible, cuando acabe se volverán a convertir libres

- Una vez que estén llenos, el siguiente fallo de pagina invocara un algoritmo de reemplazo de pagina y erigirá una de las 194

### Mínimo de Macros

- Si un proceso tiene asignados muy pocos macros su rendimiento se vera afectado. Se ha propuesto que cada instrucción puede causar un solo fallo de pagina. Cada instrucción del procesador puede (dependiendo de la arquitectura) descadenar varias solicitudes ósea varios fallos de pagina 

## Hiperpaginación

- Si un proceso no tiene marcos suficientes para su localidad, pasa mas tiempo en fallo de pagina que ejecutándose

- Es la situación en la que se utiliza una creciente cantidad de recursos para hacer una cantidad de trabajo cada vez menor. A menudo se refiere a cuando se cargan y descargan sucesiva y constantemente partes de la imagen de un proceso desde y hacia la memoria principal y la virtual. En estado normal esto permite que un proceso bloqueado y no listo para correr deje lugar en la memoria principal a otro proceso listo. Cuando se produce los ciclos de procesador se utilizan en llevar y traer paginas y el rendimiento general del sistema degrada notablemente
 


**Leer la presentación de Hiperpaginacion sobre el FIFO y eso
- https://eduuaa-my.sharepoint.com/:p:/r/personal/clelia_ruiz_edu_uaa_mx/_layouts/15/Doc.aspx?sourcedoc=%7B483C91AB-D617-4BC5-A755-B24ED7223CDD%7D&file=Hiperpaginacion.pptx&action=edit&mobileredirect=true