#!/usr/bin/env python3

"""
    This module makes use of the asynchronous function that is imported from
    0-basic_async_function
"""


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        A function that return the type of a coroutine function.
        Return: asynchio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
