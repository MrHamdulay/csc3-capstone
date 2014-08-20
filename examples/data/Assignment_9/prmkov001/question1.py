#Kovlin Perumal
#PRMKOV001
#13/05/2014
#File Reading Marks Program

from math import * #Import the maths class for sqrt function

fileName = input("Enter the marks filename:\n") #Ask for filename to be inputted

lines = []

f = open(fileName,"r") #Open the txt file for reading purposes

lines = f.readlines() #Read each line into an array

f.close()

for i in range(len(lines)): #Delete the '/n' character from the end of each line
    
    lines[i] = lines[i][:-1]

    
names = []
marks = []
total = 0 #Initialise variables needed

for i in range(len(lines)) : #For each item in lines cut the name and the mark out and store them in individual arrays
    names.append(lines[i][:lines[i].index(",")])
    marks.append(int(lines[i][lines[i].index(",") + 1:]))
    total += marks[i] #Keep track of the total mark
    
v = 0
for i in range(len(marks)) :
    v += (marks[i] - total/len(marks))**2 #Work out the v part of standard deviation using the formula

std = round(sqrt((v)/len(marks)),2) #Work out final standard deviation

print("The average is:" , '{0:.2f}'.format((total/len(marks))))
print("The std deviation is:" , '{0:.2f}'.format(std)) #Use format to make sure two decimals are displayed

adviceNeeded = False

for i in range(len(marks)):
    if (total/len(marks) - std) > marks[i] :
        adviceNeeded = True #Check if anyone lies under 1 std deviation and then set adviceNeeded to true 
        
if adviceNeeded : #Only print if advice is needed
    print("List of students who need to see an advisor:")

for i in range(len(marks)):
    if (total/len(marks) - std) > marks[i] :
        print(names[i])