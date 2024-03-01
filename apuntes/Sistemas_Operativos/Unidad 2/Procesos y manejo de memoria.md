# Procesos

Un proceso es una instancia de ejecución de un programa caracterizado por su contador de programa, su  palabra de estado, sus registros de procesos, sus segmento, pila y datos etc...

Un programa puede ser ejecutado por varios usuarios en un sistema multiusuario, para cada ejecución existirá un proceso, con su contador de programa

### Estados de los procesos

Este puede pasar por una serie de estados directos:
- nuevo
- En ejecución
- Listo o preparado
- En espera (cuando el proceso esperando a que ocurra algún evento, por ejemplo una operación de entrada o de salida)
- Terminado

![[Pasted image 20240226122619.png]]

### Bloque de control de procesos (PCB)

Es una estructura de datos que contiene información asociada a cada proceso
- Estado de proceso
- Contador del programa
- Registros del CPU
- Información de planificación de CPU
- Información Contable
- Información de estado E/S

### Control de procesos

Se requiere tener una planificación la cual tiene los siguientes objetivos

- *Ser justo*: Se refiere a que todo los procesos se les debe tratar igual
- *Maximizar la capacidad de ejecución:* Es decir maximizar el numero de procesos servidos por unidad de tiempo
- *Maximizar el numero de usuarios interactivos:* Que reciban unos tiempos de respuesta aceptables
- *Ser predecible
- *Minimizar sobrecarga

Existen 3 niveles de planificación de procesos

***A largo plazo***
- Era el mas frecuente en los sistemas de lotes y multiprogramados en lotes
- Las decisiones eran tomadas principalmente considerando los requisitos de los procesos y los que el sistema tenia libres. Puede llevarse a cabo con periodicidad de una vez, cada varios minutos y así
- Es el que usan casi todos hoy en día, este tipo de planificación no se efectúa, dado que es típicamente el usuario el que indica que procesos iniciar

***Mediano plazo***
- Decide cuales procesos es conveniente bloquear en determinado momento, sea por escases de algún recursos o por que están realizando alguna solicitud que no puede satisfacerse  momentáneamente. Se encarga de tomar decisiones respecto a los procesos conforme entran y salen del estado de bloqueo

***A corto plazo***
- Decide como compartir momento a momento el equipo entre todos los procesos (Como una fila). La planificación a corto plazo se lleva a cabo decenas de veces por segundo, es el encargado de planificar los procesos que están listos para la ejecución
- Debe ser rápido  y eficiente
- Se le llama despachador

Hay cuatro eventos principales que provocan la creación de procesos
- El arranque del sistemas
- La ejecución desde un proceso de una llamada al sistema para creación de procesos
- Una petición de usuarios para crear un proceso
- El inicio de un trabajo por lotes

### Objetivos de la planificación

- *Ser justos* debe tratarse igual a todos los procesos que tengan las mismas características
- *Maximizar rendimiento* Dar servicio a la mayor parte de procesos por unidad de tiempo
- *Ser predecible* Un mismo trabajo puede tomar aproximadamente la misma cantidad de tiempo independientemente de la carga del sistema
- *Equilibrar el uso de recursos* Favorecer a los procesos que empleen recursos subutilizado y penalizar a los que peleen un recurso sobre utilizado
- *Evitar la postergación indefinida* Aumenta la prioridad de los procesos mas viejos
- *Favorecer el uso esperado del sistema* un sistema con usuarios interactivos, maximizar la prioridad de los procesos que sirvan a solicitudes inicializadas por este
- *Dar preferencia a los procesos que podrían causar bloqueo* si un proceso de baja prioridad esta empleando algún recurso que otros procesos quieren favorecer que este termine mas rápido
- *Favorecer los procesos con un comportamiento deseable* si un proceso causa muchas demoras se le puede penalizar
- *Degradar suavemente* Si bien el uso del procesador al 100 es imposible. Un algoritmo puede buscar responder con la menor penalización a los procesos preexistentes
- *Minimizar la sobrecarga* El tiempo que el algoritmo pierda en burocracia debe mantenerse al mínimo

[[MANEJO DE PROCESOS]]

### Administración de Procesos en UNIX
- En UNIX podemos utilizar el programa para listar los procesos en ejecución
- En Windows podemos usar el administrador de tareas
- En UNIX solo hay una llamada del sistema para crear un proceso. *fork*. Esta llamada crea un clon del proceso que hizo la llamada, después de *fork* los dos procesos (padre e hijo) tienen la misma imagen de memoria, las mismas cadenas de entorno y los mismos archivos abiertos. Por lo general el proceso hijo se ejecuta después del *execveo*
- Tanto UNIX como Windows una vez que se crea un proceso, el padre y el hijo tienen sus propios espacios de direcciones distintas. Si cualquiera de los procesos modifica una palabra en su espacio de direcciones esta modificación no es visible para el otro proceso. En UNIX el espacio de direcciones inicial del hijo es una copia del padre pero en definitiva hay dos espacio de direcciones distintos involucrados, no se comparte memoria en la que se puede escribir sin embargo es posible para un proceso recién creado compartir algunos de los recursos de su creador como los archivos abiertos
- Tarde o temprano el nievo proceso terminara por log general debido a una de las siguientes condiciones
	- Salida Normal (voluntario)
	- Salida por error (voluntario)
	- Error fatal (involuntaria)
	- Eliminado por otro proceso (involuntaria)
	El voluntario por ejemplo es cuando pongo un print que diga error 
- La mayoría de los procesos terminan debido a que han concluido su trabajo
- La segunda razón de terminación es que el proceso descubra un error
- La tercera razón de terminación es un error fatal producido por el proceso a menudo debido a un error en el programa
- La cuarta razón por la que un proceso podría terminar es que ejecute una llamada al sistema que indique el sistema operativo que elimine otros procesos
