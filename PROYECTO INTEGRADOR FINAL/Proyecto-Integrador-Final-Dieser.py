
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
#Para dar un poco de color
from colorama import init, Fore, Style, Back
init(autoreset=True)

#Acá redireccionamos a la funcion correspondiente
def gestionarLocal():

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

#Menú Principal
def mostrarMenuPrincipal():
    
    while True:
        try:
            print("=" * 30)
            print(Fore.LIGHTRED_EX+Style.BRIGHT+"    🕹️  MENÚ PRINCIPAL 🕹️")
            print("=" * 30)
            print(Fore.LIGHTCYAN_EX+Style.BRIGHT+" 1- ✔️  Agregar un Juego")
            print(Fore.LIGHTCYAN_EX+Style.BRIGHT+" 2- 📄 Mostrar lista de Juegos")
            print(Fore.LIGHTCYAN_EX+Style.BRIGHT+" 3- ♻️  Modificar un Juego")
            print(Fore.LIGHTCYAN_EX+Style.BRIGHT+" 4- ❌ Eliminar un Juego")
            print(Fore.LIGHTCYAN_EX+Style.BRIGHT+" 5- 🔍 Buscar un Juego")
            print(Fore.LIGHTCYAN_EX+Style.BRIGHT+" 6- 🤝 Prestar un Juego")
            print(Fore.LIGHTCYAN_EX+Style.BRIGHT+" 7- 📊 Ver Juegos con Stock bajo")
            print(Fore.LIGHTGREEN_EX+Style.BRIGHT+" 8- 📁 Crear Base de Datos")
            print()
            print(Fore.LIGHTMAGENTA_EX+Style.BRIGHT+" 0- ❎ Salir del menú")
            print("=" * 30)
            print()

            opcion = int(input("Su elección: "))
            if 0 <= opcion <= 8:
                return opcion
            else:
                print(Back.RED+Fore.YELLOW+"Por favor, ingrese un número válido.")
        except ValueError:
            print(Back.RED+Fore.YELLOW+"ERROR, Solo ingresar número.")

#1 - Agregar un juego
def agregarNuevoJuego():
    try:
        titulo = input('Ingrese el Título del Juego: ')
        # Verificar si el título ya existe en la DB
        juego = buscarJuegoPorTitulo(titulo)
        if juego:
            print('Título ya ingresado, compruebe la lista.')
            return

        desarrollador = input('Ingrese el Desarrollador: ')
        plataforma = input('Ingrese la Plataforma: ')

        while True:
            try:
                #Nos aseguramos que se ingresen solo numeros y valores validos
                copias = int(input('Ingrese copias en stock (mayor a 0): '))
                if copias > 0:
                    break
                else:
                    print(Back.RED+Fore.YELLOW+"LA COPIAS DEBEN MAS DE 0.")
            except ValueError:
                print(Back.RED+Fore.YELLOW+'ERROR: Debe ingresar un número entero...')

        query = '''
            INSERT INTO Juegos (Titulo, Desarollador, Plataforma, Copias) 
            VALUES (?, ?, ?, ?)
        '''
        params = (titulo, desarrollador, plataforma, copias)

        if ejecutarConsulta(query, params):
            print(Back.GREEN+f'Juego "{titulo}" agregado con éxito!')
    #Por si hay algun error en la DB
    except Exception as ex:
        print(Back.RED+Fore.YELLOW+f"Error inesperado al agregar el juego: {ex}")

#2 - Mostrar juegos disponibles
def mostrarListaJuegos():    

    query = """
        SELECT * FROM Juegos
    """

    juegos = ejecutarConsulta(query, '', True)

    if not juegos:
        print(Back.YELLOW+'Sin stock de juegos disponible...')     

    else:
        #Inspirado en las clases 🤣 
        encabezado = f"{'ID':^{5}} |{'Titulo':^{20}} |{'Plataforma':^{15}} |{'Desarollador':^{15}} |{'Stock':^{4}}"
        separador = "-" * len(encabezado)

        print('\n 📄 Listado de Juegos:')

        print(encabezado)
        print(separador)

        for juego in juegos:    
            Idjuego, Titulo, Plataforma, Desarrollador, Copias = juego        
            print(
                f"{Idjuego:^{5}} |{Titulo:^{20}} |"
                f"{Plataforma:^{15}} |{Desarrollador:^{15}} |"
                f"{Copias:^{4}}"
            )

#3 - Modificar un juego
def modificarJuego():
    #Implementar buscar por ID.
    try:
        idJuego = int(input('Ingrese el ID del Juego: '))
    except ValueError:
        print(Back.RED+Fore.YELLOW+'ERROR, Ingrese solo números...')
        return
    juegos = buscarJuegoPorId(idJuego)

    if juegos:
        for juego in juegos:    
            Idjuego, Titulo, Plataforma, Desarrollador, Copias = juego
        
        while True:
            print('1 - Cambiar Titulo')
            print('2 - Cambiar Plataforma')
            print('3 - Cambiar Desarollador')
            print('4 - Cambiar Cantidad en Stock')
            print('5 - CONFIRMAR CAMBIOS')
            print('0 - Volver Atras')
            
            try:
                opcion = int(input("Su elección: "))
            except ValueError:
                print(Back.RED+Fore.YELLOW+'ERROR, Ingrese solo números...')
                continue

            if opcion == 1:
                nuevoTitulo = input('Ingrese nuevo Titulo: ')
                juegoExistente = buscarJuegoPorTitulo(nuevoTitulo)
                if juegoExistente:
                    print(Back.RED+Fore.YELLOW+'ERROR, Ya existe un juego con este titulo, pruebe con otro.')
                else:
                    Titulo = nuevoTitulo

            elif opcion == 2:
                Plataforma = input('Ingrese nueva Plataforma: ')

            elif opcion == 3:
                Desarrollador = input('Ingrese nuevo Desarrollador: ')

            elif opcion == 4:
                try:
                    nuevoStock = int(input('Ingrese nueva Cantidad: '))
                    if nuevoStock < 0:
                        print(Back.RED+Fore.YELLOW+'ERROR, ingrese solo numero positivos.')
                    else:
                        Copias = nuevoStock
                except ValueError:
                    print(Back.RED+Fore.YELLOW+'ERROR, ingrese solo numeros...')

            elif opcion == 5:
                #Confirmar y guardar los cambios
                break
            elif opcion == 0:
                #Cancelamos y volvemos al menu prinmcipal
                print(Back.GREEN+Fore.LIGHTRED_EX+'Operación cancelada.')
                return
            else:
                print('Opción incorrecta.')

        #Guardamos
        query = '''
            UPDATE Juegos
            SET Titulo = ?,
                Desarollador = ?,
                Plataforma = ?,
                Copias = ?
            WHERE IdJuego = ?
        '''
        params = (Titulo, Desarrollador, Plataforma, Copias, idJuego)

        if ejecutarConsulta(query, params):
            print("El juego fue actualizado con éxito!")
        else:
            print(Back.RED+Fore.YELLOW+"Hubo un error inesperado...")
    else:
        print(Back.GREEN+Fore.LIGHTRED_EX+'Juego no encontrado...')
        
#4 - Eliminar un juego
def eliminarUnJuego():

    try:
        idJuego = input('Ingrese el ID del Juego a eliminar: ')
        juegos = buscarJuegoPorId(idJuego)

        #Si no encuntra nada, retorna
        if not juegos:
            print(Back.YELLOW+Fore.LIGHTRED_EX+'Juego no encontrado...')
            return

        while True:
            try:
                #Pequeña validación y confrimacion antes de eliminar
                print("¿Está seguro que desea eliminar el Juego?")
                print("1 - Sí || 2 - No")
                opcion = int(input("Su elección: "))

                if opcion == 1:
                    query = '''
                        DELETE FROM Juegos WHERE IdJuego = ?
                    '''
                    params = (idJuego,)
                    #Confirmamos eliminación
                    if ejecutarConsulta(query, params):
                        print("Juego eliminado exitosamente!")
                    break

                elif opcion == 2:
                    print("Eliminación cancelada.")
                    break
                else:
                    print("Opción incorrecta, intente nuevamente.")

            except ValueError:
                print(Back.RED+Fore.YELLOW+"ERROR, ingrese un valor valido.")
    #Por si hay algun error en la DB
    except Exception as ex:
        print(Back.RED+Fore.YELLOW+f"Error inesperado al eliminar el juego: {ex}")

#5 - Buscamos un juego puede ser por Id o Titulo
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
            print(Back.YELLOW+Fore.WHITE+'Opción incorrecta.')

        if juegos:
            for juego in juegos:
                Idjuego, Titulo, Plataforma, Desarrollador, Copias = juego
                        
            print(f"Id: {Idjuego}, Titulo: {Titulo}, Plataforma: {Plataforma}, "
                  f"Desarrollador: {Desarrollador}, Cantidad: {Copias}")
        else:
            print(Back.YELLOW+Fore.WHITE+'Juego no encontrado...')
        break

#5 - Buscamos por titulo
def buscarJuegoPorTitulo(Titulo):
   
    query = """
        SELECT * FROM Juegos WHERE Titulo = ?
    """
    params = (Titulo,)
    
    juego = ejecutarConsulta(query, params, True)

    return juego   
 
#5 - Buscamos por ID
def buscarJuegoPorId(IdJuego):

    query = """
        SELECT * FROM Juegos WHERE IdJuego = ?
    """
    params = (IdJuego,)
    
    juego = ejecutarConsulta(query, params, True)

    return juego

#6 - Prestamos juegos
def prestarUnJuego():
    try:
        IdJuego = input('Ingrese Id del Juego a prestar: ')
        juegos = buscarJuegoPorId(IdJuego)

        if not juegos:
            print('Juego no encontrado...')
            return

        for juego in juegos:
            Idjuego, Titulo, Plataforma, Desarrollador, Copias = juego

        while True:
            try:
                prestamo = int(input('Ingrese cantidad a prestar: '))
                if prestamo <= 0:
                    print("La cantidad debe ser mayor a 0.")
                elif Copias - prestamo < 0:
                    print('No hay suficientes juegos para prestar...')
                else:
                    break
            except ValueError:
                print(Back.RED+Fore.YELLOW+"ERROR: Debe ingresar un número valido.")

        # Actualizamos el stock
        query = '''
            UPDATE Juegos SET Copias = ? WHERE IdJuego = ?
        '''
        params = ((Copias - prestamo), IdJuego)
        ejecutarConsulta(query, params)

        print('Juegos prestados exitosamente!')
    #Por si hay algun error en la DB
    except Exception as ex:
        print(Back.RED+Fore.YELLOW+f"Error inesperado al prestar el juego: {ex}")


#7 Consulta de stock bajos
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
            Idjuego, Titulo, Plataforma, Desarrollador, Copias = juego        
            print(
                f"{Idjuego:^{5}} |{Titulo:^{20}} |"
                f"{Plataforma:^{15}} |{Desarrollador:^{15}} |"
                f"{Copias:^{4}}"
            )

#8 - Creamos la DB con algunos registros(opcional)
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

    query = '''
        INSERT INTO Juegos (Titulo, Desarollador, Plataforma, Copias) 
        VALUES (?, ?, ?, ?)
    '''
    params = ("Maincraft", "Mojang", "PC/Consola", 2)

    cursor.execute(query, params)
    conexion.commit()

    query = '''
        INSERT INTO Juegos (Titulo, Desarollador, Plataforma, Copias) 
        VALUES (?, ?, ?, ?)
    '''
    params = ("GTA V", "Rockstar", "PC/Consola", 3)

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
    except sqlite3.Error as ex:

        print(Back.RED+Fore.YELLOW+f"Error con la Base de Datos: {ex}")
        return False

#Empieza el programa
gestionarLocal()