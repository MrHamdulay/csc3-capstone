'''Program to analyse student marks read in from a file and determine which students need to see a student advisor.
Daniel M.Tamale
TMLDAN001
2014-05-16'''

import math
filename=input('Enter the marks filename:\n')
file=open(filename,'r')
student_file=file.readlines()
file.close()

'''To calculate average mark'''
sum=0
count=0
for i in student_file:
    i=i[:-1]
    lists=i.split(',')
    if len(lists)==2:
        count+=1
        sum+=int(lists[1])  
average=sum/count
print('The average is: {:.2f}'.format(average))

'''To calculate standard deviation'''
standard_deviation=0
for i in student_file:
    i=i[:-1]
    lists=i.split(',')
    if len(lists)==2:
        standard_deviation+=(int(lists[1])-average)**2
standard_deviation=math.sqrt(standard_deviation/count)
print('The std deviation is: {:.2f}'.format(standard_deviation))

'''To print list of students to see an advisor'''
advisor=0
for i in student_file:
    i=i[:-1]
    lists=i.split(',')
    if len(lists)==2:
        if int(lists[1])<average-standard_deviation:
            if advisor==0:
                advisor=1
                print('List of students who need to see an advisor:')
            print(lists[0])