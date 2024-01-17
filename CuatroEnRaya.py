# libreria para limpiar la pantalla
from IPython.core.display_functions import clear_output


class CuatroEnRaya:
    def __init__(self, filas, columnas):
        """Establecer filas y columnas para iniciar el tablero
        :param: filas: (int) que represente el número de filas del tablero
        :param: columnas: (int) que represent el número de columnas del tablero
        """
        self._filas = filas
        self._columnas = columnas
        self._tablero = self.crear_tablero()
        # atributos de jugar
        self._turno = None

    def crear_tablero(self):
        """Crea las dimensiones del tablero de acuerdo a las filas y columnas del objeto
        :return: tablero
        """
        tablero = [None] * self._filas
        for f in range(self._filas):
            tablero[f] = ['.'] * self._columnas
        return tablero

    def mostrar_tablero(self):
        """Muestra el tablero en pantalla"""
        # sacamos por pantalla la cabecera, de acuerdo a la longitud de una posición
        for num in range(self._columnas):
            print(num, end="  ")  # cambio el salto de línea por defecto por espacios
        # sacamos por pantalla el tablero
        for fila in self._tablero:
            print("")
            # recorre cada casilla de la lista interna de cada posición y asigna 2 espacios
            for casilla in fila:
                print(casilla, end="  ")

    def introducir_ficha(self, columna_ingresada, color_ficha):
        """Esta función introduce una ficha en el tablero indicado.
        :param columna_ingresada: Número de columnas.
        :param color_ficha: Representación de la ficha del tablero
        :return:
        """
        # validamos no pasarnos el rango de la longitud de la primera fila (columnas) y menor a 0
        if columna_ingresada >= self._columnas or columna_ingresada < 0:
            print(f"Error: Número columna {columna_ingresada} fuera del rango")
            return
        elif self._tablero[0][
            columna_ingresada] != '.':  # válida si la fila y la columna respectiva es diferente a punto
            print("Error: La columna esta llena de fichas")
        else:
            # recorremos nuestro tablero desde abajo hacia arriba para validar si hay elemento e insertar
            for fila in range(self._filas - 1, -1, -1):
                # válida si existe un punto en tablero significa que esta vacío
                if self._tablero[fila][columna_ingresada] == ".":
                    self._tablero[fila][columna_ingresada] = color_ficha
                    # retorna el tablero modificado con la nueva ficha
                    return

    def _revisar_filas(self, color_ficha):
        # Recorremos las filas en busca de 4 en raya
        for fila in range(self._filas):
            for columna in range(self._columnas - 3):
                if (self._tablero[fila][columna] == color_ficha
                        and self._tablero[fila][columna + 1] == color_ficha
                        and self._tablero[fila][columna + 2] == color_ficha
                        and self._tablero[fila][columna + 3] == color_ficha):
                    return True

    def _revisar_columnas(self, color_ficha):
        # Recorremos las columnas en busca de 4 en raya
        for columna in range(self._columnas):
            for fila in range(self._filas - 3):
                if (self._tablero[fila][columna] == color_ficha
                        and self._tablero[fila + 1][columna] == color_ficha
                        and self._tablero[fila + 2][columna] == color_ficha
                        and self._tablero[fila + 3][columna] == color_ficha):
                    return True

    def _revisar_diagonal_derecha(self, color_ficha):
        # Recorremos las filas en busca de 4 en raya
        for columna in range(self._columnas - 3):
            for fila in range(self._filas - 1, 2, -1):  # desde abajo hacia arriba y de izquierda a derecha
                if (self._tablero[fila][columna] == color_ficha
                        and self._tablero[fila - 1][columna + 1] == color_ficha
                        and self._tablero[fila - 2][columna + 2] == color_ficha
                        and self._tablero[fila - 3][columna + 3] == color_ficha):
                    return True

    def _revisar_diagonal_izquierda(self, color_ficha):
        # Recorremos las filas en busca de 4 en raya
        for columna in range(self._columnas - 1, 2, -1):
            for fila in range(self._filas - 1, 2, -1):  # desde abajo hacia arriba y de derecha a izquierda
                if (self._tablero[fila][columna] == color_ficha
                        and self._tablero[fila - 1][columna - 1] == color_ficha
                        and self._tablero[fila - 2][columna - 2] == color_ficha
                        and self._tablero[fila - 3][columna - 3] == color_ficha):
                    return True

    def comprobar_ganador(self, color_ficha):
        """Comprueba si se ha producido un cuatro en raya, invocamos a todas los métodos"""
        return self._revisar_filas(color_ficha) or self._revisar_columnas(color_ficha) or \
            self._revisar_diagonal_derecha(color_ficha) or self._revisar_diagonal_izquierda(color_ficha)

    def jugar(self, jugador1='x', jugador2='0'):
        """Inicia el juego mediante los turnos de cada jugador"""
        self._turno = jugador2
        while True:
            self._turno = jugador1 if self._turno == jugador2 else jugador2
            self.mostrar_tablero()
            columnaIngresada = int(input("\nTurno del Jugador {}:".format(self._turno)))
            self.introducir_ficha(columnaIngresada, self._turno)
            # limpiar tableros repetidos
            clear_output(wait=False)
            if self.comprobar_ganador(self._turno):
                self.mostrar_tablero()
                print("\n!!Ganador el jugador", self._turno, "!!")
                break
