"""
Planimetrics
╱ line
△ triangle
□ square
▭ rectangle
○ circle

∡ angle
⫠ Perpendicular
∥ Parallel lines
"""

from math import pi, sqrt, pow
from typing import Tuple, Self
from dataclasses import dataclass
from abc import ABC, abstractmethod

Point = Tuple[float,float]

@dataclass
class Line:
    p1: Point
    p2: Point

    @property
    def slope(self) -> float:
        return (self.p2[1]-self.p2[0]) / (self.p1[1]-self.p2[0])

    def isParallelTo(self, line: Self) -> bool:
        return self.slope == line.slope

    def isPerpendicularTo(self, line: Self) -> bool:
        return (self.slope * line.slope) == -1

    def findIntersection(self, line: Self) -> Point:
        raise NotImplementedError

class LineSegment(Line):

    @property
    def length(self) -> float:
        return sqrt( pow(self.p2[0]-self.p1[0],2) + pow(self.p2[1]-self.p1[1],2))

class Shape(ABC):
    @abstractmethod
    def volume(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    @abstractmethod
    def symbol(self, verbose=False) -> str:
        pass

@dataclass
class Circle(Shape):
    o: Point
    r: float

    @property
    def center(self) -> Point:
        return self.o

    @property
    def radius(self) -> float:
        return self.r

    @property
    def diameter(self) -> float:
        return self.r * 2

    def volume(self) -> float:
        return pi * pow(self.r,2)

    def perimeter(self) -> float:
        return 2 * pi * self.r

    def symbol(self, verbose=False) -> str:
        if verbose:
            return f"○: {self.o}, ∅ {self.r}"
        return "○"

@dataclass
class Rectangle(Shape):
    """
    d ---- c
    |      |
    a ---- b
    """

    a: Point # left down corner
    c: Point # right up corner

    @property
    def b(self) -> Point:
        return (self.c[0], self.a[1])

    @property
    def d(self) -> Point:
        return (self.a[0], self.c[1])

    @property
    def edge_a(self) -> LineSegment:
        return LineSegment(self.a, self.b)

    @property
    def edge_b(self) -> LineSegment:
        return LineSegment(self.b, self.c)

    def volume(self) -> float:
        return (self.c[0] - self.a[0]) * (self.c[1] - self.a[1])

    def perimeter(self) -> float:
        return 2 * (self.edge_a.length + self.edge_b.length)

    def symbol(self, verbose=False) -> str:
        if verbose:
            return f"▭ A: {self.a}, B: {self.b}, C: {self.c}, D: {self.d}"
        return "▭"

@dataclass
class Triangle(Shape):
    a: Point
    b: Point
    c: Point

    @property
    def edge_a(self) -> LineSegment:
        return LineSegment(self.b,self.c)

    @property
    def edge_b(self) -> LineSegment:
        return LineSegment(self.a,self.c)

    @property
    def edge_c(self) -> LineSegment:
        return LineSegment(self.a,self.b)

    def volume(self) -> float:
        raise NotImplementedError()

    def perimeter(self) -> float:
        return self.edge_a.length + self.edge_b.length + self.edge_c.length

    def symbol(self, verbose=False) -> str:
        if verbose:
            return f"△ A: {self.a}, B: {self.b}, C: {self.c}"
        return "△"

class Polygon(Shape):
    pass

if __name__ == "__main__":
    po = (0,0)
    p1 = (1,1)
    p2 = (1,0)
    p3 = (1,1)
    p4 = (2,1)
    p5 = (3,3)

    l1 = Line(p1,p3)
    l2 = Line(p3,p4) # perpendicular to X axis
    l3 = Line(p3,p5)
    l4 = Line(p2,p3) # perpendicular to Y axis
    c = Circle(p3,1)
    r1 = Rectangle(p1,p3)
    r2 = Rectangle(p1,p4)
    t1 = Triangle(p1,p2,p3)

    print(
        "Example of basic planimetrics implemented in Python:\n",
        f"{l1} slope: {l1.slope}\n",
        f"{l2} slope: {l2.slope} l2 ∥ l1: {l2.isParallelTo(l1)} l2 ⫠ l1: {l2.isPerpendicularTo(l1)}\n",
        f"{l3} slope: {l3.slope} l3 ∥ l1: {l3.isParallelTo(l1)} l3 ⫠ l1: {l3.isPerpendicularTo(l1)}\n",
        f"{l4} slope: {l4.slope} l4 ∥ l2: {l4.isParallelTo(l2)} l4 ⫠ l2: {l4.isPerpendicularTo(l2)}\n",
        f"{c.symbol()} {c} ∅ {c.r}\t\tV: {c.volume():.3f}\tP: {c.perimeter():.3f}\n",
        f"{r1.symbol()} {r1}\tV: {r1.volume()}\t\tP: {r1.perimeter()}\n",
        f"{r2.symbol()} {r2}\tV: {r2.volume()}\t\tP: {r2.perimeter()}\n",
        f"{t1.symbol()} {t1} V: \t P: {t1.perimeter():.3f}"
    )
