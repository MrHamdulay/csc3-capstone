import math
studentmarks={}
student=[]
amount=0
name=input("Enter the marks filename:\n")
file=open(name,"r")
for i in  (file):
    pos=i.split(",")
    student.append(pos[0])
    amount+=1
    if(pos[1][-1]=="\n"): 
        studentmarks[pos[0]]=pos[1][:len(pos[1])-1]
    else:
        studentmarks[pos[0]]=pos[1]
file.close()
total=0
temp=[]
for a in studentmarks:
    total+=eval(studentmarks[a])
    temp.append(eval(studentmarks[a]))
average=total/amount
variance = map(lambda x: (x - average)**2, temp)
std=round(math.sqrt(sum(variance)/amount),2)
problem=average-std
print("The average is: {0:.2f}".format(average))
print("The std deviation is: {0:.2f}".format(std))
for b in studentmarks :
    if(eval(studentmarks[b])<problem):
        print("List of students who need to see an advisor:")
        break
for b in range (len(student)):
    if(eval(studentmarks[student[b]])<problem):
        print(student[b])