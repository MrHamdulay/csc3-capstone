"""kureshlen moodley
15 may 2014
mdlkur001
program to determine if students need to see the student advisor"""
import math

input_filename=input("Enter the marks filename:\n")
f=open(input_filename,"r")
x=f.readlines()
f.close()
Dictionary={}
l=[]
for i in (x):
    splitvariable=i.split(",")
    l.append(splitvariable[0])
    if  "\n" in i:
        Dictionary[splitvariable[0]]=eval(splitvariable[1][0:len(splitvariable[1])-1])
    else:
        Dictionary[splitvariable[0]]=eval(splitvariable[1])
variants=0        
average=sum(Dictionary.values())/len(x)
for j in Dictionary:
    w=(Dictionary[j]-average)**2
    variants+=w
variants=variants/len(x)
standard_deviation=math.sqrt(variants)

student_advisor=(average-standard_deviation)

print("The average is: {0:.2f}".format(average))
print("The std deviation is: {0:.2f}".format(standard_deviation))


for k in Dictionary:
    if student_advisor>Dictionary[k]:
        print("List of students who need to see an advisor:")
        break
        
for q in range(len(l)):
    if student_advisor>Dictionary[l[q]]:
        print(l[q])
        