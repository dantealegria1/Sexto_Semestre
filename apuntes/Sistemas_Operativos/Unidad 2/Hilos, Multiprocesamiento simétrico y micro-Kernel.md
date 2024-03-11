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