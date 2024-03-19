#!/usr/bin/env python3
"""
    This module conatains an coroutine genereator function that takes
    no arguments
"""

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
        this function loops over the range of 10 and sleep for one second
        in each iteration
        yield: AsyncGenerator
    """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
