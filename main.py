#!/usr/bin/python
#Things to extract
import csv
from filter_chat import extract
from average_word import average_word
from word_length import word_length
from upper_low_ratio import ratio
from msg_length import msg_length
from punctuation_usage import punctuation
from stopword_freq import stopword_usage
from smileys import smiley_count
from acro_line import acro_line

import sys
import os
#take file inp

path = './chats_process'
for filename in os.listdir(path):
		
	#f = open('./raw/'+filename, 'r')
	
	filename=filename.split("_")
	first=filename[0]
	second=filename[1]
	
	print first
	print second
	
	
	'''
	if not os.path.exists('./chats_process/'+str(first)+'_'+str(second)+'/'):
		os.makedirs('./chats_process/'+first+'_'+second+'/')		

	'''	
	t=open('./chats_process/'+str(first)+'_'+str(second)+'/'+'training_set_1.csv', 'w')
	n=open('./chats_process/'+str(first)+'_'+str(second)+'/'+'training_set_2.csv', 'w')

	t1=open('./chats_process/'+str(first)+'_'+str(second)+'/'+'training10_set_1.csv', 'w')
	n1=open('./chats_process/'+str(first)+'_'+str(second)+'/'+'training10_set_2.csv', 'w')

	c = csv.writer(t)#a writer object to write in csv file 
	d = csv.writer(n)

	c1 = csv.writer(t1)#a writer object to write in csv file 
	d1 = csv.writer(n1)


	c.writerow(["serial no"])
	d.writerow(["serial no"])

	c1.writerow(["serial no"])
	d1.writerow(["serial no"])


	i=1
	while i<500:
		c.writerow([i])
		d.writerow([i])
		c1.writerow([i])
		d1.writerow([i])
		#print i
		i=i+1

	t.close()
	n.close()
	t1.close()
	n1.close()

	
	#first feature to extract ////"""average words per line""""
	average_word('./chats_process/'+str(first)+'_'+str(second)+'/'+first+'.txt',str(first),str(second),1)
	#creates a text file named number_word_1 which contains number of word in each line.
	average_word('./chats_process/'+str(first)+'_'+str(second)+'/'+second+'.txt',str(first),str(second),2)
	print "average_word_feature extracted"
	
	'''
	#second feature """word length per line"''
	word_length("./package/1_chat.txt",1)#creates a text file named word_length_1 which contains number of word in each line.
	word_length("./package/2_chat.txt",2)
	print "word_length_feature extracted"

	#third feature ""uppercase_lowrcase ratio""""
	ratio("./package/1_chat.txt",1)#creates a text file named word_length_1 which contains number of word in each line.
	ratio("./package/2_chat.txt",2)
	print "ratio_feature extracted"

	#fourth feature ""time_chat , time to give that particular reply"""


	#sixth feature """smiley count """every 10 line feature usage
	smiley_count("./package/1_chat.txt",1)
	smiley_count("./package/2_chat.txt",2)
	print "smiley count extracted"


	#fifth feature """stopwaord usagee in a line""""every 10 line feature
	stopword_usage("./package/1_chat.txt",1)
	stopword_usage("./package/2_chat.txt",2)
	print "stopword feature extracted"

	#seventh feature """punchuation usage""""
	punctuation("./package/1_chat.txt",1)
	punctuation("./package/2_chat.txt",2)
	print "punctuation_feature extracted"


	#eighth feature """message length ""
	msg_length("./package/1_chat.txt",1)
	msg_length("./package/2_chat.txt",2)
	print "msg_length_feature extracted"

	#ninth feature """acronym count """
	acro_line("./package/1_chat.txt",1)
	acro_line("./package/2_chat.txt",2)
	print "acro_line extracted"

	#tenth feature """how much he has used his common words in these line"""

	'''


