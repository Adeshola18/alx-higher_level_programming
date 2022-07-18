#!/usr/bin/python3
#function that prints "{:d}".format()

def safe_print_integer(value):
    try:
        int(value)
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
