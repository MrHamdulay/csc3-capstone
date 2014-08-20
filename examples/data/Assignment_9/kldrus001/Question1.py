#Rushil Kalidas
#11 May 2014
#Standard Deviation Program

f= input("Enter the marks filename:\n")
marks=[]
student_marks= {}

filename = open(f,"r")
for line in filename:
    x = line.split(",")
    marks.append(x[1])
    student_marks[x[1]]= x[0]
filename.close()

for i in marks:
    x[1]= x[1].replace("\n","")
    
sum_marks=0
for a in marks:
    sum_marks += eval(a)
print("The average is: {0:0.2f}".format(sum_marks/len(marks)))

z=0 
for i in marks: 
    z+= (eval(i)-(sum_marks/len(marks)))**2
std_deviation = (z/len(marks))**0.5
print("The standard deviation is: {0:0.2f}".format(std_deviation))

cutoff= (sum_marks/len(marks))-std_deviation
print("List of students who need to see an advisor:")
for k in marks:
    if eval(k) < cutoff:
        print(student_marks[k])
