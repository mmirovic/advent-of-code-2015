#!/usr/bin/python

str = open('input3', 'r').read()
d = { "^": [0, 1], "v": [0, -1], "<": [-1, 0], ">": [1, 0] }

p = [0,0]
a = set ([ (0,0) ])
            
for chr in str:
 p = [ p[0] + d[chr][0], p[1] + d[chr][1] ]
 a.add( tuple(p) )

print len(a)
