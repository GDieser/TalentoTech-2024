"""
Escribir un programa que solicite el nombre, la
cantidad y el valor unitario de tres productos.

Luego, debe calcular el importe de IVA (21%)
de cada producto.

Por último, debe mostrar en la terminal el
ticket de la operación con todos los datos de la
compra. 
"""

productos = []

for i in range(0, 3):

    nombre = input("Ingrese nombre del producto: ")
    cantidad = int(input("Ingrese cantidad: "))
    valor = float(input("Ingrese velor: "))

    item = {
        'nombre' : nombre,
        'cantidad' : cantidad,
        'valor' : valor
    }

    productos.append(item)

for item in productos:
    item['valor'] = item['valor'] * 1.21

    print(f"Nombre: {item['nombre']}")
    print(f"Nombre: {item['cantidad']}")
    print(f"Nombre: {item['valor']}")