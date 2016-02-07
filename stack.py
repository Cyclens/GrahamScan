#!/usr/bin/env python
#coding: utf
class stack():
    def __init__(self):
        self.stack = []
        
    def __len__(self):
        return len(self.stack)
    
    def __repr__(self):
        return self.stack.__repr__()
        
    def __getitem__(self, i):
        return self.stack[i] 
    
    def __iter__(self):
        for e in self.stack:
            yield e
    
    def push(self, v):
        self.stack.append(v)

    def peek(self):
        return self.stack[-1]
        
    def pop(self):
        return self.stack.pop()
    
def testStack1(A):
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
        ST = testStack1(T)
        print "T:", T, ":", ST
        assert(e1 == e2 for e1, e2 in zip(T, ST))
