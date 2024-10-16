#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]: # type: ignore
    """
    Loops 10 times
    Yield a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
