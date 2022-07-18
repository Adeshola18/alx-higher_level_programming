#!/usr/bin/python3
#function that prints "{:d}".format()

def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:

        value (int): The integer toprint

    Returns:
        If a Type Error or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        Print("{:d}".format()(value))
        return(True)
    except (TypeError, ValueError):
        return(False)
