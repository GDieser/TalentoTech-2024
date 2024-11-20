"""
Desarrollá un programa que permita registrar las ventas diarias de un comercio durante 5 días. Al finalizar, el
sistema debe mostrar el total de ventas realizadas en cada día y el promedio de ventas.
"""

ventas = []

contador = 1
promedio = 0

while contador <= 5:
    venta = float(input(f"Ingrese ventas del dia {contador} : "))

    ventas.append(venta)
    contador+=1

for venta in ventas:
    print(f"Ventas: {venta}")
    promedio += venta

promedio = promedio/5

print(f"Promedio: {promedio}")