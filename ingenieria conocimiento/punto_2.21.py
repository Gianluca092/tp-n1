# ejeercicio 2.21

def ordenar_por_puntuacion(lista_puntuaciones):
    # key=lambda x: x[1] indica que ordene mirando la posición 1 (la nota)
    # reverse=True hace que el orden sea de mayor a menor
    lista_ordenada = sorted(lista_puntuaciones, key=lambda x: x[1], reverse=True)

    return lista_ordenada


# PRUEBA DEL CÓDIGO

puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]

resultado = ordenar_por_puntuacion(puntuaciones)
print(resultado)