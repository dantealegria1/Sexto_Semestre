Multiprocesamiento simétrico
- Debido a que los núcleos de un procesador multinúcleo son exactamente iguales, a esto se le denomina así.

A estos “procesadores con más de un procesador” se les conoció como:
- Procesador multinucleo

Son capaces de ejecutar diversos procesos de forma simultánea y, además, comparten una misma memoria para el cumplimiento de sus funciones
- Sistemas multiprocesamiento

Los hilos de ejecución son son conocidos como:
- procesos ligeros (LWP, Lightweight processes).

Un SMP es un computador con las siguientes características
- Tiene dos o más procesadores similares de capacidades comparables. 
- Los procesadores comparten la memoria principal y la E/S  
- Todos los procesadores comparten los dispositivos de E/S, pero pueden hacerlo bien a través de los mismos canales, o bien a través de otros caminos de acceso al mismo dispositivo.  
- Todos los procesadores pueden desempeñar las mismas funciones  
- El sistema está controlado por un sistema operativo que posibilita la interacción entre los procesadores y sus programas.

Ventajas potenciales de un SMP respecto a una arquitectura monoprocesador:
- Prestaciones: proporcionará mejores prestaciones que uno con un sólo procesador del mismo tipo.  
- Disponibilidad  
- Crecimiento incremental  
- Escalado

Un hilo (thread o proceso de peso liviano) es:
- una unidad básica de utilización de CPU, consiste de: contador de programa, conjunto de registros, espacio de pila

Hilos a nivel de usuario
- son implementados en alguna librería. Estos hilos se gestionan  
sin soporte del SO, el cual solo reconoce un hilo de ejecución.

Hilos a nivel de kernel
- el SO es quien crea, planifica y gestiona los hilos. Se  reconocen tantos hilos como se hayan creado.

Manipulación de datos que requiere la garantía de que se ejecutará como una sola unidad de ejecución, o fallará completamente, sin resultados o estados parciales observables por otros procesos o el entorno
- Operacion atomica

El área de código que requiere ser protegida de accesos simultáneos donde se realiza la modificación de datos compartidos.​
- Region critica

Categoría de errores de programación que involucra a dos procesos que fallan al comunicarse su estado mutuo, llevando a resultados inconsistentes
- Condicion de carrera

Recurso compartido
- Recurso al que se puede tener acceso desde mas de un proceso

Uso de bandera
- Mediante una variable de bandera se indica si hay un proceso en la region critica

Es un mecanismo que asegura que cierta región del código será ejecutada como si fuera atómica.​  
Mantiene en espera a cualquier hilo o proceso que quiera entrar a la sección crítica protegida por el _________ reteniéndolo antes de entrar a ésta hasta que el proceso que la está ejecutando salga de ella.
- Mutex o candado

Es una construcción de programación que actúa como una señal o un contador para controlar el acceso a un recurso compartido. Es una variable de tipo entero que indica cuántas unidades del recurso están disponibles
- Semaforo

Cuando hay concurrencia, además de asegurar la atomicidad de ciertas operaciones, es necesario evitar dos problemas que son consecuencia natural de la existencia de la asignación de recursos de forma exclusiva:​
- Bloqueo mutuo e inanicion