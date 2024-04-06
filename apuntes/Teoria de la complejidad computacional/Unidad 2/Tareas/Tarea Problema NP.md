![[Pasted image 20240317165319.png]]


Menor = infinito
n = 3

------------------------------------
Función Leer()

G = [0,0,0,0]
J = [1,2,3,4]

-----------------------------------------------
i = 0

Mientras i < n+1 (4)

**Ciclo 1**

Imprimo G -> [0,0,0,]
i = J[0] -> i = 1
G[1] = G[1] negada -> G[1] = 1
G = [0,1,0]
J[i-1] = J[i] -> J=[2,2,3]
J[i] = i+1 -> J=[2,2,3]
i = 1

**Ciclo 2**

Imprimo G = [0,1,0]
i = J[0] -> i = 2
G[2] = G[2] negada -> G[2] = 1
G = [0,1,1]
J[i-1] = J[i] -> J[2,3,3]
J[i] = i + 1 -> J[2,3,3]
J[0] = 1

**Ciclo 3**

Imprimo G = [0,1,1]
i = J[0] -> i = 1
G[1] = G[1] negada -> G[1] = 0
G = [0,0,1]
J[i-1] = J[i] -> J[3,3,3]
J[i] = i+1 -> J[3,2,3]


**Ciclo 4**

Imprimo G = [0,0,1]
i = J[0] -> i = 3
G[]



