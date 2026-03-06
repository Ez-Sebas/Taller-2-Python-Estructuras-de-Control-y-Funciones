#Tomar el menú de calculadora desarrollado en ejercicios anteriores y refactorizarlo, convirtiendo cada operación matemática en una función separada. El menú principal debe llamar a estas funciones según la opción seleccionada.

from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.CYAN + Style.BRIGHT + "Refactorización de Menú de Calculadora")
print(Fore.YELLOW + "===========================================")


def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return None
    return num1 / num2


while True:
    try:
        print("\nSeleccione una Operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = int(input("Ingrese el Número de la Operación que Desea Realizar: "))

        if opcion == 5:
            print("Saliendo del Programa. ¡Adiós!")
            break

        if opcion in [1, 2, 3, 4]:
            numero1 = float(input("Ingrese el Primer Número: "))
            numero2 = float(input("Ingrese el Segundo Número: "))

            if opcion == 1:
                resultado = suma(numero1, numero2)
            elif opcion == 2:
                resultado = resta(numero1, numero2)
            elif opcion == 3:
                resultado = multiplicacion(numero1, numero2)
            elif opcion == 4:
                resultado = division(numero1, numero2)
                if resultado is None:
                    print("No se puede dividir entre cero.")
                    continue

            print(f"El Resultado es: {resultado}")

        else:
            print("Opción no válida.")

    except ValueError:
        print("Error: Debe ingresar un número válido.")