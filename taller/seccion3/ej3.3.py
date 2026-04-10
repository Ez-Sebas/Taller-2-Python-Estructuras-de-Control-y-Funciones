from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Búsqueda en Lista de Nombres")
print(Fore.YELLOW + "===========================================")

nombres = ["Sebastián", "Johanna", "Daniel", "Hernan"]

buscar = input("Ingrese el Nombre que Desea Buscar: ")

encontrado = False

for i in range(len(nombres)):
    if nombres[i] == buscar:
        print("El Nombre se Encuentra en la Posición:", i)
        encontrado = True
        break
    
if not encontrado:
    print("El Nombre no se Encuentra en la Lista")