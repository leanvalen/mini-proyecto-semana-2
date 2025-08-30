# Lista de tareas pendientes para hoy
tareas = ["Revisar correos", "Preparar reunión",
          "Llamar al cliente", "Actualizar reporte"]

# Diccionario con la prioridad de cada tarea
prioridades = {
    "Revisar correos": "media",
    "Llamar al cliente": "alta",
    "Actualizar reporte": "baja",
    "Preparar reunión": "alta"
}
print(f"Hoy tienes {len(tareas)} tareas pendientes.")
for tarea in tareas:
    print(f"La tarea {tarea} tiene prioridad {prioridades[tarea]}")
