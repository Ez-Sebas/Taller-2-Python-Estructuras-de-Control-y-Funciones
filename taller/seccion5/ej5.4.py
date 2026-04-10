from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.CYAN + Style.BRIGHT + "Detector de Palíndromos")
print(Fore.YELLOW + "===========================================")

def es_palindromo(texto):

    texto = texto.lower()
    texto_limpio = ""

    for caracter in texto:
        if caracter.isalnum():
            texto_limpio += caracter

    if texto_limpio == texto_limpio[::-1]:
        return True
    else:
        return False

frase = input("Ingrese un texto: ")

if es_palindromo(frase):
    print("Es palíndromo.")
else:
    print("No es palíndromo.")