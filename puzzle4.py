#!/usr/bin/python
# Advent of code 2015
# puzzle4 by mmirovic

import hashlib
import sys
import signal

def signal_handler(signal, frame):
        print '\nTerminated at iteration %d' % i
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

key = "yzbqklnj"

l = input ("How many 0's in the hash? ")

i = 0
while hashlib.md5(key+str(i)).hexdigest()[0:l] != '0'*l :
	i += 1
	if (i % 1000000) == 0:
		sys.stdout.write('.')
		sys.stdout.flush()

print "\nIteration: %d, hash: %s" % (i, hashlib.md5(key+str(i)).hexdigest())
