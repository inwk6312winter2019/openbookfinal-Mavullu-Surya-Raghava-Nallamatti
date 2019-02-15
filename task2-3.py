
fin=open('access.log','r')


count=0
count1=0
for line in fin:
        if 'firefox' in line:
                count+=1
	if 'chrome' in line:
		count1+=1
print('firefox appeared ',count,' times')
print('chrome appeared ', count1,' times')
