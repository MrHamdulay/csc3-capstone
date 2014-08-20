#Joy Arendse-Gorvalla

filename = input("Enter the marks filename:\n") #asking user for the filename
f = open(filename,"r") #opens file to read with the filename from user input
count = 0.00 
marks = [] #creating an array
for line in f: #loop, for every  line in f
    count = count + 1.0
    marks.append (line.split(",")) #adds to the array
f.close() #close file
mean = 0.0 
for i in range (int(count)): #loop
    mean = mean + float(marks[i][1])
mean = mean/count
stdvn = 0.0
for i in range (int(count)): #loop
    stdvn = stdvn + ((float(marks[i][1]) - mean)**2)
stdvn = (stdvn/count)**0.5
print("The average is:", "%.2f" % mean)
print("The std deviation is:", "%.2f" % stdvn)
tutor = False
for i in range (int(count)): #loop
    if (float(marks[i][1]) < (mean - stdvn)): #if the mark is less the standard deviation from the mean
        tutor = True
if tutor:
    print("List of students who need to see an advisor:")
    for i in range (int(count)):
        if (float(marks[i][1]) < (mean - stdvn)):
            print(marks[i][0])

