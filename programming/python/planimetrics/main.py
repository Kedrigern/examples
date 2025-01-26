#!/usr/bin/env python3
# encoding: utf8

__doc__ = """
Initial point of app
"""

from planimetrics.core import *
from planimetrics.shape import *


def main():
    p1 = Point(0, 0)
    p2 = Point(1, 0)
    l = Line(p1, p2)
    print("Hello world")
    print("Line from %s to %s has length %s" % (p1, p2, l.distance()))

if __name__ == '__main__':
    main()
