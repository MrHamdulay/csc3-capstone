# a program to choose students that should see student advisor
# Xola Bilose
#13-05-2014

file=input("Enter the marks filename:\n")
f=open(file,"r")
# opening file for reading by lines
lines=f.readlines()
# initializing critical values
marklist=[]
namelist=[]
num=0
sum_marks=0
standard_dev=0
student=0

for line in lines:
  
    elements=line.split(",")
# adding marks to a separate list  
    mark=eval(elements[1])
    marklist.append(mark)
    names=elements[0]
    namelist.append(names)
    
# calculating sum and standard deviation

    sum_marks+=mark
    num+=1
average=sum_marks/num
for i in range(len(lines)):
    standard_dev+=(marklist[i]-average)**2

       
standard_dev=(standard_dev/num)**0.5
print("The average is:","%.2f"%average)
print("The std deviation is:","%.2f"%standard_dev)

for j in range(len(lines)):
    if marklist[j]<(average-standard_dev):
        print("List of students who need to see an advisor:")
        break

for j in range(len(lines)):
    if marklist[j]<(average-standard_dev):
        print(namelist[j])
