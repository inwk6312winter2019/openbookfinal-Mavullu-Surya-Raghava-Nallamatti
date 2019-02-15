
output='get.log'


with open('access.log','r') as f, open(output,"a+") as fout:
	for line in f:
		if 'get' in line:
			fout.write(line)
			
			print(line)
fout.close()
