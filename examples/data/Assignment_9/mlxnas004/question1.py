"""program to find students that should see the student advisor using files
nasha somoina meoli
11th may 2014"""
import math
def students_that_need_help():
    """calculates the standard deviation"""
    #calculate toal number of marks and students
    f = open ((input("Enter the marks filename:\n")),"r")
    number_of_students = 0
    total_marks = 0
    grid_of_marks = []
    grid_of_names = []
    #to find the position of the marks
    for line in f:
        position = line.find(",")
        if position == -1:continue
        
        end = line.find("\n")
        
        if end == -1:
            mark = line[position+1:]
        else:
            mark = line[position+1:end]
      #to calculate total marks and number of stuedents 
        if mark.isdigit():
            number_of_students+=1
            total_marks+=int(mark)
        
            grid_of_marks.append(mark)
            grid_of_names.append(line[:position])

    f.close()
    #calulate average and standard devaiation
    average = total_marks/number_of_students
    
    element = 0
    for grade in grid_of_marks:
        x = (int(grade)-average)**2
        
        element+=x
    #calculate standard deviation
    standard_deviation = math.sqrt(element/number_of_students)
    sd = '{0:.2f}'.format(standard_deviation)
    av=  '{0:.2f}'.format(average)  
    print("The average is:",av)
    print("The std deviation is:",sd)
    #check students outside the standard deviation
    target_mark = average-standard_deviation
    
    risk =""
    for mark in grid_of_marks:
        if int(mark) < target_mark:

            student_position = grid_of_marks.index(mark)
            risk+=grid_of_names[student_position]+"\n"
    if risk != "":
        print("List of students who need to see an advisor:\n"+risk)
        
students_that_need_help()
            