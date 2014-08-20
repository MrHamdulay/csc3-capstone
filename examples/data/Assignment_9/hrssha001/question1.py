#Shane Horsley
#Program to analye student marks read in from a file
#13 May
import math
openfile = input("Enter the marks filename:\n") #get file name
file = open(openfile, "r")
names=[]
marks=[]
namesfinal=[]
adv=[]
for line in file:
    for i in line.split(","):
        names.append(i) #get info from file and put it in to a list
file.close() #close file NB
for i in range(len(names)): #next couple loops seperate names and marks in to seperate lists. indexes correspond with each other
    if (i+1)%2==0:
        marks.append(int(names[i][:2]))
for i in range(len(names)):
    if i%2==0:
        namesfinal.append(names[i])
        
total=0
for i in marks: #work out the average
    total+=i
average=total/len(marks)

stdtotal=0
for i in marks:
    stdtotal+=(average-i)**2
dev=math.sqrt(stdtotal/len(marks)) #work out std dev

for i in range(len(marks)): #check f anyone needs to see an advisor
    if (average-dev)>marks[i]:
        adv.append(namesfinal[i])#list of names who need to see advisor
         

print("The average is:","{:.2f}".format((round(average,2))))
print("The std deviation is:","{:.2f}".format((round(dev,2))))
if len(adv) >0: #only print if there are people who need to see advisor
    print("List of students who need to see an advisor:")
    for i in adv:
        print(i)
        
  