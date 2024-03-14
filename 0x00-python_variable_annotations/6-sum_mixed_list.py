#!/usr/bin/env python3

""" This module is a type-annotated function sum_mixed_list which takes
    a list mxd_lst of integers and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ takes an args(list[float or int]) and return sum of all elements
        returns: type str
    """
    total_sum = sum(x for x in mxd_lst)

    return total_sum
