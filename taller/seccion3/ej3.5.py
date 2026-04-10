from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Eliminador de Duplicados en Lista")
print(Fore.YELLOW + "===========================================")

numeros = []

# Solicita al usuario ingresar 10 números y los guarda en una lista
for i in range(10):
    num = int(input("Ingrese un Número: "))
    numeros.append(num)
    
sin_duplicados = []

# Recorre la lista original y guarda solo los números que no se repiten
for numero in numeros:
    if numero not in sin_duplicados:
        sin_duplicados.append(numero)
        
# Muestra la lista original y la lista sin números repetidos
print("Lista original:", numeros)
print("Lista sin duplicados:", sin_duplicados)