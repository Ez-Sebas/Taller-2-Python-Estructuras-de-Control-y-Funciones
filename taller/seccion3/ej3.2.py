from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Acumulador Numérico")
print(Fore.YELLOW + "===========================================")

suma = 0

# Bucle que permite ingresar números y sumarlos hasta que el usuario ingrese 0
while True:
    numero = float(input("Ingrese un número (0 para terminar): "))

    # Si el número es 0 se finaliza el programa
    if numero == 0:
        break

    suma = suma + numero

# Muestra el resultado total de la suma de los números ingresados
print("La suma total es:", suma)