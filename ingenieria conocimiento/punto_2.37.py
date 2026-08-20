# ejercicio 2.37


def filtrar_hashtags_populares(hashtags, tendencias, limite_minimo):
    # Convertimos la lista de tuplas a un diccionario para buscar rápido su frecuencia base
    frecuencias = dict(tendencias)
    
    # Sumamos las apariciones del array de hashtags a la frecuencia existente
    for tag in hashtags:
        frecuencias[tag] = frecuencias.get(tag, 0) + 1
        
    # Filtramos los que superan el límite indicado
    populares = []
    for tag, total in frecuencias.items():
        if total > limite_minimo:
            populares.append(tag)
            
    return populares


# Prueba del código
hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]
limite = 100  # Cantidad mínima de menciones

resultado = filtrar_hashtags_populares(hashtags, tendencias, limite)
print(resultado)