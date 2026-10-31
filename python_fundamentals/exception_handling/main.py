#!/usr/bin/env python3
raise_exception_msg = __import__('raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("Hola Deborah")
except NameError as ne:
    print(ne)
