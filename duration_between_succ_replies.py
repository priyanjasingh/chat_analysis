import os
from datetime import datetime
f = open('time.txt', 'r')
prev=0
date1=0
for line in f:
	
	a = line.index(":::")
	p=line[:a]
	line = line[a:]
	b = line.index(",")
	q=line[:b].replace(":::","")
	r =line[b:].replace("," , "")
	meridian = r[1:].index(" ")
	Time = r[:meridian+1]
	t = r[meridian+1:]
	if t.find("PM")!=-1:
		hour =Time.index(":")
		n= str(int(Time[:hour].replace(":","")) + 12)
		print p + " " +q + " " +n +" "+Time[hour+1:]

	date2 = datetime.strptime(q +" "+ n +" " +Time[hour+1:]+" 00",'%m/%d/%Y %H %M %S')

	if p!=prev:
		z = open('time_intervel.txt', 'w')
		succ = date2-date1
		z.write(succ)


	date1=date2
	prev=p



		

		
		


	
