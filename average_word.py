#filtering the chat
import os
f = open('1_chat.txt', 'r')
a=0

for line in f:	
	s = open('number_word.txt','a')
	a = a+1
	count = 0
	space = 0
	if line.find("<Media omitted>")==-1:
		for t in line:
			if(t==' '):
				space=space+1
		s.write(str(a) + " -> " + str(space))
		s.write("\n")

s.close()
f.close()