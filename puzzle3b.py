#!/usr/bin/python

str = open('input3', 'r').read()
d = { "^": [0, 1], "v": [0, -1], "<": [-1, 0], ">": [1, 0] }

p1 = [0,0]
p2 = [0,0]

a = set ([ (0,0) ])
            
for i, chr in enumerate(str):
	p1 = [ p1[0] + d[chr][0]*(not(i%2)), p1[1] + d[chr][1]*(not(i%2)) ]
	p2 = [ p2[0] + d[chr][0]*(i%2),      p2[1] + d[chr][1]*(i%2)      ]
	a.update([ tuple(p1), tuple(p2) ])

print "Santa & Robo-santa visited %s houses" % len(a)  
