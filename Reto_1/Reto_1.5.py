# Ejercicio 5

def mismos_caracteres(lista):
    resultado = []
    for palabra in lista:
        for otra_palabra in lista:
            if palabra != otra_palabra and sorted(palabra) == sorted(otra_palabra):
                resultado.append(palabra)
                break
    return resultado
if __name__ == "__main__":
    try:
        entrada = input("Introduce una lista de palabras separadas por espacios: ")
        if not entrada.strip():
            raise ValueError("La entrada no puede estar vacía.")

        lista = entrada.split()
        resultado = mismos_caracteres(lista)

        if resultado:
            print("Palabras con los mismos caracteres:", resultado)
        else:
            print("No se encontraron palabras con los mismos caracteres.")

    except ValueError as ve:
        print(f"Error de entrada: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
"""
1. Se define la función `mismos_caracteres` que toma una lista de palabras como objeto a trabajar.
2. Se define el resultado como una lista vacía.
3. Se pide que se introduzca una lista de palabras separadas por espacios.
4. Se separan las palabras y se almacenan en la variable `lista`.
5. Se itera sobre cada palabra en la lista.
6. Se compara cada palabra con las demás palabras de la lista.
7. Si las palabras son diferentes y tienen los mismos caracteres (ordenados), se añade la palabra a la lista de resultados.
8. Se imprime la lista de palabras que tienen los mismos caracteres.
"""