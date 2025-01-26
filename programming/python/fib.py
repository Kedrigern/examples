#!/usr/bin/env python
"""
Fibonacci sequence in modern Python with types, pattern matching, cache and pytest.
"""

import sys
import math
import functools

Number = int | float

@functools.cache
def fib(n: Number) -> int:
    """Return the Nth member of Fibonacci sequence, an exact integer >= 0.

    >>> [fib(n) for n in range(9)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    >>> fib(30)
    832040
    >>> fib(30.0)
    832040
    >>> fib(-1)
    Traceback (most recent call last):
        ...
    ValueError: Bad input, n has to be interger greater that 0.
    """
    match n:
        case 0:
            return 0
        case 1:
            return 1
        case x if isinstance(x, int) and x>1:
            return fib(n-1) + fib(n-2)
        case x if isinstance(x, float) and x>1:
            return fib(math.floor(n)-1) + fib(math.floor(n)-2)
        case _:
            raise ValueError("Bad input, n has to be interger greater that 0.")

def example_of_fib() -> None:
    print(
        "First 9 member of fibonaci sequence:\n", [fib(n) for n in range(9)], "\n"
        "Fib 30\t\t", fib(30), "\n"
        "Fib 30.0\t", fib(30.0), "\n"
    )

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("-t", "--test"):
        import doctest
        doctest.testmod(verbose=True)
    else:
        example_of_fib()
