#!/usr/bin/env python3

"""
    This module makes use of the asynchronous function that is imported from
    0-basic_async_function
"""


from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        An asynchronous function that waits for a random seconds and returns
        Return: list of delay time
    """
    wait_list = []

    for i in range(0, n):
        wait_list.append(await task_wait_random(max_delay))

    return sorted(wait_list)
