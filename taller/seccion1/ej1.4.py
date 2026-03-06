#Validador de contraseña segura: Implementar un sistema que valide la fortaleza de una contraseña. El usuario debe ingresar una contraseña y el algoritmo debe verificar que cumpla con los siguientes criterios: tener al menos 8 caracteres, contener al menos una letra mayúscula, un número y un carácter especial (!@#$%^&*). Informar específicamente qué criterios no se cumplen.

from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Validación de Contraseña Segura")
print(Fore.YELLOW + "===========================================")

# Bucle que solicita una contraseña hasta que cumpla con los requisitos de seguridad establecidos
while True:
    try:
            contraseña = input("Ingrese su Contraseña: ")
            
            tiene_mayuscula = False
            tiene_numero = False
            tiene_especial = False
            
            caracteres_especiales = "!@#$%^&*"
            
            # Recorre cada carácter de la contraseña para verificar si cumple con las condiciones requeridas
            for caracter in contraseña:
                if caracter.isupper():
                    tiene_mayuscula = True
                    
                elif caracter.isdigit():
                    tiene_numero = True
                    
                elif caracter in caracteres_especiales:
                    tiene_especial = True
                    
            errores = []
            
            # Valida cada requisito de la contraseña y guarda los errores encontrados
            if len(contraseña) < 8:
                errores.append("Debe Tener al Menos 8 Caracteres.")
                
            if not tiene_mayuscula:
                errores.append("Debe Contener al Menos una Letra Mayúscula.")
                
            if not tiene_numero:
                errores.append("Debe Contener al Menos un Número.")
                
            if not tiene_especial:
                errores.append("Debe Contener al Menos un Carácter Especial.")
                
            # Si no hay errores la contraseña es válida, de lo contrario se muestran los errores    
            if len(errores) == 0:
                print("Contraseña Válida.")
                break
            
            else:
                print("Contraseña No Válida. Errores: ")
                for error in errores:
                    print("-" + error)
                    
    # Maneja errores si la entrada de datos es incorrecta                
    except ValueError:
        print("Error: Debe Ingresar una Contraseña Válida")