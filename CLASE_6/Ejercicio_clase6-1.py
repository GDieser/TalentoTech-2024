"""
Desarrollá un programa que permita al usuario ingresar el nombre de varios productos y la cantidad en stock
que hay de cada uno. El programa debe seguir pidiendo que ingrese productos hasta que el usuario decida
salir, ingresando "salir" como nombre de producto. Después de que el bucle termine, el programa debe mostrar
la cantidad total de productos ingresados.
"""

contador = 0
nombre = "hola"

while nombre != "salir":

    nombre = input("Nombre: ")
    if nombre.lower() == "salir":
        break
    
    cantidad = int(input("Stock: "))

    contador += cantidad

print(f"Cantidad de ingresos: {contador}")