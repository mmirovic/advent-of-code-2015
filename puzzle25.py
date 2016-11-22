#!/usr/bin/python
# Advent of code 2015
# puzzle 25 by mmirovic

#c = map ( int, raw_input("Enter code location, comma separated: ").split(',') )
c = [2978, 3083]
code = 20151125

iter = sum(range(c[0]+c[1]-1)) + c[1] -1

print "Iterations to do: ", iter

for i in range (iter):
 code = (code * 252533) % 33554393

print "Final code: ", code


