#!/usr/bin/env python3
"""
    This module imports async_generator from the previous task
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        this function collects 10 random number from the async generator
        yield: AsyncGenerator
    """
    return [i async for i in async_generator()]
