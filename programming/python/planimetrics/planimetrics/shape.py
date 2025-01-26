from planimetrics.core import Point


class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass

    @staticmethod
    def _first_point(points):
        """
        Determinate point nearest to the origin ([0,0])

        :param points: Set of points
        :type points: Set
        :return: Point
        """
        if len(points) == 0:
            raise Exception

        for i in range(4):
            quadrant = [p for p in points if Shape._quadrant(p) == 1]
            if len(quadrant) > 0:
                return Shape._nearest_to_origin(quadrant)

    @staticmethod
    def _nearest_to_origin(points):
        min = Point.maxPoint()
        for p in points:
            if p.x == min.x:
                if p.y < min.y:
                    min = p
            elif p.x < min.x:
                min = p
        return min

    @staticmethod
    def _quadrant(point):
        """
        Determinate quadrant of the given point.
        Quadrants are:
         II | I
        ----|----
        III | IV
        :param point:
        :type point: Point
        :return: int in [1,2,3,4]
        """
        if point.y > 0:
            if point.x > 0:
                return 1
            else:
                return 2
        else:
            if point.x < 0:
                return 3
            else:
                return 4


class Triangle(Shape):

    def __init__(self, points):
        """
        :param points: set of three points
        :type points: set
        :return:
        """
        if len(points) != 3:
            raise Exception

        for p in points:
            if not isinstance(p, Point):
                raise Exception

        self._determineNodes(points)

    def _determineNodes(self, points):
        distances = {
            'e1': points[0].distance(points[1]),
            'e2': points[1].distance(points[2]),
            'e3': points[2].distance(points[3])
        }

        ec = max(distances, val = lambda record: distances[record])

        if ec == 'e1':
            self.C = points.pop(2)
        elif ec == 'e2':
            self.C = points.pop(0)
        elif ec == 'e3':
            self.C = points.pop(1)

        if points[0].x < points[1].x:
            self.A = points[0]
            self.B = points[1]
        else:
            self.A = points[1]
            self.B = points[0]

    def perimeter(self):
        l1 = self.A.distance(self.B)
        l2 = self.B.distance(self.C)
        l3 = self.C.distance(self.A)
        return l1 + l2 + l3

    def area(self):
        # todo area of triangle
        pass


class Rectangle(Shape):
    # todo: ordering of points
    # only two points

    def __init__(self, points):
        """
        :param points: 2 point at
        :return:
        """
        if len(points) != 2:
            raise Exception

        p = Shape._nearest_to_origin(points)
        self.A = p
        points.remove(p)
        self.C = points.pop()
        self.B = Point(self.A.y, self.C.x)
        self.D = Point(self.A.x, self.C.y)

    def perimeter(self):
        l1 = self.A.distance(self.B)
        l2 = self.B.distance(self.C)
        l3 = self.C.distance(self.D)
        l4 = self.D.distance(self.A)
        return l1 + l2 + l3 + l4

    def area(self):
        l1 = self.A.distance(self.B)
        l2 = self.A.distance(self.D)
        return l1 * l2


