#filtering the chat
import csv
import os
import sys
f = sys.argv
if __name__ == "__main__":
	average_word(str(f[1]))
def word_length(fi,num):
	with open('./package/training_set_'+str(num)+'.csv','r') as csvinput:
		with open('./package/training_'+str(num)+'.csv', 'w') as csvoutput:
			writer = csv.writer(csvoutput)
			f = open(fi, 'r')
			a=0
			for row,line in zip(csv.reader(csvinput),f):	
				s = open('./package/word_length_'+str(num)+'.txt','a')
				count = 0
				space = 0
				if a==0:
					writer.writerow(row+["word length"])
				else:
					if line.find("<Media omitted>")==-1:
						for t in line:
							if((t>='a' and t<='z') or (t>='A' and t<='Z')):
								count = count+1
							elif(t==' '):
								space=space+1
						s.write(str(a) + " -> " + str(count/space))
						writer.writerow(row+[count/space])
						s.write("\n")
				a=a+1
			s.close()
			f.close()
			os.rename('./package/training_'+str(num)+'.csv', './package/training_set_'+str(num)+'.csv')
