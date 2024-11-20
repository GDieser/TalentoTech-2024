"""
En un sistema de inventario, cada producto tiene un código que lo identifica. Escribí un programa que permita
ingresar los códigos de 4 productos y luego mostrálos uno por uno, junto con su posición en la lista.
"""

productos = []

for i in range(4):
    codigo = input("Ingrese codigo: ")

    productos.append(codigo)

for i in range(4):
    print(f"ID {i+1}: {productos[i]}")