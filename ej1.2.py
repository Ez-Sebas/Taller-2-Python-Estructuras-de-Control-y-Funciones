#Calculadora Básica: Desarrollar una calculadora simple que solicite al usuario dos números y una opración matemática (+, -, *, /). El algortimo debe realizar la operación correspondiente y mostrar el resultado. Incluir validación para evitar la división por cero, mostrando un mensaje de error en ese caso.

from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + "Calculadora Básica")
print(Fore.YELLOW + "===========================================")

while True:
    try:
        num1 = float(input("Ingrese el Primer Número: "))
        num2 = float(input("Ingrese el Segundo Número: "))
        operacion = input("Ingrese la Operación (+, -, *, /): ")
        
        if operacion == "+":
            resultado = num1 + num2
        
        elif operacion == "-":
            resultado = num1 - num2
            
        elif operacion == "*":
            resultado = num1 * num2
            
        elif operacion == "/":
            if num2 == 0:
                print("Error: No se Puede Dividir Entre Cero")
                continue
            resultado = num1 / num2
            
        else:
            print("Operación no Válida")
            continue
        
        print("Resultado es: ", int(resultado))
        
    except ValueError:
        print("Error: Debe Ingresar Número Válidos")