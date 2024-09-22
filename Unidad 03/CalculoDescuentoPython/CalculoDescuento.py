

def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada 1: Solo el monto total
monto1 = 100
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1
print(f"Compra 1 - Monto total: {monto1}, Descuento: {descuento1}, Monto final: {monto_final1}")

# Llamada 2: Monto total y porcentaje de descuento personalizado
monto2 = 200
porcentaje_descuento_personalizado = 15
descuento2 = calcular_descuento(monto2, porcentaje_descuento_personalizado)
monto_final2 = monto2 - descuento2
print(f"Compra 2 - Monto total: {monto2}, Descuento: {descuento2}, Monto final: {monto_final2}")




