## Hilo o hebra

Es una unidad básica de utilización del CPU la cual tiene:
- ID
- Propio contador de programa
- Conjunto de registros
- Una pila

Los hilos son *procesos ligeros*

Los procesos usualmente tienen una tabla muy pesada, por eso se crearon los hilos

Un proceso puede tener varios hilos, son porciones del proceso en ejecución

### Ventajas

- Su tiempo de respuesta mejora
- Comparte recursos por que los hilos comparten la memoria y recursos del proceso al que pertenecen 
- Economía, es mas fácil crear y cambiar de contexto en los hilos que en los procesos
- Utilización de múltiples CPU

### Tipos

Existen los hilos a nivel de usuario y a nivel de kernel 

**A nivel de usuario:**
- son gestionados sin soporte del sistema operativo usualmente por alguna librería 
- Es como si estuviera a nivel de software no del sistema operativo 

**A nivel de kernel:**
- son gestionados y creados por el sistema operativo

### Formas de relacionar los hilos del kernel y el usuario

**Múltiples hilos de usuarios a un hilo del kernel**
- Los hilos implementados a nivel de usuario corresponden a este caso ya que el sistema operativo solo reconoce un hilo para el control del proceso.
- Su desventaja es que si se detiene el hilo (del kernel) todo el proceso se bloquea

**1 a 1**
- Se le asigna a cada hilo de usuario cada hilo del kernel
- Proporciona una mejor concurrencia permitiendo que se ejecute otro hilo si uno se bloquear
- Hay un limite de hilos, entonces algunos procesos van a tener que estar esperando

**Muchos a muchos**
- Se multiplexan muchos hilos de usuarios a igual o menor numero de hilos del kernel

### Micro-Kernel

- Plug-in la cual permite crear aplicaciones extensibles, lo cual permite agregar nuevas funcionalidades mediante la adición de pequeños plug-in que extienden la funcionalidad inicial del sistema 

**Definición:** Es un núcleo del sistema operativo que provee un conjunto de instrucciones o llamadas mínimas al sistema la cual permite la implementación de servicios básicos como espacios de direcciones, comunicación entre procesos y planificación básica

En las arquitecturas de micro-Kernel las aplicaciones se dividen en dos tipos de componentes

![[Pasted image 20240307122627.png]]

Un sistema con la arquitectura de micro-Kernel no es fácil de desarrollar ya que es necesario crear aplicaciones capaces de adaptar dinámicamente la funcionalidad a medida de que se van instalando nuevos plug-in y al mismo tiempo se debe de tener mucho cuidado en que esos plug in no modifiquen o alteren la escancia de la aplicación.

**Ventajas**
- Testabilidad 
- Despliegue (no necesito recargar para instalar otro)
- Dinamismo (se pueden activar y desactivar)
- Construcción modular (se construyen separadas pueden trabajar en paralelo)
- Reutilización 

**Desventajas
- No es un estilo altamente escalable
- Alta complejidad ya que son difíciles de desarrollar n solo por facilidad técnica sino por el análisis elaborado para identificar hasta que punto puede ser extendida la aplicación sin afectar la escancia del sistema central

## Concurrencia

Desde el punto de vista formal la concurrencia no se refiere a dos o mas eventos que ocurren a la vez sino a dos o mas eventos cuyo orden es no determinista, ósea eventos acerca los cuales no se puede predecir el orden relativo en que ocurrirán 

### Conceptos

**Operación atómica**

Manipulación de datos que refiere la garantía de que se ejecutara como una sola unidad de ejecución o fallara completamente. LOS HILOS NO PUEDEN DIVIDIRSE EN VARIASS PARTES

**Sección o región critica

El área de código que requiere ser protegida de accesos simultaneo donde se realiza la modificación de datos compartidos

**Condición de carrera

Categoría de errores de programación que involucra dos procesos que fallan al comunicarse su estado mutuo, llevando resultados inconsistentes. Es uno de los problemas mas frecuentes y difíciles de depurar y ocurre típicamente por no considerar atomicidad de una operación

**Recursos compartidos

Un recurso al que se puede tener acceso desde mas de un proceso. En muchos escenarios esto es una variable en memoria

### Mecanismos principales

Los mecanismos princiapeles para problemas qur implican el acceso concurrente a una seccion critical

**Utilizar bandera

Una bandera parece ser una solucion muy sencilla mediante una variable de bandera si indica si hay un proceso en la region critica, sin embargo no funciona lol

**Utilizar turnos

Una alternativa para evitar problemas de la actualización múltiple una bandera es emplear una variable adicional que indique que proceso corresponde avanzar en todo momento, esto es utilizar turnos. Así que bien esto soluciona el problema de la actualización múltiple. 

Un proceso que no esta en la sección puede obligar a que otro proceso espere mucho tiempo para ingresar a la sección critica

### El algoritmo de Peterson

![[Pasted image 20240325124434.png]]

### Mecanismos de sincronacion

**Mutex

Una de las alternativas para evitar la espera activa a lo que obliga el algoritmo de Peterson se llama mutex o candado

La palabra mutex nace de la frecuencia con la que se habla de las regiones de exclusión mutua. Es un mecanismo que asegura que cierta región del código será ejecutada como si fuera atómica

Mutex no implica que el código no se va a interrumpir dentro de la región

Es un mecanismo de prevención que mantiene en espera cualquier hilo o proceso que quiera entrar a la sección critica protegida hasta que el proceso que esta adentro salga

Sino hay nadie adentro si podrán ingresar

Un área de exclusión mutua debe:

- Ser mínima: Tan corta como puedas 
- Ser completa: Se debe analizar bien cual área proteger y no arriesgarse a proteger menos

**Semáforos**

En 1968 se propusieron los semáforos

*Inicializar*
Se puede inicializar el semáforo a cualquier valor entero, pero después de esto su valor no puede ya ser leído, es una estructura abstracta y su valor es tomado como opaco o invisible al programador

*Decrementar*
Cuando un hilo decrementa el semáforo, si el valor es negativo el hilo se bloquea y no puede continuar hasta que otro hilo incrementé el semáforo. También se le llama wait, down o acquire

*Incrementar*
Cuando un hilo incrementa el semáforo, si hay hilos esperando uno de ellos es desperado. También se le llma signal, up, relase, post o V


**Bloqueo mutuo e inanición**

*Bloqueo mutuo*

Cuando hay concurrencia hay que asegurarnos aparte de que sea atómico:

*Bloqueo mutuo*: Cuando dos o mas procesos poseen determinados recursos y ambos quedan detenidos, esperando a que el otro acabe. El sistema puede seguir pero ningún proceso puede avanzar

*Inanición*: Cuando un proceso no puede avanzar dado que necesita recursos asignados a otros procesos


## Ver procesos en UNIX

- **PS:** Muestra todos los procesos

	- Si deseas ver los procesos en Linux en una vista jerárquica, utiliza el comando ps-axjf. 
	- • ps -u [nombre de usuario]: lista todos los procesos en ejecución de un determinado usuario.
	- • ps -e o ps-A: muestra los procesos Linux activos en el formato genérico UNIX. • ps -T: imprime los procesos activos que se ejecutan desde el terminal. 
	- • Ps -C nombre proceso: filtra la lista por el nombre del proceso. Además, este comando también muestra todos los procesos hijos del proceso especificado.

- El comando **top** se utiliza para descubrir procesos que consumen muchos recursos. Este comando de Linux ordenará la lista por uso de CPU, de modo que el proceso que consuma más recursos se colocará en la parte superior. También es útil para comprobar si un proceso específico se está ejecutando.

Un proceso puede iniciarse como proceso en primer plano o en segundo plano. A cada proceso Linux se le asigna un único PID (número de identificación del proceso). 

Ocasionalmente, los procesos pueden consumir muchos recursos y necesitan ser eliminados. También puede ocurrir que quieras cambiar el nivel de prioridad de un proceso, para que el sistema le asigne más recursos. Independientemente del caso, todas estas tareas requieren que hagas lo mismo: listar los procesos en ejecución en Linux