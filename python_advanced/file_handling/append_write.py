#!/usr/bin/env python3
"""Módulo que contiene la función que agrega cadenas de texto al final."""


def append_write(filename="", text=""):
    """Añade texto al final de un archivo y devuelve los caracteres."""
    with open(filename, "a", encoding="utf-8") as f:
        cantidad = f.write(text)
    return cantidad
