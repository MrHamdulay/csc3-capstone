"""Question 1 of Assignment 9: Determine the mean, standard deviation and a list of students who should see the advisor based on a list of marks
SWNREI001
11/05/2014"""

import math

def stdDev(marks):
    """Determine standard deviation of a given list of marks"""
    mean = sum(marks)/len(marks)
    sd = 0 
    for i in marks:
        # sum of square of diff between mark and mean
        sd += (i - mean) ** 2
    # divide by total number of marks
    sd /= len(marks)
    # square rooted is standard deviation
    return math.sqrt(sd)

def getNamesAndMarks(filename):
    """Returns pair of lists of student names and corresponding marks from a file"""
    names, marks = [], []
    f = open(filename, "r")
    lines = f.readlines()
    for i in lines:
        name, mark = i.replace("\n", "").split(",") # remove trailing newline and split at comma
        names.append(name)
        marks.append(eval(mark))
    return names, marks

def twoDecFormat(num):
    """Returns num as a string formatted to two decimal places"""
    num = str(num)
    if not '.' in num:
        num += '.' # ensures that split will produce two values if there is no d.p.
    sig, dec = num.split(".") # split at decimal point
    if len(dec) < 2:
        dec += "0" * (2 - len(dec)) # pad with zeroes
    else:
        dec = dec[:2] # truncate anything after 2 dp's
    return sig + "." + dec

def main():
    """Main function of module"""
    names, marks = getNamesAndMarks(input("Enter the marks filename:\n"))
    mean = sum(marks)/len(marks)
    sd = stdDev(marks)
    print("The average is:", twoDecFormat(round(mean, 2)))
    print("The std deviation is:", twoDecFormat(round(sd, 2)))
    adv_students = [] # list of students to see the advisor
    for i in range(len(marks)):
        if marks[i] < mean - sd:
            adv_students.append(names[i])
    if len(adv_students) > 0:
        print("List of students who need to see an advisor:")
        for i in adv_students:
            print(i)
    
if __name__ == "__main__":
    main()