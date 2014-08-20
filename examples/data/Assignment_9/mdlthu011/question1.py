#-----------------------------------------------------------------------------
# A program to analyse student marks read in from a file and determine
# which students need to see a student advisor.
# Name: Thubelihle Mdlalose
# Student Number: MDLTHU011
#-----------------------------------------------------------------------------

import math         # Make the math module available.

def main():
    # Prompt the user for input and open the file entered
    # by the user.
    file_name = input("Enter the marks filename:\n")
    f = open(file_name, "r")

    # Converts the marks to float.
    li = []
    for line in f:
        line = line.rstrip()
        line = line.split(",")
        li.append(line)
    marks = []
    names = []
    for i in li:
        m = float(i[1])
        n = (i[0])
        marks.append(m)
        names.append(n)

    # Display outputo on the console.
    print("The average is:", format(mean(marks), ".2f"))
    print("The std deviation is:", format(standard_deviation(marks), ".2f"))
    if standard_deviation(marks) != 0:
        print("List of students who need to see an advisor:")
    for i in marks:
        if i < mean(marks) - standard_deviation(marks):
            print(names[marks.index(i)])

    # Close file.
    f.close()
    
def mean(values):
    """Calculate and returns the mean."""
    sum = 0
    for i in values:
        sum += i
        
    return sum / len(values)

def standard_deviation(x):
    """Calculates and return the standard deviation."""
    m = mean(x)
    total = 0
    for i in x:
        total += (i - m) ** 2

    return math.sqrt(total / len(x))

# Call the main function.
main()
    
    
