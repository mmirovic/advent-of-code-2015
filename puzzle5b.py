#!/usr/bin/python
# Advent of code 2015
# puzzle 5b by mmirovic

f = open('input5', 'r')

nice = 0

for l in f:

	double1, double2 = 0, 0

	for i in range(len(l)-1):

		if len(l.replace(l[i:i+2],'')) < 15: double1 = 1
		if l[i] == l[min(i+2, len(l)-1)]: double2 = 1
			
	if (double1 and double2) == 1: 
		nice += 1
		print "Nice ",
	else:
		print "Bad  ",
	print "word: ", l.strip(), double1, double2

print "Total nice words: ", nice
