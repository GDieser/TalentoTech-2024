"""
Escribí un programa que permita al usuario ingresar el precio de un producto, pero que sólo acepte valores
mayores a 0. Si el usuario ingresa un valor inválido (negativo o cero), el programa debe mostrar un mensaje de
error, y volver a pedir el valor hasta que se ingrese uno válido. Al final, el programa debe mostrar el precio
aceptado.
"""

valor = float(input("Ingrese valor: "))

while valor <= 0:
    print("Valor invalido, pruebe nuevamente")
    valor = float(input("Ingrese valor: "))

print(f"El valor es: {valor}")