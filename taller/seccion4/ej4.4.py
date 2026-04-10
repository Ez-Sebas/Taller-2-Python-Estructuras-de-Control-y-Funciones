from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.CYAN + Style.BRIGHT + "Analizador Estadístico de Listas Numéricas")
print(Fore.YELLOW + "===========================================")

numeros = []

# Bucle que permite ingresar números hasta que el usuario escriba -1
while True:
        agregar = int(input("Ingrese un Número (-1 para terminar): "))
        if agregar == -1:
            break
        numeros.append(agregar)
        print("Los Números son:", numeros)

# Si se ingresaron números, calcula diferentes estadísticas
if len(numeros) > 0:      
    maximo = max(numeros)
    print("El Número Máximo es:", maximo)

    minimo = min(numeros)
    print("El Número Mínimo es:", minimo)

    promedio = sum(numeros) / len(numeros)
    print("El Promeido es:", promedio)

    suma = sum(numeros)
    print("La Suma Total es:", suma)
else:
    print("No se Ingresaron Números.")