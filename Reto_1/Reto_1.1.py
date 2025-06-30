# Ejercicio 1

oper = str(input("Introduce la operación que desees realizar (+ - * /): "))
if oper not in ["+", "-", "*", "/"]:
    print("Introduce una operación válida.")
    exit()
number1 = int(input("Introduce el primer número: "))
number2 = int(input("Introduce el segundo número: "))
result = 0

try:
    oper = str(input("Introduce la operación que desees realizar (+ - * /): "))
    if oper not in ["+", "-", "*", "/"]:
        raise ValueError("Operación no válida.")

    number1 = int(input("Introduce el primer número: "))
    number2 = int(input("Introduce el segundo número: "))

    if oper == "+":
        result = number1 + number2
    elif oper == "-":
        result = number1 - number2
    elif oper == "*":
        result = number1 * number2
    elif oper == "/":
        if number2 == 0:
            raise ZeroDivisionError("No se puede dividir entre 0.")
        result = number1 / number2

    print(f"El resultado de {number1} {oper} {number2} es: {result}")

except ValueError as ve:
    print(f"Error de valor: {ve}")
except ZeroDivisionError as zde:
    print(f"Error de división: {zde}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")


print(f"El resultado de {number1} {oper} {number2} es: {result}")

""" Llegue a la solución del ejercicio de la siguiente manera:
1. Primero defini las variables que iba a utilizar, como la operación, los números y el resultado.
2. Le pedí al usuario que introdujera la operación que quería realizar.
3. Verifiqué si la operación era válida.
4. Le pedí al usuario que introdujera los dos números con los que quisiera operar.
5. Hice las operaciones correspondientes según la operación que el usuario eligió, con la unica condicion de que la division no sea por 0.
6. Por ultimo, imprimi el resultado de la operación.
"""