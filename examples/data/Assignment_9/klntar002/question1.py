""" Tarisai Kalinde
Student Number: KLNTAR002
Program to detect which students need to go and see a stuent advior"""

import math

# entering required input
filename=input('Enter the marks filename:\n')

# accessing file
f=open(filename,"r")
lines=f.readlines()
f.close()


# process to remove the '\n' function so as to access the lines better and to marks into a list
array=[]                                   # empty list
array_names=[]
for i in lines:                            # splitting by the comma
    line= i.split(',')
    for j in line:
        new_line=j.replace('\n','')         # removing '\n'
        if new_line.isdigit():
            array.append(new_line)          # isolating marks in2 an array
        else:
            array_names.append(new_line)    # isolating names in2 an array
                       
#calculating the mean/average
total=0                                    # total of marks initial
for mark in array:
    total+=int(mark)                       # total marks as we iterate
ave=round(total/len(array),2)   # CORRECT THIS ROUND ISH """
if str(ave)[-2]=='.':
    print('The average is: ',str(ave)+'0',sep='')
else:    
    print('The average is:',ave)

# calculating standard deviation
acc_dev=0                           # initial std dev
for mark in array:
    acc_dev+=(int(mark)-ave)*(int(mark)-ave)
std_dev=round( math.sqrt(acc_dev/len(array)),2)               # standard dev
if str(std_dev)[-2]=='.':
    print('The std deviation is: ',str(std_dev)+'0',sep='')
else:
    print('The std deviation is:',std_dev)

# students who should go to student advisors
students=''                                          # initial names of students
bench_mark=ave-std_dev                               # bench mark for student advisor advice
for mark in array:
    if int(mark)<bench_mark:
        students+=array_names[array.index(mark)]+'\n' # if less than bench mark ,add name to string  
if std_dev==0.0:
    print()
else:    
    print('List of students who need to see an advisor:')        
    print(students)        
        
        
