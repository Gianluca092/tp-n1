# ejercicio 2.39

def calcular_balance_acciones(precios_diarios, operaciones):
    balance_total = 0

    # Recorremos cada tupla de la lista de operaciones
    for tipo, dia in operaciones:
        precio_del_dia = precios_diarios[dia]
        
        # Si compramos, sale dinero (resta)
        if tipo == "compra":
            balance_total -= precio_del_dia
        # Si vendemos, ingresa dinero (suma)
        elif tipo == "venta":
            balance_total += precio_del_dia
            
    return balance_total


#prueba del codigo 

precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]


resultado = calcular_balance_acciones(precios_diarios, operaciones)
print("Balance final (ganancia/pérdida):", resultado)