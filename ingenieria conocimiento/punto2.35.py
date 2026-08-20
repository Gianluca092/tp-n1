# ejercicio 2.35

def filtrar_rutas(rutas, distancias_max):
    rutas_validas = []
    
    # zip une cada tupla de ruta con su distancia máxima correspondiente
    for (origen, destino, distancia), limite in zip(rutas, distancias_max):
        if distancia <= limite:
            rutas_validas.append((origen, destino, distancia))
            
    return rutas_validas


# Prueba del código
rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]

resultado = filtrar_rutas(rutas, distancias_max)
print(resultado)
    