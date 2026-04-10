from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.CYAN + Style.BRIGHT + "Calculadora de Promedios")
print(Fore.YELLOW + "===========================================")

# Función que calcula el promedio de una lista de números
def calcular_promedio(lista):
    
    if len(lista) == 0:
        return "La Lista está Vacía, no se Puede Calcular el Promedio."
    
    suma = 0
    
    # Recorre la lista y suma todos los números
    for numero in lista:
        suma += numero
        
    promedio = suma / len(lista)
    return promedio

numeros = [10, 4, 5, 6, 18, 10]

# Llama a la función para calcular el promedio de la lista
resultado = calcular_promedio(numeros)
print("El Promedio es: ", resultado)