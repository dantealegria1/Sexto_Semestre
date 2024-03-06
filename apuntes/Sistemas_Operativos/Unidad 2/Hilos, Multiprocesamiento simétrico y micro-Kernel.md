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