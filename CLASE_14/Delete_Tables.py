
import sqlite3

conexion = sqlite3.connect("Local.db")
cursor = conexion.cursor()

#DELETE FROM table_name WHERE condicion
query= '''
    DELETE FROM Juegos
    WHERE IDJuego = ?
'''

ID = int(input("Ingrese ID: "))

params = (ID,)

cursor.execute(query, params)
conexion.commit()

conexion.close()