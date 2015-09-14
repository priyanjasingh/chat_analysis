#filtering the chat and extracting time 
#for each person reply 

import os
f = open('chat.txt', 'r')
a=1 #first person speaking
for line in f:
	s = open('time.txt','a')
	line.replace("," , " ::: ")
	if line.find("Sarang")!=-1:
	
		
		index_1 = line.index(" - ") #truncate by #

		t = line[:index_1] # put date and time in a file
		print t
		a=1
		s.write(str(a) + " ::: " +t)

		s.write("\n")
		s.close()
	elif line.find("Priyanja")!=-1:
		
		index_2 = line.index(" - ")
		t = line[:index_2]
		a=2 # second person speaking
		s.write(str(a) + " ::: " +t)
		s.write("\n")
		s.close()
	
	

			
		
