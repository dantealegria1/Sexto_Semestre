https://www.youtube.com/watch?v=zbrXClNX0Yg&ab_channel=ElTallerDeTD
### Sentencias simples
Cualquier sentencia de asignación, lectura, escritura o "go to" tienen ***O(1)*** Anqué sea así una formula gigante si solo son operaciones aritméticas va tener ese tiempo

- Asignación de valores
- Impresiones
- Sumas, restas etc..

### Sentencias ciclos
La complejidad del tiempo es la complejidad del tiempo del cuerpo del ciclo ***O(g(n)*f(n))***

- While
- For
- If

### Ejercicios

```python
#Aqui seria O(n)
if (a[5] < 10){
	for i = 0 to n {
		A[i] = 0
	}
}else
{
#Aqui seria O(n2)
for i = 0 to n {
		for j = 0 to n {
			A[i][j] = A[5]
			}
	}
}
```


Entonces la complejidad del algoritmo seria 
$$O(n) * O(n) = O(n^2)$$
```python
#Aqui es O(n)
For i=0 to n-1 {

	#Aqui es otro O(n)
	for j=0 to n-1 {
	
		#Aqui es o(1)
		if (b[i][j] = 0) then
			b[i][j] = 1
		else
				 b[i][j] = 2
	}
}
```
Entonces la complejidad del algoritmo seria 
$$O(n) * O(n) * O(1) = O(n^2)$$
```python
#O(n)
for i=0 to n-2 {
	#O(n)
	for j=5 to n {
		#O(n)
		For k=0 to n-1 {
			#O(1)
			a = 1
			b = 100
				arreglo[i][j][k] =  a+b+sqrt(a+b)
		}
	}
}
```
Entonces la complejidad del algoritmo seria 
$$O(n) * O(n) *  O(n)* O(1) = O(n^3)$$
``` python
#O(n)
for i=0 to N:
	if i % 2 == 0
		print(i)
#O(n)
for i = 0 to N:
	if i % 2 != 0
	print i
```
Entonces la complejidad del algoritmo seria
$$O(n)+O(n) = O(n)$$
```python
#El valor de N es constante
N = 1000
if N % 2 == 0
	print "par"
else
	print "impar"
```
Entonces la complejidad del algoritmo seria 
$$ O(1)$$
```python
#o(n*m) -> n = max(A,B)
for i = 0 to lenght(A)
	#o(m) -> O(n)
	for j=0 to lenght(B)
	#O(1)
	print(A[i]+" "+B[j])
	#O(a*b) -> O(n2)

```
Entonces la complejidad del algoritmo 
$$O(n)*O(m)=O(n*m)$$ o en su defecto $$ O(n^2) $$
