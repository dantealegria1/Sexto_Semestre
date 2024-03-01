---
~
---
## FIFO

El esquema mas simple de planificación es el primero llegado primero servido, este mecanismo cooperativo con la misma lógica posible cada proceso se ejecuta en el orden en el que fue llegando hasta que suelta el control, Es una cola FIFO

![[Pasted image 20240228122520.png]]

Aquí los que están en colorcito es cuándo se esta ejecutando, el negro son tiempos muertos

## RONDA

La principal diferencia es que este si usa multitarea, cada proceso que este en la lista se ejecuta por un solo quantum. Sino ha terminado de ejcutarse al final de su quantum sera interrumpido y puesto al final de la lsita de procesos para que le toque otra vez

![[Pasted image 20240229180342.png]]

## Proceso mas corto a Continuacion SPN

Cuando no podemos usar la multitarea preventiva pero requerimos un algoritmo mas justo y contamos con informacion por anticipado, podemos elegir el mas corto de los presentes

![[Pasted image 20240229180640.png]]