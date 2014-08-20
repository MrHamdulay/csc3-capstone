'''program to calculate standard deviation from file of marks
nasreen hoosain
14/05/14'''

import math

#function to calculate mean/average
def mean(l):
    count = 0
    for i in range(len(l)):
        count += l[i]
    average = count/len(l)
    return average

#function to calculate standard deviation
def standard_dev (l):
    average = mean(l)
    #calculate variance
    var_list = []
    for i in range(len(l)):
        var = (l[i] - average)**2
        var_list.append(var)
    variance = mean(var_list)
    SD = math.sqrt(variance)
    return SD

if __name__ == '__main__':
    #get the names and marks
    filename = input('Enter the marks filename:\n')
    marksfile = open(filename, 'r')
    names_marks = marksfile.readlines() 
    marksfile.close()
    
    #separate name and mark
    st_n = len(names_marks) #number of students/marks
    for i in range(st_n-1):
        names_marks[i] = names_marks[i][:-1] #delete newline character
    marks = []
    for i in range(st_n): #split marks and names into 2d array
        x = names_marks[i].split(',')
        marks.append(x)
        
    #eval marks and place in separate list to calculate SD
    marklist = []
    for i in range(st_n):
        marklist.append(eval(marks[i][1]))
    
    #get students below 1 sd
    advisor_list = []
    average = round(mean(marklist), 2)
    sd = round(standard_dev(marklist), 2)    
    for i in range(st_n):
        if marklist[i] < (average - sd):
            advisor_list.append(marks[i][0])
            
    #format and print stuff
    num = '{0:0<5}'
    num2 = '{0:0<4}'
    if average < 10:
        print('The average is:', num2.format(average))
    else:
        print('The average is:', num.format(average))
    if sd < 10:
        print('The std deviation is:', num2.format(sd))
    else:
        print('The std deviation is:', num.format(sd))
    if advisor_list != []:
        print('List of students who need to see an advisor:')
        for st in advisor_list:
            print(st)