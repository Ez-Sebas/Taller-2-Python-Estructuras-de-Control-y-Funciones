#Crear un algoritmo que permita al usuario ingresar 10 números (que pueden repetirse) y luego muestre una lista sin elementos duplicados. Implementar la lógica de eliminación de duplicados usando ciclos y una lista auxiliar, sin utilizar funciones de conjuntos.

from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Eliminador de Duplicados en Lista")
print(Fore.YELLOW + "===========================================")

numeros = []

for i in range(10):
    num = int(input("Ingrese un Número: "))
    numeros.append(num)
    
    
sin_duplicados = []

for numero in numeros:
    if numero not in sin_duplicados:
        sin_duplicados.append(numero)
        
print("Lista original:", numeros)
print("Lista sin duplicados:", sin_duplicados)