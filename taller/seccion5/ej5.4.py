#Crear una función llamada es_palindromo que reciba un texto como parámetro y retorne True si es un palíndromo (se lee igual al derecho y al revés) o False en caso contrario. La función debe ignorar espacios, mayúsculas/minúsculas y signos de puntuación.

from colorama import init, Fore, Style

init(autoreset=True)

print(Fore.YELLOW + "===========================================")
print(Fore.CYAN + Style.BRIGHT + "Detector de Palíndromos")
print(Fore.YELLOW + "===========================================")

# Función que verifica si un texto es un palíndromo (se lee igual al derecho y al revés)
def es_palindromo(texto):

    texto = texto.lower()
    texto_limpio = ""

    # Elimina espacios y caracteres que no sean letras o números
    for caracter in texto:
        if caracter.isalnum():
            texto_limpio += caracter

    # Compara el texto con su versión invertida
    if texto_limpio == texto_limpio[::-1]:
        return True
    else:
        return False

frase = input("Ingrese un texto: ")

# Llama a la función para verificar si la frase es palíndromo
if es_palindromo(frase):
    print("Es palíndromo.")
else:
    print("No es palíndromo.")