"""checks marks for students who need to see a student advisor
mishka latib
14 may 2014"""

import math

a = input("Enter the marks filename:\n")
f = open(a,"r")
#reads line from file
z = f.readlines()

#puts data into lists
b = []
c = []

for i in z:
    b = i.split("\n")
    c.append(b[0])
    b = []

z = []
b = []
d = []

#separates marks and names into separate lists
for i in c:
    d = i.split(",")
    z.append(d[0])
    b.append(d[1])
    d = []
    
mark_sum = 0
s = 0
count = 0

for i in b:
    s = eval(i)
    mark_sum+=s
    count+=1
      
#calculates mean and changes mean mark to 2 decimal places
mean = (mark_sum/count)
meanstr = '%.2f'%mean

print("The average is:",meanstr)

#calculates standard deviation
v = 0
sum2 = 0
for i in b:
    v = ((eval(i))-mean)*((eval(i))-mean)
    sum2+=v

dev = round(math.sqrt(sum2/count),2)

dev1 = '%.2f'%dev

#checks marks for ones below 1 std deviation below mean and prints outputs
print("The std deviation is:",dev1)

if dev>0:
    print("List of students who need to see an advisor:")

for i in range(len(b)):
    if eval(b[i])<(mean-dev) :
        print(z[i])
 
#closes file 
f.close()