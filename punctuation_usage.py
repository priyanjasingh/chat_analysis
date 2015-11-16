#filtering the chat
import csv
import os
import sys
f = sys.argv
if __name__ == "__main__":
	punctuation(str(f[1]),0)
def punctuation(fi,num):
	with open('./package/training_set_'+str(num)+'.csv','r') as csvinput:
		with open('./package/training_'+str(num)+'.csv', 'w') as csvoutput:
			writer = csv.writer(csvoutput)
			a=0
			f = open(fi, 'r')
			for row,line in zip(csv.reader(csvinput),f):	
				s = open('./package/punctuation.txt','a')
				
				count = 0
				space = 0
				
				if a==0:
					writer.writerow(row+["punctuation"])
				else:
					if line.find("<Media omitted>")==-1:
						for t in line:
							if t>='!' and t<='@':
								count=count+1
						s.write(str(a) + " -> " + str(count-1))
						s.write("\n")
						writer.writerow(row+[count-1])
					else:
						s.write(str(a) + " -> " +"0")
						s.write("\n")
						writer.writerow(row+["0"])		
				a = a+1
			s.close()
			f.close()
			
			os.rename('./package/training_'+str(num)+'.csv', './package/training_set_'+str(num)+'.csv')




