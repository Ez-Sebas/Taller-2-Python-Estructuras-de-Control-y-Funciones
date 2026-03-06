#Implementar un sistema de lista de compras que permita al usuario agregar productos, eliminar productos específicos y mostrar todos los productos actuales. Utilizar una lista para almacenar los elementos.

from colorama import init, Fore, Style

init(autoreset=True)

productos = ["Arroz", "Pan", "Huevos", "Pollo", "Leche", "Queso", "Tomate", "Cebolla"]

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Sistema de Lista de Compras")
print(Fore.YELLOW + "===========================================")

while True:
    print("\nProductos actuales:", productos)
    print("\nSelecciona lo que quieres hacer:")
    print("1. Agregar Producto")
    print("2. Eliminar Producto")
    print("3. Mostrar Productos")
    print("4. Salir")

    try:
        opcion = int(input("Selecciona una opción: "))

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

    except ValueError:
        print("Error: Ingresa un número válido.")