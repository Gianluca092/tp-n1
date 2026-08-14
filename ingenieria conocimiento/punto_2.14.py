# ejercicio 2.14

def registros_temperaturas(temperatura):
    maxima = max(temperatura)
    minima = min(temperatura)
    media = sum(temperatura) / len(temperatura)

    return maxima, minima, media
    
#prueba del codigo

temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

tempa_max, tempa_min, tempa_prom = registros_temperaturas(temperaturas)

print("La temperatura máxima es:", tempa_max)
print("La temperatura mínima es:", tempa_min)
print("La temperatura promedio es:", round(tempa_prom, 2))