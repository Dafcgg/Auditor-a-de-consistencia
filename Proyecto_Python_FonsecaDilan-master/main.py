import gestion_libros
import buscar_libros
from género import prestamos
from género import reportes



while True:
    print("====================================================")
    print("GESTOR DE INVENTARIO PARA UNA BIBLIOTECA VIRTUAL")
    print("===================================================")
    print("1. Registrar un nuevo libro")
    print("2. Ver el inventario de libros")
    print("3. Buscar un libro")
    print("4. Prestar un libro")
    print("5. Devolver un libro")
    print("6. Generar un reporte del inventario")
    print("7. reporte auditoria de estados")
    print("8. Salir")

    opcion = input("Digite una opción: ")
    print()


    if opcion == "1":
        gestion_libros.registrar()

    elif opcion == "2":
        gestion_libros.ver_inventario()

    elif opcion == "3":
       buscar_libros.buscar()

    
    elif opcion == "4":
       prestamos.prestar()

    elif opcion == "5":
        prestamos.devolver()

    elif opcion == "6":
        reportes.generar_reporte()

    elif opcion =="7":
        reportes.revisar_estados_libros()

    elif opcion == "8":
        salir = input("¿Quieres salir del programa Si/No: ").capitalize()
        if salir == "Si":
            print("-Saliste del programa...\n")
            break
        elif salir == "No":
            print()
            continue
    else:
        print("-Error: No existe la opción.\n")









