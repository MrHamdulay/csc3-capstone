"""A9Q1 - StudentAdvisor
10/05/2014
CRNKEE002"""

import math

def main():
    """main"""
    marks = []
    filename = input('Enter the marks filename:\n')
    create_list(filename, marks)
    ave = average(marks)
    stddev = std_dev(marks, eval(ave))
    students = advise(marks, eval(ave) - eval(stddev))
    print('The average is:', ave)
    print('The std deviation is:', stddev)    
    if len(students) > 0:
        print('List of students who need to see an advisor:')
        for i in range(len(students)):
            print(students[i])
          
    
def create_list(file, array):
    """Create the 2D list from the file"""
    f = open(file, 'r')
    for line in f:
        comma= line.index(',')
        end = len(line)-1
        if '\n' in  line:
            array.append([line[:comma:], eval(line[comma+1:end:])])
        else:
            array.append([line[:comma:], eval(line[comma+1::])])  
    f.close
    return array
    
def average(mark_list):
    """Calculate the average mark"""
    total = 0
    for i in range(len(mark_list)):
        total += mark_list[i][1]        
    return "{0:.2f}".format(total/len(mark_list))

def std_dev(mark_list, average_mark):
    """calculate the standard deviation"""
    result = 0
    for i in range(len(mark_list)):
        result += (mark_list[i][1] - average_mark)**2
    result = result/len(mark_list)
    return "{0:.2f}".format(math.sqrt(result))
    
def advise(mark_list, minimum):
    students = []
    for i in range(len(mark_list)):
        if mark_list[i][1] < minimum:
            students.append(mark_list[i][0])
    return students
    
if __name__ == '__main__':
    main()