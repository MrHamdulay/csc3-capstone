'''Python program to analyse student marks read in from a file and determine which students need to see a student advisor
Nxumalo Goodman
16 May 2014'''

import math
#prompt the user to enter the filename
fname = input('Enter the marks filename:\n')
f = open(fname,'r')
flines = f.readlines()
f.close()

lines = flines
for i in range(len(lines)-1):
    lines[i] = lines[i][:-1]

#calculates the mean
total_sum = 0
for i in range(len(lines)):
    lines[i] = lines[i].split(",")
    total_sum += int(lines[i][-1])
mean = total_sum/len(lines)



m = mean
total_sum = 0
#calculates the standard  deviation
for i in range(len(lines)):
    total_sum += (int(lines[i][-1])-m)**2
    
under_root = total_sum/len(lines)  
stanDev = math.sqrt(under_root)
 

print('The average is: {:.2f}'.format(mean))
print('The std deviation is: {:.2f}'.format(stanDev))




for i in range(len(flines)-len(lines)):
    flines[i] = flines[i][:-1]
    
c = 1
stan = mean - stanDev
#checks if the student does need to see the student advisor
for i in range(len(flines)):
    fline = int(flines[i][-1])
    if fline < stan:
        for d in range(c):
            print('List of students who need to see an advisor:')
            c = 0
        print(flines[i][0])
        
