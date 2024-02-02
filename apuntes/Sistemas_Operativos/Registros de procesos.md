### 31/01/24

Es una abstracción de un programa en ejecución también se le llama tareas. Hay muchas definiciones:

1. Un programa se esta ejecutando
2. Una actividad asincrónica (no se hace en el instante que lo mande)
3. El emplazamiento del control de un procedimiento que esta siendo ejecutando
4. Entidad a la cual están asignando los procesadores
5. Una unidad despacharle (es atendida)

Emplazamiento es que le da un lugar
Despacharle es un estado del sistema operativo
PID Prioridad Tamaño T.I

Un sistema que administra procesos debe poder destruir, suspender, restaurar, cambiar la prioridad, bloquear, despertar y despachar un proceso
En la creación de un proceso se debe asignar un nombre deberá insertarlo en la lista de listos determinar cual es su prioridad inicial, crear el bloque del control de proceso y asignarle los recursos del proceso

En los administradores de tareas
## Procesos

- Google Chrome (10) significa que esta haciendo 10 cosas o ejecutando 10 procesos 
- Conecta memoria USB
- Cuando por ejemplo conecto una memoria USB cambia la prioridad de Google Chrome y lo suspendo, conecto la USB y cuando acabe de conectarla vuelve a poner la prioridad 
- El sistema de prioridades inicia desde la 0, desde mas pequeño el numero mas la prioridad, los procesos del sistema tienen prioridad 0
- El sistema operativo divide las actividades en mas pequeñas por ejemplo si tengo 90 procesos varios de esos se están haciendo procesos sin que yo me de cuenta por ejemplo usar el internet
## KERNEL

![[Pasted image 20240131122947.png]]

El punto central o parte mas importante ya que tiene el control de la maquina. El software responsable de facilitar a los distintos programas el acceso seguro al hardware de la computadora 

### Las funciones del núcleo son:

- La comunicación entre los programas
- Gestión de distintos programas de la maquina
- Gestión de software
- Manipula interrupciones (si estoy jugando y se me va acabar la pila, se manda la señal y el kernel pone en stand by el juego)
- Controla procesos
- Manipula los bloques del control de procesos (toda la información de la maquina)
- Soporte del sistema de archivos
- Soporte de ciertas funciones estadísticas del sistema (ve cuando hay colisiones)

### Memoria principal

- RAM
- ROM
- Cache N1
- Cache N2
- Disco duro o memoria secundaria
- Registros

### Prioridades del sistema

Entre mas arriba en la jerarquía es mas caro por byte
Entre mas arriba  es mas pequeño su almacenamiento
También es mas rápido
Es mas frecuente su uso
Uso de energía para mantener información

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

Siguiente apunte -> [[Memoria cache]]