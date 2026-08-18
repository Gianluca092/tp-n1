# ejercicio 2.31

# Ejercicio publicaciones de red social

def publicar(usuario, texto, **kwargs):
    # 1. Creamos el diccionario base con los datos obligatorios
    publicacion = {
        "usuario": usuario,
        "texto": texto
    }
    
    # 2. Agregamos todas las opciones adicionales pasadas en kwargs (etiquetas, visibilidad, likes, etc.)
    publicacion.update(kwargs)
    
    return publicacion


# Prueba del código
resultado = publicar(
    "Juan", 
    "Mi primer post!", 
    etiquetas=["#hola", "#primerPost"], 
    visibilidad="publica", 
    likes=100
)

print(resultado)