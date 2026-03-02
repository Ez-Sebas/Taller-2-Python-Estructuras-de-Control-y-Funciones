#Implementar una función llamada factorial que calcule el factorial de un número usando recursión. La función debe recibir un número entero positivo y retornar su factorial. Incluir validación para números negativos.

from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.CYAN + Style.BRIGHT + "Calculadora Factorial Recursiva")
print(Fore.YELLOW + "===========================================")

def factorial(n):
    
    if n < 0:
        return "No existe factorial para números negativos."
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

numero = int(input("Ingrese un número entero positivo: "))
resultado = factorial(numero)
print("Resultado:", resultado)