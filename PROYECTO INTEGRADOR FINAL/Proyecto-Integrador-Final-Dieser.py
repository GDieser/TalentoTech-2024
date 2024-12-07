
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


def mostrarMenuInicio():
    #Menú Principal
    #Me imprime unos separadores
    print("=" * 30)
    print("    🕹️  MENÚ PRINCIPAL 🕹️")
    print("=" * 30)
    print(" 1- ✔️  Agregar un Juego")
    print(" 2- 📄 Mostrar lista de Juegos")
    print(" 3- ♻️  Modificar un Juego")
    print(" 4- ❌ Eliminar un Juego")
    print(" 5- 🙌  Prestar un Juego")
    print()
    print(" 0- ❎ Salir del menú")
    print("=" * 30)
    print()
    opcion = int(input("Su elección: "))

    return opcion

def gestionarLocal(inventario):
    #Acá redireccionamos a la funcion correspondiente
    while True:
        opcion = mostrarMenuInicio()

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
            prestarUnJuego(inventario)
            pass
        elif opcion == 0:
            print('Hasta la próxima! 🖖')
            break
        else:
            print('Opción incorrecta.')
    
def agregarNuevoJuego(inventario):

    codigo = input('Ingrese el codigo del libro: ')
    titulo = input('Ingrese el titulo del libro: ')

    while True:
        #manejo de excepcion
        try:
            copias = int(input('Ingrese la cantidad de copias: '))
            if copias > 0:
                break
            else:
                print("Error: la cantidad de copias debe ser mayor que 0. Intente nuevamente.")
        except ValueError:
            print('Error: ingreso un valor no numerico')

    #libro = [codigo,titulo,cantidad]
    #diccionario
    libro = {
        'codigo' : codigo,
        'titulo' : titulo,
        'copias' : copias
    }
    #agregando a lista de biblioteca un diccionario de libro
    inventario.append(libro)
    print(f'-Juego {titulo} agregado. Codigo: # ' ) #{idCodigo}
    print('-Agregado con éxito!' )

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
        

def eliminarUnJuego(inventario):

    codigo = input("Ingrese ID del Juego: ")

    posicion = buscarUnJuego(inventario, codigo)  # Ignoramos el libro, usamos el índice

    if posicion is not None:

        inventario.pop(posicion)  # Elimina el libro usando el índice
        print(f"El Juego ID '{codigo}' fue eliminado exitosamente.")


def prestarUnJuego(inventario):

    codigo = input('Ingrese ID del Juego a prestar: ')

    posicion = buscarUnJuego(inventario,codigo)

    if posicion is not None:

        if inventario[posicion]['copias'] > 0:

            cantidad = int(input('Ingrese cantidad de copias a prestar: '))

            if cantidad > 0 and cantidad <= inventario[posicion]['copias']:

                inventario[posicion]['copias'] -= cantidad
                print(f'Prestamo exitoso.')

            else:
                print(f'Cantidad no disponible, se disponen de: {inventario[posicion]['copias']}')
        else:
            print('No hay disponibilidad del Juego actualmente.')
        
    else:
        print(f"Id no encontrado...")    


def buscarUnJuego(inventario, codigo_busqueda=''):
  
    posicion = None

    for indice in range(len(inventario)):

        if inventario[indice]['codigo'] == codigo_busqueda:
            posicion = indice
            break

    return posicion


#algortimo principal
gestionarLocal(inventario)