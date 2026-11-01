#!/usr/bin/env python3
"""Define la clase BaseGeometry."""


class BaseGeometry:
    """Clase base para figuras geométricas."""

    def area(self):
        """Lanza una excepción porque el área no está implementada."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que value sea un entero mayor que 0."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
