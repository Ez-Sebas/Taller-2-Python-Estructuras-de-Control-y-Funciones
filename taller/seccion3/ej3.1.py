from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Generador de Números Pares")
print(Fore.YELLOW + "===========================================")

N = int(input("Ingrese un Número Entero Positivo: "))

if N > 0:
    print("Números Pares de 1 hasta", N, ":")
    
    for numero in range(1, N + 1):
        if numero % 2 == 0:
            print(numero)        
else:
    print("Error: Debe Ingresar un Número Entero Positivo.")