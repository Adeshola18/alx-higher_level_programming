#!/usr/bin/python3
"""print ASCII alphabet in lowercase without new line with exemption of q and e'"""
for letter in range(97, 123):
    if chr(letter) is not 'q' and chr(letter) is not 'e'
        print("{}".format(chr(letter)), end="")
