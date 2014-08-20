"""Program to analyse marks in a file
Dumisani J Nyathi
13-05-2014"""

import math

#get filename from user
marksfile = input("Enter the marks filename:\n")   
infile = open(marksfile,"r")
readem = infile.read()
infile.close()

#make lines into a list
readem.strip("")
list1 = readem.split('\n')

#get a list of the marks without names to use in average calculation and s.d calculation
marks = []
for i in list1:
    if i!="":
        mark = i.split(',')
        x=mark[1]
        marks.append(x)

#calculate the average
summ1 = 0
num = 0
for i in marks:
    summ1 += eval(i)
    num += 1
average = (summ1/num)

#calculate the standard deviation
summ2 = 0
for i in marks:
    std = (eval(i) - average)**2
    summ2 += std
s_dev = math.sqrt(summ2/num)

#get list of pupils who have to see advisor
see_me = average - s_dev
the_list = []
for i in list1:
    if i != "":
        mark = i.split(',')
        if eval(mark[1]) < see_me:
            the_list.append(mark[0])
        else:
            continue
    

       

    
#print out results
print("The average is:","{0:.2f}".format(average))
print("The std deviation is:","{0:.2f}".format(s_dev))
if the_list !=[]:
    print("List of students who need to see an advisor:")
    for name in the_list:
            print(name)
