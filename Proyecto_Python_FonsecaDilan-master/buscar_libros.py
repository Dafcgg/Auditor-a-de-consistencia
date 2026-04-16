
from gestion_libros import cargar

def buscar():
    libros = cargar()

    print("-¿Cómo quieres buscar?")
    print("1. Título")
    print("2. Autor")
    print("3. Género")

    opcion = input("-Seleccione: ")
    texto_buscar = input("-Escriba lo que desea buscar: ").lower()

    print("\nResultados:\n")

    encontrado = False

    for libro in libros:

        if opcion == "1":
            texto = libro["titulo"]

        elif opcion == "2":
            texto = libro["autor"]

        elif opcion == "3":
            texto = libro["genero"]

        else:
            print("-Opción inválida")
            return

        if texto_buscar in texto.lower():
            estado = libro["estado"]

            if estado == "Prestado":
                estado = estado + " a " + libro["prestado_a"]

            print(f'- {libro["titulo"]} | Autor: {libro["autor"]} | Estado: {estado}')
            encontrado = True

    if encontrado == False:
        print("-No se encontraron libros.")
