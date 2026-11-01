#!/usr/bin/env python3
"""Este módulo define la clase Square con validación de tamaño."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa un cuadrado con el tamaño indicado.

        Args:
            size: El tamaño del lado del cuadrado. Por defecto es 0.

        Raises:
            TypeError: Si size no es un entero.
            ValueError: Si size es menor que 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Devuelve el área del cuadrado.

        Returns:
            El área del cuadrado.
        """
        return self.__size ** 2
        