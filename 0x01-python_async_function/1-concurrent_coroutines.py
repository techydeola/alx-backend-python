#!/usr/bin/env python3

"""
    This module makes use of the asynchronous function that is imported from
    0-basic_async_function
"""


from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        An asynchronous function that waits for a random seconds and returns it
        Return: list of delay time
    """
    wait_list = []

    for i in range(0, n):
        wait_list.append(await wait_random(max_delay))

    return wait_list
