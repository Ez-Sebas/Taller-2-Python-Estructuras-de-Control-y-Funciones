from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Convertidor de Unidades con Menú")
print(Fore.YELLOW + "===========================================")

while True:
    try:
        print("Seleccione una Opción: ")
        print("1. Convertir Celsius a Fahrenheit.")
        print("2. Convertir Kilómetros a Millas.")
        print("3. Convertir Kilogramos a Libras.")
        
        opcion = int(input("Ingrese el Número de la Opción: "))
        
        if opcion == 1:
            celsius = float(input("Ingrese la Temperatura en Celsius: "))
            resultado = (celsius * 1.8 + 32)
            print(f"La Temperatura en Fahrenheit es: {resultado:.2f} °F")
            
        elif opcion == 2:
            kilometros = float(input("Ingrese la Distancia de Kilómetros: "))
            resultado = (kilometros * 0.621371)
            print(f"La Distancia en Millas es: {resultado:.2f} Millas")
            
        elif opcion == 3:
            kilogramos = float(input("Ingrese el Peso en Kilogramos: "))
            resultado = (kilogramos * 2.20462)
            print(f"El Peso en Libras es: {resultado:.2f} Libras")
            
        else:
            print("Opción No Válida. Intente Nuevamente.")
            
    except ValueError:
        print("Error: Debe Ingresar un Número Válido.")