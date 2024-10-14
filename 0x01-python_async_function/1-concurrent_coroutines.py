#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Calls (wait_random) (n) number of times and
    Returns a list of all the delays (float values)
    """
    tasks = [wait_random(max_delay)] * n
    result = await asyncio.gather(*tasks)

    return sorted(result)
