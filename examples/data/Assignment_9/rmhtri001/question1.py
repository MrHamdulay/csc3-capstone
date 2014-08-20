filename = input ("Enter the marks filename:\n")

lines = open (filename, "r")
StudentMarks = lines.readlines()
lines.close()

NewFile = []

for StudentMark in StudentMarks:
    if StudentMark[-1] == "\n":
        StudentMark = StudentMark[:-1]
        NewFile.append(StudentMark)
    else:
        NewFile.append(StudentMark)

Sum = 0.0

for File in NewFile:
    templist = File.split(",")
    number1 = eval(templist[1])
    
    Sum = Sum + number1    

Average = Sum / len(NewFile)

Sum2 = 0.0

for File in NewFile:
    templist2 = File.split(",")
    number2 = eval(templist2[1])
    Sum2 = Sum2 + (number2-Average)**2

StandardDeviation= (Sum2 / len(NewFile))**(1/2)

print("The average is:", "%.2f" % Average)
print("The std deviation is:", "%.2f" % StandardDeviation)

Counlist = []
for file in NewFile:
    templist3 = file.split(",")
    number3 = eval(templist3[1]) 
    if number3 < (Average-StandardDeviation):
        Counlist.append (templist3[0])

if Counlist != []:
    print("List of students who need to see an advisor:")
    for z in Counlist:
        print (z)
