#!/usr/bin/env python3
"""
This module contains the function 'task_wait_n'
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Executes task_wait_random n times.

    Args:
        n (int): number.
        max_delay (int): maximum time delay.

    Returns:
        (List[float]): A list containing only floats.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
