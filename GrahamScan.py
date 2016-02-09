#!/usr/bin/env python
"""
    Computes the convex hull using the Graham scan algorithm.
    May have floating point issues if x- and y-coordinates are not integers.
"""
#from sys import stderr

from stack import stack
from math import atan2

from collections import namedtuple
Point2D = namedtuple('Point2D', ['x', 'y'])

class GrahamScan():

    """
        The GrahamScan class provides methods for computing the convex hull of a set of N points in the plane.
    
        The implementation uses the Graham-Scan convex hull algorithm.
               
        Time Complexity: O(N log N)
        Space Complexity: O(N)
    
        For additional documentation, see <a href="http://algs4.cs.princeton.edu/99scientific">Section 9.9</a> of
        Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
        
        @author Robert Sedgewick
        @author Kevin Wayne

        @translator Mauro Lacy (Java2Py)
    """
    def __init__(self, pts):
        """
            Computes the convex hull of the specified array of points.
            
            pts is a list of elements of class 'Point2D'.

        """
        self.hull = stack()
        self.concave = [] # indices of concave segments (in the original array)

        N = len(pts)
       
        # Create derived type with an added 'index' field; tag the elements with their (original) index
        Point2Di = namedtuple('Point2Di', Point2D._fields + ('index',))
        points = [Point2Di(*p, index=i) for i, p in enumerate(pts)]
        
        # Preprocess so that points[0] has lowest y-coordinate; break ties by x-coordinate
        # points[0] is an extreme point of the convex hull
#        points.sort(key = lambda p: (p.y, p.x)])
#        p0 = points[0]
        # (alternatively, could do easily (and cleanly) in linear time)
        p0 = min(points, key = lambda p: (p.y, p.x))
        
        def polar(q):
            """
                Sorts by polar angle with respect to base point p0,
                breaking ties by distance (squared) to p0
            """
            p = p0
            dx = q.x - p.x
            dy = q.y - p.y
            theta = atan2(dy, dx)
            r2 = dx*dx + dy*dy
            return (theta, r2)
        
        points.sort(key = polar)
        
        self.hull.push(p0)    # p[0] is first extreme point

        # find index k1 of first point not equal to points[0]
        equal = True
        k1 = 1
        for k1 in range(1, N):
            if p0.x != points[k1].x or p0.y != points[k1].y:
                equal = False
                break
        if equal:
            return  # all points equal
        
        # find index k2 of first point not collinear with points[0] and points[k1]
        k2 = k1 + 1
        for k2 in range(k1 + 1, N):
            if self.ccw(p0, points[k1], points[k2]) != 0:
                break
        self.hull.push(points[k2-1]) # points[k2-1] is second extreme point

        # Graham scan; note that points[N-1] is extreme point different from points[0]
        for i in range(k2, N):
            top = self.hull.pop()
            while self.hull and self.ccw(self.hull.peek(), top, points[i]) <= 0:
                # top is concave
                self.concave.append(top.index)
                top = self.hull.pop()
            self.hull.push(top)
            self.hull.push(points[i])
#        assert(self.is_convex())

    def ccw(self, a, b, c):
        """
            Is a->b->c a counterclockwise turn?
            Returns { -1, 0, +1 } if a->b->c is a { clockwise, collinear; counterclockwise } turn.
        """
        area2 = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
        if area2 < 0:
            return -1
        elif area2 > 0:
            return +1
        else:
            return  0

    def get_hull(self):
        """
            Returns the extreme points on the convex hull in counterclockwise order.
        """
        return [Point2D(p.x, p.y) for p in self.hull]

    # check that boundary of hull is strictly convex
    def is_convex(self):
        N = len(self.hull)
        if N <= 2:
            return True
        points = self.hull[::]

        for i in range(N):
            if self.ccw(points[i], points[(i+1) % N], points[(i+2) % N]) <= 0:
                return False
        return True
    
    def get_concavity_indices(self):
        return self.concave

if __name__ == '__main__':
    from sys import stdin
    
    """
        Unit tests the GrahamScan class.
        Reads in an integer N and N points (specified by
        their x- and y-coordinates) from standard input;
        computes their convex hull; and prints out the points on the
        convex hull to standard output.
    """    
    N = int(stdin.readline())
    points = list()
    for i in range(N):
        (x, y) = map(int, stdin.readline().split())
        points.append(Point2D(x, y))
    graham = GrahamScan(points)
    for p in graham.get_hull():
        print '(%d, %d)' % (p.x, p.y)

"""
    Copyright 2016, Mauro Lacy.
    
    This file is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    It is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this file. If not, see http://www.gnu.org/licenses.
 """