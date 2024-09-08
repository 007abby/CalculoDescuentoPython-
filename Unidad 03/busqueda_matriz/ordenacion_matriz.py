# Matriz bidimensional de ejemplo (3x3)
matriz = [
    [30, 10, 20],
    [60, 40, 50],
    [90, 70, 80]
]

# Función para ordenar una fila de la matriz
def ordenar_fila(matriz, fila):
    matriz[fila].sort()
    return matriz

# Fila a ordenar (0 para la primera fila, 1 para la segunda, etc.)
fila_a_ordenar = 1

# Mostrar la matriz antes de la ordenación
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila seleccionada
matriz_ordenada = ordenar_fila(matriz, fila_a_ordenar)

# Mostrar la matriz después de la ordenación
print("\nMatriz después de ordenar la fila", fila_a_ordenar + 1, ":")
for fila in matriz_ordenada:
    print(fila)
