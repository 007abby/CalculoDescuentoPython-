# Crear la matriz 3x3
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    # Recorrer cada fila de la matriz
    for i in range(len(matriz)):
        # Recorrer cada columna en la fila
        for j in range(len(matriz[i])):
            # Verificar si el valor en la posición actual es el buscado
            if matriz[i][j] == valor:
                # Retornar la posición si se encontró
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    # Retornar si no se encuentra el valor
    return f"Valor {valor} no encontrado en la matriz."

# Definir el valor que quieres buscar en la matriz
valor_a_buscar = 50

# Llamar a la función de búsqueda y mostrar el resultado
print(buscar_valor(matriz, valor_a_buscar))


