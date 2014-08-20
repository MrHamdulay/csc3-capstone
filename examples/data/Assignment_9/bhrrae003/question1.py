import math

mks = []

inputfile = input('Enter the marks filename:\n')

in_file = open(inputfile, 'r')

file_lines = in_file.readlines ()

for line in file_lines:
    
    name, mark = line.split(',')
    m = mark
    mks.append(int(m))


sum_m=0
for i in mks:
    sum_m+=i
mean=sum_m/len(mks)
fd=0
for i in range(len(mks)):
    fd=fd+((mks[i]-mean)**2)
sd = fd/len(mks)
    
std_dev = math.sqrt(sd)
    

in_file.close ()

print('The average is: {0:.2f}'.format(mean))

print('The std deviation is: {0:.2f}'.format(std_dev))


for i in range(len(mks)):
    
    if float(int(mks[i]))<(mean-std_dev):
        print('List of students who need to see an advisor:')
        break


for i in range(len(mks)):
        
    if float(int(mks[i]))<(mean-std_dev):    
        p,k=file_lines[i].split(",")
        print(p)

