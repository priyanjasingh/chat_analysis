#filtering the chat
import csv
import os
import sys
f = sys.argv
if __name__ == "__main__":
	ratio(str(f[1]),0)
def ratio(fi,num):
	with open('./package/training_set_'+str(num)+'.csv','r') as csvinput:
		with open('./package/training_'+str(num)+'.csv', 'w') as csvoutput:
			writer = csv.writer(csvoutput)
			f = open(fi, 'r')
			a=0

			for row,line in zip(csv.reader(csvinput),f):	
				s = open('./package/upp_low_ratio'+str(num)+'.txt','a')

				upp_count = 0
				low_count = 0
				if a==0:
					writer.writerow(row+["up","low_ratio"])
				else:
					for t in line:
						if t>='a' and t<='z':
							low_count=low_count+1
						if t>='A' and t<='Z':
							upp_count=upp_count+1
					s.write(str(a) + " -> " + str(low_count)+"/"+str(upp_count))
					writer.writerow(row+[low_count,upp_count])
					s.write("\n")
				a = a+1
			s.close()
			f.close()
			os.rename('./package/training_'+str(num)+'.csv', './package/training_set_'+str(num)+'.csv')
