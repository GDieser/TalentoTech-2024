
import sqlite3

conexion = sqlite3.connect("Local.db")

cursor = conexion.cursor()

#SELECT campos FROM table_name WHERE condicion
query= '''
    SELECT *
    FROM Juegos
'''

cursor.execute(query)

juegos = cursor.fetchall() #Obtiene todos los resultados

print("Lista de libros")
for juego in juegos:
    print(juego)

conexion.close()