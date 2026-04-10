from colorama import init, Fore, Back

init(autoreset = True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + "Registro de Usuario")
print(Fore.YELLOW + "===========================================")

#Solicita al usuario su nombre, edad y ciudad de residencia.
name = input("Registre su Nombre: ")
age = int(input("Registre su Edad: "))
city = input("Registre su Ciudad de Residencia: ")

#Verifica que la edad sea un número positivo y muestra un mensaje con la información ingresada.
if age > 0:
    print(f"Hola {name}, tienes {age} años y vives en {city}.")
    
else:
    print("Ingrese un Número Positivo")