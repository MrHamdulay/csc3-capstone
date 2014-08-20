from functools import reduce

#get input
fname = input("Enter the marks filename:\n")
fin = open(fname, "r")
marks = []
for line in fin.readlines():
    name, mark = line.split(",")
    marks.append((name, float(mark)))
                 
#grab mean and sdev
mean = reduce(lambda x,y: x + y[1], marks, 0)/len(marks)
sdev = (reduce(lambda x,y: x + (y[1] - mean)**2, marks, 0)/len(marks)) ** 0.5

#filter marks
marks = list(filter(lambda x: x[1] < mean-sdev, marks))

#output
print("The average is: %.2f" % mean)
print("The std deviation is: %.2f" % sdev)

if len(marks) > 0:
    print("List of students who need to see an advisor:")
    for name, mark in marks:
        print(name)
                     
