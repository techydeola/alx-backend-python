#!/usr/bin/env python3

"""
    This module makes use of the asynchronous function that is imported from
    0-basic_async_function and measures the run time
"""


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        An asynchronous function that measure run time for an async function
        Return: elapsed time / 2
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time: float = time.time()
    elapsed_time: float = end_time - start_time

    return elapsed_time / 2
