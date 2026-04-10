from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + "Calculadora Básica")
print(Fore.YELLOW + "===========================================")

# Bucle principal que permite ejecutar la calculadora continuamente hasta que el usuario detenga el programa
while True:
    try:
        num1 = float(input("Ingrese el Primer Número: "))
        num2 = float(input("Ingrese el Segundo Número: "))
        operacion = input("Ingrese la Operación (+, -, *, /): ")
        
        # Evalúa la operación matemática que el usuario desea realizar
        if operacion == "+":
            resultado = num1 + num2
        
        elif operacion == "-":
            resultado = num1 - num2
            
        elif operacion == "*":
            resultado = num1 * num2
            
        elif operacion == "/":
            # Verifica que no se intente dividir entre cero
            if num2 == 0:
                print("Error: No se Puede Dividir Entre Cero")
                continue
            resultado = num1 / num2
            
        else:
            print("Operación no Válida")
            continue
        
        print("Resultado es: ", int(resultado))
        
    # Maneja errores cuando el usuario ingresa valores que no son numéricos
    except ValueError:
        print("Error: Debe Ingresar Número Válidos")