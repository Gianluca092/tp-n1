# ejercicio 2.34

def calcular_frecuencias(encuestas):
    frecuencias = {}
    
    # Recorremos cada pregunta y su lista de respuestas
    for pregunta, respuestas in encuestas.items():
        conteo = {}
        
        # Contamos cuántas veces aparece cada valor
        for respuesta in respuestas:
            conteo[respuesta] = conteo.get(respuesta, 0) + 1
            
        frecuencias[pregunta] = conteo
        
    return frecuencias


# Prueba del código
encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

resultado = calcular_frecuencias(encuestas)
print(resultado)