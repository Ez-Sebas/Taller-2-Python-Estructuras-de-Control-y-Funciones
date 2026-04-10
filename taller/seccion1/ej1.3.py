from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Validación de Correo Electrónico")
print(Fore.YELLOW + "===========================================")

# Bucle que solicita el correo electrónico hasta que el formato sea válido
while True:
    try:
        correo = input("Ingrese su Correo Electrónico: ")
        
        # Verifica que el correo contenga los símbolos básicos de un email
        if "@" in correo and "." in correo:
            posicion_arroba = correo.find("@")
            posicion_punto = correo.rfind(".")
            
            # Comprueba que la posición de los símbolos tenga un orden correcto dentro del correo
            if posicion_arroba > 0 and posicion_punto > posicion_arroba + 1 and posicion_punto < len(correo) -1:
                input("Correo Electrónico Válido")
                break
            
            else:
                print("Formato Incorrecto. Intente Nuevamente")
                
        else:
            print("Debe contener '@' y '.'. Intente nuevamente")
            
    # Maneja errores si ocurre un problema con la entrada de datos          
    except ValueError:
        print("Error: Debe Ingresar un Correo Electrónico Válido")