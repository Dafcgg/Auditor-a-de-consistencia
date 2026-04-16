from gestion_libros import cargar, guardar


def prestar():
    libros = cargar()

    titulo = input("-Ingrese el título del libro: ")

    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():

            if libro["estado"] == "Disponible":
                usuario = input("-Ingrese el nombre del usuario: ")
                
                libro["estado"] = "Prestado"
                libro["prestado_a"] = usuario

                guardar(libros)
                print(f'\nLibro "{libro["titulo"]}" prestado a {usuario}.\n')
            
            else:
                print("-El libro ya está prestado.\n")

            return

    print("-Libro no encontrado.\n")


     

def devolver():
    libros = cargar()

    titulo = input("-Ingrese el título del libro: ")

    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():

            if libro["estado"] == "Prestado":
                libro["estado"] = "Disponible"
                libro["prestado_a"] = ""


                guardar(libros)
                print(f'\nLibro "{libro["titulo"]}" ha sido devuelto.\n')
            
            else:
                print("-El libro ya está disponible.\n")

            return

    print("-Libro no encontrado.\n")

