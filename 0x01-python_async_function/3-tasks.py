#!/usr/bin/env python3

"""
    This module makes use of the asynchronous function that is imported from
    0-basic_async_function
"""


from typing import Any
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """
        A function that measure run time for an async function
        Return: asynchio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
