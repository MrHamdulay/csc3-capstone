"""read peoples names and marks from a text file and out the names of those who arent within one standard deviaition of the marks
Michael field
10 may 2014"""

def stdDev(marks, ave):
    stddev = 0
    
    for mark in marks:
        mark = eval(mark)
        stddev += (mark - ave)**2
    
    stddev = stddev/len(marks)
    stddev = stddev**0.5
    
    return stddev

lines = []

file = input("Enter the marks filename:\n")

f = open (file, "r")
#insert each line into the lines array
for line in f:
    lines.append(line)

f.close()

#remove the \n
for i in range(len(lines)):
    if i != len(lines)-1:
        lines[i] = lines[i][:-1]

NameMark = []
names = []
marks = []

#split names and marks
for line in lines:
    NameMark = line.split(",")
    names.append(NameMark[0])
    marks.append(NameMark[1])
    
#calc the average
total = 0
for mark in marks:
    total += eval(mark)
ave = total/len(marks)

print("The average is:", '%.2f' % ave)
sd = stdDev(marks, ave)
print("The std deviation is:", '%.2f' % sd)

if (ave-sd) != ave:
    print("List of students who need to see an advisor:")

for pos in range(len(marks)):
    if eval(marks[pos]) < (ave-sd):
        print(names[pos])