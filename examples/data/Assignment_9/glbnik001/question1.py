# Nikhil Gilbert
# programme for student advisor recommendations 
# 15 May 2014
import math

#initialize...
filename = input("Enter the marks filename:\n")
f = open(filename, "r")
Filelist = f.readlines()
Editlist = [line.rstrip() for line in Filelist]
f.close()
numerical = []
name = []

#Goes through each item and finds value from each append the to a list
for i in range (len(Filelist)):
    for ele in Filelist[i]:
        x = int(''.join(ele for ele in Filelist[i] if ele.isdigit())) #Got from stack overflow
    numerical.append(x)

# This next part gets the corresponding string for the numbers that were stripped from the files
for a in range (len(Editlist)):
    for ebe in Editlist[a]:
        y = ''.join([ebe for ebe in Editlist[a] if not ebe.isdigit()])
    name.append(y)    
name_edit = [line.strip(",") for line in name]

#Workout the average 
total = 0
for i in range(len(numerical)):
    total = total + numerical[i]
average = total/len(numerical)
average2 = "{0:.2f}".format(average)
print ("The average is: ",average2,sep="")

#Workout the standard Deviation
squaredif = 0
for i in range(len(numerical)):
    converter = numerical[i]
    squaredif = squaredif + ((converter-average)*(converter-average))
variance = squaredif/len(numerical)
stddev = math.sqrt(variance)
stddev2 = "{0:.2f}".format(stddev)
print ("The std deviation is: ",stddev2,sep="")

#list of students who need to see a student advisor (workout distance from std dev)
studentad = []
for i in range (len(numerical)):
    compare=numerical[i]
    assess = compare-average
    divider = stddev/-1
    if stddev == 0:
        jinx = 0
    elif assess <= divider:
        studentad.append(name[i])

#Final phase of printing out students that need help from the advisor
studentad = [line.strip(",") for line in studentad]
if stddev != 0:
    print ("List of students who need to see an advisor:")
    for i in studentad:
        print (i)
else:
    jinx=0 # don nothing 