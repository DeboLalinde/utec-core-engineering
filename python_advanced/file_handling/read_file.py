#!/usr/bin/env python3
"""Modulo que contiene la funcion read_file."""


def read_file(filename=""):
    """Lee un archivo de texto UTF-8 y lo imprime en stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        contenido = f.read()
    print(contenido, end="")
