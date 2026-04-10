from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.CYAN + Style.BRIGHT + "Gestor de Inventario de Productos")
print(Fore.YELLOW + "===========================================")

productos = {}

# Bucle que permite gestionar productos, precios y stock mediante un menú
while True:
    print("\n--- Menú Principal ---")
    print("1. Agregar Producto")
    print("2. Buscar y Cambiar Precio")
    print("3. Salir")

    op = input("Elige una Opción: ")

    # Evalúa la opción seleccionada para realizar la operación correspondiente
    match op:
        case "1":
            name = input("Digite Nombre del Producto: ").strip()
            price = input("Digite el Precio del Producto: ")
            stock = input("Digite el Stock del Producto: ")

            productos[name] = {
                "Precio": price,
                "Stock": stock
            }

            print("Producto Agregado Correctamente.")
            continue

        # Permite buscar un producto y actualizar su precio
        case "2":
            name = input("Digite el Nombre del Producto a Buscar: ").strip()
            if name in productos:
                print(f"Producto Encontrado: {name} - Precio: {productos[name]['Precio']}, Stock: {productos[name]['Stock']}")
                new_price = input("Digite el Nuevo Precio del Producto: ")
                productos[name]["Precio"] = new_price
                print("Precio Actualizado Correctamente.")
            else:
                print("Producto No Encontrado.")

        case "3":
            print("Saliendo del Sistema...")
            break