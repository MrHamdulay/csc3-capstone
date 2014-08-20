'''program to create file and standard deviation function for student retention
Thabiso Beau
12 May 2014
Assignment 9: #question1.py'''

import math
x = input('Enter the marks filename: \n')
def stats(x):
    #finding the mean of the numbers
    file = open(x, 'r')#open the file for it to be read 
    #file = file.readline() #get one line from file
    count=0 #set a counting variable
    count_2 = 0
    for i in file:
        i = i.split(',') #split string in order to get marks
        count += eval(i[1])
        count_2 +=1
    mean = ("{0:.2f}".format(round((count/count_2),2)))#mean found
    file.close
    
    
    #finding the standard deviation
    #firstly, find sigma [Xn-1 - mean)^2
    file = open(x, 'r')
    sigma = 0
    for j in file:
        j = j.split(',')
        sum_1 = (eval(j[1]) - eval(mean))**2
        sigma += sum_1
    std_dev = ("{0:.2f}".format(round(math.sqrt(sigma/count_2), 2)))
    file.close
    
    #finding the students that are performing below the mean
    file=open(x, 'r')
    mark = eval(mean) - eval(std_dev)
    student_count = '' 
    print('The average is:',mean)
    print('The std deviation is:', std_dev)
    students_count=0
    for a in file:
            a=a.split(',')
            if eval(a[1]) < mark:
                students_count+=1   
    file.close
    if students_count > 0:
        print('List of students who need to see an advisor:')
    file =  open(x, 'r')
    names = file.readlines()
    for names in names:
        J = names.split(",")
        if eval(J[1]) < mark:
            print( J[0])
            
    file.close

stats(x)