#Validador de contraseña segura: Implementar un sistema que valide la fortaleza de una contraseña. El usuario debe ingresar una contraseña y el algoritmo debe verificar que cumpla con los siguientes criterios: tener al menos 8 caracteres, contener al menos una letra mayúscula, un número y un carácter especial (!@#$%^&*). Informar específicamente qué criterios no se cumplen.

from colorama import init, Fore, Style, Back

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.RED + Style.BRIGHT + "Validación de Contraseña Segura")
print(Fore.YELLOW + "===========================================")

while True:
    try:
            contraseña = input("Ingrese su Contraseña: ")
            
            tiene_mayuscula = False
            tiene_numero = False
            tiene_especial = False
            
            caracteres_especiales = "!@#$%^&*"
            
            for caracter in contraseña:
                if caracter.isupper():
                    tiene_mayuscula = True
                    
                elif caracter.isdigit():
                    tiene_numero = True
                    
                elif caracter in caracteres_especiales:
                    tiene_especial = True
                    
            errores = []
            
            if len(contraseña) < 8:
                errores.append("Debe Tener al Menos 8 Caracteres.")
                
            if not tiene_mayuscula:
                errores.append("Debe Contener al Menos una Letra Mayúscula.")
                
            if not tiene_numero:
                errores.append("Debe Contener al Menos un Número.")
                
            if not tiene_especial:
                errores.append("Debe Contener al Menos un Carácter Especial.")
                
            if len(errores) == 0:
                print("Contraseña Válida.")
                break
            
            else:
                print("Contraseña No Válida. Errores: ")
                for error in errores:
                    print("-" + error)
                    
    except ValueError:
        print("Error: Debe Ingresar una Contraseña Válida")