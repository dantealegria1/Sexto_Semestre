El primer Sistema Operativo de la historia fue creado en 1956 para un ordenador IBM 704, y básicamente lo único que hacía era comenzar la ejecución de un programa cuando el anterior terminaba
### Primera generacion 1945 - 1955

- Carencia del sistema operativo. El programador interactua diretamente con la maquina mediante computadores
- En los años cincuenta comienza como transicion entre trabajos

### Segunda generacion 1955 - 1965

***transistores y sistemas de procesamiento por lotes***
- Multiprogramacion: varios programas de usuarios se encuentran en el amancenamiento al mismo tiempo
- Multiprocesamiento: varios procesadores se utilizan en el mismo sistema para incrementar el poder de procesamiento
 Aparece la independencia de dispositivo
    - El usuario especifica las caracteristicas que requiere los dispositivos
    - El sistema operativo asigna los dispositivos correspondiente segun los requerimientos
- En **1963**, un equipo del Massachusetts Institute of Technology dirigido por Fernando Corbato desarrolló el sistema CTSS (Compatible Time Sharing System), que fue el primer sistema operativo práctico que permitió a varios usuarios ejecutar varios programas diferentes desde terminales.

### Tercera Generacion 1965 - 1980

***Circuitos integrados y multiprogramacion***
Difusion de la multiprogramacion
    - Particion de la memoria en porciones con trabajos distintos en cada una de ellas
    - Aprovechamiento del tiempo de espera consecuencia de operaciones de c/s para utilizarla CPU para otros procesoos

Emergieron con el desarrollo de los circuitos integrados
Las computadores de nuevo se hacen mas pequeñas

Proteccion por hardware del contenido de cada particion de la memoria
 Aparicion de tecnicas de spooling
    - Simultaneous Peripheral Operation On line
    - Almacenamiento de trabahos de entrada y de salida en dispositivos transitorios rapidos (discos)
    para disminuir el impacto de los perifericos mas lentos

- Son sistemas operativos de modos multiples, osea que tiene proporsitos generales. Son grandes y complejos pero bastantes generales
- Interponen una capa de software enter usuario el hardware
- Aparecen los lenguajes de control de trabaho para especificar trabajos y recursos requeridos
- Soportan timesharing, variante de la multiprogramación con usuarios contectados mediante terminales en linea permitiendo operación
en modo interactivo o conversacional
- Aparecen los sistemas operativos en tiempo real que requieren tiempo de respuesta muy exigente especialmente para usos indsutriales 
militares
- Se difunden las computadoras de rango medio

### Cuarta Generación 1980 - 1990
***Computadoras personales***

Aparece el software amigable con el usuario, destinado a usuarios no personales y con una interfase grafica muy desarrollada
Desarrollo de sistemas operativos de red y sistemas operativos distribuidos

Sistemas operativos de red
    - Están consientes de varias computadoras
    - Cada maquina ejecuta su propio S.0 local
    - Son similares a los S.0 de un solo procesador pero con el agregado de controlar la interfaz de red y su software

Sistemas operativos distribuidos
    - Aparece ante los usuarios como un S.O de un solo procesador aun cuando de soporte a varios procesadores
    - Los usuarios no son consientes del lugar en donde se ejecuta sus programas o donde se encuentra sus
      archivos ya que debe administrar el S.O automáticamente
    - Deben permitir que un programa se ejecute mediante varios procesadores a la vez maximizando el paralelismo

- Aparecen lo emuladores de terminal apra el acceso a equipos remotos desde computadoras personales
- Enfasis en la seguridad en especial para desarrollo de comunicacion de datos
- EL S.O crea un ambiente de trabaho segun el concepto de la aquina virtual que lo aisla del funcionamiento interno de la maquina
- Proliferacion de sistema de base de datos accesibles mediante redes de comunicacion

Windows nt se creo en 1993