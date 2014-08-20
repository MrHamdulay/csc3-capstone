""" Sizwe Sibiya
Assignment 10 """


def standard_deviation():
    
    mysum = 0
    for x in data.keys():
        y = (x-mean)**2
        mysum += y
    std = ((mysum)/len(data))**0.5
    return(std)
    
filename = input("Enter the marks filename:\n")
results = open(filename, 'r')
data = {}
total = 0

##main
while True:
    line = results.readline()
    if not len(line) == 0:
        student = line.split(",") 
        data[eval(student[1])] = student[0]
    else: break    
results.close()

for mark in data.keys():
    total += mark
mean = total/len(data)
print("The average is: {:.2f}".format(mean))
print("The std deviation is: {:.2f}".format(standard_deviation()))
print("List of students who need to see an advisor:")

for score in data.keys():
    if score < mean:
        print(data[score])

