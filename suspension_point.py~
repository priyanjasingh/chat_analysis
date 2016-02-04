#COUNTING SUSPENSION POINT PER LINE
import csv
import os
import sys
f = sys.argv

def suspension_point(fi,num):
	with open('./package/training_set_'+str(num)+'.csv','r') as csvinput:
		with open('./package/training_'+str(num)+'.csv', 'w') as csvoutput:
			writer = csv.writer(csvoutput)
			a=0
			f = open(fi, 'r')
			for row,line in zip(csv.reader(csvinput),f):
				s = open('./package/suspension_point_count_'+str(num)+'.txt','a')
				count = 0
				if a==0:
					writer.writerow(row+["suspension_point"])
				else:
					if line.find("<Media omitted>")==-1:
						while line.find("...")!=-1:
							p = line.index("...")
							count+=1
							line = line[:p] + line[p+3:] 
						s.write(str(a) + " -> " + str(count))
						writer.writerow(row+[count])
						s.write("\n")
					else:
						s.write(str(a) + " -> " + "0")
						writer.writerow(row+["0"])
						s.write("\n")
				
				a = a+1
				s.close()
			f.close()
			
			os.rename('./package/training_'+str(num)+'.csv', './package/training_set_'+str(num)+'.csv')

if __name__ == "__main__":
	suspension_point(str(f[1]),1)
