- Algunas partes del so deben interaccionarme directamente con el hardware del computador donde los eventos pueden tener una escala de tiempo tan breve como unos pocos nanosegundos. En el otro extremo del espectro se sitúan las partes del sistema operativo que se comunican con el usuario a un ritmo más lento. El uso de un conjunto de niveles se ajusta a este entorno
### Buffering para I/O

- Para evitar sobrecargas e ineficientes a veces es conveniente realizar la transferencia de entrada antes de que se hagan las particiones correspondientes y llevar a cabo la transferencia de salida un cierto tiempo después de que se haya hecho la petición. Esta técnica se conoce como E/S con buffer

- Hay dos tipos de dispositivos E/S orientados a bloques y orientados a caracteres
	- Orientado a bloques almacena la información en bloques que son  de tamaño fijo realizándose la transferencia de bloqué en bloque por ejemplo discos y cintas
	- Orientado a caracteres transmite solo un bit a la vez sin estructura de bloques. Las impresoras, puerros de comunicación, mouse y dispositivos de almacenamiento secundario. Usual mente es lo que conectamos 
	- FALTA ALGO AQUI
	- 
#### buffer unico

- es el que almacena los datos recibidos escritos del dispositivo 
- Permite sacar el proceso de memoria permite realizar lectura o escritura anticipada
#### buffer doble

- Se usan dos
- Permite leer o escribir de un buffer mientras el so escribe o lee en el otro

#### Buffer circular

- Se usan más de dos buffer 
- Modelo productor consumidor con buffer scotsfo
-  por lo general es una cols circular 
==========
- El uso de buffer es una rewcndia que amortigua los oídos en la demanda de entrada y salida sin embargo muchos buffer que se utilicen estos. No permitirán a un dispositivo mantener el ritmo de un proceso indefinidamente cuando la demanda media del proceso sea mayor que la que puede servir el dispositivo E/S incluso con múltiples todos los buffer acaban llenándose u el proceso tendrá que esperar después de procesar cada fragmento de datos 

- Sin embargo en un entorno multiprogramación donde hay diversas actividades de E/S y distintos proceso que hay que atender el uso de buffers es una técnica que puede incrementar la eficiencia de, sistema operativo y el rendimiento de procesos individuales

### Manejadores de dispositivos

- Cada dispositivo de entrada y salida o cds clase e dispositivos tiene un manejado asociado a un sistema operarivo
- inclute Código independiente del dispositivo para proporcionar a nivel superior del sistema operativo una interfaz de alto nivel y el código dependiente del dispositivo necesario para programar el controlador del dispositivo a través de sus registros y datos
- La tarea de un manejado es aceptar peticiones en formato abstracto de la parte del código de E/S independientemente del dispositivo
- Traducir dichas peticiones a términos que entienda el controlador enviar al mismo las órdenes adecuadas en la secuencia correcta 