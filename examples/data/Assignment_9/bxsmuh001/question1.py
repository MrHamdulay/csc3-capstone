#Assignment 9, Question 1
#Author: Muhammad Sabir Buxsoo (BXSMUH001)
#Class: CSC1015F 2014
#Date Modified: 16/05/2014; 17/05/2014 Modified needAdvisor() function since the output is not in  the same order as the automatic marker when a dictionary is used. When dictionary was used the list was not printing out as the AM wanted. So the function needAdvisor() had to be altered to use a list instead of a dcitionary.

#This program is designed to print the mean, standard deviation or marks and the students who need to see an advisor.
from math import *

#Function which adds a student and his/her marks as a key/value pair in the dictionary.
def addToDictionary(dictionaryName, key,value):
    dictionaryName[key] = value
    

#This function creates a dictionary of a student and his/her mark. The delimiter will find where the name and mark are separated.
def createDictionary(delimiter, myList, dictionaryName):
    for i in myList: #Looping through list.
        for j in range(len(i)):
            if i[j] == delimiter: #Find the comma
                a = i[0:j] #Split the name
                b = i[j+1::] #Split the mark
                addToDictionary(dictionaryName, a, b) #Add name and mark to dictionary.      

#This functions calculates the mean mark.
def meanMark(dictionaryName):
    totalMarks = 0
    for key,value in dictionaryName.items():
        totalMarks += float(value) #Grabs only the numbers from the dictionary and adds them to get Total.
    mean = totalMarks/len(dictionaryName) #Calculates mean using total and number of elements in dicitonary.
    return mean

#This function calculates the standard deviation.
def stdDev(dictionaryName, mean, n):
    sumSqr = 0
    for key,value in dictionaryName.items():
        sumSqr += ((eval(value) - mean)**2) #Grabs number, subtract meand and square. Keep adding to get total sum. 
    stdDeviation = sqrt(sumSqr/n) #Calculates the standard deviation.
    
    return stdDeviation

#This function goes through the dicitonary to find who needs an advisor.
def needAdvisor(listOfMarks, mean, stdDeviation):
    needAdvisor = []
    for i in listOfMarks: #Looping through list.
            for j in range(len(i)):
                if i[j] == ',': #Find the comma
                    a = i[0:j] #Split the name
                    b = i[j+1::] #Split the mark
                    if eval(b) < (mean - stdDeviation):
                        needAdvisor.append(a)
    return needAdvisor
    
    

#Checking if program is being run as standalone.
if __name__ == '__main__':
    fileName = input("Enter the marks filename:\n")
    
    #Opening file and assignning list of marks to a list.
    marksList = open(fileName, "r", encoding="utf-8") 
    listOfMarks = marksList.readlines()
    
    studentMarks = {} #Creating dictionary with list of marks and students.
    createDictionary(",", listOfMarks, studentMarks)    
    n = len(studentMarks) #Number of students/marks.
    
    mean = meanMark(studentMarks)
    stdDeviation = stdDev(studentMarks, mean, n)
    
    #Printing the outputs.
    print("The average is:", '{:.2f}'.format(mean))
    print("The std deviation is:", '{:.2f}'.format(stdDeviation))
    
    if(not needAdvisor(listOfMarks, mean, stdDeviation) == []):   
        print("List of students who need to see an advisor:")
        print('\n'.join(needAdvisor(listOfMarks, mean, stdDeviation)))

    marksList.close()
        