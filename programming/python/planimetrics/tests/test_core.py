import unittest
import math

from planimetrics.core import (Point, Line)


class Construct(unittest.TestCase):
    def test_constructor(self):
        point = Point(10,13,"Actual position")
        self.assertEqual(point.x, 10)
        self.assertEqual(point.y, 13)
        self.assertEqual(point.label, "Actual position")
        point = Point(x=10, y=13, label="Actual position")
        self.assertEqual(point.x, 10)
        self.assertEqual(point.y, 13)
        self.assertEqual(point.label, "Actual position")


class Methods(unittest.TestCase):
    p0  = Point(0,0)
    p0b = Point(0,0)
    p01 = Point(0,1)
    p10 = Point(1,0)
    p11 = Point(1,1)
    p10n = Point(-1,0)
    p01n = Point(0,-1)
    p20  = Point(2,0)
    p20n = Point(-2,0)

    def test_zero_distance(self):
        self.assertEqual(self.p0.distance(self.p0b), 0)
        self.assertEqual(self.p0.distance(self.p0),  0)

    def test_simple_distance(self):
        self.assertEqual(self.p0.distance(self.p01), 1)
        self.assertEqual(self.p0.distance(self.p10), 1)

    def test_distance(self):
        self.assertAlmostEqual(self.p0.distance(self.p11), 1.414, 3)
        self.assertAlmostEqual(self.p0.distance(self.p11), math.sqrt(2), 25)
        self.assertAlmostEqual(self.p11.distance(self.p20n), 3.162, 3)
        self.assertAlmostEqual(self.p11.distance(self.p20n), math.sqrt(2)*math.sqrt(5), 25)
        self.assertAlmostEqual(self.p11.distance(self.p20n), math.sqrt(10), 25)
        self.assertEqual(self.p0.distance(self.p20), 2)
        self.assertEqual(self.p20n.distance(self.p20), 4)

    def test_angles_agains_zero(self):
        know_values = [
            (self.p10,    0),
            (self.p11,   45),
            (self.p01,   90),
            (self.p10n, 180),
            (self.p01n, 270)
        ]
        for p, a in know_values:
            self.assertEqual(
                self.p0.angle(p),
                a,
                "Angle should be {0} (between {1} and {2}".format(a, self.p0, p)
            )


class LineTest(unittest.TestCase):
    def test_construct(self):
        l = Line((0,0), (1,0))
        self.assertEqual(str(l.start), "[0, 0]")
        self.assertEqual(l.distance(), 1)
        self.assertEqual(l.angle(), 0)


if __name__ == '__main__':
    unittest.main()