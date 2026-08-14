# ejercicio 2.15

def calcular_promedio(*notas):
    promedio = sum(notas) / len(notas)
    return promedio

# prueba del codigo

promedio_estudiante1 = calcular_promedio(85, 90, 78, 92)
print("El promedio del estudiante 1 es:", round(promedio_estudiante1))