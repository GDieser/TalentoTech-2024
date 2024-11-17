"""Escribir un programa que guarde en variables el
monto del ingreso de cada uno de los primeros 6
meses del año.

Luego, calcular y guardar en otra variable el
promedio de esos valores.

Por último, mostrar una leyenda que diga “El
ingreso promedio en el semestre es de xxxxx”
donde “xxxxx” es el valor calculado.
"""

montoMes = 0
promedio = 0
contador = 1

while contador <= 6:
    montoMes = montoMes + float(input(f'Monto del mes {contador}: ' ))
    contador = contador + 1

promedio = montoMes / 6

print(f"Promedio de ingresos es: ${promedio}")

