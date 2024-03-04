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

Una sentencia *if-then-else* consiste de una condición que hay que testear, de una parte if, que se ejecuta solo si la condición es verdadera, y de una parte (opcional) else, que solo se ejecuta cuando la condición es falsa. *Normalmente la condición consume un tiempo O(1), salvo que haya una llamada dentro de ella.*

```C++
//Aqui seria O(1)
If A[1,1] = 0 Then 
	//O(n)
	(2) For i := 1 to n do 
		//O(n)
		(3) For j := 1 to n do
			(4) A[i,j] := 0
//O(1)
Else 
	//O(n)
	(5) For i := 1 to n do 
		(6) A[i,i] := 1
```

En este caso usamos el peor caso que es que entre al if. Entonces su complejidad es de $$0(n^2)$$
``` c
(1) i := 1
(2) while x <> A[i] do
(3) i := i+1
```

Este código busca en un array de tamaño N un elemento de valor X. En el peor de los casos el ciclo while puede ejecutarse N veces y en el mejor sea de O(1) ósea que lo encuentre a la primera


```c
//O(n-1)
For i := 1 to n-1 do begin
	//O(1)		
	(2) chico := i 
	//O(n)
	(3) For j := i+1 to n do 
		//O(1)
		(4) If A[j] < A[chico] Then 
			(5) chico := j 
	//O(1)
	(6) Temp := A[chico]
	(7) A[chico] := A[i] 
	(8) A[i] := temp 
end
```

El resto es lo mismo. Como el lazo mas exterior se hace n-1 veces, si multiplicamos n-1 por O(n), obtenemos O(n 2 -n). Pero O(n 2 ) es una cota superior de O(n 2 -n), y por lo tanto el tiempo de ejecución de este algoritmo es $$O(n^2 ).$$
  
