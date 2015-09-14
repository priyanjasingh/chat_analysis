from collections import defaultdict

with open('2_chat.txt') as f:
    lines = f.read().splitlines()

result = defaultdict(int)

for line in lines:
	words = line.split()
	for word in words:
		result[word] +=1

s = open('freq_dist_2.txt','wb')

for key, value in result.items():
	s.write(str(key) + " -> " + str(value))
	s.write("\n")


		