from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.CYAN + Style.BRIGHT + "Comparador Avanzado de Listas")
print(Fore.YELLOW + "===========================================")

entrada1 = input("Ingrese Varios Productos Separados por Comas: ")

first_list = []
for producto in entrada1.split(","):
    limpio = producto.strip() 
    if limpio not in first_list:
        first_list.append(limpio)
        
entrada2 = input("Ingrese Varios Productos Separados por Comas: ")

second_list = []
for producto in entrada2.split(","):
    limpio = producto.strip()
    if limpio not in second_list:
        second_list.append(limpio)

comunes = []
unicos_first_list = []
unicos_second_list = []

for producto1 in first_list:
    if producto1 in second_list:
        comunes.append(producto1)

for producto1 in first_list:
    if producto1 not in second_list:
        unicos_first_list.append(producto1)

for producto2 in second_list:
    if producto2 not in first_list:
        unicos_second_list.append(producto2)

print("\nResultados:")
print("Los Productos Comunes son:", comunes)
print("Los Productos Únicos de la Primera Lista son:", unicos_first_list)
print("Los Productos Únicos de la Segunda Lista son:", unicos_second_list)