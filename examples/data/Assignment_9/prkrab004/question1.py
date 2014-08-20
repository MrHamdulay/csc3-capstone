#Assignment 9
#Question 1
#Rabia Parker
#Due Date: 16/05/14

import math

marks_list = []
#get filename
filename = input('Enter the marks filename:\n')
#open the file
file = open(filename, 'r')
#open per line
lines = file.readlines ()

for i in lines:
    
    word, points = i.split(',')
    p = points
    marks_list.append(int(p))


count_p=0
for j in marks_list:
    count_p+=j
average=count_p/len(marks_list)
count=0
for j in range(len(marks_list)):
    count=count+((marks_list[j]-average)**2)
d = count/len(marks_list)
    
deviation = math.sqrt(d)
    

file.close ()

print('The average is: {0:.2f}'.format(average))

print('The std deviation is: {0:.2f}'.format(deviation))


for j in range(len(marks_list)):
    
    if float(int(marks_list[j]))<(average-deviation):
        print('List of students who need to see an advisor:')
        break


for j in range(len(marks_list)):
        
    if float(int(marks_list[j]))<(average-deviation):    
        r,k=lines[j].split(",")
        print(r)

