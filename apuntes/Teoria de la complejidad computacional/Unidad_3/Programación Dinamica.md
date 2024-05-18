La programación dinámica es una técnica de diseño de algoritmos que se utiliza para resolver problemas complejos dividiéndolos en subproblemas más simples. Se basa en la idea de que los subproblemas se solapan, es decir, los mismos subproblemas se resuelven varias veces. Para evitar la redundancia, la programación dinámica almacena los resultados de los subproblemas ya resueltos, reutilizándolos cuando sea necesario. Esto se conoce como "almacenamiento en caché" o "memorización".

### Componentes de la programación dinámica

1. **División en subproblemas**: Se divide el problema original en subproblemas más pequeños que son más fáciles de resolver.
2. **Solapamiento de subproblemas**: Los mismos subproblemas aparecen una y otra vez.
3. **Almacenamiento de soluciones**: Se almacenan los resultados de los subproblemas ya resueltos para evitar cálculos redundantes.
4. **Construcción de la solución**: La solución del problema original se construye a partir de las soluciones de los subproblemas.

### Tipos de programación dinámica

Hay dos enfoques principales en la programación dinámica:

1. **Memoización (top-down)**:
   - Se resuelve el problema de forma recursiva y se almacena el resultado de cada subproblema en una tabla (generalmente un diccionario o una matriz).
   - Cuando se necesita el resultado de un subproblema ya resuelto, se recupera de la tabla en lugar de volver a calcularlo.
   - Este enfoque comienza desde el problema principal y se descompone en subproblemas más pequeños.

2. **Tabulación (bottom-up)**:
   - Se construye una tabla (matriz) desde los subproblemas más pequeños hasta el problema principal.
   - Se resuelven todos los subproblemas más pequeños primero y se almacenan sus resultados.
   - Finalmente, se utiliza esta tabla para resolver el problema principal.
   - Este enfoque es iterativo y comienza resolviendo los subproblemas más pequeños y utilizando esos resultados para resolver subproblemas más grandes.

### Ejemplo clásico: Fibonacci

El problema de calcular el enésimo número de Fibonacci es un ejemplo clásico para ilustrar la programación dinámica.

#### Enfoque recursivo sin memorización (ineficiente):

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

Este enfoque tiene una complejidad exponencial, ya que recalcula muchas veces los mismos valores de Fibonacci.

#### Enfoque con memorización (top-down):

```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]
```

#### Enfoque de tabulación (bottom-up):

```python
def fibonacci_tab(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
```

### Aplicaciones de la programación dinámica

La programación dinámica se aplica en una variedad de problemas en informática y matemáticas, tales como:

- Problemas de rutas más cortas (como el problema del camino mínimo).
- Problemas de cadenas (como el problema de la subsecuencia común más larga).
- Problemas de optimización (como el problema de la mochila).
- Problemas de corte de barras.
- Problemas de alineación de secuencias en bioinformática.

La clave para utilizar la programación dinámica es identificar si un problema puede ser dividido en subproblemas más pequeños y si estos subproblemas se repiten. Si es así, almacenar los resultados de estos subproblemas puede llevar a una solución mucho más eficiente.