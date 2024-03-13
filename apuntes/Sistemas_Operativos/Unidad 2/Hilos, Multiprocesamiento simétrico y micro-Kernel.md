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

Una alternativa para evitar problemas de la actualizacion multiple una bandera es emplear una variable adicional que indique que proceso corresponde avanzar en todo momento, esto es utilizar turnos. Asi que bien esto soluciona el problema de la actualizacion multiple. 

Un proceso que no esta en la sección puede obligar a que otro proceso espere mucho tiempo para ingresar a la sección critica

### El algoritmo de Peterson

**COMPLETAR

### Mecanismos de sincronacion

**Mutex

Una de las alternativas para evitar la espera activa a lo que obliga el algoritmo de Peterson se llama mutex o candado

La palabra mutez nace de la frecuencia con la que se habla de las regiones de exclusión mutua. Es un mecanismo que asegura que cierta región del código será ejecutada como si fuera atómica