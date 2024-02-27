### Reglas 

1. Se ignoran constantes
	- O(n/2) = O(n)
2. Dominancia de términos
	- Nos quedamos con el peor caso
	- ![[Pasted image 20240226185744.png]]

***Complejidad constante***
- Es cualquier operación aritmética e imprimir variables

***Complejidad Lineal***
```c++
#Complejiadad de n
for(int i=:i<n:i++)
	#Complejidad de O(1)
	pinrt(arr[i])
```

Entonces: $$n * O(1) = o(n)$$
El *log n* se aplica usualmente cuando el tamaño del problema se reduce a la mitad en cada iteración