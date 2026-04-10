from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Clasificación de Edad")
print(Fore.YELLOW + "===========================================")

# Bucle que solicita la edad del usuario y la clasifica en una categoría según el rango de edad
while True:
    try:
        edad = int(input("Ingrese su Edad: "))
        
        # Evalúa el rango de la edad para determinar la categoría correspondiente
        if edad >= 0 and edad <= 12:
            print("Categoría: Niño")
            
        elif edad >= 13 and edad <= 17:
            print("Categoría: Adolescente")
            
        elif edad >= 18 and edad <= 64:
            print("Categoría: Adulto")
            
        elif edad >= 65:
            print("Categoría: Adulto Mayor")
            
        else:
            print("Edad Inválida")
            
    # Maneja errores cuando el usuario no ingresa un número válido
    except ValueError:
        print("Error: Edad no Válida")