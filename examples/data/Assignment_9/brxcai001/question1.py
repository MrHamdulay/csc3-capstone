#Python program to analyse student marks read in from a file and determine which students need to see a student advisor (marks less than one standard deviation below mean).
#BRXCAI001
#16 May 2014

import math

filename = input("Enter the marks filename:\n")
f = open( filename, "r")
lines = f.readlines ()
f.close()

list1 = []
for i in lines:
    strings = i.split(",")
    list1.append(eval(strings[1]))

#Calculate sum of values.
sum_of_marks = 0
for j in list1:
    sum_of_marks += j
    
#Calculate the avergae of values.
average = sum_of_marks/len(list1)
normAV = "{:.2f}".format(average)

print("The average is:",normAV)

#Calculate the variance. 
var = 0
for l in list1:
    var += (l- average)**2
    
#Calculate the standard deviation.
std = math.sqrt(var/len(list1))
stdround = round(std,2)
normstd = "{:.2f}".format(stdround)
print("The std deviation is:",normstd)

#Calculate the minimum value against which the marks will be tested.
lowerlimit = average - std
needadvisor  = " "

#Check in orginal list of strings if the mark is lower than the minimum limit. If it is match this mark to the name of the student.
for i in lines:
    if eval(i.split(",")[1]) < lowerlimit:
            needadvisor += '\n' +i.split(",")[0]
if needadvisor != ' ':
    print("List of students who need to see an advisor:",needadvisor,sep='')
    



        

    

    
