#Question 1, Assignment 9
#Gina Horscroft
#10.05.2014
import math

filename = input("Enter the marks filename:\n")
f = open(filename, "r")
x = f.readlines()
f.close()

lowMarks = 0
average = 0
count = 0
stdD = 0

#remove the \n characters
for a in range(len(x)):
    temp = x[a]
    temp = temp.replace("\n", "")
    x[a] = temp   
arr2D = []
#calculate the average
for i in range(len(x)):
    temp = x[i]
    pos =  temp.find(",")#pos of comma
    key = temp[0:pos]
    value = eval(temp[pos+1:len(temp)])
    arr2D.append(key)
    arr2D.append(value)
    
    average+=value#calculates sum    
    count+=1#counts how many values
average = average/count

#calculate standard deviation
for a in range(1, len(arr2D), 2):
    stdD+= (arr2D[a]-average)**2
stdD = math.sqrt(stdD/count)
lowMarks = average - stdD

print("The average is: %0.2f" %average)
print("The std deviation is: %0.2f" % stdD)

for a in range(1, len(arr2D), 2): 
    if (arr2D[a] < lowMarks):
        print("List of students who need to see an advisor:")
        break
        
for a in range(1, len(arr2D), 2): 
    if (arr2D[a] < lowMarks):
        print(arr2D[a-1])