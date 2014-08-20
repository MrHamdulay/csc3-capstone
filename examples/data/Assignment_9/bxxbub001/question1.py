
import math


def avg(l):
    total = 0
    for i in range(len(l)):
        total = total+l[i]
        
    
    theAvg = total/len(l)
        
   
        
    return theAvg

def stdDev(l):
    top = 0
    avgMark = avg(l)
    for mark in l:
        top = top+ ((mark - avgMark)**2)
        
    
    deviation = math.sqrt(top/len(l))
    return deviation
    
    
#print(stdDev(l))
filename = input("Enter the marks filename:\n") #input("Enter the marks filename:\n")
f = open(filename, "r")
lines = f.readlines()
f.close()

for x in range(len(lines)): #split name and mark into list
    lines[x] = lines[x].split(",")
    
for x2 in range(len(lines)-1): #remove \n
    lines[x2][1]=lines[x2][1][:-1]

list_marks = []

for x in range(len(lines)):
    list_marks.append(eval(lines[x][1]))
    
    
average = avg(list_marks)
StandardDeviation = stdDev(list_marks)

print("The average is:","{0:.2f}".format(average))
print("The std deviation is:","{0:.2f}".format(StandardDeviation))

for x4 in range(len(lines)):
    if list_marks[x4] < (average - StandardDeviation):
        print ("List of students who need to see an advisor:")
        break
        
for x3 in range(len(lines)):
    if list_marks[x3] < (average - StandardDeviation):
        print(lines[x3][0])
    
    
#print(lines)

#print(list_marks)


