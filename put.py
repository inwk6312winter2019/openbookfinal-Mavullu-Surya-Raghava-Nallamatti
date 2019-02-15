output='put.log'


with open('access.log','r') as f, open(output,"a+") as fout:
        for line in f:
                if 'PUT' in line:
                        fout.write(line)

                        print(line)
fout.close()






