# ejercicio 2.17

def filtrar_empleados_por_salario(registro_empleados, salario_minimo):
    empleados_filtrados = {}  # Diccionario nuevo para guardar los resultados

    # .items() nos da tanto el ID (clave) como la tupla (datos)
    for id_empleado, datos in registro_empleados.items():
        # datos[2] es la posición donde está el salario
        if datos[2] > salario_minimo:
            empleados_filtrados[id_empleado] = datos

    return empleados_filtrados


# PRUEBA DEL CÓDIGO

empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

# Buscamos a los que ganen más de 2800
resultado = filtrar_empleados_por_salario(empleados, 2800)

print("Empleados que ganan más de 2800:")
print(resultado)