#!/usr/bin/env python3

"""
    an asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random that waits for
    a random delay between 0 and max_delay (included and float value) seconds
    and eventually returns it.
"""


import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
        An asynchronous function that waits for a random seconds and returns it
        Return: random value
    """

    random_delay: Union[float, int] = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
