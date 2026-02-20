#Implementar un menú interactivo con tres opciones: 1. Saludar, 2. Despedirse, 3. Salir. El programa debe mostrar el menú, leer la opción seleccionada y ejecutar la acción correspondiente utilizando estructuras condicionales if-elif-else.

from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Menú Interactivo")
print(Fore.YELLOW + "===========================================")

while True:
    try:
        print("Selecciona una Opción")
        print("1. Saludar")
        print("2. Despedirse")
        print("3. Salir")
        
        opcion = int(input("Ingrese el Número de la Opción: "))
        
        if opcion == 1:
            print("Hola Señor Usuario. Espero que se Encuentre bien. ")
        elif opcion == 2:
            print("Hasta Luego Señor Usuario. Que Tenga un Excelente Día.")
        elif opcion == 3:
            print("Saliendo del Programa. ¡Adiós!")
            break
        else:
            print("Opción no Válida. Intente Nuevamente.")
            
    except ValueError:
        print("Error: Debe Ingresar un Número Válido.")