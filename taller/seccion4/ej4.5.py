#Implementar un programa que permita al usuario ingresar dos listas de elementos. El algoritmo debe mostrar: los elementos comunes a ambas listas, los elementos únicos de la primera lista y los elementos únicos de la segunda lista, implementando esta lógica con ciclos sin usar funciones de conjuntos.

from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.CYAN + Style.BRIGHT + "Comparador Avanzado de Listas")
print(Fore.YELLOW + "===========================================")

entrada1 = input("Ingrese Varios Productos Separados por Comas: ")

first_list = []

# Divide los productos ingresados y elimina espacios o duplicados
for producto in entrada1.split(","):
    limpio = producto.strip() 
    if limpio not in first_list:
        first_list.append(limpio)

entrada2 = input("Ingrese Varios Productos Separados por Comas: ")

second_list = []

# Procesa la segunda lista de productos evitando duplicados
for producto in entrada2.split(","):
    limpio = producto.strip()
    if limpio not in second_list:
        second_list.append(limpio)

comunes = []
unicos_first_list = []
unicos_second_list = []

# Identifica los productos que están en ambas listas
for producto1 in first_list:
    if producto1 in second_list:
        comunes.append(producto1)

# Identifica los productos que solo están en la primera lista
for producto1 in first_list:
    if producto1 not in second_list:
        unicos_first_list.append(producto1)

# Identifica los productos que solo están en la segunda lista
for producto2 in second_list:
    if producto2 not in first_list:
        unicos_second_list.append(producto2)

# Muestra los resultados de la comparación entre listas
print("\nResultados:")
print("Los Productos Comunes son:", comunes)
print("Los Productos Únicos de la Primera Lista son:", unicos_first_list)
print("Los Productos Únicos de la Segunda Lista son:", unicos_second_list)