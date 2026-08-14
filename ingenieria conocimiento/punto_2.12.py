# Ejercicio 2.12


def obtener_producto_mas_caro(lista_productos):
    mas_caro = lista_productos[0]

    for producto in lista_productos:
        if producto[1] > mas_caro[1]:
           mas_caro = producto

    return mas_caro

#prueba de el inventario

productos = [
   ("laptop", 1200, 5),
   ("mouse",25, 50),
   ("teclado",100, 30)
]

resultado = obtener_producto_mas_caro(productos)
print("El producto más caro es", resultado[0], "con un precio de:", resultado[1])
