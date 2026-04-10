from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.CYAN + Style.BRIGHT + "Calculadora Factorial Recursiva")
print(Fore.YELLOW + "===========================================")

# Función recursiva que calcula el factorial de un número entero
def factorial(n):
    
    if n < 0:
        return "No existe factorial para números negativos."
    
    # Casos base del factorial
    if n == 0 or n == 1:
        return 1
    
    # Llamada recursiva para calcular el factorial
    return n * factorial(n - 1)

numero = int(input("Ingrese un número entero positivo: "))

# Llama a la función para calcular el factorial del número ingresado
resultado = factorial(numero)
print("Resultado:", resultado)