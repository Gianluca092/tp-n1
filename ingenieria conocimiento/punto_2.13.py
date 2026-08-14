#ejercicio 2.13 

def promedio_estudiantes(registros, matricula):
    # 1 buscamos al estudiante con su numero de matricula
    estudiante = registros[matricula]

    # 2 entramos a su diccionario de notas
    calificaciones = estudiante["calificaciones"]

    # 3 sacamos sus notas para poder calcular el promedio 
    notas = calificaciones.values()

    # 4 calculamos el promedio
    promedio = sum(notas) / len(notas)

    return promedio 

#prueba del codigo

estudiantes = {
101: {"nombre":"Ana", "edad": 16, "calificaciones": {"matematicas": 85, "ciencias":90}},
102: {"nombre": "Luis", "edad": 17, "calificaciones":  {"matematicas": 78, "ciencias": 88}}    
}


ana = promedio_estudiantes(estudiantes, 101)
luis = promedio_estudiantes(estudiantes, 102)

print("El promedio de Ana es:", ana)
print("El promedio de Luis es:", luis)






