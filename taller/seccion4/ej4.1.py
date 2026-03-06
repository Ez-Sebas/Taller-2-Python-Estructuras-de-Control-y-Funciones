#Implementar un sistema de lista de compras que permita al usuario agregar productos, eliminar productos específicos y mostrar todos los productos actuales. Utilizar una lista para almacenar los elementos.

from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Sistema de Lista de Compras")
print(Fore.YELLOW + "===========================================")

productos = ["Arroz", "Pan", "Huevos", "Pollo", "Leche", "Queso", "Tomate", "Cebolla"]

# Bucle principal que permite administrar la lista de productos mediante un menú
while True:
    print("\nProductos actuales:", productos)
    print("\nSelecciona lo que quieres hacer:")
    print("1. Agregar Producto")
    print("2. Eliminar Producto")
    print("3. Mostrar Productos")
    print("4. Salir")

    try:
        opcion = int(input("Selecciona una opción: "))

        # Permite agregar varios productos a la lista hasta que el usuario escriba "fin"
        if opcion == 1:
            agregados = []
            while True:
                agregar = input("Ingrese producto (o 'fin' para terminar): ")
                if agregar.lower() == "fin":
                    break
                productos.append(agregar)
                print("Producto agregado.")
                agregados.append(agregar)
                print("\nProductos agregados:", agregados)

        # Permite eliminar productos existentes en la lista
        elif opcion == 2:
            eliminados = []
            while True:
                borrar = input("Producto a eliminar (o 'fin' para terminar): ")
                if borrar.lower() == "fin":
                    break
                if borrar in productos:
                    productos.remove(borrar)
                    print("Producto eliminado.")
                    eliminados.append(borrar)
                    print("\nProductos eliminados:", eliminados)
                else:
                    print("Ese producto no está en la lista.")

        elif opcion == 4:
            print("Saliste del programa.")
            break

        else:
            print("Opción inválida.")

    # Maneja errores cuando se ingresa un valor que no es numérico
    except ValueError:
        print("Error: Ingresa un número válido.")