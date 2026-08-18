#ejercicio 2.29

def registro_notas(lista_estudiantes):
    promedios = {}

    for nombre, notas in lista_estudiantes:
        promedio = sum(notas) / len(notas)
        promedios[nombre] = round(promedio , 2)

    return promedios  


#prueba del codigo 

notas_estudiantes = [
    ("Ana", [85,90,78]),
    ("Luis", [88,92,80]),
    ("Maria", [75,85,70 ])
]

resultado = registro_notas(notas_estudiantes)

print(resultado)
    

    