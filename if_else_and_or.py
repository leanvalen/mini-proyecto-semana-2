total_compra = 15000
es_cliente_frecuente = False
usa_cupon_envio = True
if total_compra > 10000 or es_cliente_frecuente or usa_cupon_envio:
    print("Envio gratuito")
else:
    print("Costo de envio aplicado")
