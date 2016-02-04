#filtering the chat
import os
f = open('chat.txt', 'r')
a=0
for line in f:
	if line.find("Sarang")!=-1:
	
		s = open('1_chat.txt','a')
		index_1 = line.index(": ")

		t = line[index_1:]
		print t
		a=0
		s.write(t)
	elif line.find("Priyanja")!=-1:
		p = open('2_chat.txt','a')
		index_2 = line.index(": ")
		t = line[index_2:]
		a=1
		p.write(t)
	else:
		if a==0:
			s = open('1_chat.txt','a')
			s.write(line)
		else:
			p = open('2_chat.txt','a')
			p.write(line)

			
		
