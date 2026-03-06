#Crear un directorio de contactos utilizando diccionarios, donde cada contacto tenga un nombre (clave) y un número telefónico (valor). El sistema debe permitir agregar nuevos contactos, buscar contactos por nombre y eliminar contactos existentes.

from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.CYAN + Style.BRIGHT + "Sistema de Directorio de Contactos")
print(Fore.YELLOW + "===========================================")

contact = {}

# Bucle principal que permite gestionar una agenda de contactos mediante un menú
while True:
    print("\n--- Menú Principal ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos")
    print("5. Salir")
    
    op = input("Elige una opción: ")

    # Evalúa la opción seleccionada y ejecuta la acción correspondiente
    match op:
        case "1":
            name = input("Digite Nombre: ").strip()
            if not name:
                print("El nombre no puede estar vacío.")
                continue

            cel = input("Digite Teléfono: ").strip()
            contact[name] = cel
            print("Contacto agregado correctamente.")

        case "2": 
            name = input("Digite nombre a buscar: ").strip()
            if name in contact:
                print(f"Contacto encontrado: {name} - {contact[name]}")
            else:
                print("Contacto no encontrado.")

        case "3":
            name = input("Digite nombre a eliminar: ").strip()
            if name in contact:
                del contact[name]
                print("Contacto eliminado correctamente.")
            else:
                print("Contacto no encontrado.")

        # Muestra todos los contactos almacenados en el diccionario
        case "4":
            if not contact:
                print("No hay contactos registrados.")
            else:
                print("\nLista de contactos:")
                for name, phone in contact.items():
                    print(f"{name}: {phone}")

        case "5":
            print("Saliendo del sistema...")
            break

        case _:
            print("Opción inválida. Intente nuevamente.")