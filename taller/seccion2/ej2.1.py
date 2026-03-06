#Crear un algoritmo que solicite la edad de una persona y la clasifique en una de las siguientes categorías: niño (0-12 años), adolescente (13-17 años), adulto (18-64 años) o adulto mayor (65 años o más). Mostrar la categoría correspondiente.

from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Clasificación de Edad")
print(Fore.YELLOW + "===========================================")

while True:
    try:
        edad = int(input("Ingrese su Edad: "))
        
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
            
    except ValueError:
        print("Error: Edad no Válida")