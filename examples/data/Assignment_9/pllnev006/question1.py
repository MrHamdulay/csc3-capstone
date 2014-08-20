# Reading in from a file and display trouble students 
# Nevarr Pillay - PLLNEV006
# 12 May 2014

students = [] # List of students
marks = [] # List of marks that correspond with the students


def readin(filename):
    """Reads in info from file and populates lists"""
    file = open(filename,"r") # File to read from with given file name
    for line in file:
        info = line.split(",")
        students.append(info[0]) # First part of line (name) added to the students list
        marks.append(eval(info[1])) # Second part of line(mark) added to the marks list
    file.close()    
    
def mean(listnum):
    """Calculates the mean of a list of numbers"""
    mean = 0
    for num in listnum: 
        mean += num
    mean = mean/len(listnum)   
    return mean

def standarddev(listnum):    
    """Calculates the standard deviation of the list of numbers"""
    defmeansqrd = 0
    tempmean = mean(listnum) # Mean of list is calculated
    for num in listnum:
        temp = num - tempmean # Difference between number in list and mean
        defmeansqrd += temp**2 # Difference squared
    standard = (defmeansqrd/len(listnum))**(1/2) # Square root of the sum of the differences squared
    return standard
    
def names(listnames,listmarks):
    """Returns the list of the names of students whose mark is less than one standard deviation of the mean"""
    riskstudents = []
    tempmean = mean(listmarks)
    standard = standarddev(listmarks)
    for i in range(len(listmarks)):
        if listmarks[i] < (tempmean-standard): # If the mark is less than one standard deviation of the mean of the list of numbers
            riskstudents.append(listnames[i])
    return riskstudents        
    
def main():
    filename = input("Enter the marks filename:\n") # Get file name
    readin(filename)
    meanf = "The average is: {0:.2f}"
    standf = "The std deviation is: {0:.2f}"
    print(meanf.format(mean(marks))) # Print out the mean formatted to 2 decimal points
    print(standf.format(standarddev(marks))) # Print out the standard deviation formatted to 2 decimal points
    risknames = names(students,marks)
    if len(risknames) > 0: 
        print("List of students who need to see an advisor:")
        for i in risknames:
            print(i)
    

if __name__ == "__main__":
    main()  

