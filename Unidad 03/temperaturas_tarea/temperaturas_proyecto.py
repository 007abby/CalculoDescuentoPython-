# Crear una matriz 3D: Ciudades, Semanas, Días de la semana (7 días)
# Ejemplo con 2 ciudades, 2 semanas, y 7 días por semana.
# Puedes modificar los datos según lo requieras.

# Matriz que contiene temperaturas aleatorias para ejemplo
temperaturas = [
    [  # Ciudad 1
        [20, 21, 19, 23, 20, 18, 22],  # Semana 1 (lunes a domingo)
        [24, 25, 22, 26, 23, 21, 27]   # Semana 2 (lunes a domingo)
    ],
    [  # Ciudad 2
        [15, 16, 17, 18, 19, 20, 21],  # Semana 1 (lunes a domingo)
        [22, 21, 20, 19, 18, 17, 16]   # Semana 2 (lunes a domingo)
    ]
]

# Recorrer la matriz y calcular el promedio semanal para cada ciudad
for ciudad_index, ciudad in enumerate(temperaturas):
    for semana_index, semana in enumerate(ciudad):
        promedio = sum(semana) / len(semana)  # Calcula el promedio de la semana
        print(f"Promedio de la Ciudad {ciudad_index + 1}, Semana {semana_index + 1}: {promedio:.2f}")

