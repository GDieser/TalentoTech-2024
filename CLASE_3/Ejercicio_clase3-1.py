"""
Crea un programa que solicite al usuario dos
números enteros.

Realiza las siguientes operaciones: suma,
resta, multiplicación, y módulo.

Muestra el resultado de cada operación en un
formato claro y amigable.

Asegúrate de incluir mensajes personalizados que
expliquen cada resultado, por ejemplo: "La suma
de tus números es: X". 
"""

numero1 = float(input("Ingrese primer numero: "))
numero2 = float(input("Ingrese segundo numero: "))

suma = numero1 + numero2
print(f"La suma de los numeros es: {suma}")

resta = numero1 - numero2
print(f"La resta de los numeros es: {resta}")

multiplicacion = numero1 * numero2
print(f"La multiplicacion de los numeros es: {multiplicacion}")

modulo = numero1 % numero2
print(f"El modulo entre los numeros es: {modulo}")