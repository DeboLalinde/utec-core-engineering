#!/usr/bin/env python3
"""Modulo que contiene la funcion write_file."""


def write_file(filename="", text=""):
    """Escribe un texto en un archivo UTF-8 y devuelve los caract. escr."""
    with open(filename, "w", encoding="utf-8") as f:
        cantidad = f.write(text)
    return cantidad
