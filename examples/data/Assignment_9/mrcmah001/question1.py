import math

list1 = []

file1 = input('Enter the marks filename:\n')

file2 = open(file1, 'r')

file3 = file2.readlines ()

for line in file3:
    
    name, marks1 = line.split(',')
    m = marks1
    list1.append(int(m))


add1=0
for j in list1:
    add1+=j
ave=add1/len(list1)
z=0
for x in range(len(list1)):
    z=z+((list1[x]-ave)**2)
w = z/len(list1)
    
deviate = math.sqrt(w)
    

file2.close ()

print('The average is: {0:.2f}'.format(ave))

print('The std deviation is: {0:.2f}'.format(deviate))


for i in range(len(list1)):
    
    if float(int(list1[i]))<(ave-deviate):
        print('List of students who need to see an advisor:')
        break


for s in range(len(list1)):
        
    if float(int(list1[s]))<(ave-deviate):    
        a,b=file3[s].split(",")
        print(a)

