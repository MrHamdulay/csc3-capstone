# a program to analyse student marks read in from a file and determine which students need to see a student advisor 
# Sarayn Subroyen
# 12 May 2014

import math

marks = []

file = input('Enter the marks filename:\n')

f = open(file, 'r')                            #open file

lines = f.readlines ()                        #reads file as list of strings

for line in lines:                            # get names and marks from line                            
    name, mark = line.split(',') 
    marks.append(int(mark))


sum_1=0
for i in marks:               
    sum_1=sum_1+i
mean=sum_1/len(marks)                         #calculate the average of the marks

sum_2=0
for j in range(len(marks)):
    sum_2=sum_2+((float(int(marks[j]))-mean)**2)   
std_dev = math.sqrt(sum_2/len(marks))          #calculate the standard deviation of the marks

    
f.close ()                                     #close file

print('The average is: {0:.2f}'.format(mean))

print('The std deviation is: {0:.2f}'.format(std_dev))

for k in range(len(marks)):                   
    
    if float(int(marks[k]))<(mean-std_dev):     #print only if there are sudents who need to see advisor 
        print('List of students who need to see an advisor:')
        break


for l in range(len(marks)):                      #prints names of students who need to see advisor
        
    if float(int(marks[l]))<(mean-std_dev):    
        stu_adv,a=lines[l].split(",")
        print(stu_adv)
    
        
        