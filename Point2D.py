#!/usr/bin/env python
"""
    ./Point2D.py x0 y0 N
    
    Immutable point data type for points in the plane.
"""

import math

"""
    The Point class is an immutable data type to encapsulate a
    two-dimensional point with real-value coordinates.
    
    Note: in order to deal with the difference behavior of double and 
    Double with respect to -0.0 and +0.0, the Point2D constructor converts
    any coordinates that are -0.0 to +0.0.
    
    For additional documentation, see Section 1.2 of
    Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
    
    author: Robert Sedgewick
    author: Kevin Wayne    
    
    author: Mauro Lacy (Java2Py)
"""
class Point2D:
    def __init__(self, x, y, i=None):
        """
            Initializes a new point (x, y)
                x the x-coordinate
                y the y-coordinate
                throws IllegalArgumentException if either x or y is NaN, float('inf') or float('-inf')
        """
        if x == float('inf') or y == float('inf'):
            raise Exception("Coordinates must be finite")
        if x == float('-inf') or y == float('-inf'):
            raise Exception("Coordinates must be finite")
        if x == float('NaN') or y == float('NaN'):
            raise Exception("Coordinates cannot be NaN")
        if (x == 0.0):
            x = 0.0 # convert -0.0 to +0.0
        if (y == 0.0):
            y = 0.0 # convert -0.0 to +0.0
        self.x = x
        self.y = y

        self.index = i

    def xOrder(self, q):
        """
            Orders points by x-coordinate.
        """
        return q.x

    def yOrder(self, q):
        """
            Orders points by y-coordinate,
            breaking ties by x-coordinate
        """
        return (q.y, q.x)

    def rOrder(self, q):
        """
            Orders points by polar radius.
        """
        # compare points according to their polar radius
        return q.x*q.x + q.y*q.y
   
    def polarOrder(self, q):
        """
            Orders by polar angle with respect to this point,
            breaking ties by distance (squared) to this point.
        """
        dx = q.x - self.x
        dy = q.y - self.y
        theta = math.atan2(dy, dx)
        r2 = dx*dx + dy*dy
        return (theta, r2)

    def atan2Order(self, q):
        """
            Order points by atan2() angle (between -pi and pi) with respect to this point.
        """
        # compare other points relative to atan2 angle (bewteen -pi/2 and pi/2) they make with this Point
        return self.angleTo(q)

    def distanceOrder(self, q):
        """
            Order points by distance
        """
        # compare points according to their distance to this point
        return self.distanceSquaredTo(q)

    """
        Returns the polar radius of this point.
        @return the polar radius of this point in polar coordiantes: sqrt(x*x + y*y)
    """
    def r(self):
        return math.sqrt(self.x*self.x + self.y*self.y)
    
    """
        Returns the angle of this point in polar coordinates.
        @return the angle (in radians) of this point in polar coordiantes (between -pi/2 and pi/2)
    """
    def theta(self):
        return math.atan2(self.y, self.x)

    """
        Returns the angle between this point and that point.
        @return the angle in radians (between -pi and pi) between this point and that point (0 if equal)
    """
    def angleTo(self, that):
        dx = that.x - self.x
        dy = that.y - self.y
        return math.atan2(dy, dx)

    """
        Is a->b->c a counterclockwise turn?
        @param a first point
        @param b second point
        @param c third point
        @return { -1, 0, +1 } if a->b->c is a { clockwise, collinear; counterclocwise } turn.
    """
    def ccw(self, b, c):
        area2 = (b.x-self.x)*(c.y-self.y) - (b.y-self.y)*(c.x-self.x)
#        print 'ccw: area:', area2, ', a:', self, ', b:', b, ', c:', c
        if area2 < 0.:
            return -1
        elif area2 > 0.:
            return +1
        else:
            return  0

    """
        Returns twice the signed area of the triangle self-b-c.
        @param self first point
        @param b second point
        @param c third point
        @return twice the signed area of the triangle self-b-c
    """
    def area2(self, b, c):
        return (b.x - self.x) * (c.y - self.y) - (b.y - self.y) * (c.x - self.x)

    """
        Returns the Euclidean distance between this point and that point.
        @param that the other point
        @return the Euclidean distance between this point and that point
    """
    def distanceTo(self, that):
        dx = self.x - that.x
        dy = self.y - that.y
        return math.sqrt(dx*dx + dy*dy)

    """
        Returns the square of the Euclidean distance between this point and that point.
        @param that the other point
        @return the square of the Euclidean distance between this point and that point
    """
    def distanceSquaredTo(self, that):
        dx = self.x - that.x
        dy = self.y - that.y
        return dx*dx + dy*dy

    """
        Compares this point to that point by y-coordinate, breaking ties by x-coordinate.
        @param that the other point
        @return { a negative integer, zero, a positive integer } if this point is
           { less than, equal to, greater than } that point
    """
    def __cmp__(self, that):
        if (self.y < that.y):
            return -1
        if (self.y > that.y):
            return +1
        if (self.x < that.x):
            return -1
        if (self.x > that.x):
            return +1
        return 0

    def __eq__(self, other):
        """
            Does this point is equal to other?
            @param other the other point
            @return true if this point equals the other point; false otherwise
        """
        if other is self:
            return True
        if other is None:
            return False
        if type(other) != type(self):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """
            Does this point is not equal to other?
            @param other the other point
            @return true if this point is not equal to the other point; false otherwise
        """
        if other is self:
            return False
        if other is None:
            return True
        if type(other) != type(self):
            return True
        return self.x != other.x or self.y != other.y

    def __repr__(self):
        """
            Return a string representation of this point.
            @return a string representation of this point in the format (x, y)
        """
        return '(%s, %s)' % (str(self.x), str(self.y))

    def __hash__(self):
        """
            Returns an integer hash code for this point.
            @return an integer hash code for this point
        """
        hashX = self.x.__hash__()
        hashY = self.y.__hash__()
        return 31*hashX + hashY

    def draw(self):
        """
            Plot this point using standard draw.
        """
        # TODO: implement using matplotlib
#        StdDraw.point(self.x, self.y)
        pass

    def drawTo(self, that):
        """
            Plot a line from this point to that point using standard draw.
            @param that the other point
        """
        # TODO: implement using matplotlib
#        StdDraw.line(self.x, self.y, that.x, that.y)
        pass

if __name__ == '__main__':
    from sys import argv, stderr, exit
    from random import randint
    """
        Unit tests the point data type.
    """
    if len(argv) != 4:
        print >>stderr, 'Usage: %s <x0> <y0> <N>' % argv[0]
        exit(1)
    x0 = int(argv[1])
    y0 = int(argv[2])
    N  = int(argv[3])
    
#    StdDraw.setCanvasSize(800, 800)
#    StdDraw.setXscale(0, 100)
#    StdDraw.setYscale(0, 100)
#    StdDraw.setPenRadius(.005)
    
    points = [ None ] * N
    print 'Points:'
    for i in range(N):
        x = randint(1, 100)
        y = randint(1, 100)
        points[i] = Point2D(x, y)
        points[i].draw()
        print points[i]

    # draw p = (x0, x1) in red
    p = Point2D(x0, y0)
#    StdDraw.setPenColor(StdDraw.RED)
#    StdDraw.setPenRadius(.02)
    p.draw()
    print
    print 'Point:', p
    # draw line segments from p to each point, one at a time, in polar order
#    StdDraw.setPenRadius()
#    StdDraw.setPenColor(StdDraw.BLUE)

#    Arrays.sort(points, p.POLAR_ORDER)
    points.sort(key = p.polarOrder)
    print 'Sorted by polar angle wrt to %s:' % p
    for i in range(N):
#        p.drawTo(points[i])
        print points[i]
#        StdDraw.show(100)