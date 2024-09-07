# Definimos la matriz 3D de temperaturas
temperaturas = [
    [  # Ciudad 1
        [22, 24, 23, 21, 25, 20, 22],  # Semana 1
        [21, 23, 22, 24, 20, 19, 21],  # Semana 2
        [24, 26, 25, 22, 23, 21, 24]   # Semana 3
    ],
    [  # Ciudad 2
        [18, 20, 19, 17, 21, 20, 18],  # Semana 1
        [19, 21, 20, 22, 18, 17, 19],  # Semana 2
        [20, 22, 21, 19, 20, 18, 21]   # Semana 3
    ]
]

# Iteramos sobre las ciudades
for i, ciudad in enumerate(temperaturas):
    print(f"Ciudad {i + 1}:")
    # Iteramos sobre las semanas de la ciudad
    for j, semana in enumerate(ciudad):
        promedio = sum(semana) / len(semana)  # Calculamos el promedio de la semana
        print(f"  Semana {j + 1}: Promedio de temperatura = {promedio:.2f}°C")
