#!/usr/bin/env python
#coding: utf
class stack(list):
    def __init__(self):
        super(stack, self).__init__()
        
    def push(self, v):
        self.append(v)

    def peek(self):
        return self[-1]
        
def testStack(A):
    st = stack()
    for a in A:
        st.push(a)
    return st

TEST = [
        [(4, 0), (3, 1), (2, 0), (1, 0), (5, 0)],
        [(1, 0)],
        [(1, 1)],
        [(1, 0), (2, 1)],
        [(1, 1), (2, 0)],
        [(2, 1), (3, 1), (5, 0)],
        [(6, 1), (3, 1), (5, 0)],
       ]

if __name__ == "__main__":
    from sys import stderr
    for T in TEST:
        print "T:", T, ":", testStack(T)
