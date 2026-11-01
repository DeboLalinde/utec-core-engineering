#!/usr/bin/env python3
"""Este módulo define la clase Rectangle."""


class Rectangle:
    """Representa un rectángulo."""

    def __init__(self, width=0, height=0):
        """Inicializa un rectángulo con ancho y alto.

        Args:
            width: El ancho del rectángulo. Por defecto es 0.
            height: El alto del rectángulo. Por defecto es 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Devuelve el ancho del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Asigna el ancho del rectángulo después de validarlo.

        Args:
            value: El nuevo ancho.

        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Devuelve el alto del rectángulo."""
        return self.__height

    @height.setter
    def height(self, value):
        """Asigna el alto del rectángulo después de validarlo.

        Args:
            value: El nuevo alto.

        Raises:
            TypeError: Si value no es un entero.
            ValueError: Si value es menor que 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
