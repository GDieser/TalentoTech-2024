"""
En una tienda, es necesario actualizar el inventario cuando se venden productos. A continuación, te
proporcionamos un arreglo con una lista de productos, donde cada producto tiene un código, una descripción y
una cantidad en stock. Escribí un programa que permita:

Seleccionar un producto a partir de su código.

Ingresar la cantidad vendida (que debe ser mayor que cero).

Actualizar la cantidad en stock de ese producto restando la cantidad vendida.
El script que tenés que hacer debe modificar la cantidad en stock de acuerdo a cada venta realizada. Si la
cantidad vendida es mayor que la cantidad disponible en stock, el programa debe mostrar un mensaje de error.
"""

productos = [   
    ["P001", "Manzanas", 50],
    ["P002", "Peras", 40],
    ["P003", "Bananas", 30],
    ["P004", "Naranjas", 60]
]

codigo = input('Ingrese el codigo: ')

encontrado = False
indice = 0

while indice < len(productos):
    
    if codigo == productos[indice][0]:
        encontrado = True
        break
    else:
        indice += 1
    
if not encontrado:
    print('Codigo de producto no encontrado en la lista')
else:
    cantidad_vendida = int(input('Ingrese la cantidad vendida: '))

    if cantidad_vendida > 0:

        productos[indice][2] -= cantidad_vendida
        print(f"Venta realizada, Stock : {productos[indice][2]}")

    else:
        print('La cantidad vendidad debe ser mayor a cero.')