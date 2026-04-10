from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.CYAN + Style.BRIGHT + "Calculadora de Promedios")
print(Fore.YELLOW + "===========================================")

def calcular_promedio(lista):
    
    if len(lista) == 0:
        return "La Lista está Vacía, no se Puede Calcular el Pormedio."
    
    suma = 0
    for numero in lista:
        suma += numero
        
    promedio = suma / len(lista)
    return promedio

numeros = [10, 4, 5, 6, 18, 10]
resultado = calcular_promedio(numeros)
print("El Promedio es: ", resultado)