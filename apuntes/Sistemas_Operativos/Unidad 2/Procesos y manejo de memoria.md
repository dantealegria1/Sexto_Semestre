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

### Administración de Procesos en UNIX
- En UNIX podemos utilizar el programa para listar los procesos en ejecución
- En Windows podemos usar el administrador de tareas
- En UNIX solo hay una llamada del sistema para crear un proceso. *fork*. Esta llamada crea un clon del proceso que hizo la llamada, después de *fork* los dos procesos (padre e hijo) tienen la misma imagen de memoria, las mismas cadenas de entorno y los mismos archivos abiertos. Por lo general el proceso hijo se ejecuta después del *execveo*