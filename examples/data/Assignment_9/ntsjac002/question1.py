'''A program that creates a file
Jacob ntesang
10 May 2014'''
'''marks = input("Enter the marks and a student no separated by a comma:\n")
f = open("test1.txt","w")
while marks != "":
    f.write(marks + "\n")    
    marks = input()
f.close()'''
from math import*

file = input("Enter the marks filename:\n")
f = open(file,"r")
line = f.readlines()
S = " "
for line_no in range(len(line)):
    for i in line[line_no]:
        S += i
W=S.split("\n")
Mean = 0
C = 0
Mark = ""
for j in W:
    if j == "":
        break
    else:
        j = j.split(",")
        #print(j)
        C += 1
        j = eval(j[-1])
        Mean += j
Average = Mean/C
print("The average is: {0:.2f}".format(Average))
#Calculate the standard deviation
s_d = 0
for i in W:
    if i == "":
        break  
    else:
        i = i.split(",")
        s_d += (eval(i[-1])-Average)**2
Standard_devi = sqrt(s_d/C)
print("The std deviation is: {0:.2f}".format(Standard_devi),end="")
for j in W:
    if j == "":
        print("")
    else:
        j = j.split(",")
        #print(j)
        C += 1
        h = eval(j[-1])
        if h < Average - Standard_devi:
            Mark += j[0]+" "
if Mark != "":
    print("List of students who need to see an advisor:")
    if "" in Mark:
        for i in Mark.split():
            print(i,end="\n")
    else:
        print(Mark)
    

    
    
    