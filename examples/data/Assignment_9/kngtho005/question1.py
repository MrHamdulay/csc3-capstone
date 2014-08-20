# question1.py
# a program to analyse student marks read in from a file and determine
# which students need to a see a student advisor.
# Thomas Konigkramer
# 11 May 2014

import math

marks = input("Enter the marks filename:\n")

def deviation():
    # opening file
    f = open(marks, "r")
    # reading file into a list of strings
    lines = f.readlines()
    # closing file
    f.close
    
    # creating a 2-d list
    pairs = [[""]] * len(lines)
    for j in range(len(lines)):
        pairs[j] = lines[j].split(",")
    
    # calculating the average
    total = 0
    counter = 0
    for k in range(0,len(pairs)):
        total += eval(pairs[k][1])
        counter += 1
    average = total/counter
    
    # calculating the standard deviation
    std_deviation = 0
    for l in range(len(pairs)):
        std_deviation += (eval(pairs[l][1]) - average)**2
    std_deviation = math.sqrt(std_deviation/counter)
    
    # checking which students should see the advisor
    advisor = []
    for m in range(len(pairs)):
        if average - std_deviation > eval(pairs[m][1]):
            advisor.append(pairs[m][0])
        
    print("The average is:", "%.2f" % average) 
    print("The std deviation is:", "%.2f" %std_deviation)
    if advisor != []:
        print("List of students who need to see an advisor:")
        # printing list of students
        for l in advisor:
            print(l)     

deviation()