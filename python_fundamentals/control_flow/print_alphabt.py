#!/usr/bin/env python3
letters = ""
for code in range(ord("a"), ord("z") + 1):
    letter = chr(code)
    if letter != "e" and letter != "q":
        letters = letters + letter
print("{}".format(letters), end="")
