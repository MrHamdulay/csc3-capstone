# Align text

x = input("Enter the marks filename:\n") 
wfile = open(x, "r")

x = wfile.readlines()
wfile.close()

lst = []
for i in x:
    i = i[:-1]
    lst.append(i)

num = []
for j in lst:
    if j[-2] == ',':
        j = int(j[-1])
    else:
        j = int(j[-2:])
    num.append(j)


name = []
for k in lst:
    if k[-2] == ',':
        k = k[:-2]
    else:
        k = k[:-3]
    name.append(k)


average = sum(num)/len(num)
print("The average is:", format(average, '.2f'))

std = []
for n in num:
    n = (n-average)**2
    std.append(n)

stdev = (((sum(std))/len(num))**0.5)

print("The std deviation is:", format(stdev, '.2f'))

if stdev > 0:
    print("List of students who need to see an advisor:")
elif stdev == 0:
    print()

for l in num:
    if l < (average - stdev):
        print (name[num.index(l)])
    
    

    