
#Importamos 
import sqlite3

#Estblecemos la conexion, crea o conecta a la db
conexion = sqlite3.connect("Local.db")

#Objeto cursor, actua como intermediario del programa y la bd
cursor = conexion.cursor()

#SQL Structured Query Language 

#Crear Tabla
query = '''
    Create Table If Not Exists Juegos(
        IdJuego Integer Primary Key Autoincrement,
        Titulo Text Not Null,
        Desarollador Text,
        Plataforma Text,
        Copias  Integer Not Null
    )
'''
#Lo usamos para ejecutar comando en SQL
cursor.execute(query)

#Guarda los cambios en la bd
conexion.commit()

#Cerrar la conexion
conexion.close()