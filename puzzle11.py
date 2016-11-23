#!/usr/bin/python
# Advent of code 2015
# puzzle 11 by mmirovic

#pwd = map (ord, "hepxcrrq")
pwd = map (ord, "hepxxzaa")

pwd[:] = [x - 97 for x in pwd] + [-1,-1]

bad = map (ord, "iol")
bad[:] = [x - 97 for x in bad]

while 1:

	# inc function, base 26, start from right, reminder set to 1
	i, r = 7, 1
	while i >= 0:	
		n = pwd[i]+r
		pwd[i] = n%26
		r      = n/26
		i -= 1

	# found next pass: 3 consecutive, no 'iol', 2xpairs
	f = [0,1,0]		
	dou = set([])
	for i in range(len(pwd)-2):
		if pwd[i] == pwd[i+1]-1 and pwd[i+1] == pwd[i+2]-1: f[0]=1
		if pwd[i] in bad: f[1]=0
		if pwd[i] == pwd[i+1]: dou.add(pwd[i])
	if len(dou) >= 2: f[2]=1
	
	if sum(f) == 3: break	
		
pwd[:] = [x + 97 for x in pwd]
pwd[8:10]=[]
print "".join (map (chr, pwd))
