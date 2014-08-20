import math

markslist = []

inputfile = input('Enter the marks filename:\n')

infile = open(inputfile, 'r')

linestring = infile.readlines ()

for line in linestring:
    
    name, mark = line.split(',')
    m = mark
    markslist.append(int(m))


sum_m=0
for i in markslist:
    sum_m+=i
mean=sum_m/len(markslist)
fd=0
for i in range(len(markslist)):
    fd=fd+((markslist[i]-mean)**2)
sd = fd/len(markslist)
    
std_dev = math.sqrt(sd)
    

infile.close ()

print('The average is: {0:.2f}'.format(mean))

print('The std deviation is: {0:.2f}'.format(std_dev))


for i in range(len(markslist)):
    
    if float(int(markslist[i]))<(mean-std_dev):
        print('List of students who need to see an advisor:')
        break


for i in range(len(markslist)):
        
    if float(int(markslist[i]))<(mean-std_dev):    
        p,k=linestring[i].split(",")
        print(p)

