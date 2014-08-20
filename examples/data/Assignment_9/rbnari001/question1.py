#Ariel Rubin
#RBNARI001
#program to clacualte marks below one standard deviation for students who need a tutor
#13 May 2014

#user enters file name
#program opens the file to read inoformation from it
filename = input("Enter the marks filename:\n")
f = open(filename,"r")

#variable that will be used later inthe prgram
count = 0.00

#creating an array
marks = []
#counting number of lines in the file
#splitting the contents of the file by a comma
for line in f:
    count = count + 1.0
    marks.append (line.split(","))
    
#closing the file
f.close()

#calculates the mean (average) for the student marks
mean = 0.0
for i in range (int(count)):
    mean = mean + float(marks[i][1])
mean = mean/count

#calculates the standard deviation for the student marks
stdvn = 0.0
for i in range (int(count)):
    stdvn = stdvn + ((float(marks[i][1]) - mean)**2)
stdvn = (stdvn/count)**0.5

#prints out mean and standard deviation
print("The average is:", "%.2f" % mean)
print("The std deviation is:", "%.2f" % stdvn)

#checks to see if a student's mark is below the standard deviation
needtutor = False
for i in range (int(count)):
    if (float(marks[i][1]) < (mean - stdvn)):
        needtutor = True

#prints out the name of all the students who need to see a tutor
if needtutor:
    print("List of students who need to see an advisor:")
    for i in range (int(count)):
        if (float(marks[i][1]) < (mean - stdvn)):
            print(marks[i][0])    
    
