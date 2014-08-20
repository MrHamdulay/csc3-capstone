#Shivam Ragoonaden RGNSHI002
#Program to check if students need to see student advisors or not
#10 May 2014
import math
fileinput = input("Enter the marks filename:\n")

f = open(fileinput,"r")

lines = []

for line in f:
    lines.append(line)  #Create an array of the lines from the textfile

f.close

values = []  
arrNames = []
arrMarks = []

for i in range(len(lines)):
    if i != len(lines)-1: #As long as it's not the last line (Last line doesn't have \n)
        lines[i] = lines[i][:-1]  #Get rid of the \n
    
for line in lines:
    values = line.split(",")  #It will split the name and mark of one line and assign the values to the array
    arrNames.append(values[0])  #First item of array is name
    arrMarks.append(int(values[1]))  #2nd item is mark, convert to integer
    
total = 0
totalstd = 0.0  #Make it a float
count = 0

for mark in arrMarks:
    total += mark #Add up marks
    count += 1  #Keep count of number of marks
    
average = round(total/count,2)  #Get average

for mark in arrMarks:
    totalstd += (mark - average)**2  #Formula total
    
std = round(math.sqrt(totalstd/count),2)  #Rest of formula

stddown = average - std  #One standard deviation down

print("The average is: %.2f" % average)
print("The std deviation is: %.2f" % std)  #Formatting for double decimal when x.00

Advisor = []

for mark in range(len(arrMarks)):
    if arrMarks[mark] < stddown:  #Test if smaller than one SD down
        Advisor.append(arrNames[mark])  #Add name to list of advisor

if len(Advisor) > 0:  #Is  there atleast one student with less than one standard deviation?
    print("List of students who need to see an advisor:\n", end = "")    
    for i in Advisor:
        print(i)  #Print the students that need to see advisor