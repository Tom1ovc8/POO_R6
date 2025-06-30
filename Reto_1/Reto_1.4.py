# Ejercicio 4

def mayor_suma_consecutivos(lista):
    if len(lista) < 2:
        return None 
    return max(lista[i] + lista[i + 1] for i in range(len(lista) - 1))

if __name__ == "__main__":
    try:
        entrada = input("Introduce una lista de números separados por espacios: ")
        if not entrada.strip():
            raise ValueError("La lista no puede estar vacía.")

        lista = list(map(int, entrada.split()))
        resultado = mayor_suma_consecutivos(lista)

        if resultado is None:
            print("Se necesitan al menos dos números para calcular la suma de consecutivos.")
        else:
            print("La mayor suma de consecutivos es:", resultado)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

"""
1. Se define la función `mayor_suma_consecutivos` que toma una lista como objeto a evalar.
2. Se verifica si la longitud de la lista es menor que 2, ya que no habrian suficientes elementos para formar una suma de consecutivos.
3. Si la longitud es menor que 2, se devuelve `None` como resultado.
4. Se realizan todas las sumas consecutivas posibles de la lista para posteriormente devolver el máximo de todas ellas.
5. Se utiliza `max` para encontrar la suma máxima de los elementos consecutivos en la lista.
6. Se imprime el resultado de la mayor suma consecutiva.
"""