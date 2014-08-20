#Asil Motala
#MTLASI002
#Assignment 9
#Question 1
#09 May 2014

from math import sqrt                                   #import square root function from math module

file_name=input("Enter the marks filename:\n")          #get file name from user
file=open(file_name,"r")                                #open file in read mode
mark_book=[]                                            #intialize empty list of names and marks
for student in file:                                    #loop through each line in file
    mark_book.append(student)                           #add each students details to list
file.close()                                            #close file

while "\n" in mark_book:                                #check for any empty lines in list
    mark_book.remove("\n")                              #remove empty lines from list
for student in range(len(mark_book)):                   #checks for new line character at end of line
    if mark_book[student][-1:]=="\n":                   #checks if last character on line is a new line character
        mark_book[student]=mark_book[student][:-1]      #removes new line characters from line

marks=[]                                                #initalizes empty list of marks
for individual in range(len(mark_book)):
    if mark_book[individual][-2:].isdigit():            #checks if last two characters of each line are numbers
        mark=eval(mark_book[individual][-2:])           #slices line into the mark only
        marks.append(mark)                              #adds mark to a list
    elif mark_book[individual][-1:].isdigit():          #checks if last character of each line is a number
        mark=eval(mark_book[individual][-1:])           #slices line to mark only
        marks.append(mark)                              #adds mark to a list

def mean(data):                                         #function to calculate the average of a list of data
    total=0                                             #intialize sum of data variable
    for value in data:                                  #loop through each value in the list
        total+=value                                    #add each value to the running total
    avg=total/len(data)                                 #find the average by dividing the number of pieces of data
    avg=round(avg,2)                                    #round off answer to two decimal places
    return avg                                          #return answer out of the function

print("The average is:","{0:0.2f}".format(mean(marks))) #prints average of data out, formatted to two decimal places, filled with zeroes if required

def std_deviation(data):                                #function to calculate the standard deviation of a list of data
    avg=mean(data)                                      #calculate the average of the list of data
    total=0                                             #intialize sum of data variable
    for value in data:                                  #loop through each value of data
        total+=(avg-value)**2                           #add the square of the difference between the average and the data value to the running total
    average=total/len(data)                             #find the average of the squares of the differences by dividing by the number of data in the list
    deviation=sqrt(average)                             #squareroot the average of the squares of the differences
    deviation=round(deviation,2)                        #round off the answer to two decimal places
    return deviation                                    #return the answer out off the function

print("The std deviation is:","{0:0.2f}".format(std_deviation(marks)))  #prints the standard deviation of the data, formatted to two decimal places, filled with zeroes if required

minimum_mark=mean(marks)-std_deviation(marks)           #calculates the minimum mark to avoid student advisor
if std_deviation(marks)>0:                              #if there are any students who did deviate from the mean
    print("List of students who need to see an advisor:")#print out the heading
for mark in range(len(marks)):                          #loop through each student's mark
    if marks[mark]<minimum_mark:                        #checks if a students mark is less than the required minimum
        if len(str(marks[mark]))>1:                     #checks if students mark is two digits
            print(mark_book[mark][:-3])                 #prints out students name
        elif len(str(marks[mark]))<=1:                  #checks if mark is single digit
            print(mark_book[mark][:-2])                 #prints out students name