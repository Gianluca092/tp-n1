# ejercicio 2.30

def configurar_perfiles(usuarios, **kwargs):
    perfiles = {}
    
    # Convertimos los pares de configuración (clave, valor) en una lista/array
    configuraciones = list(kwargs.items())
    
    # Asignamos esa lista de configuraciones a cada usuario
    for usuario in usuarios:
        perfiles[usuario] = configuraciones
        
    return perfiles


# Prueba del código
usuarios = ["Ana", "Luis", "María"]

resultado = configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)
print(resultado)

    