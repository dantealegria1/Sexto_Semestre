1. Multiprocesamiento simétrico
	- Debido a que los núcleos de un procesador multinúcleo son exactamente iguales, a esto se le denomina así.

2. A estos “procesadores con más de un procesador” se les conoció como:
	- Procesador multinucleo

3. Son capaces de ejecutar diversos procesos de forma simultánea y, además, comparten una misma memoria para el cumplimiento de sus funciones
	- Sistemas multiprocesamiento

4. Los hilos de ejecución son son conocidos como:
	- procesos ligeros (LWP, Lightweight processes).

5. Un SMP es un computador con las siguientes características
	- Tiene dos o más procesadores similares de capacidades comparables. 
	- Los procesadores comparten la memoria principal y la E/S  
	- Todos los procesadores comparten los dispositivos de E/S, pero pueden hacerlo bien a través de los mismos canales, o bien a través de otros caminos de acceso al mismo dispositivo.  
	- Todos los procesadores pueden desempeñar las mismas funciones  
	- El sistema está controlado por un sistema operativo que posibilita la interacción entre los procesadores y sus programas.

6. Ventajas potenciales de un SMP respecto a una arquitectura monoprocesador:
	- Prestaciones: proporcionará mejores prestaciones que uno con un sólo procesador del mismo tipo.  
	- Disponibilidad  
	- Crecimiento incremental  
	- Escalado

7. Un hilo (thread o proceso de peso liviano) es:
	- una unidad básica de utilización de CPU, consiste de: contador de programa, conjunto de registros, espacio de pila

8. Hilos a nivel de usuario
	- son implementados en alguna librería. Estos hilos se gestionan  
		sin soporte del SO, el cual solo reconoce un hilo de ejecución.

9. Hilos a nivel de kernel
	- el SO es quien crea, planifica y gestiona los hilos. Se  reconocen tantos hilos como se hayan creado.

10. Manipulación de datos que requiere la garantía de que se ejecutará como una sola unidad de ejecución, o fallará completamente, sin resultados o estados parciales observables por otros procesos o el entorno
	- Operacion atomica

11. El área de código que requiere ser protegida de accesos simultáneos donde se realiza la modificación de datos compartidos.​
	- Region critica

12. Categoría de errores de programación que involucra a dos procesos que fallan al comunicarse su estado mutuo, llevando a resultados inconsistentes
	- Condicion de carrera

13. Recurso compartido
	- Recurso al que se puede tener acceso desde mas de un proceso

14. Uso de bandera
	- Mediante una variable de bandera se indica si hay un proceso en la region critica

15. Es un mecanismo que asegura que cierta región del código será ejecutada como si fuera atómica.​  
	Mantiene en espera a cualquier hilo o proceso que quiera entrar a la sección crítica protegida por el _________ reteniéndolo antes de entrar a ésta hasta que el proceso que la está ejecutando salga de ella.
		-  Mutex o candado

16. Es una construcción de programación que actúa como una señal o un contador para controlar el acceso a un recurso compartido. Es una variable de tipo entero que indica cuántas unidades del recurso están disponibles
	- Semaforo

17. Cuando hay concurrencia, además de asegurar la atomicidad de ciertas operaciones, es necesario evitar dos problemas que son consecuencia natural de la existencia de la asignación de recursos de forma exclusiva:​
	- Bloqueo mutuo e inanicion

18. Paso de mensajes
	- Permite a los procesos intercambiar mensajes, el sistema operativo debe proporcionar al menos dos llamadas al sistema similares a:​  send( message ) y receive( &message )

19. Comando de linux que produce una instantánea de todos los procesos en ejecución.
	- ps

20.  Su tarea consiste en llevar un registro de las partes de memoria que se estén utilizando y las que no, con el fin de asignar espacio en memoria a los procesos cuando éstos la necesiten y liberándola cuando terminen, así como administrar el intercambio entre la memoria principal y el disco. ​
	- Administrador de memoria

21. Funciones de administrador de memoria
	- Control de que partes de la memoria están utilizadas o libres. ​  
		Asignar memoria a procesos y liberarla cuando terminan. ​  
		Administrar intercambio entre memoria y disco (Memoria Virtual)
		
22. Tipo de asignación de memoria en a que un programa se divide en varios bloques o “segmentos” que pueden almacenarse en direcciones que no tienen que ser necesariamente adyacentes, por lo que es más compleja pero más eficiente
	- Asignacion no contigua

23. Asignación de memoria en la que cada programa ocupa un bloque contiguo y sencillo de localizaciones de almacenamiento
	- Asignacion contigua

24. La memoria se divide en varias particiones de tamaño fijo, del mismo tamaño o de tamaño diferente. Cada partición puede contener exactamente un proceso
	- Particiones fijas

25. Desventajas del particionamiento fijo
	- Un programa podría ser demasiado grande para caber en una partición. En este caso, el programador debe diseñar el programa con el uso de overlays. ​
	- La utilización de la memoria principal es extremadamente ineficiente. fragmentación interna.​

26. Consiste en particiones de memoria de tamaño variable, es decir, a cada proceso se le asigna la cantidad de memoria que necesita.
	- Particionamiento dinamico

27. Desventajjas del particionamiento dinamico de memoria
	 - Fragmentacion externa

28. Segmentacion
	- Divide la memoria en segmentos, cada uno de los cuales tiene una longitud variable, que está definida intrínsecamente por el tamaño de ese segmento del programa. ​

29. Ventajas de la segmentacion
	- Ayuda a incrementar la modularidad de nuestro programa,incluso facilita el proceso de carga.​
	- El programador puede conocer las unidades lógicas de su programa, dándoles un tratamiento particular.​
	- Es posible compilar módulos separados como segmentos

30. Paginacion
	- Consiste en dividir la memoria en un conjunto de marcos de igual tamaño, cada proceso se divide en una serie de páginas del tamaño de los marcos fijo

31. En la paginacion si todos los macros estan ocupados que debe de hacer el sistema
	 - el sistema deberá encontrar una página que pueda liberar y llevarla al espacio de intercambio en el disco.​

32. Que se hace ante un fallo de pagina
	 - hay que localizar la página solicitada en el disco, cargarla en memoria y reiniciar la instrucción.​

33. Paginacion previa
	- Se cargan paginas distintas a las demandas debido a un fallo de pagina. Esta politica no es efectiva si la mayoria de las paginas extra que se traen no se referencian

34. POLÍTICAS DE UBICACIÓN
	- Tiene que ver con determinar donde va a residir una parte de un proceso en la memoria principal, es importante en el diseno de un sistema puro de segmentacion

35. Politica de reemplazo
	- Trata de la seleccion de la pagina a reemplazar en la memoria principal cuando se debe cargar una nueva pagina

36. Politica de vaciado
	- Se preocupa de determinar el momento en que hay que escribnir en la memoria secundaria una pagina modificada