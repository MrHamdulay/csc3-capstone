"""Program to determine standard deviation
Sbonelo Mntungwa
16 May 2014"""

#opening file
filename = input("Enter the marks filename:\n")
f = open(filename,'r')
file= f.readlines()
f.close()


#Removing new line
for i in range (len (file)-1):
    file[i] = file[i][:-1]
    
#Creating new list
listfile = []
for i in file:
    data= i.split(',')
    listfile.append(data)

#average value
avg = 0
n = 0
for n in range(len(listfile)):
    num = int(listfile[n][1])
    avg+=num
avg = avg/(n+1)
print("The average is:","%.2f"%(avg))

#standard deviation
sumsquared = 0
for i in range(len(listfile)):
    x = int(listfile[i][1])
    sumsquared+=(x-avg)**2  
import math
deviation = round(math.sqrt(sumsquared/(n+1)),2)
print("The std deviation is:","{0:0<4}".format(deviation))

#Students who need to see advisor
listno = []
for person in listfile:
    mark = int(person[1])
    if mark < avg-deviation:
        listno.append(person[0])
        print("List of students who need to see an advisor:")
        break
for i in listno:
    print(i)
