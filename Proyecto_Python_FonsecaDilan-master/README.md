\# Gestor de Inventario para una Biblioteca Virtual



\## Descripción



Este proyecto es un programa hecho en Python que permite gestionar una biblioteca virtual desde la consola. La idea es poder registrar libros, ver el inventario, buscarlos, prestarlos y devolverlos sin necesidad de usar papel.



Toda la información se guarda en archivos JSON, lo que permite que los datos no se pierdan cuando se cierra el programa.



===



\## Funcionalidades



El sistema permite:



\- Registrar nuevos libros con su información

\- Ver todos los libros del inventario

\- Buscar libros por título, autor o género

\- Prestar libros a un usuario

\- Devolver libros prestados

\- Generar un reporte del inventario



===



\## Estructura del proyecto



Gestor\_Biblioteca\_Virtual/

│

├── main.py

├── gestion\_libros.py

├── buscar\_libros.py

├── prestamos.py

├── reportes.py

│

├── data/

│ ├── libros.json

│ └── reportes/

│ └── reporte\_libros\_2026.json





===



\## Cómo ejecutar el programa



1\. Abrir la carpeta del proyecto

2\. Ejecutar el archivo principal:



python main.py





===



\## Ejemplo de uso



\### Menú principal



&#x20;  1. Registrar un nuevo libro



&#x20;  2. Ver el inventario de libros



&#x20;  3. Buscar un libro



&#x20;  4. Prestar un libro



&#x20;  5. Devolver un libro



&#x20;  6. Generar un reporte del inventario



&#x20;  7. Salir





===



\### Registrar un libro



El usuario ingresa los datos del libro:



Titulo: El Hobbit

Autor: J.R.R. Tolkien

Genero: Fantasía

Año: 1937





Luego el sistema lo guarda en el archivo JSON.



===



\### Buscar un libro



Ejemplo:



Fantasía





Salida:



Libros encontrados en la categoría "Fantasía":



&#x20;   El Hobbit | Autor: J.R.R. Tolkien | Estado: Disponible





===



\### Prestar un libro



El sistema cambia el estado del libro a "Prestado" y guarda el nombre del usuario.



===



\### Devolver un libro



El libro vuelve a estar disponible y se elimina el nombre del usuario.



===



\### Generar reporte



Se muestra un resumen en consola y también se guarda en un archivo JSON dentro de la carpeta `data/reportes`.



===



\## Herramientas que se utilizo

\- Python

\- Archivos JSON



===



\## Posibles mejoras



\- Agregar interfaz gráfica

\- Usar base de datos en lugar de JSON

\- Manejar usuarios

\- Mejorar el diseño del programa



===



\## Autor



Nombre: Dilan Fonseca



===



\## Comentario final



Este proyecto me ayudó a entender cómo manejar archivos JSON, trabajar con listas y diccionarios,

y organizar un programa en varios archivos para que sea más claro. 

