from juego import crear_tablero, mostrar_tablero


def ejecutar_juego():
    tablero_asignado = crear_tablero(6, 7)
    mostrar_tablero(tablero_asignado)


if __name__ == '__main__':
    ejecutar_juego()
