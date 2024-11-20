"""
Desarrolla un programa en Python que calcule la suma de los números naturales hasta un número dado
utilizando un bucle for. La suma de los números naturales hasta el número n se define como la suma de todos
los números enteros positivos desde 1 hasta n.

Por ejemplo, la suma de los números naturales hasta 6 es 1 + 2 + 3 + 4 + 5 + 6 = 21.
"""

num = int(input("Ingrese numero: "))
suma = 0

for i in range(num):
    print(i+1, end=" ")
    suma += (i+1)

print(f"Suma = {suma}")