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

from elongation_of_vowel import elongation_vowel
from suspension_point import suspension_point
from imitation_rate import imitation_rate


import sys
import os
#take file inp
f = str(sys.argv[1])
t=open("./package/training_set_1.csv", 'w')
n=open("./package/training_set_2.csv", 'w')

t1=open("./package/training10_set_1.csv", 'w')
n1=open("./package/training10_set_2.csv", 'w')

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

#f = open("package/"+file[1], 'r')
#seperating the two chats

print f
extract(f)

#two files 1_chat and 2_chat are created
#first feature to extract ////"""average words per line""""
average_word("./package/1_chat.txt",1)#creates a text file named number_word_1 which contains number of word in each line.
average_word("./package/2_chat.txt",2)
print "average_word_feature extracted"

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


#tenth feature """elongation of vowel count"""
elongation_vowel("./package/1_chat.txt",1)
elongation_vowel("./package/2_chat.txt",2)
print "elongation of vowel count"

#eleventh feature """suspension count """
suspension_point("./package/1_chat.txt",1)
suspension_point("./package/2_chat.txt",2)
print "suspension count"

#twelth feature """imitiation_rate """
imitation_rate("./package/number_word_1.txt",1)
imitation_rate("./package/number_word_2.txt",2)
print "imitiation_rate"


#tenth feature """how much he has used his common words in these line"""




