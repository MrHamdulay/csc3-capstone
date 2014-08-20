"""danson masuka
program to analyse student marks read in from a file and determine which students need to see a student advisor
14 may 2014"""
import math
#input for file to be read
fileinput = input ("Enter the marks filename:\n")

#open the file to read it
f = open (fileinput,"r")
lines = f.readlines()
f.close()

#open new list called marks to append the marks only
marks = []

#create loop to append marks to the list
for i in range(len(lines)):
    marks.append(lines[i].split(',')[-1])
    
#create loop to count the number of marks in list
count = 0
for i in range(len(marks)):
    count+=1

#now create another loop to find the total of the marks
total = 0
for j in range(len(marks)):
    total += eval(marks[j])

#now calculate the mean
mean = total/count
print ("The average is:","{:.2f}".format(mean))
#now we make a loop for the summation for the calculation of the standard deviation
summ = 0
for i in range(len(marks)):
    tot = (eval(marks[i])-mean)**2
    summ += tot
standd = math.sqrt(summ/count)

#now print the standard deviation
print ("The std deviation is:","{:.2f}".format(standd))

#now to output the students to see advisor we use a loop

for i in range(len(marks)):
    if eval(lines[i].split(',')[-1]) < mean-standd:
        print ("List of students who need to see an advisor:")
        break
for i in range(len(marks)):
    if eval(lines[i].split(',')[-1]) < mean-standd:
        print(lines[i].split(',')[0])

