# ejercicio 2.23

def valores_viajes(lista_viajes):

    totales_por_destino = {}

    for paquetes in lista_viajes:
        destino = paquetes[0]
        precio = paquetes[1]
        dias = paquetes[2]

        totales_por_destino[destino] = precio * dias

    return totales_por_destino


# prueba del codigo 

paquetes = [

    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
     
 ]   

precio_viajes = valores_viajes(paquetes)

print(precio_viajes)
