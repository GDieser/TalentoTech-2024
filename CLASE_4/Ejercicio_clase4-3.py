"""Realizar una aplicación en Python que;
A partir de la cantidad de litros de combustible que
consume un coche por cada 100 km de recorrido,
el costo de cada litro de combustible y la longitud
del viaje realizado (en kilómetros), muestra un
detalle de los litros consumidos y el dinero
gastado."""

consumo = float(input("Consumo por 100km: "))

costo = float(input("Costo del litro de nafta: "))

longitud = float(input("Viaje a realizar en km: "))

litros = (longitud * consumo) /  100
gasto = litros * costo

print(f"Total de litros gastados: {litros}, y se gastara: ${gasto}")