
import sqlite3

conexion = sqlite3.connect("Local.db")

cursor = conexion.cursor()

#Insert INTO table_name (campos) VALUES (Valores)
query = '''
    INSERT INTO Juegos (Titulo, Desarollador, Plataforma, Copias) 
    VALUES (?, ?, ?, ?)
'''
#Aca deberiamos poner las variables
params = ("Pacman", "Consola", "Atari", 35)

cursor.execute(query, params)

conexion.commit()

conexion.close()