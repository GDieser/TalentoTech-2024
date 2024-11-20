"""
Imaginá que en tu tienda querés implementar un sistema de descuentos automáticos. Vas a desarrollar un programa que permita
calcular el precio final de un producto después de aplicar un descuento. Para hacerlo:

Crea una función que reciba como parámetros el precio original del producto y el porcentaje de descuento, y que retorne
el precio final con el descuento aplicado.

Luego, pedí que se ingrese el precio y el porcentaje de descuento. Mostrá el precio final después de aplicar el descuento.
"""


def descuento(precio, desc):

    desc = (100 - desc) * 0.01
    resultado = precio * desc

    return resultado

precio = float(input("Ingrese precio: "))
desc = float(input("Ingrese descuento: "))

total = descuento(precio, desc)

print(f"Total a pagar: ${total}")