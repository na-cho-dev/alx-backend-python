#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
from typing import AsyncIterator
import random


async def async_generator() -> AsyncIterator[float]:
    """
    Loops 10 times
    Yield a random number between 0 and 10
    """
    iter = 1

    while iter < 11:
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

        iter += 1
