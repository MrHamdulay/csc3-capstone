"""Program to find the standard deviation an average of marks
   Rivoningo Seweya
   12 April 2014"""
import math
filename=input("Enter the marks filename:\n")
#create a function
file=open(filename,"r")
#read the lines in the file and create a list
lines=file.readlines()
#close open file
file.close
#iterate through the list and remove the \n
for i in range(len(lines)):
        if lines[i][-1:]=="\n":
                lines[i]=lines[i][:-1]
        lines[i]=lines[i].split(",")
#create two counters
x=0
y=0
for k in range(len(lines)):
        x+=int(lines[k][1])
        y+=1
avg=x/y
#calculating standard deviation
stndrd=0
num=0
vari=0
#loop through loop to add the numbers
for i in range(len(lines)):
        num+=1
        vari=int(lines[i][1])
        stndrd+=((vari-avg)**2)
#calculating standard deviation
devi=math.sqrt(stndrd/num)           
print("The average is: "+"{0:.2f}".format(avg))
print("The std deviation is: "+"{0:.2f}".format(devi))
#finding the person who should see the student advisor
advisor=[]
for j in range(len(lines)):
        if int(lines[j][1])< avg:
                advisor.append(lines[j][0])
if advisor!=[]:
        print("List of students who need to see an advisor:")
        for j in advisor:
                print(j)