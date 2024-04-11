### Hilos
- Unidad basica del CPU
- Tiene
	- ID
	- Conjunto de registros
	- Pila
	- Contador del programa
- Son ligeros
- Un proceso puede tener varios hilos
- Son pedazos del proceso
#### Ventajas
- Tiempo de respuesta mejor
- Comparte recursos
- Economicos
- Utilizacion de multiples cpu
#### Tipos
- Nivel usuario
	- Son de alguna libreria
- Nivel de kernel
	-  Creados/gestionados por el SO

#### Formas de relacionar el kernel y el usuario
- Multiples hilos de usuario a un hilo de kernel
	- Los hilos a nivel de usuario son estos
	- Si se detiene el hilo de kernel se bloquea todo
- 1 a 1
		- 1 de usuario a 1 de kernel
		- Mejor concurrencia
		- Limite de hilos
- Muchos a muchos
	- Se multiplexean muchos hilos de usuario a igual o menor numero de hilos de kernel
#### Microkernel
- Nucleo del SO que provee instrucciones minimas al sistema que permite implementación de servicios básicos
-  Se divide en core system y plug ins
##### Ventajas
- Testabilidad
- Despliegue
- Dinamismo
- Modular
- Reutilizable
##### Desventajas
- No es escalable
- Complejo

### Concurrencia
- Dos o mas eventos cuyo orden no es determinista
##### Conceptos
- *Operacion atomica:*
	- Los hilos no pueden dividirse en varias partes
- *Seccion critica*
	- Area del codigo que requiere ser protegida de accesos simultaneos
- *Condicion de carrera*
	- Categoria de errores de programacion que involucra dos procesos que fallan al comunicarse su estado mutuo, dando resultados inconsistentes
- *Recursos compartidos*
	- Recurso que puede tener acceso desde mas de un proceso, es una variable en memoria usualmente
##### Mecanismos principales
- *Usar bandera*
	- Una variable dice si hay proceso en la region critica, no funciona
- *Utilizar turnos*
	- Usar una variable adicional que diga que proceso le toca avanzar
- *Peterson*
	- 