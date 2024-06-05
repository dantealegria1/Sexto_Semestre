- *Seguridad* es la ausencia de riesgo

- *Proteccion* son los diferentes mecanismos usados por el SO para cuidar la información, proceso, usuarios etc

#### La seguridad va dirigida a 4 requisitos

- Confidencialidad: información de un sistema solo se encuentra accesible para la lectura. Osea que tengan permisos para esto
	- Impresión 
	- Mostrado de datos 
	- Otras formas de observación

- Integridad: Requiere que los contenido solo puedan ser modificadas por partes autorizadas
	- Escritura
	- Cambio
	- Modificaciones de estado
	- Borrado y creación

- Disponibilidad: Requiere que los componentes de un sistema esten disponibles para esas partes autorizadas

- Autentificacion: Requiere que el sistema sea capaz de verificar la identidad de los usuarios

#### Ataques contra la seguridad

Se clasifican considerando las funciones de un sistema informatico como si se tratase de un proveedor de información

- Interrupción: Se destruye un componente o no se encuentre. Centrado en la disponibilidad. Ejem.. La destrucción de una pieza de HW o eliminación de un sistema gestor de archivos

- Intercepcion: Una parte no autorizada consiga acceso a un componente. Centrado a la confidencialidad. Ejem. La escucha de un canal de comunicaciones para capturar datos

- Modificación: Un elemento no autorizado no solo tiene acceso sino que es capaz de modificarlo. Centrado en la integridad. Ejem cambiar valores de ficheros de datos

- Fabricación: Un elemento no autorizado inserta objetos raros, Centrado en la Autentificaron. Ejem inserción de mensajes externos a una red

#### Validacion y amenazas del sistema

- La validacion tiene que ver con
	- Verificacion y autoria del sistema
	- Autentificacion de los ususarios

- Sistemas sofisticados de autentifiacion de usuarios son muy dificiles de evitar

- Un problema es que rechace usuarios legitimos
	- Reconocimiento por huella podria rechazar a alguien quemado

- Deitel 1087 dice que se debe identificar cada flujo de entrada y tipo de dato sea esperado

- Las amenazas se pueden clasificar en 
	- intrusos
	- virus
#### Intrusos

- Enmascarado: Alguien no autorizado se mete a una compu de un usuario legal

- Transgresor: Usuario legitimo que usa sus privilegios de forma maliciosa

- Clandestino: Sobrepasa la revision y usa dicho control para suprimir la recogida de recursos de acceso

Entran adivinando contra: interviniendo lineas, usando troyans, descifrando archivos de contrasenas

Para evitar eso: Establecemos una buena estrategia de eleccion de contras, ya sea generadas por ordenador, inspeccion activa o proactiva

Para detectarlos investigamos actividades inusuales: anomalias estadisticas, deteccion basada en reglas

#### Virus

##### Tipos de amenaza

- Pasiva
	- Revelacion de contenido de mensaje
	- Analisis de trafico
	- Determinar las maquinas que se comunican, frecuencia y longitud de los mensajes

- Activa
	- Alteracion del flujo de mensajes
	- Privacion del servicio
	- Impide el uso normal
	- Suplantacion
##### Seguridad

- Activa
	- Conjunto de medidas que previenen e intentan evitar los danos en los sitemas informaticos
	- Contras, lista de control de acceso, encriptacion, firmas y certificados

- Pasiva
	- Complementa a la activa y se encarga de minimizar los efectos que haya ocasionado algun percance
	- Discos redundantes, copias de seguridad

#### Cifrado

- Aumenta la seguridad de un mensaje mediante la codificacion del contenido, de manera que solo puede leerlo la persona con la clave de cifrado para decodificarla

- Cuando compro en amazon se cifran mis cosas

##### Tecnicas y metodos

- Sustitucion, Reemplazar una o mas unidades de un mensaje por entidades diferentes

	- Monoalfabetica, reemplaza cada letra por otra del alfabeto
	
	- Polialfabetica, Utiliza una serie de cifrados monoalfabeticvos reutilziados periodicamente
	
	- Homofona, hace posible que cada letra del mensaje se corresponda con un grupo de caracteres distintos
	
	- Poligrafica, reemplaza un grupo de caracteres en un mensaje por otro grupo

- Transposicion, Reordena los datos con el fin de hacerlos inintengibles, reordena los datos geometricamente para hacerlos visualmente inutilizables

- Simetrico, usa la misma clave para cifrarlo y descifrado, consiste en aplicar una operacion a los datos que se quieran cifrar utilizando una clave privaeda para hacerlos intangibles puedecrear un sistema a prueba de falsificaciones

- Asimetrico, Es un criptosistema asimetrico las claves de dan por pares. una publica para el cifradfo y una secreta para el descifrado

Es un sistema con clave publica, los usuarios eligen una clave aleatorio que solo ellos conoces. apartir de esa automaticamente se deduce un algoritmo. Los usuarios intercambian esta clave publica mediante un canal no seguro

Otras tecnicas 
- Cesar
- Gronsfeld
- RSA
- DES
- SKIPJAK
- Chaffing & winnowing