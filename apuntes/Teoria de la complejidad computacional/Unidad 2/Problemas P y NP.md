### Problema P

- P es el conjunto de problemas que se resuelven en una *maquina de Turing determinística* y el algoritmo para resolverlo tiene una complejidad polinomial O(p) donde p es un polinomio 

##### Ejemplos:

- Un ejemplo clásico de un problema polinomial es el problema de la suma de dos números. Dado un conjunto de números enteros, ¿hay dos de ellos cuya suma sea igual a un valor específico �k? Este problema se puede resolver en tiempo polinomial utilizando un algoritmo de fuerza bruta que verifica todas las posibles combinaciones de pares de números.

- Sea U un conjunto de números naturales cuya cardinalidad es par encuentre dos subconjuntos A y B tal que $A\cup B$ tal que $A\cap B= vacio$ y $A\cup B=U$ de tal forma que $|A| = |B|$ y $\max (|\sum ai - \sum bi |)$ . No se adivina por que para resolverlo solamente tenemos que hacer es:
	- Ordenar de menor a mayor
	- Sumar los primeros n/2 números
	- Segundo n/2 números y hacer hasta el valor máximo e imprimir 

### Problema NP

- NP es el conjunto de problemas que se necesita implementar en una *maquina de Turing no determinista* y el algoritmo que comprueba si un resultado obtenido es una solución tiene una complejidad polinomial, es decir O(Pk). Aquí se tiene que adivinar

##### Ejemplos:

- **Problema No Polinomial (NP):** Un ejemplo clásico de un problema no polinomial es el problema del subconjunto, también conocido como el Problema de la Suma de Subconjuntos (Subset Sum). Dado un conjunto de números enteros, ¿hay un subconjunto de ellos cuya suma sea igual a un valor específico �k? Este problema es conocido por ser NP-completo, lo que significa que cualquier problema en la clase NP (problemas cuya solución se puede verificar en tiempo polinomial) se puede reducir a él en tiempo polinomial. Aunque la verificación de la solución es polinomial, no se conoce un algoritmo eficiente para encontrar la solución en tiempo polinomial para instancias generales de este problema.

![[Pasted image 20240404082719.png]]
### Problemas NP-Completos

- Imposible encontrar un algoritmo eficiente para encontrar una solución optima
- Ejemplos:
	- Agente viajero
	- Mochila
- Que este en la lista de problemas
- https://mahtblog.wordpress.com/2012/02/29/np-para-no-matematicos/
### Diferencias

| Problemas P                                                 | Problemas NP                                                           | P. NP Completos                                     |
| ----------------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------- |
| Existe un algoritmo de tiempo polinomial para su resolucion | Sus mejores algoritmos conocidos son no deterministas                  | Imposible encontrar un algoritmo eficiente          |
| El tiempo de ejecucion esta dado por un polinomio           | Puede usar un algoritmo polinomico para ver si su solucion es correcta | Se basa en el concepto de transformacion polinomial |
| Ej. Factorial, busqueda secuencial                          | Ej. Ordenamiento por Shell                                             | Ej. Vendedor viajero, mochila etc                   |
