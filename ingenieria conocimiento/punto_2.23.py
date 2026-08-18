# ejejercicio 2.23

def inventario_actualizado(inventario, ventas):

    inventario_actualizado = [inv - ven for inv, ven in zip(inventario, ventas)]
    return inventario_actualizado


# prueba del codigo

inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

resultado = inventario_actualizado(inventario, ventas)

print("El resultado actualizado es: ", resultado)



