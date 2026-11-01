#!/usr/bin/env python3
"""Este módulo define la clase Square con posición e impresión."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa un cuadrado con tamaño y posición.

        Args:
            size: El tamaño del lado del cuadrado. Por defecto es 0.
            position: Tupla (x, y) con el desplazamiento. Por defecto (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Devuelve la posición del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Asigna la posición del cuadrado después de validarla.

        Args:
            value: Tupla de 2 enteros mayores o iguales a 0.

        Raises:
            TypeError: Si value no es una tupla de 2 enteros positivos.
        """
        message = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(message)
        for number in value:
            if type(number) is not int or number < 0:
                raise TypeError(message)
        self.__position = value

    def area(self):
        """Devuelve el área del cuadrado.

        Returns:
            El área del cuadrado.
        """
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado con el carácter #, respetando la posición."""
        print(self)

    def __str__(self):
        """Devuelve el dibujo del cuadrado como cadena.

        Returns:
            Una cadena vacía si size es 0; si no, el cuadrado desplazado.
        """
        if self.__size == 0:
            return ""
        lines = []
        for _ in range(self.__position[1]):
            lines.append("")
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(lines)
