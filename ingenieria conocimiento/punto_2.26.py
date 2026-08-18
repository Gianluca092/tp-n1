# ejercicio 2.26

def resgistros_de_empleados(nombre, edad, salario, **datos_opcionales):

    empleado = {
        "nombre": nombre,
        "edad": edad, 
        "salario": salario
    }

    empleado.update(datos_opcionales)
    return empleado

#prueba del codigo
 
resultado = resgistros_de_empleados(

    "Ana",
    30,
    3000,
    direccion = "calle falsa 123",
    telefono = "123456789" 
 )

print(resultado)

