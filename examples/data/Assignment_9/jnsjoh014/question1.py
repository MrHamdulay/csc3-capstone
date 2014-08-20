__author__ = 'JNSJOH014'
"""Question 1, Assignment 9
11/05/2014"""
import math
def main():
    fileName = input("Enter the marks filename:\n")
    print("The average is: {:.2f}".format(average(fileName)))
    print("The std deviation is: {:.2f}".format(deviation(fileName)))

    list = print_names(fileName)
    if len(list)>0:
        print("List of students who need to see an advisor:")
    for i in list:
        print(i)

def readFile(fileName):
    f = open(fileName,"r")
    lines = []
    for c in f:
        lines.append(c.split(","))#list of lines
    f.close()
    return(lines)

def deviation(fileName):
    marks = readFile(fileName)
    inside = 0
    for i in marks:
        inside+=(eval(i[1])-average(fileName))**2
    result = math.sqrt((inside)/len(marks))
    return result

def average(fileName):
    marks = readFile(fileName)
    tot = 0
    for mark in marks:
        #print("a",mark)
        tot+=eval(mark[1])
    return tot/len(marks)

def print_names(fileName):
    marks = readFile(fileName)
    cutoff = average(fileName) - deviation(fileName)
    dprList = []
    for i in marks:
        if eval(i[1])<cutoff:
            dprList.append(i[0])
    return dprList

if __name__=="__main__":
    main()
