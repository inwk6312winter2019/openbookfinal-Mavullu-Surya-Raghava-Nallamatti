fin=open('access.log','r')



k=[]

for line in fin:
	if 'GET' in line:
		line=line.split()
		k.append(line[0])

i=0

for i in range(0,100,2):
	print(k[i])

