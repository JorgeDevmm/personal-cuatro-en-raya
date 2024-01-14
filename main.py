# libreria para limpiar la pantalla
from IPython.core.display_functions import clear_output

from juego import crear_tablero, mostrar_tablero,introducir_ficha,comprobar_ganador


def ejecutar_juego():

    tablero_asignado = crear_tablero(6, 7)
    turno = 'R'
    siguiente_turno = 'A'
    while True:
        # inicia el turno del segundo jugador y regresa al primero en la sgte iteración
        turno = siguiente_turno
        mostrar_tablero(tablero_asignado)
        if turno == 'R':
            columna = int(input(f"turno 'R' Jugador, seleccione columna:"))
            siguiente_turno = 'A'
        elif turno == 'A':
            columna = int(input(f"Turno 'A' jugador, seleccione columna:"))
            siguiente_turno = 'R'
        introducir_ficha(tablero_asignado,columna,turno)
        clear_output(wait=False)
        if comprobar_ganador(tablero_asignado,turno):
            print("Ganador el jugador",turno, "\n\n")
            mostrar_tablero(tablero_asignado)
            break



if __name__ == '__main__':
    ejecutar_juego()
    # help(print)
