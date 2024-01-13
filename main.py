from juego import crear_tablero, mostrar_tablero,ingreso_ficha_usuario,introducir_ficha


def ejecutar_juego():
    tablero_asignado = crear_tablero(6, 7)
    columna,color = ingreso_ficha_usuario()
    introducir_ficha(tablero_asignado,columna,color)
    mostrar_tablero(tablero_asignado)


if __name__ == '__main__':
    ejecutar_juego()
    # help(print)
