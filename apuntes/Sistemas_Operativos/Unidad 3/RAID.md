#### Definición

- Redundant Array Independent Disk. Es cuando usamos multiples discos y hay varias formas para organizar la redundancia y datos. Estos multiples discos el SO los trata como un dispositivo logico. La redundancia se utiliza para guardar información de paridad [Garantiza que se puedan recuperar en caso de que falle un disco]

- **Siete Niveles** del 0 -> 6

- El termino salió de un articulo de investigadores de la universidad de california en berkeley

![[Pasted image 20240604181543.png]]


#### Nivel 0

- No incluye redundancia y no es un verdadero miembro.
- Algunas super computadoras lo usan
- Los datos del Sistema y del usuario estan distribuidos a lo largo de todos los discos del vector. El disco logico esta dividido en bandas. pueden ser bloques, sectores o alguna otra unidad. Las bandas se asignan de forma rotatoria a discos físicas consecutivos en el vector
- Si tenemos 2 discos de 4TB tendremos capacidad de 8TB, un rendimiento de lectura x2, de escritura x2 y la integridad de los datos si se pierde uno mamo todo 

![[Pasted image 20240604181600.png]]

#### Nivel 1

- Conseguimos la redundancia duplicando TODOS los datos. Cada disco tiene otro con los mismos datos
- Una petición de lectura puede agarrar cualquiera de los dos discos, menor tiempo de búsqueda
- Si escribes ocupas actualizar los dos
- Cuando un dispositivo falla se accede a los datos del segundo
- Si tengo 2 discos de 4TB tendremos capacidad de 4TB, rendimiento de lectura x2, escritura es como si fuera un disco simple, la rotura de un disco no lleva perdida de información completa

![[Pasted image 20240604181607.png]]

#### Nivel 2

- Tienen acceso paralelo, todos los miembros participan en la ejecución de cada petición de E/S
- En 2 y 3 las bandas son muy peques a menudo un unico byte o una palabra. Se calcula un código de corrección de error, almacenando los bits del código en las correspondientes posiciones de bit en los multiples discos de paridad. Se utiliza el código Haming que es capaz de corregir errores en un unico bit y detectar en 2
- Es costoso y no se implementa

![[Pasted image 20240604181618.png]]

#### Nivel 3

- Solo ocupa un disco redundante independiente al tamaño del vector del disco. Usa acceso paralelo
- En lugar de un código de corrección de errores se calcula un bit de paridad simple para el conjunto de bits almacenados en la misma posición
- Si falla un dispositivo se accede al de paridad y se reconstruyen
- Dado que están en diferentes bandas los datos, puede alcanzar velocidades de transferencia muy altos

![[Pasted image 20240604181636.png]]

#### Nivel 4

- Es un vector de acceso independiente, cada disco del vector opera independientemente, puede servir el paralelo particiones de E/S.
- Adecuados para aplicaciones con tasas elevadas de peticiones de E/S y menos adecuado para altas tasas de transferencias de datos
- Bandas grandes se calculan bit a bit una banda de paridad a partir de las bandas de cada disco
- Penalización en la escritura cuando son de size peque. Cada que algo escribe deben actualizar los datos de paridad
- Para calcular la nueva paridad. El SW debe leer las bandas de datos y paridad antiguas y actualizar
- Cada operación debe involucrar el disco de paridad y ocasionar cuello de botella

![[Pasted image 20240604181646.png]]

#### Nivel 5

- Similar al nivel 4. Este destruye las bandas de paridad. Para un vector de n discos la banda de paridad esta en un disco diferente para las n primeras listas
- La distribución evita el potencial cuello de botella debido a la existencia de un unico disco de paridad que aparece en el nivel 4
- Si tenemos 4 discos de 4 TB la capacidad de un RAID 5 sera de 12 TB [X-1] si todos los discos son iguales. La lectura sera de X-1 veces el numero de discos, escritura como si fuera un disco simple, la rotura de un disco no lleva perdida, si se rompe 1> si mamo

![[Pasted image 20240604181656.png]]

#### Nivel 6

- Fue propuesto por investigadores Berkeley. Se hace dos cálculos de paridad diferentes. almacenando en bloques separados de distintos discos. Un vector RAID 6 cuyos datos ocupen N entonces necesitaran N+2 discos
- La ventaja de RAID 6 es que da una MUY alta disponibilidad de datos. tienen que fallar 3 discos para que cause perdida de datos. Tiene penalización en la escritura ya que afecta a dos bloques de paridad
- Si tenemos 4 discos de 4TB la capacidad sera de 8 [x-2]. la lectura sera de X-2 veces. la escritura es como si fuera un disco simples

![[Pasted image 20240604181704.png]]

#### Nivel 10

- No necesita hacer calculo de paridad como en el 5 y el 6. ósea mas veloz, menos recursos tambien. Nos permite crear un raid 0 de dos raid 1 pero ocupas minimo 4 discos
- Se podran romper maximo 2 discos de cada grupo de raid 1, sino perdemos toda las informacion

![[Pasted image 20240604181715.png]]


#### Nivel 0+1

- Un nivel principal de RAID 1 que replica los datos en el primer sub nivel en un segundo. Tambien va existir un nivel raid 0 que hara las funciones de este. ósea almacenar los datos
- Un nivel principal en forma de espejo y sub niveles que hacen la division. Si un disco falla los datos estan en el otro Raid 0
- La desventaja es que si agregamos un disco a un sub nivel lo tenemos que agregar al otro

![[Pasted image 20240604181727.png]]

#### Nivel 50

- Un nivel principal en Raid 0 que se divide en sub niveles de raid 5 con sus 3 discos duros
- En cada RAID 5 tendremos una serie de datos con su correspondiente paridad. En este caso un disco puede fallar en cada raid, si perdemos mas bye bye

![[Pasted image 20240604181735.png]]

#### Cache de disco

- Es un buffer en memoria principal para almacenar sectores de disco. Cuando se hace una petición de E/S ve el cache de disco a ver si ahi esta el sector que ocupa

#### Consideraciones de diseño

- Cuando se satisface una petición de E/S de la cache de disco se entregan los datos del cache al proceso. se puede hacer copiando el bloque en la memoria princiapl al cache o usand la tecnica de memoria compartida pasando un puntero al cache del disco. Esta es mejor mejora la transferencia de la memoria y acceso compartido

- cuando se trae un nuevo sector a cache del disco se debe reemplazar uno de los bloques existentes. El algoritmo mas utilizado es LRU [Least recently used] y otro es LFU [Least frequently used] 
- LFU los bloques se organizan en una pila, Una porcion de la parte superior se considera separada como una seccion nuevacuando hay un acierto en la cache el bloque accedido se mueve hacia arriba de la pila, si ya estaba en la seccion neuva incrementa en 1. Si ya la seccion nueva es grande se consigue que permanezcan inalterados los contadores de referencia. En caso de fallo se escoge para reemplazar el contador mas bajo