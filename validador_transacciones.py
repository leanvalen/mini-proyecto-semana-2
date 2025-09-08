# Lista de transacciones crudas en formato "id_usuario,monto,pais"
transacciones_raw = [
    "user001,150.50,AR",
    "user002,2000.00,US",      # Fallará por monto
    "user003,75.20,KP",       # Fallará por país
    "user001,25.10,AR",
    "user004,9.99,MX",        # Fallará por monto
    "user005,120.00,AR",      # Fallará por usuario inactivo
    "user002,50.00,US"        # Usuario desconocido en el mapa
]

# Diccionario con el estado de cada usuario
estado_usuarios = {
    "user001": "activo",
    "user003": "activo",
    "user005": "inactivo"
}

# Set con códigos de países bloqueados
paises_bloqueados = {"KP", "IR", "SY"}

# Tupla que define el rango de montos válidos (mínimo, máximo)
rango_monto_valido = (10.00, 1000.00)

transacciones_rechazadas = []
usuarios_procesados = set()
# datos_transacciones_rechazadas = {}
transacciones_aprobadas = []
# transacciones_procesadas = 0

# for transaccion in transacciones_raw:
#     usuario, monto, pais = transaccion.split(",")
#     monto = float(monto)
#     usuarios_procesados.add(usuario)
#     transacciones_procesadas += 1
#     if (not usuario in estado_usuarios or estado_usuarios[usuario] != "activo"):
#         datos_transacciones_rechazadas = {"Usuario": usuario, "Monto": monto,
#                                           "Pais": pais, "Motivo rechazo": "Usuario inactivo o desconocido"}
#         transacciones_rechazadas.append(datos_transacciones_rechazadas)
#     elif monto < rango_monto_valido[0] or monto > rango_monto_valido[1]:
#         datos_transacciones_rechazadas = {
#             "Usuario": usuario, "Monto": monto, "Pais": pais, "Motivo rechazo": "Monto invalido"}
#         transacciones_rechazadas.append(datos_transacciones_rechazadas)
#     elif pais in paises_bloqueados:
#         datos_transacciones_rechazadas = {
#             "Usuario": usuario, "Monto": monto, "Pais": pais, "Motivo rechazo": "Pais bloqueado"}
#         transacciones_rechazadas.append(datos_transacciones_rechazadas)
#     else:
#         datos_transacciones_aprobadas = {
#             "Usuario": usuario, "Monto": monto, "Pais": pais}
#         transacciones_aprobadas.append(datos_transacciones_aprobadas)

# print("----------------Reporte final de transacciones--------------------")
# print(f"Total de transacciones procesadas: {transacciones_procesadas}")
# print(f"Numero de usuarios unicos vistos: {len(usuarios_procesados)}")
# print(f"Transacciones aprobadas: {len(transacciones_aprobadas)}")
# print(f"Transacciones rechazadas: {len(transacciones_rechazadas)}")
# print("------Detalle de transcciones rechazadas------")
# for transacciones in transacciones_rechazadas:
#     print(
#         f"Transaccion de {transacciones["Usuario"]} por {transacciones["Monto"]} rechazada. Motivo: {transacciones["Motivo rechazo"]}")
# ... (las variables iniciales son las mismas) ...

for transaccion in transacciones_raw:
    usuario, monto_str, pais = transaccion.split(",")
    monto = float(monto_str)
    usuarios_procesados.add(usuario)

    # Paso 1: Primero, determinamos si hay un motivo de rechazo.
    # Empezamos asumiendo que no hay ninguno.
    motivo_rechazo = None

    # Usamos .get() para una búsqueda segura. Si el usuario no existe, devuelve None.
    estado = estado_usuarios.get(usuario)

    # Esto cubre si el usuario es "inactivo" o si no existe (None)
    if estado != "activo":
        motivo_rechazo = "Usuario inactivo o desconocido"
    # Una forma más limpia de chequear el rango
    elif not (rango_monto_valido[0] <= monto <= rango_monto_valido[1]):
        motivo_rechazo = "Monto fuera de rango"
    elif pais in paises_bloqueados:
        motivo_rechazo = "País bloqueado"

    # Paso 2: Actuamos basándonos en si encontramos un motivo o no.
    if motivo_rechazo:
        # Si hay un motivo, construimos el diccionario de rechazo y lo añadimos.
        # Solo escribimos este código UNA VEZ.
        registro_rechazado = {
            "Usuario": usuario,
            "Monto": monto,
            "Motivo": motivo_rechazo
        }
        transacciones_rechazadas.append(registro_rechazado)
    else:
        # Si no hubo ningún motivo de rechazo, la transacción está aprobada.
        registro_aprobado = {
            "Usuario": usuario,
            "Monto": monto,
            "Pais": pais
        }
        transacciones_aprobadas.append(registro_aprobado)

# ... (la sección del reporte final puede quedar igual, es perfecta) ...
# Aunque puedes simplificar el conteo de transacciones procesadas usando len(transacciones_raw)
print("----------------Reporte final de transacciones--------------------")
print(f"Total de transacciones procesadas: {len(transacciones_raw)}")
print(f"Numero de usuarios unicos vistos: {len(usuarios_procesados)}")
print(f"Transacciones aprobadas: {len(transacciones_aprobadas)}")
print(f"Transacciones rechazadas: {len(transacciones_rechazadas)}")
print("------Detalle de transcciones rechazadas------")
for transacciones in transacciones_rechazadas:
    print(
        f"Transaccion de {transacciones["Usuario"]} por {transacciones["Monto"]} rechazada. Motivo: {transacciones["Motivo"]}")
