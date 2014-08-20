""" A program that analyses student marks read in from a file and determines which students need to see a student advisor.
Author: Afika Nyati
Date: 10th May 2014"""

from math import sqrt   # Imports the square root function from the math library.
formatting = "{0:.2f}"  # Creates the nice formatting to print the results.

def main():

    student_marks = file_to_list()    # Assigns the list of students and their marks (returned by the file_to_list function) to a variable.
    avg = average(student_marks)    # Assigns the average of all the students (returned by the average function) to a variable.
    stdd = stddeviation(avg,student_marks)  # Asigns the standard deviation of all the students (returned by the stddeviation function) to a variable.
    
    print("The average is:", formatting.format(avg))    # Prints the average using formatting.
    print("The std deviation is:", formatting.format(stdd))     # Prints the standard deviation using formatting.
    
    need_advice = needadvice(student_marks, avg, stdd)  # Assigns a list of students (returned by the needadvice function) to a variable.
    
    if need_advice != []:
        
        print("List of students who need to see an advisor:")   # A heading for the students who need to see an advisor.
    
        for person in need_advice: # For each person in the 'needs advice' list:
        
            print(person)   # Print the name


def file_to_list():     # A function that creates returns a list of students and their marks from data extracted from a file.
    
    filename = input("Enter the marks filename:\n")     # Asks user for the filename of the file with the marks.
        
    file = open(filename, "r")      # Opens the file with the marks and assigns the file to the 'file' variable.
        
    lst = file.readlines()      # Creates a list of strings containing each line in the file.
        
    file.close()    # Closes the file.
        
    for i in range(len(lst)):    # A definite loop that splits the strings in the list into a list of the student and his/her mark.
        lst[i] = lst[i].split(",")
        
    for i in range(len(lst)):   # A definite loop that evaluates the mark of each student to a integer for integer manipulation
        lst[i][1] = eval(lst[i][1])
    
    return lst  # Return the list

    

def average(marks):     # A function that determines the average of a set of marks given as an arguement.
    
    accumulator = 0     # Initializes the accumulator to zero. This is the variable that will add all the students' marks together
    people_count = len(marks)   # Sets the variable to number of students. This is what we will devide the accumulator by, to get the average.
    
    for i in range(len(marks)): # A definite loop that adds the marks of each student together.
        
        accumulator += marks[i][1]      # Adds the mark to the accumulator. Notice that the first index is the only number that needs changing. The first index correlates with each student.
        
        average = accumulator/ people_count # Calculates the average
    
    return average  # Returns the average.


def stddeviation(average, marks):   # A function that determines the standard deviation of a set of marks given as an argument. To calculate standard deviation, you need the average. Therefore I inputted the previously calculated average to keep the code efficient.
    
    summing = 0     # Initializes the summing variable to zero. This is the variable that will add all the square differences of each mark together.
    people_count = len(marks)   # Sets the variable to number of students. This is what we will devide summing by, to get the standard deviation.
    
    for i in range(len(marks)):     # A definite loop that adds all the square differences of each mark together.
        
        summing += ((marks[i][1] - average)**2)     # Adds the mark to summing. Notice that the first index is the only number that needs changing. The first index correlates with each student.
    
    std_d = sqrt(summing/people_count)      # Calculates the standard deviation.
    
    return std_d    # Returns the standard deviation.
    

def needadvice(marks, average, stddeviation):       # A function that determines whether a student needs to see a student advisor. The determinant is whether the mark is one standard deviation below the mean. Arguements are the list of marks, the avarage, and the standard deviation.
    
    determinant = average - stddeviation    # Calculates the determinant.
    need_help = []      # Initializes a list that will store the names of the people who need help.
    
    
    for i in range(len(marks)):     # A definite loop that checks if any students need help.    
        
        if marks[i][1] < determinant:       # If the students mark is below one standard deviation of the mean:
            
            need_help.append(marks[i][0])   # Add his/her name to the list of people who need help
            
    return need_help    # Return the list
        
main()

    
