"""
Imaginá que estás ayudando a una tienda de videojuegos a organizar su inventario. Su dueño te pide que escribas
un programa que verifique si hay stock suficiente de un videojuego y, si no hay, que avise que hay que
reponerlo.

El programa debería pedirle al usuario que ingrese la cantidad actual en stock y, en base a esa cantidad,
mostrar si se necesita hacer un nuevo pedido o no.
"""

stock = int(input("Ingrese stock actual: "))

if stock <= 0:
    print("El stock es insuficiente, se debe realizar un nuevo pedido")
else:
    print(f"El stock actual es: {stock}")