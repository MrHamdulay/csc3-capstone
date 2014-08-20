""" a program that determines which students, according to the marks need to see a student an advisor
nelisile mkhwebane
13/05/2014"""

import math

""" get the text file from the user"""
filename= input("Enter the marks filename:\n")

"""open the file and get it's content"""
f = open(filename, "r")
lines = f.readlines()
f.close()

"""get the sum of the marks for the average"""
sum_marks= 0
for i in range (len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j]==",":
            sum_marks = sum_marks+ int(lines[i][j+1:])
average = sum_marks/ len(lines)

"""calculating the standard deviation"""
sum_s = 0
for i in range (len(lines)):
    for j in range (len(lines[i])):
        if lines[i][j] ==",":
            sum_s = sum_s + (int(lines[i][j+1:])-average)**2
"""therefore, the standard deviation"""
stand_dev = math.sqrt(sum_s/len(lines))

"""printing out the resuts"""
print("The average is:", "%.2f" % (average))
if stand_dev==0:
    print("The std deviation is:", "0.00")
else:
    print("The std deviation is:", "%.2f" % (stand_dev))
if stand_dev>0:
    print("List of students who need to see an advisor:")
    """to get the list of students"""
    for i in range (len(lines)):
        for j in range (len(lines[i])):
            if lines[i][j]==",":
                if int(lines[i][j+1:]) < average - stand_dev:
                    print(lines[i][:j])
    




 