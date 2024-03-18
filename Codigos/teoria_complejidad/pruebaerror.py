def generar_gray(n):
    if n <= 0:
        return []

    if n == 1:
        return ['0', '1']

    # Generar la secuencia Gray para n-1 elementos
    prev_gray = generar_gray(n - 1)

    # Reflejar la secuencia Gray generada para n-1 elementos
    reflected_gray = prev_gray[::-1]

    # Agregar un bit '0' al frente de la secuencia Gray generada para n-1 elementos
    prev_gray = ['0' + code for code in prev_gray]

    # Agregar un bit '1' al frente de la secuencia Gray reflejada para n-1 elementos
    reflected_gray = ['1' + code for code in reflected_gray]

    # Concatenar las secuencias Gray generada y reflejada
    return prev_gray + reflected_gray

# Generar secuencia Gray para un arreglo de 20 elementos
gray_sequence = generar_gray(3)

# Imprimir la secuencia Gray
for code in gray_sequence:
    print(code)
