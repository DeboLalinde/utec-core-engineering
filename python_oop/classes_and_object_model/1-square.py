#!/usr/bin/env python3
"""Este módulo define la clase Square con un tamaño privado."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size):
        """Inicializa un cuadrado con el tamaño indicado.

        Args:
            size: El tamaño del lado del cuadrado.
        """
        self.__size = size
