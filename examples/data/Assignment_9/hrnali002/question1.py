"""A program to analyse student marks from a file
Alison Hoernle
HRNALI002
10 May 2014"""

import math # for the standard deviation calculation

file_1 = input("Enter the marks filename:\n")

f = open(file_1, "r") # open the file that they input and we want to read info from this file

# make a list of lists, each item has the name as pos 0 and the mark as pos 1
list = []
for line in f:
    x = line.split(',')
    list.append(x)
    
f.close()

# add the marks together and divide by the length of the list to get ave
sum = 0
for row in list:
    sum += int(row[1])

ave = sum / len(list)
ave = "{0:0.2f}".format(ave)
print("The average is:", ave)

# now work out the standard deviation using given formula
sd_sum = 0
for row in list:
    sd_sum += (int(row[1]) - eval(ave))**2

    
sd = math.sqrt(sd_sum/len(list))
sd = "{0:0.2f}".format(sd)

print("The std deviation is:", sd)
 
# find the students whose marks are lower than the ave - sd and print only the names of those students
def find_students(list):
    if len(list) == 0:
        return ''
    elif int(list[0][1]) < eval(ave) - eval(sd):
        return list[0][0] + '\n' + find_students(list[1:])
    else:
        return find_students(list[1:])

students = find_students(list) # call this function

if students != '':
        print("List of students who need to see an advisor:\n", students, sep = '')