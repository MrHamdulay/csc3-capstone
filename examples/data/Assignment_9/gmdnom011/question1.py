# Program to detect marks in a file less than one standard deviation below the mean
# Nomsa Gamedze
# 11 May 2014

import math

def find_mean(marks):
    total = 0
    count = 0
    for i in range(len(marks)):
        total += marks[i]
        count += 1
    return total/count
        
def find_SD(marks, mean):
    SD_squared = 0
    count = 0
    for i in range(len(marks)):
        term = (marks[i] - mean)**2
        SD_squared += term
        count += 1
    return math.sqrt(SD_squared/count)

def get_marks(file):
    marks = []
    for line in file:
        line = list(line)
        ind = line.index(",")
        mark = line[ind+1]
        if len(line) >= ind+3:
            mark += line[ind+2]
        if len(line) == ind+4:
            mark +=  line[ind+3]
        mark = int(mark)
        marks.append(mark)
    return marks

def get_names(file, marks, SD, mean, lines):
    names = []
    line_number = 0
    cut_off = abs(SD - mean)
    for i in range(len(marks)):
        if marks[i] < cut_off:
            ind = lines[i].index(",")
            name = lines[i][:ind]
            names.append(name)
    return names

def format_num(num):
    num_r = round(num, 2)
    num_s = str(num_r)
    num_l = list(num_s)
    ind = num_l.index(".")
    new = num_s[ind+1:]
    x = len(new)
    if x < 2:
        num_s += "0"
    return num_s

def main():
    file_name = input("Enter the marks filename:"'\n')
    file = open(file_name, "r")
    marks = get_marks(file)
    lines = open(file_name, "r").readlines()
    mean = find_mean(marks)
    SD = find_SD(marks, mean)
    names = get_names(file, marks, SD, mean, lines)
    print("The average is:", format_num(mean))
    print("The std deviation is:", format_num(SD))
    if names:
        print("List of students who need to see an advisor:"'\n', '\n'.join(names), sep="")

main()