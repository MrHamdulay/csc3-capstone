"""Program that analyses student's marks read in from a file and determines which students need to see a student advisor.
Mtunzi France
15 May 2014"""

def students():
    import math
    """Opens the text file and reads the data from it"""
    file_name = input("Enter the marks filename:\n")
    new_file = open(file_name, "r")
    marks = new_file.readlines()
    new_file.close()
    #NOTE TO SELF ____working with marks
    #Removes the new line character "/n"
    for i in range (len(marks)):
        marks[i] = marks[i][:-1]
        
    #Convert everything in the list to a string
    for i in range(len(marks)):
        marks[i]= str(marks[i])
        
    #Separates the mark and the name
    for i in range(len(marks)):
        marks[i] = marks[i].split(",")
    
    #converts the names to keys which correspond to marks in a dictionary
    names = []
    percentages = []
    j = 0
    k = 1
    for i in range(len(marks)):
        names.append(marks[i][j]) # Takes first item of every list in the 2d array
        percentages.append(marks[i][k]) #Takes second item of every list in the 2d array
        
    #convert all numbers in percentages to integers
    for i in range (len(percentages)):
        percentages[i] = int(percentages[i])
        
    mean = sum(percentages)/ (len(percentages)) #computes the mean
    #Finds the standard deviation
    sum_marks = 0
    for i in percentages:
        dif = (i - mean)**2
        sum_marks = sum_marks + dif #Sum of differences from the mean
    std_dev = math.sqrt(sum_marks / len(percentages))
    lowest = mean - std_dev
    print("The average is:","{0:.2f}".format(mean))
    print("The std deviation is:","{0:.2f}".format(std_dev))
    if std_dev == 0:
        pass
    else:
        print("List of students who need to see an advisor:")
    for i in percentages:
        if i < lowest:
            print(names[percentages.index(i)])
students()