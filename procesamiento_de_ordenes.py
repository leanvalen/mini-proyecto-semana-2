# Pedidos que llegan como strings simples
ordenes_raw = [
    "Tornillo,50",
    "Tuerca,120",
    "Arandela,200"
]

# Diccionario con los precios de cada producto
precios = {
    "Tornillo": 150.75,
    "Tuerca": 80.50,
    "Arandela": 25.00
}

# Aquí guardarás los resultados
ordenes_procesadas = []

for orden in ordenes_raw:
    partes_orden = orden.split(",")
    nombre_producto = partes_orden[0]
    cantidad_producto = int(partes_orden[1])
    costo_total = precios[nombre_producto] * cantidad_producto
    ordenes_procesadas.append(
        {"producto": nombre_producto, "cantidad": cantidad_producto, "total_orden": costo_total})

print("-----Reporte de ordenes procesadas-----")
# indice = 0
# for producto in ordenes_procesadas:
#     print(
#         f"Producto: {ordenes_procesadas[indice]['producto']} - Cantidad: {ordenes_procesadas[indice]['cantidad']} - Total: {ordenes_procesadas[indice]["total_orden"]}")
#     indice += 1
# El modo más directo de leerlo
print("-----Reporte de ordenes procesadas-----")
for orden_actual in ordenes_procesadas:
    print(
        f"Producto: {orden_actual['producto']} - Cantidad: {orden_actual['cantidad']} - Total: ${orden_actual['total_orden']:.2f}")
