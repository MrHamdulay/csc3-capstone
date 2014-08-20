# Program to determine students in need of help
# Khwezi Majola
# MJLKHW001
# 10 May 2014

def stu():
    import math 
    total = 0 #Variables for later use
    count = 0
    mean = 0 
    stadev = 0
    filename = input('Enter the marks filename:\n') #Gets the file name
    ffile = open(filename, 'r') #Opens the file to be read
    lines = ffile.readlines() #Reads the lines into a list of strings
    ffile.close #Closes the file
    
    count = len(lines) #Find out how many students in the class
    for a in lines:
        posc = a.find(',') #Find the position of the seperating comma
        total += int(a[posc+1:]) #Add to the total
    mean = total/count #Determine the mean
    
    for a in lines:
        posc = a.find(',') #Find the position of the seperating comma
        val = int(a[posc+1:]) #Extract the mark
        stadev += (val - mean)**2 #Add to the standard deviation variable
    
    stadev = math.sqrt(stadev/count) #Calculate the standard deviation
    
    temp = '{0:.2f}'.format(mean) #Format the mean & print
    print('The average is:', temp)
    temp = '{0:.2f}'.format(stadev) #Format the standard deviation & print
    print('The std deviation is:', temp)
    
    itemp = 0
    
    for a in lines:
        posc = a.find(',') #Find the position of the seperating comma
        if int(a[posc+1:]) < (mean - stadev):
            itemp = 1 #Change the value to one only if there is at least one student required to see the advisor
            break
        
    if itemp > 0:  
        print('List of students who need to see an advisor:') #Print the title depending on what happened above
        for a in lines:
            posc = a.find(',') #Find the position of the seperating comma
            if int(a[posc+1:]) < (mean - stadev):
                print(a[:posc]) #Print the students
    
stu()