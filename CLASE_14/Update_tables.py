
import sqlite3

conexion = sqlite3.connect("Local.db")
cursor = conexion.cursor()

#UPDATE table_name SET campo1=valor1, campo2=valor2 WHERE condicion

query = '''
    UPDATE Juegos
    SET Titulo = ?,
        Desarollador = ?,
        Plataforma = ?,
        Copias = ?
    WHERE IdJuego = ?
'''
params = ('Half-Life', 'Sierra', 'PC', 25, 2)

cursor.execute(query, params)

conexion.commit()

conexion.close()