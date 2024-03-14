#!/usr/bin/env python3

""" a type-annotated function sum_list which takes a list input_list
    of floats as argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ takes an args(list[float]) and return sum of all elements
        returns: type str
    """
    total_sum = sum(x for x in input_list)

    return total_sum
