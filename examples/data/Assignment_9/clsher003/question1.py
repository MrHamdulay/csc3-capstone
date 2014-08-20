"""program to analyse student marks
herman claassens
11 may 2014"""

import math

text_file=input('Enter the marks filename:\n') # get markd file from user

inputfile=open(text_file,'r')   # open marksfile 
data=inputfile.readlines()      # save marksfile as a list
inputfile.close()               # close marksfile


for i in range (len (data)):     # remove \n from list
    data[i] = data[i][:-1]  
    

sum1=0                   
count=0
marks_list=[]

for i in data:
    i=i.split(',')                 # seperate names from marks
    marks_list.append(eval(i[1]))   # add marks to a seperate list
    sum1+=eval(i[1])                # add marks up
    count+=1                        # counter to keep track of number of students
    
average=(sum1/count)                # calculate average

sum2=0
for i in range(count):                # go through marks to calculate the standart deviation
    sum2+=(marks_list[i]-average)**2
    
std_deviation=math.sqrt(sum2/count)  
average_std=average-std_deviation

students=[]
for i in data:                     # create a list of students who need to see a advisor
    i=i.split(',')
    if eval(i[1])<average_std:      # if mark is lower than average - one std_deviation, add to list
        students.append(i[0])
    

print('The average is: {0:<.2f}'.format(average))               # print average, std_deviation and the list of students who need to see an advisor
print('The std deviation is: {0:<.2f}'.format(std_deviation))
print('List of students who need to see an advisor:')
for i in students:
    print(i)
    

    
