# Logs crudos del sistema
logs_raw = [
    "INFO:user_juan:login_success",
    "WARNING:user_ana:login_fail",
    "INFO:user_pedro:view_dashboard",
    "ERROR:user_ana:access_denied",
    "INFO:user_juan:logout"
]

# Diccionario que mapea usuarios a departamentos
mapa_usuarios = {
    "user_juan": "Ventas",
    "user_ana": "Marketing",
    "user_pedro": "IT"
}

# Tupla con los niveles de log considerados críticos
niveles_criticos = ("WARNING", "ERROR")

# Lista con los logs procesados
logs_procesados = []
# Set de usuarios activos
usuarios_activos = set()

for log in logs_raw:
    nivel, usuario, accion = log.split(':')
    usuarios_activos.add(usuario)
    departamento = mapa_usuarios.get(usuario, "Desconocido")
    es_critico = nivel in niveles_criticos
    log_procesado = {"Nivel": nivel, "Usuario": usuario,
                     "Departamento": departamento, "Accion": accion, "Critico": es_critico}
    logs_procesados.append(log_procesado)

print("-----Reporte de logs-----")
print(f"La cantidad de logs procesados es: {len(logs_procesados)}")
print(
    f"La cantidad de usuarios unicos procesados es de: {len(usuarios_activos)}")

for log in logs_procesados:
    if log["Critico"]:
        print(
            f"[!!][{log["Nivel"]}]El usuario {log["Usuario"]} del Dto. {log["Departamento"]} realizo la accion: {log["Accion"]}")
    else:
        print(
            f"[{log["Nivel"]}]El usuario {log["Usuario"]} del Dto. {log["Departamento"]} realizo la accion: {log["Accion"]}")
