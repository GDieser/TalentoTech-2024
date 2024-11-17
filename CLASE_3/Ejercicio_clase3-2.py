"""
Escribe un programa en Python que calcule la
propina que se debe dejar en un restaurante.

El script debe solicitar al usuario el monto total de
la cuenta y el porcentaje de propina que desea
dejar.

Utilizando operadores aritméticos, calcula la
cantidad de propina y el total a pagar (incluyendo
la propina).

Finalmente, muestra los resultados en la pantalla. 
"""

monto = float(input('Ingrese el monto de la cuenta: '))
porcentaje = float(input('Ingrese el porcentaje de propina que desea dejar: '))

propina = monto * (porcentaje * 0.01)

monto = monto + propina
print(f"Total a pagar: ${monto}")
