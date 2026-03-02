#Crear una función llamada saludar que reciba dos parámetros: nombre y hora del día. La función debe retornar un saludo apropiado según la hora: "Buenos días [nombre]" (5-12), "Buenas tardes [nombre]" (13-19), "Buenas noches [nombre]" (20-4).

from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.CYAN + Style.BRIGHT + "Generador de Saludos Personalizados")
print(Fore.YELLOW + "===========================================")

def saludar(name, hour):
    if hour >= 5 and hour <= 12:
        return "Buenos Días " + name
    elif hour >= 13 and hour <= 19:
        return "Buenas Tardes " + name
    else:
        return "Buenas Noches " + name
    
name_usuario = input("Ingrese su Nombre: ")
current_time = int(input("Ingrese la Hora (0-23): "))

mensaje = saludar(name_usuario, current_time)
print(mensaje)