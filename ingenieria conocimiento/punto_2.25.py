# ejercicio 2.25

def analizar_finanzas(**movimientos):
    # .values() extrae solo los números (positivos y negativos)
    balance_final = sum(movimientos.values())
    return balance_final


# PRUEBA DEL CÓDIGO

balance = analizar_finanzas(
    sueldo=2000, 
    renta=-800, 
    transporte=-150, 
    comida=-300, 
    freelance=500
)

print(f"Balance final: ${balance}")