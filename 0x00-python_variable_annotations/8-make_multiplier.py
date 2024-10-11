#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies
    a float by multiplier
    """
    def func(n: float) -> float:
        """ multiplies a float by multiplier """
        return float(n * multiplier)

    return func
