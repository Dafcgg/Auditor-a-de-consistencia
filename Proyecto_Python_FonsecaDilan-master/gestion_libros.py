import json
from config import RUTA_LIBROS

def cargar():
    try:
        with open("RUTA_LIBROS", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except:
        return []


def guardar(libros):
    with open("RUTA_LIBROS", "w", encoding="utf-8") as file:
        json.dump(libros, file, indent=4, ensure_ascii=False)

def registrar():
    libros = cargar() 

    titulo = input("-Titulo: ")

    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            print("-Ese libro ya existe")
            return

    autor = input("-Autor: ")
    genero = input("-Genero: ")
    año = input("-Año: ")

    libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "publicacion": año,
        "estado": "Disponible",
        "prestado_a": ""
    }

    libros.append(libro)
    guardar(libros)

    print("-Libro registrado.")


def ver_inventario():
    libros = cargar()

    if not libros:
        print("-No hay libros.\n")
        return

    print("==========================================================================================")
    print("| Título                     | Autor                     | Género         | Estado       |")
    print("==========================================================================================")

    for libro in libros:
        estado = libro["estado"]

        if estado == "Prestado":
            estado += " a " + libro["prestado_a"]

        print(f"| {libro['titulo'][:25]:25} | {libro['autor'][:25]:25} | {libro['genero'][:15]:15} | {estado[:25]:12} |\n")

    print("======================================================================================\n")



    