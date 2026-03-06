#Convertidor de unidades con menú: Desarrollar un convertidor de unidades con un menú interactivo que ofrezca tres opciones: 1. Convertir Celsius a Fahrenheit, 2. Convertir kilómetros a millas, 3. Convertir kilogramos a libras. El usuario debe seleccionar una opción, ingresar el valor a convertir y el programa mostrará el resultado con dos decimales.


from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Convertidor de Unidades con Menú")
print(Fore.YELLOW + "===========================================")

# Bucle principal que muestra un menú para realizar diferentes conversiones de unidades
while True:
    try:
        print("Seleccione una Opción: ")
        print("1. Convertir Celsius a Fahrenheit.")
        print("2. Convertir Kilómetros a Millas.")
        print("3. Convertir Kilogramos a Libras.")
        
        opcion = int(input("Ingrese el Número de la Opción: "))
        
        # Realiza la conversión de temperatura de Celsius a Fahrenheit
        if opcion == 1:
            celsius = float(input("Ingrese la Temperatura en Celsius: "))
            resultado = (celsius * 1.8 + 32)
            print(f"La Temperatura en Fahrenheit es: {resultado:.2f} °F")
        
        # Realiza la conversión de distancia de kilómetros a millas    
        elif opcion == 2:
            kilometros = float(input("Ingrese la Distancia de Kilómetros: "))
            resultado = (kilometros * 0.621371)
            print(f"La Distancia en Millas es: {resultado:.2f} Millas")
            
        # Realiza la conversión de peso de kilogramos a libras    
        elif opcion == 3:
            kilogramos = float(input("Ingrese el Peso en Kilogramos: "))
            resultado = (kilogramos * 2.20462)
            print(f"El Peso en Libras es: {resultado:.2f} Libras")
            
        else:
            print("Opción No Válida. Intente Nuevamente.")
    
    # Maneja errores cuando el usuario ingresa datos que no son numéricos        
    except ValueError:
        print("Error: Debe Ingresar un Número Válido.")