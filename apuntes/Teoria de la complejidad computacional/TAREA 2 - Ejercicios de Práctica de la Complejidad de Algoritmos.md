
```C++
void main(){ 
	int m;
	#O(1)
	m = 10 * 10; /*producto*/
	printf("%d\n", m); 
}
```

La complejidad de este algoritmo seria O(1) debido a que lo único que hace son operaciones aritméticas

```c++
void main() { 
	int i, j, n, m; 
	#O(1)------------------------------------------------------------------------
	m=0;
	scanf("%d", &n); 
	#o(n)----------------------------------------------------------------------------
	for (i=1; i<=n; i++) 
		#O(n)
		for (j=1; j<=n; j++) m++; /*sucesor*/ 
		printf("%d\n", m); 
		}
```

La complejidad de este algoritmo será $$O(1)*O(n)*O(n) = O(n^2) $$
```C++
#include 
#define maxN 1000000 
void main(){ /* invOrd.c */ 
	int i, n, x, X[maxN];
	n=0; /* Inicializa contador de datos (talla) */
	#O(1)--------------------------------------------------------------------------
	printf("Teclear datos (fin: ^D)\n"); /* Lee datos hasta fin de fichero, */ /* los memoriza y actuliza la talla */
	#O(1)--------------------------------------------------------------------------
	while (scanf("%d", &x) != EOF)
		{ X[n]=x; n++; } /* imprime resultados en orden inverso */ 
	#O(n)----------------------------------------------------------------------------
	for (i=n-1; i>=0; i--) 
		rintf("%d ", X[i]); 
		printf("\n"); }
```

La complejidad de este código será $$O(1)+O(n)+O(1) = O(n)$$
```c++
#include <stdio.h> 
# define maxEdad 150 
void main() { /* moda.c: cálculo eficiente de la moda */
	int n,edad,maxFrec,moda, frecs[maxEdad];
	/* Inicaliza contador de datos (talla) y vector de frecuencias */ 
	n=0; 
	#Max edad = n -> O(n) ---------------------------------------------
	for (edad=0; edad<maxEdad; edad++) 
		frecs[edad] = 0; 
	#O(1) ------------------------------------------------------------
	printf("Teclear edades, fin con ^D\n"); /* Lee edades hasta EOF */ 
	#O(1)-------------------------------------------------------------
	while (scanf("%d", &edad) != EOF) 
	/* y actualiza frecuencias */ 
	#O(1)
		if ((edad>=0) && (edad<maxEdad)) {
			 n++; 
			 frecs[edad]++; }
	 maxFrec=0; /* Determina la edad de */ 
	 #O(n)-------------------------------------------------------------
	 for (edad=0; edad<maxEdad; edad++) /* m´axima frecuencia (moda) */ 
		 #O(1)
		 if (frecs[edad] > maxFrec) { 
		 maxFrec=frecs[edad];
		  moda=edad; } 
	#O(1)---------------------------------------------------------------
	printf("Leidos %d datos; Moda=%d (frecuencia=%d)\n", n,moda,maxFrec); 
}
```

La complejidad será: $$O(n)+O(1)+O(1)*O(1)+O(n)*O(1)+O(1)=O(n)$$
```c++
#O(n)--------------------------------------------
for j = 2 to n:
	i = j-1
	X=xj
	while X < xi:
		xi=1 + xi
		i+i-1
	xi+1+X
```
La complejidad será:

```c++
c=1; 
#Complejidad de O(log N)-------------------------------------------------------
while (c<N)
{
	#O(1)
	algoritmo de O(1)
	c = 2*c
}
```

La complejidad será: $$O(\log n)*O(1)=O(\log n)$$
Ya que el valor de C se multiplica por dos en cada iteración

```c++
#O(n)---------------------------------------------------
for (int i=0; i < N; i++) 
{ 
	c=i; 
	#O(log c)
	while (c > 0) 
	{ 
		algoritmo_de_O(1) c=c/2;
	} 
}
```

Entonces la complejidad será: $$O(n)*O(\log c)=O(n \log c)$$
Por la misma razón que se divide c entre 2


![[Pasted image 20240227180942.png]]

 Este algoritmo lo que esta haciendo es ordenar de menor a mayor los números dentro de un vector. El numero de comparaciones depende del tamaño de ese vector

![[Pasted image 20240302224812.png]]