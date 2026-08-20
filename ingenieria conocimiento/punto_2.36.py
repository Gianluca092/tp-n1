# ejercicio 2.36

# Ejercicio gestión de inventario con **kwargs



def actualizar_inventario(tienda, **kwargs):
    # Verificamos si la tienda existe en el inventario
    if tienda in inventario:
        # Recorremos los productos y las cantidades que vienen en **kwargs
        for producto, cantidad in kwargs.items():
            # Si el producto ya existe en la tienda, sumamos la cantidad (positiva o negativa)
            if producto in inventario[tienda]:
                inventario[tienda][producto] += cantidad
            else:
                # Si el producto no existía, lo inicializamos con esa cantidad
                inventario[tienda][producto] = cantidad
                
    return inventario


# Prueba del código

inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}

resultado = actualizar_inventario(tienda="Tienda A", producto_1=10, producto_2=-5)
print(resultado)