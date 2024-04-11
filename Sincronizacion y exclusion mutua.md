## Mecanismos principales

- Los mecanismos principales para problemas que implican el acceso concurrente a una sección critical
### Utilizar bandera

- Una bandera parece ser una solución muy sencilla mediante una variable de bandera si indica si hay un proceso en la region critica, sin embargo no funciona lol
### Utilizar turnos

- Una alternativa para evitar problemas de la actualización múltiple una bandera es emplear una variable adicional que indique que proceso corresponde avanzar en todo momento, esto es utilizar turnos. Así que bien esto soluciona el problema de la actualización múltiple. 

- Un proceso que no esta en la sección puede obligar a que otro proceso espere mucho tiempo para ingresar a la sección critica
## Mecanismos de sincronacion

### Mutex

- Una de las alternativas para evitar la espera activa a lo que obliga el algoritmo de Peterson se llama mutex o candado

- La palabra mutex nace de la frecuencia con la que se habla de las regiones de exclusión mutua. Es un mecanismo que asegura que cierta región del código será ejecutada como si fuera atómica

- Mutex no implica que el código no se va a interrumpir dentro de la región

- Es un mecanismo de prevención que mantiene en espera cualquier hilo o proceso que quiera entrar a la sección critica protegida hasta que el proceso que esta adentro salga

- Sino hay nadie adentro si podrán ingresar

- Un área de exclusión mutua debe:

	- Ser mínima: Tan corta como puedas 
	- Ser completa: Se debe analizar bien cual área proteger y no arriesgarse a proteger menos
### Semáforos

- En 1968 se propusieron los semáforos
#### Inicializar

- Se puede inicializar el semáforo a cualquier valor entero, pero después de esto su valor no puede ya ser leído, es una estructura abstracta y su valor es tomado como opaco o invisible al programador
#### Decrementar

- Cuando un hilo decrementa el semáforo, si el valor es negativo el hilo se bloquea y no puede continuar hasta que otro hilo incrementé el semáforo. También se le llama wait, down o acquire
#### Incrementar

- Cuando un hilo incrementa el semáforo, si hay hilos esperando uno de ellos es desperado. También se le llama signal, up, relase, post o V
### Bloqueo mutuo e inanición

#### Bloqueo mutuo

- Cuando hay concurrencia hay que asegurarnos aparte de que sea atómico:

- Cuando dos o mas procesos poseen determinados recursos y ambos quedan detenidos, esperando a que el otro acabe. El sistema puede seguir pero ningún proceso puede avanzar
#### Inanición 

- Cuando un proceso no puede avanzar dado que necesita recursos asignados a otros procesos