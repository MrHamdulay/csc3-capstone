#Programme to see which students need to see a student advisor
#Joe Sutton
#11 May 2014

import math

filename=input("Enter the marks filename:\n")
f=open(filename, "r")
marksheet=f.readlines()
f.close()
total=0
divisor=0
count=0

for line in marksheet:
    names_and_marks=line.split(",")
    total+=eval(names_and_marks[1])
    divisor+=1

average=round(total/divisor,2)

variance=0
counter=0

for line in marksheet:
    names_and_marks=line.split(",")
    variance+=(eval(names_and_marks[1])-average)**2
    counter+=1

variance=variance/counter

standard_deviation=round(math.sqrt(variance),2)

print("The average is:","{0:.2f}" .format(average))
print("The std deviation is:", "{0:.2f}".format(standard_deviation))
for line in marksheet:
    names_and_marks=line.split(",")
    if eval(names_and_marks[1])<(average-standard_deviation):
        if count==0:
            print("List of students who need to see an advisor:")
            count=1
        print(names_and_marks[0])