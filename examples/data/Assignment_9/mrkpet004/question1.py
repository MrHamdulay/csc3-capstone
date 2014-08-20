"""program to analyse student marks read in from a file and determine which students need to see a student advisor
peter m muriuki
16/5/14"""

import math
#open and load the data from the file
filename=input("Enter the marks filename:\n")
file=open (filename, "r")
lines=file.readlines ()
file.close()
sum_n=0
n=0

#get the student names and their respective marks
for i in range(len(lines)):
    x=lines[i].find(",")
    name=lines[i][:(x)]
    mark=int(lines[i][(x+1):])
    sum_n+=mark
    n+=1

#find the average and the standard deviation and print them out
average=sum_n/n
sum_ave=0
for i in range (len(lines)):
    x=lines[i].find(",")
    mark=int(lines[i][(x+1):])
    item=((mark-average)**2)/n
    sum_ave+=item
stdev=math.sqrt(sum_ave)
print("The average is: "+"{:0.2f}".format(average))
print("The std deviation is: "+"{:0.2f}".format(stdev))

if stdev!=0:
    print("List of students who need to see an advisor:")
    #get names of students with marks less than 1 standard deviation below the average
    for i in range (len(lines)):
        x=lines[i].find(",")
        name=lines[i][:(x)]
        mark=int(lines[i][(x+1):]) 
        if mark<(average-stdev):
            print(name)