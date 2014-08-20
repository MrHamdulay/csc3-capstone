"""analyse student marks read in from a file and determine which students need to see a student advisor
barak setton
11/05/2014"""

import math
file = input("Enter the marks filename: \n")

# reading from file
f = open(file,"r")
count = 0
stand =0
totmark =0
listmark =[]
listname =[]
line = f.readline()
while line:
    count += 1
    l = line.split(",")
    listmark.append(eval(l[1])) # making arrays to use later
    listname.append(l[0])
    totmark += eval(l[1])   # calculating total marks 
    line = f.readline()
f.close
mean = (totmark/count) # geting the mean
for i in range (count):
    stand = stand + ((listmark[i] -mean )**2)
    
stdev = round((math.sqrt(stand / count)),2)
#---------------------------------

#  print info
print("The average is:",("%.2f" % mean))
print("The std deviation is:",("%.2f" % stdev))
li = ""

for c in range(count):
    if listmark[c]<(mean-stdev): # checking if the person has to go to adviser
        li = li+ (listname[c])+"\n"

if li:
    print("List of students who need to see an advisor: ")
    print(li)
    
#-----------------


