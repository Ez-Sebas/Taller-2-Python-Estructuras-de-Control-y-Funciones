from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Expandir Calculadora Básica")
print(Fore.YELLOW + "===========================================")

while True:
    try: 
        print("\nSeleccione una Operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = int(input("Ingrese el Número de la Operación que Desea Realizar: "))
        
        if opcion == 1:
            ingrese_num1 = float(input("Ingrese el Primer Número: "))
            ingrese_num2 = float(input("Ingrese el Segundo Número: "))
            resultado = ingrese_num1 + ingrese_num2
            print(f"El Resultado de la Suma es: {resultado:.2f}")
            
        elif opcion == 2:
            ingrese_num1 = float(input("Ingrese el Primer Número: "))
            ingrese_num2 = float(input("Ingrese el Segundo Número: "))
            resultado = ingrese_num1 - ingrese_num2
            print(f"El Resultado de la Resta es: {resultado:.2f}")
            
        elif opcion == 3:
            ingrese_num1 = float(input("Ingrese el Primer Número: "))
            ingrese_num2 = float(input("Ingrese el Segundo Número: "))
            resultado = ingrese_num1 * ingrese_num2
            print(f"El Resultado de la Multiplicación es: {resultado:.2f}")
            
        elif opcion == 4:
            ingrese_num1 = float(input("Ingrese el Primer Número: "))
            ingrese_num2 = float(input("Ingrese el Segundo Número: "))
            if ingrese_num2 == 0:
                print("Error: No se Puede Dividir Entre Cero")
                continue
            resultado = ingrese_num1 / ingrese_num2
            print(f"El Resultado de la División es: {resultado:.2f}")
            
        elif opcion == 5:
            print("Saliendo del Programa. ¡Adiós!")
            break
        
        else:
            print("Opción no Válida. Intente Nuevamente.")
            
    except ValueError:
        print("Error: Debe Ingresar un Número Válido.")