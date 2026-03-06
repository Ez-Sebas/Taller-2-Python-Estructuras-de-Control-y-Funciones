#Desarrollar un sistema que convierta una calificación numérica (0-100) a su equivalente en letras según la siguiente escala: A (90-100), B (80-89), C (70-79), D (60-69), F (0-59). Validar que la nota ingresada esté dentro del rango permitido.

from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Calificación Numérica")
print(Fore.YELLOW + "===========================================")

nota = float(input("Ingrese su Nota (0-100): "))

if 90 <= nota <= 100:
    print("Tu Nota es: A")
    
elif 80 <= nota <= 89:
    print("Tu Nota es: B")
    
elif 70 <= nota <= 79:
    print("Tu Nota es: C")
    
elif 60 <= nota <= 69:
    print("Tu Nota es: D")
    
elif 0 <= nota <= 59:
    print("Tu Nota es: F")
    
else:
    print("Error Ingrese un Número del 0 al 100")