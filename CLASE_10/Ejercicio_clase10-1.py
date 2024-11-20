"""
En un comercio, se necesita gestionar los productos y sus precios. Desarrollá un programa que permita:

Ingresar el nombre de tres productos y su precio correspondiente, guardándolos en un diccionario donde
la clave es el nombre del producto y el valor es su precio.

Una vez ingresados, mostrará todos los productos y sus precios en pantalla.
"""

productos = {}

for i in range(3):
    nombre = input(f'Ingrese el nombre del producto {i+1}: ')
    precio = float(input(f'Ingrese el precio del producto {i+1}: '))
    productos[nombre] = precio

for nombre, precio in productos.items():
    print("Producto: ", nombre, " Precio: ", precio)
