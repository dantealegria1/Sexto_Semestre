La filosofia jerarquía se basa en
- Que las funciones del sistema operativo deberán estar separadas dependiendo de su complejidad, su escala de tiempo, características y su nivel de abstracción. Conduce a una organización del sistema operativo en una serie de niveles

Un dispositivo orientado a caracteres
- Transmite solo bit por bit sin estructura de bloques. Impresoras puertos de comunicación, mouse, la mayoría de los dispositivos de almacenamiento secundario

Buffer unico
- Se almacenan datos leidos escritos del o al dispositivo
- Permite sacar el proceso de memoria
- Permite realizar lectura o escritura anticipada

Buffer doble
- Se usan 2 buffers
- Permite leer o escribir de un buffer mientras el SO hace otra cosa en el otro

La manera en que se estructuran, denominan, abren, utilizan, protegen, implementan y administran los archivos son tópicos fundamentales en
- El design de sistemas operativos

El uso de buffers es una tecnica que
- Amortigua los picos en la demanda de E/S

Hay cinco organizaciones fundamentales en la organización de ficheros

El derecho de accesod e archivo conocimiento es aquel que:
- El usuario puede determinar si el fichero existe y quien es su propietario. El usuario entonces es capaz de solicitar acceso

Los archivos tienen nombres y pueden tener permiso de acceso asociados que permitan controlar la compartición. Esta propiedad de archivos es:
- Compatible entre procesos

Organización de ficheros
- Estructura logica de los registros determinados por la forma en la que accedes

Son los 4 aspectos a considerar para el compromiso entre la eficiencia desde el punto de vista de un único archivo y la eficiencia del sistema completo
1. La contigüidad del espacio incrementa el rendimiento  
2. Utilizar un gran número de porciones pequeñas incrementa el tamaño de las tablas.  
3. Utilizar porciones de tamaño fijo simplifica la reasignación de espacio.  ​  
4. Utilizar porciones de tamaño variable o pequeñas de tamaño fijo minimiza el espacio malgastado.

El acceso simultaneo es
- Cuando se garantiza acceso de adición o actualización de un fichero a mas de un usuario el sistema operativo o sistema de gestion debe forzar una disciplina

Asignacion de ficheros que tipicamente se realiza a nivel de bloques individuales cada bloque contiene un puntero al siguiente bloque de cadena
- Asignación encadenada

Los archivos (Ficheros) se almacenan en discos u otro almacenamiento secundario y no desaparece cuando u usuario se desconecta
- Existencia a largo plazo

Se pueden proporcionar diferentes accesos a distintas clases de usuarios
- Usuario especifico, grupo de usuario y todos

RAID
- Cuando se usan multiples discos, es un vector de discos redundantes

La eficacia es importante en el design de modulo de E/S por
- Es importante debido a que las operaciones de E/S significan cuello de botella. La mayoria son muy lentos comparados con la memoria principal

La generalidad en el diseño de modulo de E/S se refiere a:
- en aras de la simplicidad y la eliminación de errores, es deseable manejar todos los dispositivos de manera uniforme 


Un dispositivo orientado a bloques
- Almacena la informacion en bloques que son de size fijo realizandose la transferencia de bloque en bloque por ejemplo discos y cintas

El manejador de dispositivos
- Proporciona una interfaz de software con el hardware, lo que permite a los sistemas operativos y a otros programas informaticos acceder a las funciones de hardware sin necesidad de conocer detalles del hardware. 

Lo que se busca atraves de la planificacion de discos es
- reducir tiempos de acceso tanto en la lectura como en la escritura de los datos

RAID designan a diversas arquitecturas de design que comparten 3 caracteristicas comunes
1. Varios discos se ven como uno solo para el S.O
2. Datos distribuidos a lo largo de las unidades fisicas de un vector
3. Capacidad de redundancia del disco para almacenar informacion de paridad

Es la arquitectura de RAID que no tiene redundancia pero mejora la fiabilidad
- Raid 0

En este RAID se consigue la redundancia mediante la simple estrategia de dumplicar todos los datos
- RAID 1

El aspecto de comparticion de archivos de derechos de acceso se refiere a
- El sistema de ficheros deberia proporcionar una herramienta flexible para permitir la comparticion de ficheros extensiva entre los usuarios

Es un vector de acceso paralelo todos los miembros del disco participan en la ejecucion de cada particion de E/S. Es decir en todo momento la cabeza de cada disco esta en la misma posicion en todos los discos
- RAID 2

Es un vector de acceso independiente de manera que se puede servir el paralelo peticiones son mas adecuados para la aplicaciones que requieren tasas elevadas de peticiones de E/S y relativamente menos adecuadas para aquellas que necesitan tasas elevadas de transferencia de datos
- RAID 4

Destruye las bandas de paridad a traves de todos los discos. La asignacion habitual usa un esquema rotatorio. se usa un disco extra para paridad
- RAID 5

RAID que usa dos algoritmos de comprobacion de datos diferentes, proporciona una extremadamente alta disponibilidad de datos
- RAID 6

El derecho de acceso de archivo lectura, es aquel que
- El usuario puede leer el fichero para cualquier proposito incluyendo copia y ejecucion. algunos sistemas son capaces de forzar una distincion entre ver y copiar

Un cache de disco es
- Un buffer en memoria principal para almacenar sectores de disco

En cache de disco el algoritmo mas utilizado es
- El de menos recientemente usado, se reemplaza el bloque que ha estado mas tiempo sin ser accedido

Es la ausencia de un riesgo aplicando esta definicion al tema correspondiente, hace referencia al riesgo de accesos no autorizados, de manipulacion de informacion entre otros
- la seguridad

El derecho de acceso de archivo adicion, es aquel en el que
- El usuario puede agregar datos al fichero solo al final pero no puede modificar o borar cualquiera del contenido, util para recolectar datos de varias fuentes

Son los diferentes mecanismos utilizados por el SO para cuidar la ifnroamcon, los procesos, los ussuarios etc
- La proteccion

El derecho de acceso de archivo ejecucion es aquel en el que
- El usuario puede cargar y ejectuar un programa pero no puede copiarlo

Este requisito de seguridad requiere que la información de un sistema informático solo se encuentre accesible para lectura para aquellas partes, que estén autorizadas a este tipo de acceso. Este tipo de acceso incluye impresión, mostrado de datos y otras formas de observación, incluyendo la simple revelación de la existencia de un elemento.
- Confidencialidad

Este requisito de seguridad requiere que los componentes de un sistema informático estén disponibles para todas aquellas partes autorizadas. ​
- Disponibilidad

Este requisito de seguridad requiere que el sistema informático sea capaz de verificar la identidad de los usuarios.
- Autenticacion


Esta tecnica se conoce como E/S con buffers
- Para evitar las sobrecargas e ineficientes a veces es conveniente realizar la transferencia de entrada antes de que se hagan las peticiones correspondientes y llevar a cabo las transferencias de salida un cierto tiempo despues de que se haya hecho la peticion

Este requisito de seguridad requiere que los contenidos de un sistema informático solo podrán modificarse por las partes que se encuentran autorizadas. Las modificaciones incluyen escritura, cambio, modificación del estado, borrado y creación. ​
- Integridad

Tipo de ataque en el que se destruye un componente del sistema o se encuentra no disponible o utilizable. Es un ataque centrado en la disponibilidad.
- Interrupcion

Tipo de ataque que una parte no autorizada consiga acceso a un componente esto es un ataque dirigido a la confidencialdiad
- Intercepcion

Tipo de ataque en que un elemento no autorizado no solo tiene acceso a un componente sino que tambien es capaz de modificarlo es un ataque que va dirigido a la integridad
- Modificacion

Tipo de ataque en el que un elemento no autorizado inserta objetos raros en el sistema es dirigido a la autenticacion
- Fabricacion 

Las amencasa a la aseguridad en ela cceso al sistema pueden clasificarse en 2
- intrusos
- programas malignos

Individuo que no esta autorizado a utilizar un ordenador y que penetra en ls controles de acceso del sistema para aproecharse de una cuenta de usuario legitima
- Enmascarado

Un usuario legitimo que accede a datos programas o recursos para los cuales dicho acceso no esta autorizazado o si esta autorizado pero usa sus privilegios de forma maliciosa
- transgresor

Un usuario que sobrepasa el control de supervicion del sistema y usa dicho control para suprimir la recogida de registro de acceso
- Usuario clandestino

Tecnicas de intrusion
- Averiguar passwords
- Probar muchas veces
- troyanos
- intervenir lineas

Es un método que permite aumentar la seguridad de un mensaje o de un archivo mediante la codificación del contenido, de manera que sólo pueda leerlo la persona que cuente con la clave de cifrado adecuada para decodificarlo
- Cifrado

Este tipo de cifrado consiste en reemplazar una o mas entidades de un mensaje
- sustitucion

Este cifrado simétrico consiste en utilizar la misma clave para el cifrado y el descifrado. ​

El cifrado consiste en aplicar una operación (un algoritmo) a los datos que se desea cifrar utilizando la clave privada para hacerlos ininteligibles
- cifrado simetrico

Este metodo de cifrado consiste en reordenar datos para cifrarlos a fin de hacerlos ininteligibles
- cifrado de transposicon

Este tipo de seguridad complementa a la seguridad activa y se encarga de minimizar los efectos que haya ocasionado algún percance
- Pasiva

Este tipo de criptosostemas de sustitución consiste en reemplazar cada una de las letras del mensaje por otra letra del alfabeto:
- Homofona?????????

Hay cinco organizaciones fundamentales. en la organización de ficheros:
- Indexado, secuencial, secuencial indexado, acceso directo y la pila

Los archivos tienen nombres y pueden tener permiso de acceso asociados que permitan controlar la comparticion esta propiedad es
- Compatrible entre procesos
- 