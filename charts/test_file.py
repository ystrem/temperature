import random
h = 1
m  = 1
s = 1
t = {}


with open('temperature.log','w') as f:
	for i in range(500):
		h += 1
		m += 1 
		s += 1
		if h == 24:
			h = 1
		if m == 60:
			m = 1
		if s == 60:
			s = 1
		f.writelines('2014-02-07 ' + str(h) + ':' + str(m + 2) + ":" + str(s + 1) + '; ' + str(round(random.uniform(15,30),1)) + '\n')
	print f


with open('temperature.log','r') as f:
	data = f.readlines()
	
	for line in data:
		t[line.split(';')[0]] = line.split(';')[1]

print t
		
