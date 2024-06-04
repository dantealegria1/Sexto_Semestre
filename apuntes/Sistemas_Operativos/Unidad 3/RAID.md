#### Definición

- Redundant Array Independent Disk. Es cuando usamos multiples discos y hay varias formas para organizar la redundancia y datos. Estos multiples discos el SO los trata como un dispositivo logico. La redundancia se utiliza para guardar información de paridad [Garantiza que se puedan recuperar en caso de que falle un disco]

- **Siete Niveles** del 0 -> 6

- El termino salió de un articulo de investigadores de la universidad de california en berkeley

#### Nivel 0

- No incluye redundancia y no es un verdadero miembro.
- Algunas super computadoras lo usan
- Los datos del Sistema y del usuario estan distribuidos a lo largo de todos los discos del vector. El disco logico esta dividido en bandas. pueden ser bloques, sectores o alguna otra unidad. Las bandas se asignan de forma rotatoria a discos físicas consecutivos en el vector
- Si tenemos 2 discos de 4TB tendremos capacidad de 8TB, un rendimiento de lectura x2, de escritura x2 y la integridad de los datos si se pierde uno mamo todo 

#### Nivel 1

- Conseguimos la redundancia duplicando TODOS los datos. Cada disco tiene otro con los mismos datos
- Una petición de lectura puede agarrar cualquiera de los dos discos, menor tiempo de búsqueda
- Si escribes ocupas actualizar los dos
- Cuando un dispositivo falla se accede a los datos del segundo
- Si tengo 2 discos de 4TB tendremos capacidad de 4TB, rendimiento de lectura x2, escritura es como si fuera un disco simple, la rotura de un disco no lleva perdida de información completa

#### Nivel 2

- Tienen acceso paralelo, todos los miembros participan en la ejecución de cada petición de E/S
- En 2 y 3 las bandas son muy peques a menudo un unico byte o una palabra. Se calcula un código de corrección de error, almacenando los bits del código en las correspondientes posiciones de bit en los multiples discos de paridad. Se utiliza el código Haming que es capaz de corregir errores en un unico bit y detectar en 2
- Es costoso y no se implementa

#### Nivel 3

- Solo ocupa un disco redundante independiente al tamaño del vector del disco. Usa acceso paralelo
- En lugar de un código de corrección de errores se calcula un bit de paridad simple para el conjunto de bits almacenados en la misma posición
- Si falla un dispositivo se accede al de paridad y se reconstruyen
- Dado que están en diferentes bandas los datos, puede alcanzar velocidades de transferencia muy altos

#### Nivel 4

- Es un vector de acceso independiente, cada disco del vector opera independientemente, puede servir el paralelo particiones de E/S.
- Adecuados para aplicaciones con tasas elevadas de peticiones de E/S y menos adecuado para altas tasas de transferencias de datos
- Bandas grandes se calculan bit a bit una banda de paridad a partir de las bandas de cada disco
- Penalización en la escritura cuando son de size peque. Cada que algo escribe deben actualizar los datos de paridad
- Para calcular la nueva paridad. El SW debe leer las bandas de datos y paridad antiguas y actualizar
- Cada operación debe involucrar el disco de paridad y ocasionar cuello de botella

#### Nivel 5

- Similar al nivel 4. Este destruye las bandas de paridad. Para un vector de n discos la banda de paridad esta en un disco diferente para las n primeras listas
- La distribución evita el potencial cuello de botella debido a la existencia de un unico disco de paridad que aparece en el nivel 4
- Si tenemos 4 discos de 4 TB la capacidad de un RAID 5 sera de 12 TB [X-1] si todos los discos son iguales. La lectura sera de X-1 veces el numero de discos, escritura como si fuera un disco simple, la rotura de un disco no lleva perdida, si se rompe 1> si mamo

#### Nivel 6

- Fue propuesto por investifadores Berkeley. Se hace dos calculos de paridad diferentes. almacenando en bloques separados de distintos discos. Un vector RAID 6 cuyos datos ocupen N entonces necesitaran N+2 discos
- La ventaja de RAID 6 es que da una MUY alta disponibilidad de datos. tienen que fallar 3 discos para que cause perdida de datos. Tiene penalizacion en la escritura ya que afeca a dos bloques de paridad
- Si tenemos 4 discos de 4TB la capacidad sera de 8 [x-2]. la lectura sera de X-2 veces. la escritura es como si fuera un disco simples