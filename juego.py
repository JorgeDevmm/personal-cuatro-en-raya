
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


def introducir_ficha(tablero, columna, color_ficha):
    """Esta función introduce una ficha en el tablero indicado.

    :param tablero: Lista.
    :param columna: Número de columnas.
    :param color_ficha: Representación de la ficha del tablero
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
                tablero[fila][columna] = color_ficha
                # retorna el tablero modificado con la nueva ficha
                return tablero



def revisar_filas(tablero, color_ficha):
    # Obtenemos el número de filas y columnas
    numero_filas = len(tablero)
    numero_columnas = len(tablero[0])
    # Recorremos las filas en busca de 4 en raya
    for fila in range(numero_filas):
        for columna in range(numero_columnas - 3):
            if (tablero[fila][columna] == color_ficha and tablero[fila][columna + 1] == color_ficha
                    and tablero[fila][columna + 2] == color_ficha and tablero[fila][columna + 3] == color_ficha):
                return True


def revisar_columnas(tablero, color_ficha):
    # Obtenemos el número de filas y columnas
    numero_filas = len(tablero)
    numero_columnas = len(tablero[0])
    # Recorremos las columnas en busca de 4 en raya
    for columna in range(numero_columnas):
        for fila in range(numero_filas - 3):
            if (tablero[fila][columna] == color_ficha and tablero[fila + 1][columna] == color_ficha
                    and tablero[fila + 2][columna] == color_ficha and tablero[fila + 3][columna] == color_ficha):
                return True


def revisar_diagonal_derecha(tablero, color_ficha):
    # obtenemos el número de filas y columnas
    numero_filas = len(tablero)
    numero_columnas = len(tablero[0])
    # Recorremos las filas en busca de 4 en raya
    for columna in range(numero_columnas - 3):
        for fila in range(numero_filas - 1, 2, -1):  # desde abajo hacia arriba y de izquierda a derecha
            if tablero[fila][columna] == color_ficha and tablero[fila - 1][columna + 1] == color_ficha and \
                    tablero[fila - 2][columna + 2] == color_ficha and tablero[fila - 3][columna + 3] == color_ficha:
                return True


def revisar_diagonal_izquierda(tablero, color_ficha):
    # obtenemos el número de filas y columnas
    numero_filas = len(tablero)
    numero_columnas = len(tablero[0])
    # Recorremos las filas en busca de 4 en raya
    for columna in range(numero_columnas - 1, 2, -1):
        for fila in range(numero_filas - 1, 2, -1):  # desde abajo hacia arriba y de derecha a izquierda
            if tablero[fila][columna] == color_ficha and tablero[fila - 1][columna - 1] == color_ficha and \
                    tablero[fila - 2][columna - 2] == color_ficha and tablero[fila - 3][columna - 3] == color_ficha:
                return True


def comprobar_ganador(tablero, color_ficha):
    """Comprueba si se ha producido un cuatro en raya, invocamos a todas las funciones"""
    return revisar_filas(tablero, color_ficha) or revisar_columnas(tablero, color_ficha) or revisar_diagonal_derecha(
        tablero, color_ficha) or revisar_diagonal_izquierda(tablero, color_ficha)


