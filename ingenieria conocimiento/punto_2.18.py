# ejercicio 2.18

def ventas_diarias(*venta):
 total = sum(venta)
 promedio = total / len(venta)

 return total, promedio

# prueba del codigo

ventas_dia = [200, 450, 300, 400, 350, 500, 600]

total, promedio = ventas_diarias(*ventas_dia)

print("Total de ventas:", total)
print("Promedio de ventas:", round(promedio, 2))