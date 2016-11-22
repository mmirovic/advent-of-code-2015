#!/usr/bin/python
# Advent of code 2015
# puzzle 7 by mmirovic

from collections import defaultdict
import signal, sys

def signal_handler(signal, frame):
        print '\nTerminated with value ', v['a']
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


f = open('input7b', 'r')

v = defaultdict(lambda: 0) 
 
def val(s):
    try: 
        return int(s)
    except ValueError:
        return v[s]

print "Running..."
while 1:
	for l in f:

		l1= l.strip().split()

		if l1[0] == 'NOT':
			v[l1[-1]] = 65535 - val(l1[1])
		if l1[1] == '->':
			v[l1[-1]] = val(l1[0])
		if l1[1] == 'RSHIFT':
			v[l1[-1]] = val(l1[0]) >> val(l1[2])
		if l1[1] == 'LSHIFT':
			v[l1[-1]] = (val(l1[0]) << val(l1[2]))
		if l1[1] == 'AND':
			v[l1[-1]] = val(l1[0]) & val(l1[2])
		if l1[1] == 'OR':
			v[l1[-1]] = val(l1[0]) | val(l1[2])

	f.seek(0)
