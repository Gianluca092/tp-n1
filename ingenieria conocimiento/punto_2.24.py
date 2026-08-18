# ejercicio 2.24

def organizador_eventos(*eventos):

    for numero, evento in enumerate(eventos, start=1):
        print(f"{numero}. {evento}")

#prueba del codigo 

organizador_eventos("conciertos", "exposicion de arte", "conferencia")
