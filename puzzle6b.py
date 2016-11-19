#!/usr/bin/python
# Advent of code 2015
# puzzle 6b by mmirovic

import numpy as np

f = open('input6', 'r')
a = np.zeros((1000,1000))
m = { 'on':1 , 'off':-1, 'toggle':2}

for l in f:
	l1= l.strip().replace('turn ','').split()
	d = map(int, l1[1].split(',') + l1[3].split(',') )

	a[ d[0]:d[2]+1 , d[1]:d[3]+1 ] += m[l1[0]]
	a[ d[0]:d[2]+1 , d[1]:d[3]+1 ] += a[ d[0]:d[2]+1 , d[1]:d[3]+1 ] < 0


print 'Total lights lit:', int(a.sum())
