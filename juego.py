def crear_tablero(filas, columnas):
    """Crea el tablero de Juego

    :param: filas: (int) que represente el número de filas del tablero
    :param: columnas: (int) que represent el número de columnas del tablero
    :return: tablero
    """
    tablero = [None] * filas
    for f in range(filas):
        tablero[f] = ['.'] * columnas

    return tablero


def mostrar_tablero(tablero):
    """Muestra el tablero en pantalla

    :param tablero:
    :return:
    """
    # sacamos por pantalla la cabecera, de acuerdo a la longitud de una posición
    for num in range(len(tablero[0])):
        print(num, end="  ")  # cambio el salto de línea por defecto por espacios

    # sacamos por pantalla el tablero
    for fila in tablero:
        print("")
        # recorre cada casilla de la lista interna de cada posición y asigna 2 espacios
        for casilla in fila:
            print(casilla, end="  ")


def introducir_ficha(tablero, columna, color):
    """Esta función introduce una ficha en el tablero indicado.

    :param tablero: Lista.
    :param columna: Número de columnas.
    :param color: Representación de la ficha del tablero
    :return:
    """
    # validamos no pasarnos el rango de la longitud de la primera fila (columnas) y menor a 0
    if columna >= len(tablero[0]) or columna < 0:
        print(f"Error: Número columna {columna} fuera del rango")
        return
    elif tablero[0][columna] != '.':  # válida si la fila y la columna respectiva es diferente a punto
        print("Error: La columna esta llena de fichas")
    else:
        # recorremos nuestro tablero desde abajo hacia arriba para validar si hay elemento e insertar
        for fila in range(len(tablero) - 1, -1, -1):
            # válida si existe un punto en tablero significa que esta vacío
            if tablero[fila][columna] == ".":
                tablero[fila][columna] = color
                # retorna el tablero modificado con la nueva ficha
                return tablero


def ingreso_ficha_usuario():
    """Ingreso de la columna y el tipo de ficha de usuario """

    columna = int(input("Ingresar la posición de columna a ingresar ficha: "))
    color = input("Ingresar el tipo de ficha a utilizar: ")

    return columna, color
