"""
Tu programa debe permitir al usuario consultar el inventario de una tienda para verificar si un producto está en
stock. Si el producto está en la lista, el programa debe informarlo, si no, debe mostrar un mensaje indicando
que no está disponible.
"""

inventario = [
    ["Papa", 20],
    ["Manzana", 10],
    ["Cebolla", 15],
    ["Leche", 8],
    ["Queso", 2],
    ["Pan", 5]
]

indice = 0

nombre = input("Nombre a buscar: ")
contador = 0

while indice < len(inventario):
    producto = inventario[indice]
    if producto[0]  == nombre:
        print("Poducto encontrado!!!")
        contador += 1

    indice += 1

if contador == 0:
    print("Producto no encontrado")