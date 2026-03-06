#Desarrollar un programa que solicite al usuario un número y genere su tabla de multiplicar del 1 al 10. Luego, debe preguntar si desea generar otra tabla, continuando este proceso hasta que el usuario decida salir.

from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "==================================================")
print(Fore.RED + Style.BRIGHT + "Generador de Tablas de Multiplicar Interactivo")
print(Fore.YELLOW + "==================================================")

# Bucle que permite generar tablas de multiplicar hasta que el usuario decida salir
while True:
    numero = int(input("Ingrese un número para generar su tabla: "))

    print("Tabla de multiplicar del", numero)

    # Genera la tabla de multiplicar del número desde 1 hasta 10
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

    opcion = input("¿Desea generar otra tabla? (s/n): ")

    # Si el usuario no escribe "s", el programa finaliza
    if opcion.lower() != "s":
        print("Programa finalizado.")
        break