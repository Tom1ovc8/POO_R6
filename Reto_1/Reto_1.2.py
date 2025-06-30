# Ejercicio 2

palabra = str(input("Introduce una palabra o frase: "))

def palindrome(palabra):
    palabra = palabra.lower().replace(" ", "")
    longitud = len(palabra)
    for i in range(longitud // 2):
        if palabra[i] != palabra[longitud - i - 1]:
            return False
    return True

try:
    palabra = str(input("Introduce una palabra o frase: ")).strip()
    if not palabra:
        raise ValueError("La entrada está vacía. Debes introducir una palabra o frase.")

    if palindrome(palabra):
        print("La palabra o frase es un palíndromo.")
    else:
        print("La palabra o frase no es un palíndromo.")

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
    
print("La palabra o frase no es un palíndromo.")

"""
1. Se pide al usuario que introduzca una palabra o frase.
2. Se define la función palindrome para indentificar si la palabra o frase introducida es un palíndromo.
3. Se convierte la palabra a minúsculas y se eliminan los espacios.
4. Se calcula la longitud de la palabra.
5. Se itera sobre la mitad de la longitud de la palabra.
6. Se compara cada letra con su correspondiente desde el final.
7. Si alguna letra no coincide, se devuelve False, si todas las letras coinciden, se devuelve True.
8. Se imprime si la palabra o frase es un palíndromo o no.
"""