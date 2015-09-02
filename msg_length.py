#filtering the chat
import os
f = open('1_chat.txt', 'r')
a=0
for line in f:	
	s = open('msg_length.txt','a')
	a = a+1
	count = 0
	if line.find("<Media omitted>")==-1:
		for t in line:
			if((t>='a' and t<='z') or (t>='A' and t<='Z')):
				count = count+1
		s.write(str(a) + " -> " + str(count))
		s.write("\n")


