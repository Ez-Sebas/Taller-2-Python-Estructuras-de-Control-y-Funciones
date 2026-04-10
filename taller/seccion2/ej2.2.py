from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Menú Interactivo")
print(Fore.YELLOW + "===========================================")

# Bucle que muestra un menú de opciones para interactuar con el usuario
while True:
    try:
        print("Selecciona una Opción")
        print("1. Saludar")
        print("2. Despedirse")
        print("3. Salir")
        
        opcion = int(input("Ingrese el Número de la Opción: "))
        
        # Ejecuta la acción correspondiente según la opción elegida
        if opcion == 1:
            print("Hola Señor Usuario. Espero que se Encuentre bien. ")
            
        elif opcion == 2:
            print("Hasta Luego Señor Usuario. Que Tenga un Excelente Día.")
            
        elif opcion == 3:
            print("Saliendo del Programa. ¡Adiós!")
            break
        
        else:
            print("Opción no Válida. Intente Nuevamente.")
            
    # Maneja errores cuando se ingresa un valor que no es numérico
    except ValueError:
        print("Error: Debe Ingresar un Número Válido.")