import math


class Point:
    x = 0
    y = 0
    label = ""

    def __init__(self, x, y, label = ""):
        """
        :param x: position on x axe
        :param y: position on y axe
        :param label: label
        :return:
        """
        self.x = x
        self.y = y
        self.label = label

    def __str__(self):
        return "[{0}, {1}]".format(self.x, self.y)

    @property
    def toTuple(self):
        return (self.x, self.y)

    def distance(self, point):
        """
        Calculate distance between this instance and given point.

        :param point:
        :return: number
        """
        dx = math.pow(self.x - point.x, 2)
        dy = math.pow(self.y - point.y, 2)
        return math.sqrt(dx + dy)

    def angle(self, point):
        """
        Slope or gradient of a line
        Czech: Směrnice přímky

        :param point:
        :return:
        """
        dx = point.x - self.x
        dy = point.y - self.y

        if dx == 0:
            if dy < 0:
                return 180+90
            else:
                return 90

        if dy == 0 and dx < 0:
            # negative zero
            return 180

        k = dy / dx

        radians = math.atan(k)

        angle = math.degrees(radians)

        return angle

    @staticmethod
    def maxPoint():
        """
        :return: maximum point
        """
        return Point(float("inf"), float("inf"))


class Line:

    def __init__(self, start, end):
        if isinstance(start, tuple):
            self.start = Point(start[0],start[1])
        else:
            self.start = start
        if isinstance(end, tuple):
            self.end = Point(end[0], end[1])
        else:
            self.end = end

    def distance(self):
        return self.start.distance(self.end)

    def angle(self):
        return self.start.angle(self.end)

    # todo: směrnicová rovnice přímky