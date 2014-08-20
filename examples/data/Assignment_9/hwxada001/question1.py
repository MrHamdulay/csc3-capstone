import math
file = input("Enter the marks filename:\n")
f = open(file, "r")
a = []
t = 0
sum = 0
n = 0
std = 0
for line in f:
    if line[len(line)-4] == ",":
        a.append(line[0:len(line)-4])
        a.append(line[len(line)-3:len(line)-1])
        sum += eval(str(a[len(a)-1]))
        n +=1
    else:
        a.append(line[0:len(line)-3])
        a.append(line[len(line)-2:len(line)-1])
        sum += eval(str(a[len(a)-1]))
        n +=1        
mean = sum/n
for i in range(n):
    std += (int(str(a[i*2+1]))-mean)**2
std = math.sqrt(std/n)
print("The average is:", "%.2f" % mean, "\nThe std deviation is:", "%.2f" % std,end='')
advisor = ""
for j in range(n):
    if int(a[j*2+1])<int(mean-std):
        advisor += "\n" + (a[j*2])
if advisor != "":
    print("\nList of students who need to see an advisor:",end='')
    print(advisor)
f.close()