"""Student mark checker
Christopher Sterley
11/05/2014"""

import math

test_results=input("Enter the marks filename:\n") #get input from user

f = open(test_results, "r") #open file that user wants to use
test_results = f.readlines()
f.close() #close file for efficiency

total_mark=0 #variable to keep track of the marks that are found

for lines in range(len(test_results)):
    for position in range(len(test_results[lines])):
        if test_results[lines][position]==",":
            total_mark+=int(test_results[lines][position+1:]) #total all marks

average_mark=total_mark/len(test_results) #determine the average of all the marks

std=0

for lines in range(len(test_results)):
    for position in range(len(test_results[lines])):
        if test_results[lines][position]==",":
            std+=(int(test_results[lines][position+1:])-average_mark)**2 #first step for determining standard deviation
            
standard_deviation=math.sqrt(std/len(test_results)) #final standard deviation value

print("The average is:","{:.2f}".format(average_mark))
print("The std deviation is:","{:.2f}".format(standard_deviation))
if round(standard_deviation,0)!=0:
    print("List of students who need to see an advisor:") #final print statements



for lines in range(len(test_results)):
    for position in range(len(test_results[lines])):
        if test_results[lines][position]==",":
            std_range=int(test_results[lines][position+1:])
            if std_range<average_mark-standard_deviation: #checking which students marks are more than one standard deviation away from the mean
                print(test_results[lines][:position])        