#!/usr/bin/env python3

""" This module is a Annotation that annotates function parameters and return
    values with the appropriate types
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ A function that return values with appropriate types
        return: values
    """
    return [(i, len(i)) for i in lst]
