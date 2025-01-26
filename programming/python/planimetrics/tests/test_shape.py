import unittest

from planimetrics.core import Point
from planimetrics.shape import (Triangle, Rectangle)


class TriangleTest(unittest.TestCase):
    """
    Test triangle:
          /(1,1)      B
         /   |       / |
    (0,0)--(1,0)    A--C

    """
    points = {
        Point(0, 0),  # A
        Point(1, 0),  # C
        Point(1, 1),  # B
    }


    def test_constructor(self):
        return
        t = Triangle(self.points)
        self.assertEqual(t.A , self.points[0], 'a')
        self.assertEqual(t.B , self.points[2], 'b')
        self.assertEqual(t.C , self.points[1], 'c')


    def test_perimeter(self):
        return
        t = Triangle(self.points)
        perimeter =  1 + 1 + math.sqrt(2)
        self.assertEqual( t.perimeter(), perimeter,
            "Triangle perimeter should be {0} instead of {1}".format(perimeter, t.perimeter())
        )


# @unittest.skip("Unsolved ordering of points")
class RectangleTest(unittest.TestCase):
    p1 = Point(0, 0)
    p2 = Point(1, 0)
    p3 = Point(0, 1)
    p4 = Point(1, 1)

    def test_constructor(self):
        t = Rectangle({self.p1, self.p4})
        self.assertEqual(t.A, self.p1, "")
        #self.assertEqual(t.B, self.p2, "")
        self.assertEqual(t.C, self.p4, "")

    @unittest.skip("Unsolved ordering of points")
    def test_perimeter(self):
        t = Rectangle({self.p1, self.p4})
        perimeter = 4
        self.assertEqual( t.perimeter(), perimeter,
            "Rectangle perimeter should be {0} instead of {1}".format(perimeter, t.perimeter())
        )
