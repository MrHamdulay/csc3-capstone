'''Program to determine which students need to go see a student advisor
Matshepo Malatji 
13 May 2014'''

import math

#Ask user to enter the file name
UserData = {}
filename = input("Enter the marks filename:\n")
f = open(filename, "r")


#Enter the textfile data into a dictionary
for s in f:
    pos = s.find(',')
    UserData[s[:pos]] = s[pos+1:-1]
UserData[s[:pos]] = s[pos+1:]
    
#print(UserData)
f.close()

#Find the mean and print it
mean = 0
counter = 0
for item in UserData: 
    mean += float(UserData[item])
    counter += 1
mean = mean/counter
sObj = "{0:0.2f}"
print("The average is: " + sObj.format(mean))

#Find the standard deviation an print it
standard_dev = 0
for item in UserData: 
    standard_dev += (float(UserData[item]) - mean)**2
standard_dev = math.sqrt(standard_dev/counter)
print("The std deviation is: " + sObj.format(standard_dev))
    
#Detrmine which students are below one standard deviation and print

AdvisorList = []
boundary = mean - standard_dev
for item in UserData: 
    if float(UserData[item]) < boundary :
        AdvisorList.append(item)

if len(AdvisorList) > 0:
    print("List of students who need to see an advisor:")
    for k in AdvisorList:
        print(k)
