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
        print(num, end="  ")

    # sacamos por pantalla el tablero
    for fila in tablero:
        print("")
        # recorre cada casilla de la lista interna de cada posición y asigna 2 espacios
        for casilla in fila:
            print(casilla, end="  ")

