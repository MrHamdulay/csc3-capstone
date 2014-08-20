#program to calculate std andmean of file of marks and check the failures
#victor gueorguiev
#10 may 2014

import math

def calc_mean(marks):
    total = 0
    for i in marks:
        total += i
    return total/len(marks)

def calc_std(marks):
    totalnum = 0
    mean = calc_mean(marks)
    for i in marks:
        totalnum += (i-mean)**2
    return math.sqrt(totalnum/len(marks))

def main():
    filename = input("Enter the marks filename:\n")
    f = open(filename,"r")
    lines = f.readlines()
    f.close()
    
    marks = []
    names = []
    for line in lines:
        names.append(line[:line.find(',')])
        marks.append(eval(line[line.find(',')+1:]))
    mean = calc_mean(marks)
    std = calc_std(marks)
    print('The average is:','{0:.2f}'.format(mean))
    print('The std deviation is:','{0:.2f}'.format(std))
    advisor_help = []
    for i in range(len(marks)):
        if marks[i] < mean - std:
            advisor_help.append(names[i])
    if advisor_help:
        print('List of students who need to see an advisor:')
        for i in advisor_help:
            print(i)
            
main()   
        
    
    