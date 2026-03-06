#Sistema de gestión de biblioteca Descripción del sistema: Desarrollar un programa completo en Python para gestionar los libros de una biblioteca, aplicando todos los conceptos aprendidos en las secciones anteriores. El sistema debe permitir realizar operaciones básicas de mantenimiento de un catálogo bibliográfico.

#Requisitos funcionales:

#Estructura de datos: Utilizar una lista de diccionarios para almacenar la información de los libros. Cada libro debe contener: id (numérico autoincremental), título, autor, año de publicación y estado de disponibilidad (True/False).
#Funciones principales: o agregar_libro(): Permite registrar un nuevo libro validando que el año sea numérico y mayor a 1900. o mostrar_libros(): Muestra todos los libros en formato legible: "ID: 1 - 'Cien años de soledad' (Gabriel García Márquez, 1967) [Disponible]" o buscar_libro(): Permite buscar libros por título o autor, mostrando coincidencias parciales. o prestar_libro(id): Cambia el estado de disponibilidad a False si el libro existe y está disponible. o devolver_libro(id): Cambia el estado de disponibilidad a True. o eliminar_libro(id): Elimina un libro solo si no está prestado actualmente. o menu_principal(): Implementa un menú interactivo con las opciones anteriores utilizando while para repetir hasta que se seleccione salir.
#Funciones adicionales desafiantes: o libros_por_autor(autor): Lista todos los libros de un autor específico. o estadisticas(): Muestra estadísticas del sistema: cantidad total de libros, libros disponibles y libros prestados. o exportar_a_txt(): Guarda todos los libros en un archivo de texto llamado "biblioteca.txt".

from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.CYAN + Style.BRIGHT + "Sistema de Gestión de Biblioteca")
print(Fore.YELLOW + "===========================================")

# Lista global que almacenará los libros
biblioteca = []

# Variable global para ID autoincremental
contador_id = 1


# ==============================
# FUNCIONES PRINCIPALES
# ==============================

def agregar_libro():
    #Permite agregar un nuevo libro a la biblioteca
    global contador_id

    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")

    # Validación del año
    while True:
        anio = input("Ingrese el año de publicación: ")
        if anio.isdigit() and int(anio) > 1900:
            anio = int(anio)
            break
        else:
            print("Año inválido. Debe ser numérico y mayor a 1900.")

    # Crear diccionario del libro
    libro = {
        "id": contador_id,
        "titulo": titulo,
        "autor": autor,
        "anio": anio,
        "disponible": True
    }

    biblioteca.append(libro)
    contador_id += 1

    print("Libro agregado correctamente.\n")


def mostrar_libros():
    #Muestra todos los libros en formato legible
    if not biblioteca:
        print("No hay libros registrados.\n")
        return

    for libro in biblioteca:
        estado = "Disponible" if libro["disponible"] else "Prestado"
        print(f"ID: {libro['id']} - '{libro['titulo']}' "
            f"({libro['autor']}, {libro['anio']}) [{estado}]")
    print()


def buscar_libro():
    #Busca libros por título o autor (coincidencias parciales)
    texto = input("Ingrese título o autor a buscar: ").lower()

    encontrados = False

    for libro in biblioteca:
        if (texto in libro["titulo"].lower() or
                texto in libro["autor"].lower()):
            estado = "Disponible" if libro["disponible"] else "Prestado"
            print(f"ID: {libro['id']} - '{libro['titulo']}' "
                f"({libro['autor']}, {libro['anio']}) [{estado}]")
            encontrados = True

    if not encontrados:
        print("No se encontraron coincidencias.")
    print()


def prestar_libro():
    #Marca un libro como prestado
    try:
        id_buscar = int(input("Ingrese el ID del libro a prestar: "))
    except ValueError:
        print("ID inválido.\n")
        return

    for libro in biblioteca:
        if libro["id"] == id_buscar:
            if libro["disponible"]:
                libro["disponible"] = False
                print("Libro prestado correctamente.\n")
            else:
                print("El libro ya está prestado.\n")
            return

    print("Libro no encontrado.\n")


def devolver_libro():
    #Marca un libro como disponible nuevamente
    try:
        id_buscar = int(input("Ingrese el ID del libro a devolver: "))
    except ValueError:
        print("ID inválido.\n")
        return

    for libro in biblioteca:
        if libro["id"] == id_buscar:
            if not libro["disponible"]:
                libro["disponible"] = True
                print("Libro devuelto correctamente.\n")
            else:
                print("El libro ya estaba disponible.\n")
            return

    print("Libro no encontrado.\n")


def eliminar_libro():
    #Elimina un libro solo si no está prestado
    try:
        id_buscar = int(input("Ingrese el ID del libro a eliminar: "))
    except ValueError:
        print("ID inválido.\n")
        return

    for libro in biblioteca:
        if libro["id"] == id_buscar:
            if libro["disponible"]:
                biblioteca.remove(libro)
                print("Libro eliminado correctamente.\n")
            else:
                print("No se puede eliminar un libro prestado.\n")
            return

    print("Libro no encontrado.\n")


# ==============================
# FUNCIONES ADICIONALES
# ==============================

def libros_por_autor():
    #Muestra todos los libros de un autor específico
    autor_buscar = input("Ingrese el autor: ").lower()
    encontrados = False

    for libro in biblioteca:
        if autor_buscar == libro["autor"].lower():
            estado = "Disponible" if libro["disponible"] else "Prestado"
            print(f"ID: {libro['id']} - '{libro['titulo']}' "
                f"({libro['autor']}, {libro['anio']}) [{estado}]")
            encontrados = True

    if not encontrados:
        print("No se encontraron libros de ese autor.")
    print()


def estadisticas():
    #Muestra estadísticas del sistema
    total = len(biblioteca)
    disponibles = 0
    prestados = 0

    for libro in biblioteca:
        if libro["disponible"]:
            disponibles += 1
        else:
            prestados += 1

    print("Estadísticas:")
    print(f"Total de libros: {total}")
    print(f"Disponibles: {disponibles}")
    print(f"Prestados: {prestados}\n")


def exportar_a_txt():
    #Exporta todos los libros a un archivo biblioteca.txt
    with open("biblioteca.txt", "w", encoding="utf-8") as archivo:
        for libro in biblioteca:
            estado = "Disponible" if libro["disponible"] else "Prestado"
            linea = (f"ID: {libro['id']} - '{libro['titulo']}' "
                    f"({libro['autor']}, {libro['anio']}) [{estado}]\n")
            archivo.write(linea)

    print("Biblioteca exportada a biblioteca.txt\n")


# ==============================
# MENÚ PRINCIPAL
# ==============================

def menu_principal():
    #Menú interactivo del sistema
    while True:
        print("==== SISTEMA DE BIBLIOTECA ====")
        print("1. Agregar libro")
        print("2. Mostrar libros")
        print("3. Buscar libro")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Eliminar libro")
        print("7. Libros por autor")
        print("8. Estadísticas")
        print("9. Exportar a TXT")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            mostrar_libros()
        elif opcion == "3":
            buscar_libro()
        elif opcion == "4":
            prestar_libro()
        elif opcion == "5":
            devolver_libro()
        elif opcion == "6":
            eliminar_libro()
        elif opcion == "7":
            libros_por_autor()
        elif opcion == "8":
            estadisticas()
        elif opcion == "9":
            exportar_a_txt()
        elif opcion == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.\n")


# Ejecutar el programa
menu_principal()