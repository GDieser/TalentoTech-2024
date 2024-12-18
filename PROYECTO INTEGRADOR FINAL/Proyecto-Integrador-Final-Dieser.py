
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
inventario = [    
    {
        'codigo':'1000',
        'titulo':'Halo',
        'copias' : 5
    },
    {
        'codigo':'1001',
        'titulo':'Half-Life',
        'copias' : 15
    }
]


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
    print(" 6- 🔍 Prestar un Juego")
    print(" 7- 📊 Ver Juegos con Stock bajo")
    print(" 8- 📁 Crear Base de Datos")
    print()
    print(" 0- ❎ Salir del menú")
    print("=" * 30)
    print()
    opcion = int(input("Su elección: "))

    return opcion

def gestionarLocal(inventario):
    #Acá redireccionamos a la funcion correspondiente
    while True:
        opcion = mostrarMenuPrincipal()

        if opcion == 1 :
            agregarNuevoJuego(inventario)            
        elif opcion == 2:
            mostrarListaJuegos(inventario)            
        elif opcion == 3:
            modificarJuego(inventario)
            pass
        elif opcion == 4:
            eliminarUnJuego(inventario)
            pass
        elif opcion == 5:
            buscarJuegoPorTitulo()
            pass
        elif opcion == 6:
            #verStockBajo(inventario)
            pass
        elif opcion == 7:
            verStockBajo(inventario)
            pass
        elif opcion == 8:
            inicializarBaseDeDatos()
            pass
        elif opcion == 0:
            print('Hasta la próxima! 🖖')
            break
        else:
            print('Opción incorrecta.')

#1   
def agregarNuevoJuego(inventario):

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
        print('Titulo ya ingresaso, compruebe la lista')


#2
def mostrarListaJuegos(inventario):    

    if not inventario:
        print('Sin stock de juegos disponible...')     

    else:
        encabezado = f"{'Codigo':<10} |{'Titulo':<30} |{'Copias':<10}"
        separador = "-" * len(encabezado)

        print('\n 📄 Listado de Juegos:')

        print(encabezado)
        print(separador)

        for librito in inventario:            
            print(f"{librito['codigo']:<10} |{librito['titulo']:<30} |{librito['copias']:<10}")
        
#3
def modificarJuego(inventario):

    #Implementar buscar por ID y por Titulo.
    codigo = input('Ingrese el ID del Juego: ')
    posicion = buscarUnJuego(inventario,codigo)

    if posicion is not None:

        nuevo_titulo = input('Ingrese el nuevo titulo: ')
        nuevas_copias = int(input('Ingrese la nueva cantidad de copias: '))
        
        #actualizacion de los valores
        inventario[posicion]['titulo'] = nuevo_titulo
        inventario[posicion]['copias'] = nuevas_copias

        print("El juego fue actualizado con éxito.")

    else:
        print('Juego no encontrado...')
        
#4
def eliminarUnJuego(inventario):

    codigo = input("Ingrese ID del Juego: ")

    posicion = buscarUnJuego(inventario, codigo)

    if posicion is not None:

        inventario.pop(posicion)
        print(f"El Juego ID '{codigo}' fue eliminado exitosamente.")

#5
def buscarJuegoPorTitulo(Titulo):
   
    query = """
        SELECT * FROM libros WHERE Titulo = ?
    """
    params = (Titulo,)
    
    juego = ejecutarConsulta(query, params, True)

    return juego    

#6
def buscarJuegoPorId(IdJuego):

    query = """
        SELECT * FROM libros WHERE IdJuego = ?
    """
    params = (IdJuego,)
    
    juego = ejecutarConsulta(query, params, True)

    return juego


#7
def verStockBajo(inventario):
    print("Lala")

#8
def buscarUnJuego(inventario, codigo_busqueda=''):
  
    while True:
        print('1 - Buscar por ID')
        print('2 - Buscar por Titulo')
        print('0 - Volver Atras')
        opcion = int(input("Su elección: "))

        if opcion == 1 :
            IdJuego = input('Ingrese Id del Juego a buscar: ')
            juego = buscarJuegoPorId(IdJuego)  
            if juego:
                print(f'Titulo: {juego[1]}')
            else:
                print('ID no encontrado...')
            return          
        elif opcion == 2:
            titulo = input('Ingrese Titulo del Juego a buscar: ')
            juego = buscarJuegoPorTitulo(titulo)
            if juego:
                print(f'Titulo: {juego[1]}')
            else:
                print('Titulo no encontrado...')
            return
        elif opcion == 0:
            return
        else:
            print('Opción incorrecta.')



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
    params = ("Pacman", "Consola", "Atari", 35)

    cursor.execute(query, params)
    conexion.commit()

    query = '''
        INSERT INTO Juegos (Titulo, Desarollador, Plataforma, Copias) 
        VALUES (?, ?, ?, ?)
    '''
    params = ("Half-Life", "PC", "Sierra", 50)

    cursor.execute(query, params)
    conexion.commit()

    query = '''
        INSERT INTO Juegos (Titulo, Desarollador, Plataforma, Copias) 
        VALUES (?, ?, ?, ?)
    '''
    params = ("Halo", "PC/XBOX", "Microsoft", 30)

    cursor.execute(query, params)
    conexion.commit()

    query = '''
        INSERT INTO Juegos (Titulo, Desarollador, Plataforma, Copias) 
        VALUES (?, ?, ?, ?)
    '''
    params = ("Doom", "PC", "ID", 25)

    cursor.execute(query, params)
    conexion.commit()

    query = '''
        INSERT INTO Juegos (Titulo, Desarollador, Plataforma, Copias) 
        VALUES (?, ?, ?, ?)
    '''
    params = ("Counter-Strike", "PC", "Valve", 55)

    cursor.execute(query, params)
    conexion.commit()

    query = '''
        INSERT INTO Juegos (Titulo, Desarollador, Plataforma, Copias) 
        VALUES (?, ?, ?, ?)
    '''
    params = ("BioShock", "PC/Consola", "2K", 35)

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

#algortimo principal
gestionarLocal(inventario)
