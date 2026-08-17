# ejercicio 2.20

def configuraciones_app(**kwargs):
    return kwargs


# prueba del codigo 

configuraciones = configuraciones_app(

    modo_oscuro = True,
    idioma = "es",
    notificaciones = False

)

print("configuracion aplicada: ")
print(configuraciones)

