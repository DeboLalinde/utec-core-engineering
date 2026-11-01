#!/usr/bin/env python3
"""Este módulo define la clase Square con getter y setter para size."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa un cuadrado con el tamaño indicado.

        Args:
            size: El tamaño del lado del cuadrado. Por defecto es 0.
        """
        self.size = size

    @property
    def size(self):
        """Devuelve el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Asigna el tamaño del cuadrado después de validarlo.

        Args:
            value: El nuevo tamaño del lado del cuadrado.

        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Devuelve el área del cuadrado.

        Returns:
            El área del cuadrado.
        """
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado con el carácter #.

        Si size es 0, imprime una línea vacía.
        """
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__size):
            print("#" * self.__size)
