### Dispositivos de I/O

- Los dispositivos externos dedicados a entrada y salida en un computador de puede agrupar a grandes rasgos en 3 categorias
	- **legibles para el usuario**: adecuando para la comunicación con el usuario del computador por ejemplo moresorad pantallas teclado, mouse etc
	- **legibles para la maquina**: adecuadas para la comunicación el equipamiento electrónico por ejemplo unidades de disco y de cintad
	- **comunicacion**: adecuados para dispositivos remotos por ejemplo controladores de. Una línea digital 

- Hay grandes diferencias entre distintas categorías e incluso dentro de cada una, entre las inferencias fundamentales se encuentran
	- **Velocidad de transferencia de datos**: puede haber diferencias de varios órdenes de magnitud ente las velocidades de transferencia de datos
	 
	- **Aplicación**: el uso está destinado un dispositivo tiene influencia en el SW u en ,s políticas del S.O y de las herramientas que le dan soporte
	
	 - **Complejidad de control:** cada dispositivo  puede tener una interfaz de control desde sencilla hasta compleja, por ejemplo la impresiona puede ser sencilla lefo un disco es mucho más complejo
##### Unidad de transferencia
- Los datos pueden transferirse como un flujo de bytes o de caracteres
##### Representación de datos
- Los dispositivos utilizan diferentes esquemas de codificación Rea datos incluyendo diferencias en el código del carácter y en las convenciones sobre la paridad
##### Condiciones de error:
- La naturaleza de los errores, el modo en el que se notifican, sus consecuencias y el largo disponible de respuestas difieren considerablemente de un dispositivo a otro

### Organización de las tres funciones de entrada y salida

- E/S programada: El programador envía un mandato de E/S a petición de un proceso a un módulo de E/S a continuación ese proceso realiza una espera activa hasta de completar la operación de continuar
- E/S dirigida por interrupciones: El procesador emite un mandato a petición de un proceso y continúa ejecutando las instrucciones siguientes siendo interrumpido por el módulo de E/S cuando este ha completado su trabajo. Las siguientes instrucciones
### Aspectos básicos del diseño de sistemas operativos

-  hay dos objetivos de suma importancia en el diseño del sistema de entrada y salida eficacia y generalidad. La eficacia es importantes debido a que las operaciones de entrada y salida significan un cuello de botella en un computador. 
- La mayoría de los dispositivos de entrada y salida son sumamente lentos comparados con la memoria principal u el procesador Una manera de afrontar el problema es la multiprogramación, ya que permite que algunos procesos esperen por la finalización de operaciones de E/S mientras se está ejecutando otro proceso. Sin embargo, se dará con cierta frecuencia que la E/S no puede seguir el ritmo del procesador.
- La generalidad, en aras de la simplicidad y la eliminación de errores, es deseable manejar todos los dispositivos de una manera uniforme.
- El S.O lo mismo que hace con la memoria también tiene jerarquía con los datos que entran y salen en el módulo de entrada y salida, la filosofía jerárquica dice que tienen que estar separada y clasifica da por su complejidad, la información que mande etc.. La jerarquía más baja le mandan información a la más alta 


--- hasta aquí viene el examen —- 