#ejercicio 2.40

def ranking_estudiantes(estudiantes):
    lista_promedios = []

    # Recorremos cada ID de estudiante y su diccionario de materias
    for estudiante_id, materias in estudiantes.items():
        todas_las_notas = []
        
        # Juntamos todas las notas de todas las materias del estudiante
        for notas in materias.values():
            todas_las_notas.extend(notas)
            
        # Calculamos el promedio general
        promedio_general = sum(todas_las_notas) / len(todas_las_notas)
        
        # Guardamos la tupla (ID, promedio redondeado a 2 decimales)
        lista_promedios.append((estudiante_id, round(promedio_general, 2)))

    # Ordenamos de mayor a menor según el promedio (posición 1 de la tupla)
    ranking = sorted(lista_promedios, key=lambda x: x[1], reverse=True)

    return ranking


# prueba del codigo
estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

resultado = ranking_estudiantes(estudiantes)
print("Ranking de estudiantes:", resultado)