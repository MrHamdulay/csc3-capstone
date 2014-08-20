#Program to analyse student marks and determine need for student advisor
#Ethan Jackson 
#14 May 2014

import math
marks = []
filename = input("Enter the marks filename:\n")
f = open(filename, "r")
readfile = f.readlines()
names = []
advs = []
for i in readfile:#runs through list
    names.append(i.split(",")[0])#creates list of names only
#print(names)
for j in readfile:
    marks.append(j.split(",")[1].replace('\n','').replace(' ',''))#creates list of marks only
#print(marks)
summarks = 0
counter = 0
for i in marks:
    summarks += int(i)
    counter += 1
mean = "{0:.2f}".format((summarks/counter))#finds average of marks
s = 0
for i in marks:
    s += ((int(i) - eval(mean))**2)
   #print(s)
#mean2 = "{0:.2f}".format(mean)
sd = "{0:.2f}".format(math.sqrt(s/counter))#finds standard deviation of marks
dev = eval(mean) - eval(sd)
for i in marks:
    if int(i) < dev:
        ad = marks.index(i)#finds each mark of the student who needs an advisor
        advs.append(ad)
print("The average is:", mean)
print("The std deviation is:", sd)
if len(advs) > 0:
    print("List of students who need to see an advisor:")
    for i in advs:
        print(names[i])
        #if in marks1:
            #print(readfile[advs][:-3])
        #else:
            #print(readfile[advs][:-2])


