#ejercicio 2.27

def ventas_anual(ventas):

    total_ventas = sum(ventas)
    promedio_ventas = total_ventas / len(ventas)

    venta_maxima = max(ventas)
    mes_mayor = ventas.index(venta_maxima) + 1

    analisis = {

    "total de ventas en el ano: ": total_ventas,
    "mayor venta del ano fue en el mes: ": mes_mayor,
    "promedio de ventas en el ano: ": round(promedio_ventas, 2)
    }

    return analisis
 

    


#prueba del codigo

ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]
resultado = ventas_anual(ventas_mensuales)

print(resultado)

