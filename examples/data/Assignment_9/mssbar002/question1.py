"""program to analyse student marks read in from a file and determine which 
students need to see a student advisor
Barnett Msiska
13 May 2014"""

import math

def main():
    filename = input("Enter the marks filename:\n")
    f = open(filename, "r")
    lines = f.readlines()
    #remove new line character
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    #collect marks
    marks = []
    for i in range(len(lines)):
        line = lines[i].split(',')
        marks.append(line[1])
    #calculate average
    total = 0
    for i in marks:
        total += int(i) 
    average = round(total/len(marks), 2)
    print("The average is: {0:.2f}".format(average))
    #calculate the standard deviation
    sd_total = 0
    for i in marks:
        sd_total += (int(i) - average)**2
        sd = math.sqrt(sd_total/len(marks))
    print("The std deviation is: {0:.2f}".format(sd))
    #print list of students to see an advisor
    for i in range(len(lines)):
        line = lines[i].split(',')
        if average - int(marks[i]) > sd:
            print("List of students who need to see an advisor:")
            break
    for i in range(len(lines)):
        line = lines[i].split(',')
        if average - int(marks[i]) > sd:
            print(line[0])    
main()