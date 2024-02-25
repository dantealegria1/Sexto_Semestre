### 6/2/24

Es un suceso que altera la ejecución de las instrucciones
Las interrupciones mas compones:

- **De programa o verificación de programas**: Son ocasionados por condiciones que se producen como resultado de una ejecución de una instrucción por ejemplo la división entre 0

- **De reloj:** Las produce el reloj interno de la computadora

- **De entrada o salida:**  Es genera por los drivers o controladores que nos indican que una tarea a finalizado o algún equipo fue conectado o marca algún error

- **Por fallo de HW o verificación de maquinas:** Son causadas por el mal funcionamiento del equipo, cortes de energías etc..

## PSW
Tiene tres tipos
- El actual: El que se ejecuta, almacena la dirección de la próxima instrucción a ejecutar
- La nueva: El que va a ejecutar. Almacena la dirección de la instrucción que se suspendió o interrumpió
- La vieja: El que se ejecuto almacena la dirección de HW donde reside el manipulador de la interrupción
- Los sistemas operativos un procesadores solo tienen PSW actual

Que diga Dual Core no significa que tenga dos procesadores, sino que simula que tiene dos