#!/usr/bin/env python3
"""
    This module imports async_generator from 1-async_comprehension
"""

import time
import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        this function measures the run time of several asynchronous task
        return: elapsed time
    """
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.time()

    return end_time - start_time
