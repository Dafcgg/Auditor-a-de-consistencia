import json
import os
from gestion_libros import cargar

def generar_reporte():
    libros = cargar()

    reporte = {}

    for libro in libros:
        genero = libro["genero"]

        if genero not in reporte:
            reporte[genero] = []

        estado = libro["estado"]

        if estado == "Prestado":
            estado = estado + " a " + libro["prestado_a"]

        reporte[genero].append({
            "titulo": libro["titulo"],
            "autor": libro["autor"],
            "estado": estado
        })

    print("==========================================")
    print("    REPORTE DEL INVENTARIO DE LIBROS")
    print("==========================================")

    for genero in reporte:
        print(f"{genero}:")
        for libro in reporte[genero]:
            print(f'- {libro["titulo"]} | Autor: {libro["autor"]} | Estado: {libro["estado"]}')
        print()

    input("-Presione ENTER para continuar...")


    lista_reporte = []

    for genero in reporte:
        lista_reporte.append({
            "categoria": genero,
            "libros": reporte[genero]
        })

        with open("género/data/reportes/reporte_libros_2026.json", "w", encoding="utf-8") as file:
            json.dump(libros, file, indent=4, ensure_ascii=False)

    print("-Reporte guardado en data/reportes/reporte_libros_2026.json\n")




def revisar_estados_libros():
    lista_libros = cargar()

    errores_detectados = []
    
    contador_errores = {
        "ESTADO_INVALIDO": 0,
        "PRESTAMO_SIN_USUARIO": 0,
        "DISPONIBLE_CON_USUARIO": 0
    }

    cantidad_total = len(lista_libros)

    for item in lista_libros:
        nombre_libro = item.get("titulo")
        escritor = item.get("autor")
        estado_actual = item.get("estado", "")
        usuario_asignado = item.get("prestado_a", None)

        tipo_falla = None

        
        if estado_actual not in ["Disponible", "Prestado"]:
            tipo_falla = "ESTADO_INVALIDO"

        elif estado_actual == "Disponible" and usuario_asignado:
            tipo_falla = "DISPONIBLE_CON_USUARIO"

        elif estado_actual == "Prestado" and (usuario_asignado is None or usuario_asignado == ""):
            tipo_falla = "PRESTAMO_SIN_USUARIO"

        
        if tipo_falla:
            errores_detectados.append({
                "titulo": nombre_libro,
                "autor": escritor,
                "estado": estado_actual,
                "prestado_a": usuario_asignado,
                "tipo_error": tipo_falla
            })

            contador_errores[tipo_falla] += 1

   
    informe_final = {
        "lista_errores": errores_detectados,
        "estadisticas": {
            "total_libros": cantidad_total,
            "libros_con_error": len(errores_detectados),
            "errores_por_tipo": contador_errores
        }
    }

   
    with open("género/data/reportes/informe_revision_libros.json", "w", encoding="utf-8") as archivo:
        json.dump(informe_final, archivo, indent=4, ensure_ascii=False)

    print(" Informe generado en data/reportes/informe_revision_libros.json")



