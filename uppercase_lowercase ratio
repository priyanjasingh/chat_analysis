#filtering the chat
import os
f = open('1_chat.txt', 'r')
a=0

for line in f:	
	s = open('punctuation.txt','a')
	a = a+1
	count = 0
	space = 0
	
	for t in line:
		if t>='!' and t<='@':
			count=count+1
	s.write(str(a) + " -> " + str(count-1))
	s.write("\n")

s.close()
f.close()