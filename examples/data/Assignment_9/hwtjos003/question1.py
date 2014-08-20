"""mark checker
Joshua Hewitson
2/5/2014"""

import math # need math module for square root and power
# create variables; mylist will be a list of lists with length 2, containing the name and the mark of each student
mylist = []
# lines is a list for reading in the lines of the text file
lines = []
# total is the sum of all the marks, devtotal is used to calculate the standard deviation, which is stdev 
total = 0
devTotal = 0
stdev = 0

# ask the user to input a file name and read in the lines of the file:
file_name = input("Enter the marks filename:\n")
f = open(file_name , "r")
lines = f.readlines()
f.close()

#calculate the total:
for line in lines:
    mylist.append(line.split(","))
    total += eval(mylist[lines.index(line)][1])

#calculate and print out the average
average = total/len(lines)
print ('The average is:' , '%.2f' % average)

#find devTotal:
for i in mylist:
    devTotal += math.pow(eval(i[1]) - average, 2)

#calculate stdev and print it out:
stdev = math.sqrt(devTotal/len(lines))
print("The std deviation is:", '%.2f' % stdev)

#find all the students who are below one stdev from the mean and print out their names:
printed = False
for i in mylist:
    if eval(i[1]) < average - stdev:
        if printed == False:
            print("List of students who need to see an advisor:")
            printed = True
        print(i[0])

