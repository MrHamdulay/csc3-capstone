#Ikhlaas Pohplonker
#16 May 2014
#a program to analyse student marks read in from a file and determine which students need to see a student advisor
import math
filename=input("Enter the marks filename:\n")
f=open(filename,"r")#opens a file to read from
lines=f.readlines()#reads the lines as a list of strings
names=[]#empty list
n=0
x=0
for i in range(len(lines)):
    line=lines[i].split(",")#splits each line by a comma
    n=n+eval(line[1])#calculates the total marks
average=round(n/len(lines),2)#calculates the average
for i in range(len(lines)):
    line=lines[i].split(",")#splites each line by a comma
    x=x+((eval(line[1]))-average)**2
standard=round(math.sqrt(x/len(lines)),2)#calculate standard deviation
for i in range(len(lines)):
    line=lines[i].split(",")#splits each line by a comma
    if average-eval(line[1])>standard:#determines who must go see the student advisor
        names.append(line[0])
z=str(round((n%len(lines))/len(lines),2)).split(".")
q=str(round((math.sqrt(x)%math.sqrt(len(lines)))/math.sqrt(len(lines)),2)).split(".")
print("The average is:", str(int(average))+".{0:0<2}".format(z[1]))
print("The std deviation is:", str(int(standard))+".{0:0<2}".format(q[1]))
if len(names)>0:
    print("List of students who need to see an advisor:")
    for z in names:
        print(z)#print the names that must see the student advisor
f.close()#closes the file



 
    