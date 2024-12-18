
"""
Proyecto Final Integrador:
1. Deberán desarrollar una aplicación en Python que permita gestionar el inventario de una pequeña tienda.
2. La aplicación debe ser capaz de registrar, actualizar, eliminar y mostrar productos en el inventario.
3. Además, debe incluir funcionalidades para realizar búsquedas y generar reportes de stock.

Requerimientos
1. Crear una base de datos SQLite para almacenar los datos de los productos (nombre, descripción, cantidad, precio, categoría).
2. Implementar una interfaz de usuario básica para interactuar con la base de datos desde la terminal (línea de comandos).
3. Incluir funcionalidades de registro, actualización, eliminación y visualización de productos.
4. Generar reportes de productos con bajo stock.

"""


def gestionarLocal():
    #Acá redireccionamos a la funcion correspondiente
    while True:
        opcion = mostrarMenuPrincipal()

        if opcion == 1 :
            agregarNuevoJuego()            
        elif opcion == 2:
            mostrarListaJuegos()            
        elif opcion == 3:
            modificarJuego()
            pass
        elif opcion == 4:
            eliminarUnJuego()
            pass
        elif opcion == 5:
            buscarUnJuego()
            pass
        elif opcion == 6:
            prestarUnJuego()
            pass
        elif opcion == 7:
            verStockBajo()
            pass
        elif opcion == 8:
            inicializarBaseDeDatos()
            pass
        elif opcion == 0:
            print('Hasta la próxima! 🖖')
            break
        else:
            print('Opción incorrecta.')

def mostrarMenuPrincipal():
    #Menú Principal
    #Me imprime unos separadores
    print("=" * 30)
    print("    🕹️  MENÚ PRINCIPAL 🕹️")
    print("=" * 30)
    print(" 1- ✔️  Agregar un Juego")
    print(" 2- 📄 Mostrar lista de Juegos")
    print(" 3- ♻️  Modificar un Juego")
    print(" 4- ❌ Eliminar un Juego")
    print(" 5- 🔍 Buscar un Juego")
    print(" 6- 🤝 Prestar un Juego")
    print(" 7- 📊 Ver Juegos con Stock bajo")
    print(" 8- 📁 Crear Base de Datos")
    print()
    print(" 0- ❎ Salir del menú")
    print("=" * 30)
    print()
    opcion = int(input("Su elección: "))

    return opcion

#1   
def agregarNuevoJuego():

    titulo = input('Ingrese el Titulo del Juego: ')
    juego = buscarJuegoPorTitulo(titulo)

    if not juego:
        desarollador = input('Ingrese el Desarollador: ')
        plataforma = input('Ingrese la Plataforma: ')

        while True:
            try:
                copias = int(input('Ingrese copias en stock: '))
                if copias > 0:
                    break
                else:
                    print("LA COPIAS DEBEN SUPERIOR A 0.")
            except ValueError:
                print('ERROR DE INGRESO')
        query = '''
            INSERT INTO Juegos (Titulo, Desarollador, Plataforma, Copias) 
            VALUES (?, ?, ?, ?)
        '''
        params = (titulo, desarollador, plataforma, copias)
        if ejecutarConsulta(query,params):
            print(f'Juego {titulo} agregado con exito!')
    else:
        print('Titulo ya ingresado, compruebe la lista')


#2
def mostrarListaJuegos():    

    query = """
        SELECT * FROM Juegos
    """

    juegos = ejecutarConsulta(query, '', True)

    if not juegos:
        print('Sin stock de juegos disponible...')     

    else:
        encabezado = f"{'ID':^{5}} |{'Titulo':^{20}} |{'Plataforma':^{15}} |{'Desarollador':^{15}} |{'Stock':^{4}}"
        separador = "-" * len(encabezado)

        print('\n 📄 Listado de Juegos:')

        print(encabezado)
        print(separador)

        for juego in juegos:    
            Idjuego, Titulo, Plataforma, Desarrollador, Cantidad = juego        
            print(
                f"{Idjuego:^{5}} |{Titulo:^{20}} |"
                f"{Plataforma:^{15}} |{Desarrollador:^{15}} |"
                f"{Cantidad:^{4}}"
            )
        
#3
def modificarJuego():

    #Implementar buscar por ID.
    idJuego = input('Ingrese el ID del Juego: ')
    juegos = buscarJuegoPorId(idJuego)

    if juegos:

        for juego in juegos:    
            Idjuego, Titulo, Plataforma, Desarrollador, Cantidad = juego
        
        while True:
            print('1 - Cambiar Titulo')
            print('2 - Cambiar Plataforma')
            print('3 - Cambiar Desarollador')
            print('4 - Cambiar Cantidad en Stock')
            print('5 - CONFIRMAR CAMBIOS')
            print('0 - Volver Atras')
            opcion = int(input("Su elección: "))

            if opcion == 1 :
                Titulo = input('Ingrese nuevo Titulo: ')
            elif opcion == 2:
                Plataforma = input('Ingrese nueva Plataforma: ')
            elif opcion == 3:
                Desarrollador = input('Ingrese nuevo Desarollador: ')
            elif opcion == 4:
                Cantidad = int(input('Ingrese nueva Cantidad: '))
            elif opcion == 5:
                break
            elif opcion == 0:
                return
            else:
                print('Opción incorrecta.')
        
        query = '''
            UPDATE Juegos
            SET Titulo = ?,
                Desarollador = ?,
                Plataforma = ?,
                Copias = ?
            WHERE IdJuego = ?
        '''
        params = (Titulo, Desarrollador, Plataforma, Cantidad, idJuego)

        ejecutarConsulta(query, params)

        print("El juego fue actualizado con éxito.")
    else:
        print('Juego no encontrado...')
        
#4
def eliminarUnJuego():

    idJuego = input('Ingrese el ID del Juego: ')
    juegos = buscarJuegoPorId(idJuego)

    if juegos:
        while True:
            print("¿Está seguro que desea eliminar el Juego?")
            print("1 - SI || 2 - NO")
            opcion = int(input("Su elección: "))

            if opcion == 1:

                query= '''
                    DELETE FROM Juegos
                    WHERE IDJuego = ?
                '''
                params = (idJuego,)
                ejecutarConsulta(query, params)

                print("Registro borrado exitosamente!")
                break
            elif opcion == 2:
                break
            else:
                print("Opcion incorrecta, intente nuevamete")
    else:
        print('Juego no encontrado...')

#5
def buscarJuegoPorTitulo(Titulo):
   
    query = """
        SELECT * FROM Juegos WHERE Titulo = ?
    """
    params = (Titulo,)
    
    juego = ejecutarConsulta(query, params, True)

    return juego    

#6
def prestarUnJuego():
    print("Lala")

def buscarJuegoPorId(IdJuego):

    query = """
        SELECT * FROM Juegos WHERE IdJuego = ?
    """
    params = (IdJuego,)
    
    juego = ejecutarConsulta(query, params, True)

    return juego


#7
def verStockBajo():

    query = """
        SELECT * FROM Juegos WHERE Copias <= 5
    """
    juegos = ejecutarConsulta(query, '', True)

    if not juegos:
        print('Todos los juegos tienen Stock suficiente actualmente!')     

    else:
        encabezado = f"{'ID':^{5}} |{'Titulo':^{20}} |{'Plataforma':^{15}} |{'Desarollador':^{15}} |{'Stock':^{4}}"
        separador = "-" * len(encabezado)

        print('\n 📄 Listado de Juegos Bajo Stock:')

        print(encabezado)
        print(separador)

        for juego in juegos:    
            Idjuego, Titulo, Plataforma, Desarrollador, Cantidad = juego        
            print(
                f"{Idjuego:^{5}} |{Titulo:^{20}} |"
                f"{Plataforma:^{15}} |{Desarrollador:^{15}} |"
                f"{Cantidad:^{4}}"
            )

#8
def buscarUnJuego():
  
    while True:
        print('1 - Buscar por ID')
        print('2 - Buscar por Titulo')
        print('0 - Volver Atras')
        opcion = int(input("Su elección: "))

        if opcion == 1 :
            IdJuego = input('Ingrese Id del Juego a buscar: ')
            juegos = buscarJuegoPorId(IdJuego)        
        elif opcion == 2:
            titulo = input('Ingrese Titulo del Juego a buscar: ')
            juegos = buscarJuegoPorTitulo(titulo)
        elif opcion == 0:
            return
        else:
            print('Opción incorrecta.')

        if juegos:
            for juego in juegos:
                Idjuego, Titulo, Plataforma, Desarrollador, Cantidad = juego
                        
            print(f"Id: {Idjuego}, Titulo: {Titulo}, Plataforma: {Plataforma}, "
                f"Desarrollador: {Desarrollador}, Cantidad: {Cantidad}")
        else:
            print('Juego no encontrado...')
        break



#Creamos la DB con algunos registros
def inicializarBaseDeDatos():

    import sqlite3
    conexion = sqlite3.connect("LocalDeJuegos.db")
    cursor = conexion.cursor()

    query = '''
        CREATE TABLE IF NOT EXISTS Juegos(
            IdJuego INTEGER PRIMARY KEY AUTOINCREMENT,
            Titulo TEXT NOT NULL,
            Desarollador TEXT,
            Plataforma TEXT,
            Copias INTEGER NOT NULL CHECK(typeof(copias) = 'integer')
        )
    '''
    cursor.execute(query)
    conexion.commit()

    query = '''
        INSERT INTO Juegos (Titulo, Desarollador, Plataforma, Copias) 
        VALUES (?, ?, ?, ?)
    '''
    params = ("Pacman", "Atari", "Consola", 35)

    cursor.execute(query, params)
    conexion.commit()

    query = '''
        INSERT INTO Juegos (Titulo, Desarollador, Plataforma, Copias) 
        VALUES (?, ?, ?, ?)
    '''
    params = ("Half-Life", "Sierra", "PC", 50)

    cursor.execute(query, params)
    conexion.commit()

    query = '''
        INSERT INTO Juegos (Titulo, Desarollador, Plataforma, Copias) 
        VALUES (?, ?, ?, ?)
    '''
    params = ("Halo", "Microsoft", "PC/XBOX", 30)

    cursor.execute(query, params)
    conexion.commit()

    query = '''
        INSERT INTO Juegos (Titulo, Desarollador, Plataforma, Copias) 
        VALUES (?, ?, ?, ?)
    '''
    params = ("Doom", "ID", "PC", 25)

    cursor.execute(query, params)
    conexion.commit()

    query = '''
        INSERT INTO Juegos (Titulo, Desarollador, Plataforma, Copias) 
        VALUES (?, ?, ?, ?)
    '''
    params = ("Counter-Strike", "Valve", "PC", 55)

    cursor.execute(query, params)
    conexion.commit()

    query = '''
        INSERT INTO Juegos (Titulo, Desarollador, Plataforma, Copias) 
        VALUES (?, ?, ?, ?)
    '''
    params = ("BioShock", "2K", "PC/Consola", 35)

    cursor.execute(query, params)
    conexion.commit()

    conexion.close()
    
    print("Base de Datos creada exitosamente!")

#Modularizamos la consultas
def ejecutarConsulta(query, params=(), fetch=False):
    
    import sqlite3
    
    try:

        with sqlite3.connect("LocalDeJuegos.db") as conexion:

            cursor = conexion.cursor() 
            cursor.execute(query, params)

            if fetch:
                return cursor.fetchall()
            
            conexion.commit()
            return True
    #No necesitamoas cerrar la conexion conexion.close(), se administra automaticamente
    except sqlite3.Error as excepcion:

        print(f"Error en la base de datos: {excepcion}")
        return False

gestionarLocal()