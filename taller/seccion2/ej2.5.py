from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Simulador de Descuentos")
print(Fore.YELLOW + "===========================================")

while True:
    try:
        
        print("\nSeleccione su Categoría:")
        print("1. Categoría: A")
        print("2. Categoría: B")
        print("3. Categoría: C")
        print("4. Otra Categoría")
        print("5. Salir")
        
        opcion = int(input("Ingrese el Número Donde se Encuentra su Categoría: "))
        
        if opcion == 1:
            monto = float(input("Ingrese su Monto de Compra: "))
            cantidad_ahorrada = monto * 0.20
            monto_final = monto - cantidad_ahorrada
            print("La Cantidad Ahorrada es: ", cantidad_ahorrada)
            print("El Monto Final a Pagar es: ", monto_final)
            
        elif opcion == 2:
            monto = float(input("Ingrese su Monto de Compra: "))
            cantidad_ahorrada = monto * 0.15
            monto_final = monto - cantidad_ahorrada
            print("La Cantidad Ahorrada es: ", cantidad_ahorrada)
            print("El Monto Final a Pagar es: ", monto_final)
            
        elif opcion == 3:
            monto = float(input("Ingrese su Monto de Compra: "))
            cantidad_ahorrada = monto * 0.10
            monto_final = monto - cantidad_ahorrada
            print("La Cantidad Ahorrada es: ", cantidad_ahorrada)
            print("El Monto Final a Pagar es: ", monto_final)
            
        elif opcion == 4:
            monto = float(input("Ingrese su Monto de Compra: "))
            cantidad_ahorrada = monto * 0
            monto_final = monto - cantidad_ahorrada
            print("La Cantidad Ahorrada es: ", cantidad_ahorrada)
            print("El Monto Final a Pagar es: ", monto_final)
            
        elif opcion == 5:
            print("Saliendo del Programa. ¡Adiós!")
            break
        
        else:
            print("Opción no Válida. Intente Nuevamente.")
            
    except ValueError:
        print("Error: Debe Ingresar un Número Válido.")