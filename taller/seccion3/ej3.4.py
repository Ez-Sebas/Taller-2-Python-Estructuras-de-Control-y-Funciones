from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "==================================================")
print(Fore.RED + Style.BRIGHT + "Generador de Tablas de Multiplicar Interactivo")
print(Fore.YELLOW + "==================================================")

while True:
    numero = int(input("Ingrese un número para generar su tabla: "))

    print("Tabla de multiplicar del", numero)

    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

    opcion = input("¿Desea generar otra tabla? (s/n): ")

    if opcion.lower() != "s":
        print("Programa finalizado.")
        break