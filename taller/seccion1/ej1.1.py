from colorama import init, Fore, Back

init(autoreset = True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + "Registro de Usuario")
print(Fore.YELLOW + "===========================================")


name = input("Registre su Nombre: ")
age = int(input("Registre su Edad: "))
city = input("Registre su Ciudad de Residencia: ")

if age > 0:
    print(f"Hola {name}, tienes {age} años y vives en {city}.")
    
else:
    print("Ingrese un Número Positivo")