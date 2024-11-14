"""
Crear un menú interactivo utilizando bucles while y condicionales if-elif-else:
● El menú debe permitir al usuario seleccionar entre diferentes opciones relacionadas con la gestión de productos.
(Cada producto debe ser almacenado en una lista, y debe tener al menos un nombre y una cantidad asociada)
● Entre las opciones, deben incluirse: agregar productos al inventario y mostrar los productos registrados.
(Al seleccionar la opción correspondiente, el sistema debe permitir visualizar los productos almacenados hasta el
momento.)
"""

#Para que los codigos sean autonumerales
idCodigo = 1000
#Para que ingrese al while
opcion = 3
stock = []

while opcion != 0:
    #Me imprime unos separadores
    print("=" * 30)
    print("    🕹️  MENÚ PRINCIPAL 🕹️")
    print("=" * 30)
    print(" 1- ✔️  Agregar un Juego")
    print(" 2- 📄 Mostrar lista de Juegos")
    print(" 3- ♻️  Modificar un juego")
    print()
    print(" 0- ❌Salir del menú")
    print("=" * 30)
    print()
    opcion = int(input("Su elección: "))

    if opcion == 1:
        
        titulo = input('Titulo del juego: ')
        cantidad = int(input('Cantidad disponible: '))
        precio = float(input('Precio de venta: '))
        
        juego = {
            'codigo' : idCodigo,
            'titulo' : titulo,
            'copias' : cantidad,
            'precio' : precio
        }

        stock.append(juego)
        print(f'Juego {titulo} agregado. Codigo: # {idCodigo}' )
        
        #Incrementamos el codigo del juego, que empieza en 1000
        idCodigo = idCodigo+1

    elif opcion == 2:
        #Mostramos cada juego disponible con un for
        print("=" * 30)
        print('     📄 Lista de Juegos:')

        for juego in stock:    
            print("=" * 30)        
            print(f"Titulo: {juego['titulo']} - Codigo: {juego['codigo']}")
            print(f"Copias: {juego['copias']} - Precio: {juego['precio']}")
            
    elif opcion == 3:
        
        codigo = int(input("Codigo del juego a modifica: "))
        contador = 0

        #Lo malo es que modifica todo los parametros (Capaz podria hacer un submenu para cada uno)
        for juego in stock:
            if juego['codigo'] == codigo:
                contador = contador + 1

                juego['titulo'] = input('Nuevo titulo: ')
                juego['cantidad'] = int(input('Cantidad: '))
                juego['precio'] = float(input('Nuevo precio: '))
        
        #Si termina el for y no encontro nada :(
        if contador == 0:
            print("Código no encontrado")

    elif opcion == 0:
        #Salimos del menu con condicion de corte del while
        print('Hasta la proxima! 🖖')
        break
    else:
        print('Ingreso incorrecto.')