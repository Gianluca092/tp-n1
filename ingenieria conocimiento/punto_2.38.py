# ejercicio 2.38


def actualizar_suscripcion(usuario, suscripcion, **kwargs):
    # Si el usuario no existe en el diccionario, lo creamos con una lista vacía
    if usuario not in suscripciones:
        suscripciones[usuario] = []
        
    # Agregamos la nueva suscripción al historial (array) del usuario
    suscripciones[usuario].append(suscripcion)
    
    # Si vienen opciones adicionales en **kwargs, las agregamos al historial
    if kwargs:
        suscripciones[usuario].append(kwargs)
        
    return suscripciones


# Diccionario base con las suscripciones iniciales
suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

# Prueba del código
resultado = actualizar_suscripcion(usuario="Luis", suscripcion="mensual", auto_renovacion=True)
print(resultado)