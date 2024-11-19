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
