#!/usr/bin/env python3
"""Define la clase Rectangle con área y representación en texto."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representa un rectángulo con ancho y alto."""

    def __init__(self, width, height):
        """Inicializa un rectángulo con width y height validados."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Devuelve el área del rectángulo."""
        return self.__width * self.__height

    def __str__(self):
        """Devuelve la descripción del rectángulo."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
