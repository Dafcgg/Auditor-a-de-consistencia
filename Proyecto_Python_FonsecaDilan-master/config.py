import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

RUTA_LIBROS = os.path.join(DATA_DIR, "libros.json")

REPORTES_DIR = os.path.join(DATA_DIR, "reportes")


RUTA_REPORTE_LIBROS = os.path.join(REPORTES_DIR, "reporte_libros_2026.json")
RUTA_INFORME_LIBROS = os.path.join(REPORTES_DIR, "informe_revision_libros.json")

