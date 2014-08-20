#Question1, Assignment 9, Test for Student Advisor
# Michael Sanne
# 2014/05/10
import sys
import math

# Function to determine the standard deviation with input list of marks and the mean of those marks
def standard (average, marks):
    sums = 0
    for i in range (len(marks)):
        sums += ((marks[i] - average)**2)
    divisor = sums/(len(marks))
    deviation = math.sqrt (divisor)
    return deviation

# Main execution in the program allows for input "Name of the file"
def main(fileName):
    # Exception handling in case the File can not be found
    try:
        marks = []
        students = []
        file = open (fileName, "r")
        reader = file.readline()
        #Splits each line into student list and marks list
        while (reader!= ""):
            line = reader.split(",")
            students.append (line[0])
            marks.append (eval(line[1]))
            reader = file.readline()
        file.close()
            
        suma = 0
        for i in range (len(marks)):
            suma += marks[i]
            average = suma/(len(marks))
            deviation = standard(average, marks)
        #Output of average, standard deviation and students that are below standard deviation from mean
        print ("The average is: " + str(round(average, 2)), end="")
        if (round(average,2) % 0.5 == 0):
            print ("0", end = "")
        print ()    
        print ("The std deviation is: " + str(round(deviation,2)), end ="")
        if (round(deviation,2) % 0.5 == 0):
            print ("0", end = "")
        print()     
    
        printer = False
        for i in range (len(marks)):
            if (marks[i] < (average-deviation)):
                if (printer == False):
                    print ("List of students who need to see an advisor:")
                    printer = True
                print (students[i])
    #Exception catcher
    except IOError as errno:
        print ("Could not read file")
        print ("Error number:",errno)
        
fileName = input("Enter the marks filename:\n")
main (fileName)