## El Hardware

Tiene 3 componentes principales
- **El CPU** que es la unidad de control de procesamiento *Procesa que hará la maquina*
- **Memoria** que es donde se almacenan los datos
- **Dispositivos** E/S que son periféricos que nos permiten ingresar datos o nos dan salida de estos
- **Controladores** son los drivers para controlar los elementos

## El software

- **Núcleo del sistema operativo** que es como se mueven los datos del sistema
- **Editores compiladores** que es el que convierte el lenguaje de programación a uno por la maquina y permite editar código

Los programas de aplicación son los que hace una actividad especifica 

El sistema operativo es el que controla todos los dispositivos del PC

[[Memoria]]

## Procesos

*Un proceso es una abstracción de un programa en ejecución*, también se le llama tareas, significa que
- Un programa se esta ejecutando
- Una actividad asincrónica
- Se le da lugar a algún procedimiento siendo ejecutado
- Entidad a la cual se le asignan procesadores

Un sistema que administra procesos debe
- destruir
- suspender
- restaurar
- cambiar la prioridad
- bloquear
- despertar 

Cuando se crea un proceso se debe asignar un nombre, insertarse en la lista de listos para determinar cual es su prioridad inicial, crear el bloque de control y asignar los recursos del proceso

- El sistema de prioridades inicia desde la 0, entre mas peque mas prioridad
- El sistema operativo se divide en actividades mas peque
- Muchos procesos no nos damos cuenta de que están ocurriendo

## kernel

La parte *mas importante* ya que tiene el control de la maquina es un intermediario entre el hardware y el software

**Sus funciones son:
- Comunicación entre programas
- Gestión de software
- Manipular interrupciones
- Controlar procesos
- Soporte del sistema de archivos

## Prioridades del sistema

Nivel 1
- Registros del sistema
Nivel 2
- Cache Nivel 1
Nivel 3
- Cache nivel 2
Nivel 4
- RAM
- ROM
Nivel 5
- Disco duro o memoria secundaria (USB, Disco externo etc.)
Nivel 7
- Copias de seguridad 

Entre mas arriba
- Mas caro
- Menos almacenamiento
- Mas frecuente su uso
- Mas rápido

[[Registros de procesos]]

 ## Memoria Cache

Es mas rápida y costosa que las demás. Antes de que los programas sean ejecutados pasan por la memoria cache y luego a la principal

Se espera que la sobrecarga en el transpuso de una memoria a otra sea menor

Espera reducir el ancho de banda entre la memoria principal y el procesador. Reduce el tiempo de acceso a la memoria

 El cache contiene una copia de una parte de la memoria principal. Primero el procesador ve si esta en el cache, si esta super bien sino un bloque de la memoria principal se mueve a la memoria cache y se devuelve al procesador

***Tipos de cache
- *Disco*: se tata de asociar una porción de memoria RAM asociada a un disco particular en los que se almacenan los datos de reciente acceso para agilizar su carga
- *pista*: Es tipo de cache solida, similar a la RAM y esta en supercomputadoras
- *web*: Es la memoria cache que se ocupa de guardas los datos de las paginas que hemos visitado recientemente
- *Nivel 1*: Es la que esta mas cerca del proceso ósea que es mas rápida. Llamada cache interna
- *Nivel 2*: Esta en la placa madre. es mas grande que la nivel 1 pero mas lenta. Es tipo externa

[[Memoria cache]]

## interrupciones

- *De programa o verificacion de programas* Son ocacionados por condiciones que se producen como resultado de una ejecucion de una instruccion como por ejemplo la division entre 0
- *De reloj* los produce el reloj interno de la computadora
- *De entrada o salida* que es cuando los drivers o controladores nos indican que una tarea se finalizo, algo fue conectado o marca un error
- *Por fallo de HW* que son causados por el mal funcionaiento del equipo como cortes de energia o asi

[[Interrupciones]]
## PSW

Tiene tres tipos
- *El actual:* El que se ejecuta, almacena la dirección de la próxima instrucción a ejecutar
- *La nueva:* El que va a ejecutar. Almacena la dirección de la instrucción que se suspendió o interrumpió
- *La vieja:* El que se ejecuto almacena la dirección de HW donde reside el manipulador de la interrupción
- Los sistemas operativos un procesadores solo tienen PSW actual

Que diga Dual Core no significa que tenga dos procesadores, sino que simula que tiene dos

## Técnicas de comunicación de I,0

la función principal del S,O es el control de dispositivos de E/S
hay tres tácticas para llevar a cabo las operaciones de entrada y salida

***Entrada y salida programada

Es como si cierro la puerta y cada cinco min reviso si hay alguien en la puerta. Ósea que verifica si hay periféricos que quieren dar información cada cierto tiempo, ya no se usa mucho por que se quedan en espera 

Los datos se intercambian entre el CPU y el modulo de entrada y salida. El CPU ejecuta un programa que controla directamente la operación de entrada y salida. El CPU es el responsable de comprobar periódicamente el estado del modulo de entrada y salida hasta que se encuentra que la operación ha finalizado

*Instrucciones*
- Control: Usada para activar un dispositivo externo y decirle que hacer
- Estado: Usada para comprobar condiciones de estado asociadas a un modulo de E/S
- Transferencia: Usada para leer o escribir datos entre los registros del procesador y dispositivos externos

***Entrada y salida dirigda por interrupciones

Cuando el dispositivo quiere mandar algo le avisa al sistema y no existen tiempos muertos. Es lo que mas se usa

Cuando una interrupcion ocurre el CPU salva el contexto del programa actual y procesa la interrupciones

Hay dos tipos
- *Sincronica* Cuando una operacion es finalizada el control es retomado por el proceso que la genero, solo se atiende una solicitud de entrada y salida a la vez
- *Asincronica*: Este ipo retoma el programa sin esperar que la operación de entrada y salida finalice. Este tipo de entrada y salida incrementa la eficiencia del sistema ya que mientras se lleva a cabo la entrada o salida el CPU puede ser usado para procesar o planificar otra entrada o salida

***Acceso directo a la memoria

Aquí el modulo de entrada-salida y la memoria central intercambian datos sin usar el CPU, es capaz de limitar al CPU y de relevarlo en el control del sistema para transferir los datos. Cargan los datos pero no hacen nada se quedan ahí esperando

No es muy eficiente en grandes volúmenes de datos

[[Técnicas de comunicación de I,O]]
## Introducción a los sistemas operativos

Lo primero que hace la computadora es un *auto diagnostico* llamado prueba de encendido. Identifica su memoria, discos etc.. después busca su sistema operativo y hace *boot*

Una vez que se prendió, el S.O mantiene una parte de este en su memoria SIEMPRE, y esto lo hace por que le toca hacer:
- Proporciona una interfaz de lineal de comando
- Administra los dispositivos del hardware. Sirve de intermediario entre el sistema y el hardware

Un sistema operativo es un conjunto de programas que se integran con el hardware para facilitar al usuario el aprovechamiento de recursos disponibles

***Funciones:
- Ejecuta los programas
- Hace uso eficiente del hardware
- Provee un control de recursos
- Interpreta comandos
- Manejo de errores
- Acepta trabajos y conservarlos hasta su finalización
- *Secuencia de tareas*: debe administrar la manera en la que se reparten los procesos (definir un orden)
- *Protección*: Evita que las acciones del usuario afecte el trabajo de otro usuario
- *Multiacceso*: Un usuario puede conectarse a otra maquina sin estar cerca de ella
- *Contabilidad de recursos*: Establece el costo que se le cobra a un usuario para utilizar determinados recursos (Si tengo varios recursos a cada proceso se le asigna determinado tiempo y espacio)

***características:
- *Conveniencia*: Un sistema operativo hace mas conveniente el uso de una computadora
- *Eficiencia*: Permite que los recursos de la computadora se usen mas eficiente
- *Habilidad para evolucionar*: Debe permitir el desarrollo o prueba mediante funciones del sistema sin interferir
- *Encargado de administrar hardware*: Se encarga de manejar recursos de hardware
- *Relacionar dispositivos* El sistema opeativo se debe de encargar de la comunicacion de dispositivos perifericos
- *Organizar datos* acceso rapido y seguro
- *Manejo de comunicaciones* el sistema operativo permite al usuario manejar las instalaciones
- *Manejar entradas y salidas* Un sistema operativo debe hacerse facil al usuario el acceso y manejo de los dispositivos de E-S

[[Introduccion a los sistemas operativos]]
## Evolución de los sistemas operativos

El primer sistema operativo fue creado en 1956 para la IBM 704 lo único que hacia era comenzar la ejecución de un programa cuando el anterior terminaba

**Generacion cero 1940's

- Carencia total de S.O
- Completo acceso a lenguaje maquina

**Primera generación 1945-1955

- Sin sistema operativo, el programador interactúa directamente usando computadores
- comienza como transición entre trabajos

**Segunda Generación 1955-1965

Transistores y sistemas de procesamiento por lotes 

En los anos sesenta aparecen los S.O con:
- *Multiprogramación* varios programas de usuarios se encuentran en el almacenamiento al mismo tiempo
- *Multiprocesamiento* varios procesadores se usan en el mismo sistema para aumentar el poder de procesamiento

Aparece la independencia de dispositivo
- El usuario especifica las características que requiere los dispositivos
- El sistema operativo asigna los dispositivos según los requerimientos

En 1963 un equipo del MIT desarrollo el CTSS que fue el primer sistema operativo practico que permitió a varios usuarios ejecutar varios programas diferentes desde terminales

***Tercera generación 1965-1980

*Circuitos integrados y multiprogramación* 

Difusión de la multiprogramación
- Partición de la memoria en porciones con trabajos distintos
- Aprovechamiento del tiempo de espera para utilizar la CPU para otros procesos
- Emergieron con el desarrollo de los circuitos integrados
- Las computadoras se hacen mas pequeñas

Protección por hardware, del contenido de cada partición de memoria

Aparece el *spooling
- Simultaneous Peripheral Operation On line
- Almacenamiento de trabajos de entrada y salida en dispositivos transitorios rápidos (discos) para disminuir el impacto de los periféricos mas lentos
- Sistemas operativos grandes y complejos pero que tienen propósitos generales (modos múltiples)
- Interponen una capa de software entre el usuario y el hardware
- Aparecen los lenguajes de control que sirven para especificar trabajos y recursos requeridos
- Soportan timesharing (variable de la multiprogramación) con usuarios conectados en línea
- Aparecen los sistemas operativos en tiempo real para la industria y la milicia
- Se difunden las computadoras de rango medio

***Cuarta generación 1980-1990

*Aparecen las computadoras personales*

Aparece el software amigable con el usuario y destinado a usuarios no personales

Desarrollo de sistemas operativos de red y sistemas operativos distribuidos

Sistemas operativos de red
- Están consientes de varias computadoras
- Cada maquina ejecuta su propio S.O local

Sistemas operativos distribuidas
- Aparece como un S.O de un solo procesador
- Los usuarios no están consientes en donde se ejecuta sus programas ya que el S.O administra automáticamente
- Debe permitir que un programa se ejecute mediante varios procesadores a la vez
- Aparecen los emuladores de terminal para el acceso a equipos remotos
- Énfasis en la seguridad
- El S.O crea un ambiente de trabajo según el concepto de maquina virtual
- Proliferación de sistema de base de datos accesibles mediante redes de comunicación
[[Evolucion_SO]]

## UNIX 

Fue desarrollado en *1965* por *Ken Thompson* en los laboratoristas de Bell AT&T su objetivo era desarrollar un sistema operativo interactivo simple llamado multics

Fue creado para correr el juego *Viaje en el espacio*

En *1969* GECOS lo rediseño para desarrollar UNICS que abreviaron UNIX (Servicio informático y de información Unipixeliado)

El *1 de Enero de 1970* se considera el nacimiento de UNIX

La versión 7 que salió en *1979* vino con:
- Mejor portabilidad
- Extracción de limitaciones relacionadas con el tamaño de los archivos
- Corre en 386 maquinas

En *1977* la UCLA desarrollan el BSD (Beckley Software development) para ejecutar el sistema en su plataforma VAX y se convierten en dos ramas
- La de AT&T que es UNIX USL
- La rama BSD

Desarrollaron muchos sistema similares a UNIX
- AIX
- Sun Solaris
- HP-UX
- ULTRIS
- IRIX
- Unixware
- Unix SCO (Se usa mucho en bases de datos)
- Tra64 UNIX 

*Filosofa de UNIX*

Resumido por *Peter H Salus* en *1974*

Escribe programas que:
- Hagan una cosa y la hagan bien
- Trabajar juntos
- Maneje flujos de texto por que es una interfaz universal

En *1974* Ritchie y Thompson citan lo siguiente
- Facilitan la escritura y prueba
- Uso interactivo en lugar de procesamiento por lotes
- Economía y elegancia
- Sistema autosuficiente 

17 Reglas para programar en Unix
- Construye programas modulares
- Escribe programas legibles
- Uso de composición de uso
- Mecanismos separados de la politicé
- Escribe programas simples
- Escribe programas pequeños
- Escribe programas transparentes
- Escribe programas robustos
- Compilar los datos cuando es necesario no el programa
- Aprovechar los conocimientos de los usuarios esperados
- Evitar la salida innecesaria
- Escribe programas que faltan de una manera que es fácil de diagnosticar
- Valorar el tiempo del Desarrollador sobre el tiempo de las maquinas
- Escribe programas abstractos que generen código en lugar de escribir código a mano
- Prototipo de software antes de pulirlo
- Escribe programas flexibles y abierto hacer el programa y protocolo existente

***UNIX ES SIMPLE Y SENCILLO

[[Unix]]
## Linux 

Creada en *1991 por Linux Torvald* lo creo por pasatiempo

GNU/LINUX surge de varios proyectos. GNU HARD era el KERNEL que usa linux en el *1991*

Primero se queria llamar FREAX a Ari Lennacake no le gusto

Linux se lanzo en virtud de la licencia publica del GNU asi que era abierto

Linux se convirtio en el estandar *Corre en las 500 computadoras mas grandes que hay*

Se usa mucho para la nube, 1/3 de las maquinas virtuales se basan en Linux 

Los dispositivos móviles están basado en el kernel de Linux 


## Procesos y manejo de memoria

[[Procesos y manejo de memoria]]


 