#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
from typing import AsyncIterator
import random


async def async_generator() -> AsyncIterator[float]:
    iter = 1

    while iter < 11:
        await asyncio.sleep(1)
        yield random.uniform(0, 11)

        iter += 1
