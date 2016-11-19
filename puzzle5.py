#!/usr/bin/python

f = open('input5', 'r')

v = 'aeiou'
b = ['ab', 'cd', 'pq', 'xy']

nice = 0

for l in f:
	vow, bw, dou = 0, 0, 0

	for i in range(len(l)-1):

		if l[i] in v: vow += 1 
		if l[i] == l[i+1]: dou = 1
		if any(k == l[i:i+2] for k in b): bw = 1
	
	if vow >= 3 and bw == 0 and dou == 1: 
		nice += 1
		print "Nice ",
	else:
		print "Bad  ",
	print "word: ", l.strip(), vow, bw, dou

print "Total nice words: ", nice
