""" Q1 of Assignment 9: Student Marks Analyser
Shaheel Kooverjee - KVRSHA004
15 May 2014 """

filename = input("Enter the marks filename: \n")
marklist = []
studentmarks = {}

file = open(filename, "r")
for line in file: #read each line of file
    entry = line.split(",") #entry[0] = name; entry[1] = mark
    entry[1] = entry[1].replace("\n", "") #replace "new line" with empty string
    marklist.append(entry[1]) #append mark to marklist
    studentmarks[entry[1]] = entry[0] #add marks (keys) with student names (values) to dictionary
file.close()

marksum = 0 #sum of all marks
for i in marklist:
    marksum += eval(i) #add each mark to mark sum
mean = marksum/len(marklist) #mean = sum of marks / number of marks
print("The average is: {0:0.2f}".format(mean))

xm = 0 #where xm = sum of (mark - mean)^2
for x in marklist:
    xm += (eval(x)-mean)**2
stddev = (xm/len(marklist))**0.5 #standard deviation = sqrt(xm / number of marks)
print("The std deviation is: {0:0.2f}".format(stddev))

criteria = mean - stddev #one standard deviation below mean
notmetcriteria = [] #list of students who have not met criteria
for j in marklist:
    if eval(j) < criteria:
        notmetcriteria.append(studentmarks[j]) #add name if mark less than criteria
if len(notmetcriteria) != 0:
    print("List of students who need to see an advisor:")
    for name in notmetcriteria:
        print(name)