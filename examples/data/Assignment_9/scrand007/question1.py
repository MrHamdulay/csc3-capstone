import math
fileName = input("Enter the marks filename:\n")
n = []
m = []
sum1 = 0
num1 = 0

#create list of lines from marks file
f = open(fileName, 'r')
lines = f.readlines()
f.close()

for i in range(len(lines)):
    lines[i] = lines[i].split(",")
    
for i in range(len(lines)):
    n.append(lines[i][0])
    m.append(lines[i][1])
    
m[len(m)-1] = m[len(m)-1]+"\n"
    
for i in range(len(m)):
    m[i] = int(m[i][:-1])
    
for i in range(len(m)):
    sum1 += m[i]
mean = round(sum1/len(m),2)

for i in range(len(m)):
    num1 += (m[i] - mean)**2

stddev = round(math.sqrt(num1/len(m)),2)
    
print("The average is:", "%.2f" % mean)
print("The std deviation is:", "%.2f" % stddev)

risk = mean - stddev

for i in range(len(m)):
    if m[i] < risk:
        print("List of students who need to see an advisor:")
        break
    
for i in range(len(m)):
    if m[i] < risk:
        print(n[i])