#Thembekile Dubazana
#dbzphi002
#Assignment 9:Q1

"""Read a file and find student whose mark is one standard deviation from the mean"""
import math

#The opening and closing of the file
#The inputs
filename=input("Enter the marks filename:\n")
file=open(filename,"r")
student=file.readlines()
file.close()

#Remove the \n at the end
for i in range(len(student)):
    if student[i][-1]=="\n":
        student[i]=student[i][:-1]

#Separate list through commas
student=",".join(student)
student=student.split(",")

#Calculate the average
count=len(student)//2
total=0
for j in range(1,len(student)+1,2):
    total+=int(student[j])
    
average=total/count

#Calculate the standard deviation
stddev=0
for k in range(1,len(student)+1,2):
    stddev+=(int(student[k])-average)**2

stddev=math.sqrt(stddev/count)

#The results
print("The average is: ","{0:.2f}".format(average),sep="")
print("The std deviation is: ","{0:.2f}".format(stddev),sep="")
advisor=[]

for l in range(1,len(student)+1,2):
    if int(student[l]) < average-stddev:
        advisor.append(student[l-1])

if len(advisor)!=0:
    print("List of students who need to see an advisor:")
    for m in range(len(advisor)):
        print(advisor[m])
        


        


