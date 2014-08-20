# 13 May 2014
# Shaun Muzenda
# Program to analyse student marks read in from a file and to determine which students need to see a student advisor

import math

def main():
    f_name = input("Enter the marks filename:\n") 
    infile = open (f_name, "r") #opens and reads file with student numbers and marks  
    student_marks = [] #list with students marks
    student_names = [] #list with students names    
    
    
    for line in infile:
        student_number, marks = line.split(",")     #splits student names and marks from read file
        student_marks.append(marks) #adds the students marks in the marks list  
        student_names.append(student_number)    #adds the students names inti the names list

    no_of_marks = int(len(student_marks))   # finds the integer value of the length of the marks list

    
    class_total = 0 
    for mark in student_marks:
        class_total = class_total + float(mark) #calculates the total marks of the students

    class_average = class_total / no_of_marks   #finds the average mark of the students
    
    
    
    stdDev_add = 0
    for mark2 in student_marks:
        stdDev_add = stdDev_add + (math.pow(float(mark2)-class_average,2))  #calculates the total for standard deviation. i.e. the numerator only
        
    class_std_dev = math.sqrt(stdDev_add / no_of_marks) #calculates the standard deviation of the marks
    
    mark_advisor = format((class_average - class_std_dev), '.2f')   #claculates the highest possible mark required to see the student advisor
    
    cd = [] #list of student names to see student advisor

    
    for mark3 in student_marks: #calculating which marks are below the mark to see the student advisor
        if float(mark3) < float(mark_advisor): 
            acd = student_marks.index(mark3)    #index the marks
            cd.append(acd)  #adds the students names who need to see the student advisor in a list
    
    print("The average is:", format(class_average, '.2f'))
    print("The std deviation is:", format(class_std_dev, '.2f'))
    
    if cd != []:    
        print("List of students who need to see an advisor:")   #only prints if names in list
    for i in cd:
        print(student_names[i])    #prints the names of students who need to see the student advisor
    
    infile.close()
    
main()