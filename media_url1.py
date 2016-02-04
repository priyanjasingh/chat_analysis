#filtering the chat
import os
f = open('1_chat.txt', 'r')
a=0
s = open('media_url_1.txt','wb')
count_media = 0
count_url = 0

for line in f:		
	a = a+1
	if line.find("<Media omitted>")>=1:
		count_media+=1
	if line.find("http:")>=1 or line.find("https:")>=1 :
		count_url+=1		
	
	if (a%10) == 0:	
		s.write(str(a) + " -> " + str(count_media) + ", " + str(count_url))
		s.write("\n")
		count_media=0
		count_url=0


s.close()
f.close()