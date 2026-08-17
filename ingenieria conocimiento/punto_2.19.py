# ejercicio 2.19

def calcular_goles_temporada(resultados):

    goles_anotados = 0 
    goles_recibidos = 0

    for goles in resultados.values():
        goles_anotados += goles[0] 
        goles_recibidos += goles[1]

    return goles_anotados, goles_recibidos

# PRUEBA DEL CÓDIGO

resultados = {
 "EQUIPO A": (3,2),
 "EQUIPO B": (1,1),
 "EQUIPO C": (4,0)
}
anotados, recibidos = calcular_goles_temporada(resultados)

print(f"Goles anotados en la temporada: {anotados}")
print(f"Goles recibidos en la temporada: {recibidos}")