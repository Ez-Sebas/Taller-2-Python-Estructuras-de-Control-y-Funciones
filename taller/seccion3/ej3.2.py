from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Acumulador Numérico")
print(Fore.YELLOW + "===========================================")

suma = 0

while True:
    numero = float(input("Ingrese un número (0 para terminar): "))

    if numero == 0:
        break

    suma = suma + numero

print("La suma total es:", suma)