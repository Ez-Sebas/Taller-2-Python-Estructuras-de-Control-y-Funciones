from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Validación de Correo Electrónico")
print(Fore.YELLOW + "===========================================")

while True:
    try:
        correo = input("Ingrese su Correo Electrónico: ")
        
        if "@" in correo and "." in correo:
            posicion_arroba = correo.find("@")
            posicion_punto = correo.rfind(".")
            
            if posicion_arroba > 0 and posicion_punto > posicion_arroba + 1 and posicion_punto < len(correo) -1:
                input("Correo Electrónico Válido")
                break
            
            else:
                print("Formato Incorrecto. Intente Nuevamente")
                
        else:
            print("Debe contener '@' y '.'. Intente nuevamente")
                
    except ValueError:
        print("Error: Debe Ingresar un Correo Electrónico Válido")