'''This program analyses students marks from a file and then prints out the
students that need to see an advisor: those whose marks are below one standard
deviation of the mean
By Kouame Hermann KOUASSI: KSSKOU001
On 11 May 2014'''

import math

def get_file(file):
    students = []
    marks = []
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    if lines != '':
        for line in lines:
            if line[-1] == '\n':
                line = line[:-1]
            position = line.index(',')
            students.append(line[:position])
            marks.append(eval(line[position+1:]))
    return students , marks

def mean(marks):
    '''return the mean of given values'''
    sum_m = 0
    for mark in marks:
        sum_m += mark 
    average = sum_m/len(marks)
    return average

def standard_D (marks, average) :
    total = 0
    for mark in marks:
        total += (mark - average) ** 2
    stand_D = math.sqrt((total) / len(marks))
    
    return stand_D
    
def main():
    condition = True
    file = input('Enter the marks filename:\n')
    students = get_file(file)[0]
    marks = get_file(file)[1]
    average = mean(marks) 
    print('The average is:', "{0:.2f}".format(average))
    stand_D = standard_D(marks, average)
    print('The std deviation is:', "{0:.2f}".format(stand_D))
    for std_no in range(len(students)):
        if  marks[std_no] < (average - stand_D) :
            if condition:
                print("List of students who need to see an advisor:")
                condition = False
            print(students[std_no])


if __name__=="__main__":
    main()
    