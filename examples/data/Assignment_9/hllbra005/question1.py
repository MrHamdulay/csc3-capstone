# Program to calculate mean and standard deviation of marks from a file
# Brandon Hall (HLLBRA005)
# 16/05/2014


filename = input("Enter the marks filename:\n") 
f = open(filename,"r") #program opens the file (read function)
 
#counter variable (Float)
count = 0.00
 
#create the array
marks = []
#count the number of lines in the file

for line in f:
    count = count + 1.0
    marks.append (line.split(","))
   
#close the file
f.close()
 
#The mean of the student marks
mean = 0.0
for i in range (int(count)):
    mean = mean + float(marks[i][1])
mean = mean/count
 
#The standard deviation for the marks
sd = 0.0
for i in range (int(count)):
    sd = sd + ((float(marks[i][1]) - mean)**2)
sd = (sd/count)**0.5
 
#prints to screen
print("The average is:", "%.2f" % mean)

print("The std deviation is:", "%.2f" % sd)
 
#is a student's mark is below the standard deviation?
needtutor = False
for i in range (int(count)):
    if (float(marks[i][1]) < (mean - sd)):
        needtutor = True
 
#students that need to see a tutor
if needtutor:
    print("List of students who need to see an advisor:")
    for i in range (int(count)):
        if (float(marks[i][1]) < (mean - sd)):
            print(marks[i][0])