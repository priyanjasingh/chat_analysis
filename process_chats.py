#filtering the chat
import os
import sys


def process():

	path = './raw'
	for filename in os.listdir(path):
		f = open('./raw/'+filename, 'r')
		x=0
		
		for line in f:
			#print line
			a = line.split(":")
			
			first = a[1]

			b=first.split("-")

			first=b[1]


			f = open('./raw/'+filename, 'r')
			for l in f:
				if l.find(first)==-1:
					a=l.split(":")
					second = a[1]
					b=second.split("-")

					second=b[1]

					print "in loop"
					break
			break	
		print first,second
		
		if not os.path.exists('./chats_process/'+str(first)+'_'+str(second)+'/'):
			os.makedirs('./chats_process/'+first+'_'+second+'/')		

		f = open('./raw/'+filename, 'r')
		a=0
		for line in f:
			if line.find(first)!=-1:
			
				s = open('./chats_process/'+first+'_'+second+'/'+first+'.txt','a')
				index_1 = line.index(first)

				u = line[index_1:]
				m = u.index(":")
				t = u[m:]
			
				a=0
				s.write(t)
			elif line.find(second)!=-1:
				s = open('./chats_process/'+first+'_'+second+'/'+second+'.txt','a')
				index_2 = line.index(second)
				u = line[index_2:]
				m = u.index(":")
				t = u[m:]
				
				a=1
				s.write(t)
			else:
				if a==0:
					s = open('./chats_process/'+first+'_'+second+'/'+first+'.txt','a')
					s.write(line)
				else:
					s = open('./chats_process/'+first+'_'+second+'/'+second+'.txt','a')
					s.write(line)



if __name__ == "__main__":
	process()
		
