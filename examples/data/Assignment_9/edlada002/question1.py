"""Assignment 9 Question 1
Adam Edelberg
2014-05-16"""


file = input("Enter the marks filename:\n")
f = open(file, "r")

count = 0
std = 0
mean = 0


marks = []


for line in f:
    count += 1.0
    marks.append (line.split(","))
f.close()


for i in range (int(count)):
    mean = mean + float(marks[i][1])
mean = mean/count

for i in range (int(count)):
    std = std + ((float(marks[i][1]) - mean)**2)
std = (std/count)**0.5

std2 = format(std,'.2f')
mean2 = format(mean, '.2f')

print ("The average is:", mean2)
print("The std deviation is:", std2)


students=[]
for i in range(int(count)):
    if float(marks[i][1]) < (mean-std):
        students.append(marks[i][0])
if len(students) > 0:
    print('List of students who need to see an advisor:')
    for i in students:
        print(i)