import csv
import os
import sys
from collections import defaultdict
import codecs


f = sys.argv
if __name__ == "__main__":
    average_word(str(f[1]),0)

def smiley_count(fi,num):
    with open('./package/training_set_'+str(num)+'.csv','r') as csvinput:
        with open('./package/training_'+str(num)+'.csv', 'w') as csvoutput:
            writer = csv.writer(csvoutput)
            f = open(fi, 'r')
            cnt = 0
            a=0
            s = open('./package/smiley_'+str(num)+'.txt','a')
            
            for row,line in zip(csv.reader(csvinput),f):    
                
                line=unicode(line,"utf-8")

                if a==0:
                    writer.writerow(row+["smiley_count"])
                else:
                    words = line.split()
                    for word in words: 
                        for letter in word:
                            st=letter.encode('utf-8')
                            if st >= '\xF0\x9F\x98\x81' and st <='\xF0\x9F\x99\x8F':
                                cnt+=1
                    #if (a%10) == 0: 
                        #print str(a)
                    s.write(str(a) + " -> " + str(cnt))
                    writer.writerow(row+[cnt])
                    s.write("\n")
                    cnt=0
                a+=1       
            s.close()
            f.close()
            
            os.rename('./package/training_'+str(num)+'.csv', './package/training_set_'+str(num)+'.csv')



