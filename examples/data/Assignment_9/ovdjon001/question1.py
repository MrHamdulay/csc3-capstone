"""Assignment 9, question1, question1.py
10 May 2014 
by Jonathan Ovadia"""
import math
def main():
    file_name = input("Enter the marks filename:\n")
    print("The average is: {:.2f}".format(calc_average(file_name)))
    print("The std deviation is: {:.2f}".format(calc_std_deviation(file_name)))
    dpr_list = drp_lisyt(file_name)
    if len(dpr_list) > 0:
        print("List of students who need to see an advisor:")
        for i in dpr_list:
            print(i)

def read_file(file_name):
    f = open(file_name,"r")
    marks = []
    for i in f:
        marks.append(i.split(","))
    return marks
def calc_average(file_name):
    marks = read_file(file_name)
    total = 0
    for i in marks:
        total+=eval(i[1])
    return total/len(marks)

def calc_std_deviation(file_name):
    marks = read_file(file_name)
    average = calc_average(file_name)
    sqr_sum = 0
    for i in marks:
        sqr_sum += (eval(i[1])-average)**2
    return math.sqrt(sqr_sum/len(marks))

def drp_lisyt(file_name):
    marks = read_file(file_name)
    std_deviation = calc_std_deviation(file_name)
    x_bar = calc_average(file_name)
    students = []
    for i in marks:
        if eval(i[1]) < round(x_bar-std_deviation,2):
            students.append(i[0])
    return students
if __name__ == "__main__": main()