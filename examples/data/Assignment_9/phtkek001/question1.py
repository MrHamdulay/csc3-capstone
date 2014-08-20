file= input('Enter the marks filename:\n')
f=open(file, 'r')
list1=f.readlines()
f.close()

#strip off /n:
for i in range (len(list1)):
    list1[i] = list1[i][:-1]

import math
sums = 0
mark_list=[]
name_list=[]
#calculating the mean
for i in range(len(list1)):
    list2=list1[i].split(',')
    mark_list.append(list2[1])
    name_list.append(list2[0])
    sums += int(list2[1])


mean = sums/len(list1)
print('The average is:',"%0.2f" % mean, sep=' ')

#calculating the standard deviation
addm = 0
for mark in mark_list:
    meani = (int(mark) - mean) **2
    addm += meani
sd = round(math.sqrt(addm/len(mark_list)),2)
print('The std deviation is:', "%0.2f" % sd, sep=' ')

#checking for students who need to see a student advisor
sd_mean = mean - sd
student_names = []    
for mark in range(len(mark_list)):
    if int(mark_list[mark]) < sd_mean:
        student_names.append(name_list[mark])
if len(student_names)!=0:
    print('List of students who need to see an advisor:')
    for name in student_names:
        print(name)
    

        
#making each line a list and just some list manipulation 
"""for line in f:
    list1 = line.split(',')
    if int(list1[1]) <=25:
        print(list1[0], ',','Get help now!')
    elif int(list1[1]) >=25:
        print(list1[0], ',','You are passing')"""



  
