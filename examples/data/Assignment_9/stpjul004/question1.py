""" Program to advise students on their marks
 Author: Julius Stopforth (STPJUL004)
 Date: 2014-05-12 """

def sum_marks(list):
    """Recursive function that summs up all the marks in the list"""
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum_marks(list[1:])

def calc_dev(mean, list):
    """ Recusrive function that finds the sum of (x0-u)^2 + (x1-u)^2 + ..."""
    if len(list) == 1:
        return (list[0]-mean)**2
    else:
        return (list[0]-mean)**2 + calc_dev(mean,list[1:])
    
def calc_stnd_dev(list):
    """ Function that returns the standard deviation """
    return (calc_dev(sum_marks(list)/len(list), list)/len(list))**0.5
# Breakdown of above code:
# sum_marks/len(list) gives the average mark
# calc_dev returns the standard deviation squared
# calc_dev**0.5 returns the square root of the deviation

# Set format strings
avgString = "The average is: {:.2f}"
devString = "The std deviation is: {:.2f}"

# Ask the user to choose a filename
filename = input("Enter the marks filename:\n")

# Attempt to open the selected file so that itcan be read from
try:
    f = open(filename, "r")
    # Extract all the data from the file into and array
    lines = f.readlines()
    # Close the file
    f.close()
except IOError:
    print("No such file exists!\n")

# Create a new dictionary to store two parallel arrays
course = {"students":[], "marks": []}

# Parse the contents of the file into the dictionary
for entry in lines:
    # Find the position of the comma
    comm_pos = entry.find(',')
    # Add the name of the student to the students list
    course["students"].append(entry[:comm_pos])
    # Remove the student's name and the following comma
    entry = entry[comm_pos+1:]
    # Add the mark to the marks list, (eval used to remove '\n')
    course["marks"].append(eval(entry))

# Find the average mark of the course
averageMark = sum_marks(course["marks"])/len(course["marks"])

# Find the standard deviation of the marks
standardDeviation = calc_stnd_dev(course["marks"])

# Create an empty list to hold student names that need to see advisors
advisoryList = []

# Find all the students who need to see advisors and add them to the list
for i in range(len(course["marks"])):
    # Check if the student's mark is below one standard deviation from the mean
    if course["marks"][i] < (averageMark - standardDeviation):
        advisoryList.append(course["students"][i])

# Print the average mark of the course
print(avgString.format(averageMark))

# Print the standard deviation of the course
print(devString.format(standardDeviation))


if len(advisoryList) > 0:
    # Print out the list of students who need to see an advisor
    print("List of students who need to see an advisor:")

    for student in advisoryList:    
        print(student)
