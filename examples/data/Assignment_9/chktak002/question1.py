#takunda chikondo
# a progrmmme to determine if a student should see a tutor
import math
grades=input("Enter the marks filename:\n")
f= open(grades,"r")
lines= f.readlines ()
f.close
file=[]
marks=[]
names=[] 


for i in range(len(lines)):
    if i != len(lines)-1:
        lines[i] = lines[i][:-1] #femoves the \n character

for line in lines:
    file=line.split(",")
    names.append(file[0]) #adds the names and marks to their respective lists
    marks.append(file[1])

#average    
total=0
for i in range(len(marks)):
    total+=eval(marks[i])

ave= total/(len(marks))
print("The average is: %.2f"%ave)


#standard deviation
variance=0
for i in range(len(marks)):
    variance += ((eval(marks[i])-ave)**2)
std = math.sqrt(variance/len(marks))
print("The std deviation is: %.2f"%std)

x =ave-std

count=0
for i in range(len(marks)):
    if eval(marks[i])<x: #determines if the students mark is greater than 1 standard deviation from the mean  
        count += 1
        if count == 1 :
            print("List of students who need to see an advisor:")            
        print(names[i])

        
    







    
    
    


    