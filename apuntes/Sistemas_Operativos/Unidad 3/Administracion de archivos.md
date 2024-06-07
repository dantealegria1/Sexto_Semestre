El *Sistema de archivos* proporciona las abstracciones de recursos asociadas con el almacenamiento secundario, crea [ficheros] 

- Existen a largo plazo: Se almacenan en discos secundarios

- Compatible entre procesos: Tienen nombres y pueden pedir permiso de acceso asociados

- Estructura: Dependiendo de archivos un fichero puede tener una estructura interna conveniente para aplicaciones particulares [Jerárquico o mas complejos]

- Tiene muchas funciones como:
	- Crear
	- Borrar
	- Abrir
	- Cerrar
	- Leer
	- Escribir

Los archivos son administrados por el SO se le conoce como sistema de archivos

Desde el punto de vista del usuario el aspecto mas importante es su apariencia es decir como se construye un archivo, como se denominan y protegen los archivos. Lo demas tecnico no interesa pero es importante

#### Asignación de archivos

Varios aspectos estan involucrados:
- Cuando se crea u archivo nuevo
- El espacio se asigna a un archivo como una o mas unidades contiguas. lo que se denomina porcion. El size de una porcion puede ir desde un unico bloque al archivo completo
- Que clase de estructura de datos o tabla se utiliza para guardar traza de las porciones asignadas

##### *Preasignacion frente a asignacion dinamica*
Esta requiere que el size maximo de un archivo sea declarado en tiempo de creación del archivo

##### *Size*
En un extremo se puede asignar una porcion suficientemente grande para contener el archivo completo. En el otro extremo para el especio de disco se puede asignar un bloque cada vez. Para escoger un size debe existir un compromiso entre eficiencia del sistema y desde el puntod e vista del archivo

4 aspectos a considerar para este compromiso 

1. La contigüidad del espacio incrementa el rendimiento
2. Utilizar un gran numero de porciones tiny incrementa el size de las tablas necesarias para gestionar información de asignación
3. Utilizar porciones de size fijo significa reasignación de espacio
4. Utilizar porciones de size variables o tiny de size fijo minimiza el espacio malgastado