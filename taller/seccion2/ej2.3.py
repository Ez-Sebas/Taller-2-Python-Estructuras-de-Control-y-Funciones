#Expandir la calculadora básica del ejercicio 1.2 agregando un menú que permita al usuario realizar múltiples operaciones sin salir del programa. El menú debe incluir las cuatro operaciones básicas y una opción para salir.

from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Expandir Calculadora Básica")
print(Fore.YELLOW + "===========================================")

# Bucle que muestra un menú de operaciones matemáticas para que el usuario elija cuál realizar
while True:
    try: 
        print("\nSeleccione una Operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = int(input("Ingrese el Número de la Operación que Desea Realizar: "))
        
        # Realiza la operación matemática seleccionada por el usuario
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
            
            # Verifica que no se realice una división entre cero
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
            
    # Maneja errores cuando el usuario ingresa valores no válidos
    except ValueError:
        print("Error: Debe Ingresar un Número Válido.")