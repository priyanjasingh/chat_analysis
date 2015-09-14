import os
f = open('time.txt', 'r')
for line in f:
	a = line.index(":::")
	p=line[:a]
	line = line[a:]
	b = line.index(",")
	q=line[:b].replace(":::","")
	r =line[b:].replace("," , "")
	print p,q,r
	
