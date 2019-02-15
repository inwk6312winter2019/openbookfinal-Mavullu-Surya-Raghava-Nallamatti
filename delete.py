output='delete.log'


with open('access.log','r') as f, open(output,"a+") as fout:
        for line in f:
                if 'delete' in line:
                        fout.write(line)

                        print(line)
fout.close()






