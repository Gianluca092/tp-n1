# ejrcicio 2.32 

# Ejercicio simular ventas con *args

def simular_ventas(*ventas):
    total_ingresos = 0.0
    
    # Recorremos cada tupla de ventas que llega en *args
    for producto, cantidad, precio_unidad in ventas:
        total_ingresos += cantidad * precio_unidad
        
    return total_ingresos


# Prueba del código
resultado = simular_ventas(
    ("Producto A", 10, 15.0),
    ("Producto B", 5, 25.0),
    ("Producto C", 3, 50.0)
)

print("Total de ingresos:", resultado)

