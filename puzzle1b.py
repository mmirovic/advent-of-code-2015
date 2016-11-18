#!/usr/bin/python

str = open('input1', 'r').read()

f = 0

i = 0
while f != -1:
	f += 1 if str[i] == "(" else -1
	i += 1

print i
