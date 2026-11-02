#!/usr/bin/env python3
"""Define la clase Square que hereda de Rectangle."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado."""

    def __init__(self, size):
        """Inicializa un cuadrado con size validado."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size * self.__size
