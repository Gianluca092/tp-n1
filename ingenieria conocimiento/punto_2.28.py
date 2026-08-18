# ejercicio 2.28

def registros_libros(biblioteca):

    libros = []

    for titulo, info in biblioteca.items():
        if info["año"] > 2000:
         libros.append(titulo)

    return libros 

#prueba del codigo 

biblioteca = {

"El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}

}

resultado = registros_libros(biblioteca)
print("los libros que salieron despues del 2000 son: ", resultado)
   