"""Assignment 9, Question 1
Jadon Thomson
13-05-2014"""

import math
  
def get_list(filename):
    """Opens file and creates a list of the marks read from the file"""
    f = open(filename, "r")
    lst = []
    for line in f:
        lst.append([])
        for i in line:
            if i in '0123456789':
                lst[-1].append(i)
            else:
                continue
        lst[-1] = ''.join(lst[-1])
    return lst

def calc_average(filename):
    """calculates the average mark from the list"""
    f = open(filename, "r")
    lst = get_list(filename)
    _sum = 0
    for i in lst:
        a = eval(i)
        _sum += a
    average = _sum / len(lst)
    f.close()
    return average
    
def calc_stand_dev(filename,average):
    """calculates standard deviation"""
    f = open(filename, "r")
    lst = get_list(filename)
    f.close()
    sum_sqr = 0
    for i in lst:
        a = eval(i)
        sum_sqr += (a - average)**2
    b = sum_sqr/(len(lst))
    std_dev = math.sqrt(b)
    return std_dev

def choose(filename,average,std_dev,lst):
    """determines the students whose mark is below one std deviation of the average"""
    string = "List of students who need to see an advisor:\n"
    f = open(filename, 'r')
    file = f.readlines()
    for i in range(len(lst)):
        name = ''
        if eval(lst[i]) < (average - std_dev):
            for j in file[i]:
                if j != ',':
                    name += j
                else:
                    break
            string += name + '\n'
    if len(string) > len("List of students who need to see an advisor:\n"):
        print(string)        
    f.close()
                

def main():
    """controls the whole process"""
    m = input("Enter the marks filename:\n")
    print("The average is:", ("{0:.2f}".format(calc_average(m))))
    print("The std deviation is:", ("{0:.2f}".format(calc_stand_dev(m,(calc_average(m))))))
    choose(m,calc_average(m),calc_stand_dev(m,(calc_average(m))),get_list(m))
    
main()
    
    