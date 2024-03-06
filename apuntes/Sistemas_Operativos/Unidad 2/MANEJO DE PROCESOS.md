---
~
---
## FIFO

El esquema mas simple de planificación es el primero llegado primero servido, este mecanismo cooperativo con la misma lógica posible cada proceso se ejecuta en el orden en el que fue llegando hasta que suelta el control, Es una cola FIFO

![[Pasted image 20240228122520.png]]

Aquí los que están en colorcito es cuándo se esta ejecutando, el negro son tiempos muertos

## RONDA

La principal diferencia es que este si usa multitarea, cada proceso que este en la lista se ejecuta por un solo quantum. Sino ha terminado de ejcutarse al final de su quantum sera interrumpido y puesto al final de la lsita de procesos para que le toque otra vez, si llegan al mismo tiempo se ejecuta el mas corto

![[Pasted image 20240229180342.png]]

## Proceso mas corto a Continuacion SPN

Cuando no podemos usar la multitarea preventiva pero requerimos un algoritmo mas justo y contamos con informacion por anticipado, podemos elegir el mas corto de los presentes

![[Pasted image 20240229180640.png]]

## Por prioridad 

La prioridad mas alta es la que se sirve, se acaba el proceso actual y después sigo con el siguiente que tenga mas prioridad, si dos procesos tienen la misma prioridad se pasa al que llego antes

![[Pasted image 20240304122121.png]]

https://eduuaa-my.sharepoint.com/:x:/r/personal/clelia_ruiz_edu_uaa_mx/_layouts/15/Doc.aspx?sourcedoc=%7BF71C7E1D-7069-487C-A679-A0970DA80551%7D&file=Algoritmos%20de%20planificaci%C3%B3n%20de%20procesos.xlsx&action=default&mobileredirect=true

## SPN apropiativo 

Es igual al SPN pero cuando quien pero en cuanto llega un proceso mas corto se cambia a ese. Se trabaja con el que le quede menos tiempo

