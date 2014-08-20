"""program to anaylyse students marks
Claudia Pastellides
13 May 2014"""

import math

filename = input("Enter the marks filename:\n")
#gets file name and opens file to read
f = open(filename, 'r')
marks_str = f.read() #reads whole file as string

total = 0
counter = 0
std = 0
marksarray = []
array2 = []
array1 = []
array1 = marks_str.split("\n") #splits file string into list using \n as seperator

for line in array1:
    array2.append(line.split(",")) #array 2 with seperate marks and students

for loop in range(0,len(marks_str)+1): 
    if marks_str[loop:loop+1] == ",": #if it is a common in string file, then exclude this
        mark = marks_str[loop+1:loop+3]
        marksarray.append(int(mark)) #adding to list of marks
        total += int(mark)
        counter += 1

average = total/counter
newaverage = round(total/counter, 2) #rounding to 2 decimals
for loop2 in marksarray: #adding to pre standard dev
    std += (int(loop2)-average)**2    

std = math.sqrt(std/counter) #calculating std dev
newstd = round(std,2) #rounding to 2 decimals

newaverage = str(newaverage)
finalstd = str(newstd)

for loop2 in range(0,len(finalstd)): #loop to accounter for .00 for dev
    if (finalstd[loop2] == ".") and (finalstd[loop2+1:] == "0"):
        finalstd = finalstd+"0"
        
for loop1 in range(0,len(newaverage)): #loop to accounter for .00 for av
    if (newaverage[loop1] == ".") and (newaverage[loop1+1:] == "0"):
        newaverage = newaverage+"0"
        
namesarray = []
boolean = False
advisorcheck = average-std
for i in range(len(array2)-1):
    if eval(array2[i][1]) < advisorcheck: # if mark is less, then need to see advisor
        boolean = True
        namesarray.append(array2[i][0]) #attatching names to array of students 

print("The average is:", newaverage)
print("The std deviation is:", finalstd)
if boolean == True:
    print("List of students who need to see an advisor:")
    for loop4 in namesarray: #printing out student names item by item in list
        print(loop4)