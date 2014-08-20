""" a program that takes in a list of marks (separated by spaces) and outputs 
a histogram representation of the marks according to the mark categories at UCT.
Author: Dominic Manthoko
21 April 2014
"""

# prompt the user to enter a list of marks
marks = input("Enter a space-separated list of marks: \n")

# convert the marks string into a list
marks = marks.split()

if len(marks) > 0:
    # create dictinary to store the marks in a specific mark category
    grades = {'1' : '', '2+': '', '2-' : '', '3' : '', 'F' : ''}
    
    # iterate through the list and add a X to the corresponding mark category
    for mark in marks:
        # if the mark is greater than 75%, add a X to the value of '1' in the 
        # dictionary
        if int(mark) >=75:
            grades['1'] = grades['1'] + 'X'
         
        # if the mark lies between 70%(inclusive) and 75% add a X to the value of 
        # '2+' in the dictionary
        elif 70<= int(mark) < 75:
            grades['2+'] = grades['2+'] + 'X'
        
        # add X to value of '2-' if mark is between 60% and 70%
        elif 60 <= int(mark) < 70:
            grades['2-'] = grades['2-'] + 'X'
        
        # add X to the value of '3' if mark is between 50% and 60%
        elif 50 <= int(mark) < 60:
            grades['3'] = grades['3'] + 'X'
        
        # add X to the value of 'F' if mark is less than 50%
        else:
            grades['F'] = grades['F'] + 'X'
            
# print the dictionary grades in the required format
print("{0:<2}|{1}".format('1', grades['1']))
print("{0:<2}|{1}".format('2+', grades['2+']))
print("{0:<2}|{1}".format('2-', grades['2-']))
print("{0:<2}|{1}".format('3', grades['3']))
print("{0:<2}|{1}".format('F', grades['F']))