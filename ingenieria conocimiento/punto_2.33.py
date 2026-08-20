# ejercicio 2.33

# Ejercicio reservas de hotel

def hacer_reserva(reservas, fecha, huesped, habitacion, precio):
    # Si la fecha ya existe en el diccionario, verificamos las habitaciones ocupadas
    if fecha in reservas:
        for reserva in reservas[fecha]:
            # reserva[1] corresponde al número de habitación
            if reserva[1] == habitacion:
                return f"La habitación {habitacion} no está disponible en la fecha {fecha}."
    else:
        # Si la fecha no existe todavía, creamos una lista vacía para esa fecha
        reservas[fecha] = []

    # Si la habitación está libre, agregamos la tupla con los datos
    reservas[fecha].append((huesped, habitacion, precio))
    return f"Reserva exitosa para {huesped} en la habitación {habitacion} el {fecha}."


# Prueba del código
reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

# 1. Intentar reservar una habitación ocupada (debe rechazar)
print(hacer_reserva(reservas, "2024-08-15", "Carlos", 101, 150))

# 2. Reservar una habitación disponible en fecha existente (debe aceptar)
print(hacer_reserva(reservas, "2024-08-16", "María", 102, 180))

# 3. Reservar en una fecha nueva (debe aceptar)
print(hacer_reserva(reservas, "2024-08-17", "Pedro", 101, 150))