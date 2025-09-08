es_admin = False
es_miembro_vip = True
mensaje_acceso = ""
if es_admin:
    mensaje_acceso = "Tienes acceso total(Admin)"
elif es_miembro_vip:
    mensaje_acceso = "Tienes acceso a contenido exclusivo(VIP)"
else:
    mensaje_acceso = "Tienes acceso limitado(Lector)"

print(mensaje_acceso)
