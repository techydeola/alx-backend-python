#!/usr/bin/env python3

""" This module is a type-annotated function make_multiplier that takes a
    float multiplier as argument and returns a function that multiplies a
    float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ a function that takes one argument (multiplier)
        returns: a function
    """
    def mult(x: float) -> float:
        """ An inner function that takes one argument
            Return: a float
        """
        
        return multiplier * x
    
    return mult
