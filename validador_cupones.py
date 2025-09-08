total_compra = 8000
cupon = "DTO15"
es_nuevo_usuario = True
if cupon == "DTO15" and (total_compra > 5000 or es_nuevo_usuario):
    print("Descuento aplicado")
else:
    print("El cupon no es valido para esta compra")
