#Registro de usuario: Crear un algortimo que permita resgitrar los datos de un usuario. El programa debe solicitar: nombre, edad y ciudad de residencia. Luego, mostrar un mensaje personalizado con el siguiente formato: "Hola [nombre], tienes [edad] años y vives en [ciudad]." Validar que la edad sea un número positivo.

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