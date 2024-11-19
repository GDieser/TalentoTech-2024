"""
Vas a implementar un sistema básico para registrar productos en el inventario de una tienda. El programa debe
permitir que el usuario agregue productos a una lista hasta que decida no agregar más. Luego, deberás mostrar
todos los productos ingresados al inventario.
"""

productos = []
idProducto = 1

while idProducto != 0:
    nombre = input("Ingrese nombre: ")
    cantidad = int(input("Ingrese cantidad: "))
    idProducto = int(input("Ingrese el id: "))

    if idProducto == 0:
        break

    item = {
        'nombre': nombre,
        'cantidad': cantidad,
        'id': idProducto
    }
    productos.append(item)
contador = 0

for item in productos:
    print(f"Nombre: {item['nombre']}")
    print(f"Cantidad: {item['cantidad']}")
    print(f"ID: {item['id']}")
    contador +=1