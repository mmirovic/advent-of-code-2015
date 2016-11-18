#!/usr/bin/python

f = open('input2', 'r')

b = 0

for l in f:
 a = sorted( map(int, l.strip().split("x") ) )
 b += 2*(a[0]+a[1]) + a[0]*a[1]*a[2]

print b

