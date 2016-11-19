#!/usr/bin/python
# Advent of code 2015
# puzzle 6 by mmirovic

import numpy as np

f = open('input6', 'r')
a = np.zeros((1000,1000))

for l in f:
	l1= l.strip().replace('turn ','').split()
	d = map(int, l1[1].split(',') + l1[3].split(',') )

	if l1[0] == 'on':	
		a[ d[0]:d[2]+1 , d[1]:d[3]+1 ] = np.ones( (abs(d[0]-d[2])+1 , abs(d[1]-d[3])+1) )
	elif l1[0] == 'off':
		a[ d[0]:d[2]+1 , d[1]:d[3]+1 ] = np.zeros( (abs(d[0]-d[2])+1 , abs(d[1]-d[3])+1) )
	else:
		a[ d[0]:d[2]+1 , d[1]:d[3]+1 ] = np.logical_not( a[ d[0]:d[2]+1 , d[1]:d[3]+1 ] )

print 'Total lights lit:', int(a.sum())
