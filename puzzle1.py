#!/usr/bin/python

str = open('input1', 'r').read()

f = 0
for chr in str:
 f += 1 if chr == "(" else -1
print f

