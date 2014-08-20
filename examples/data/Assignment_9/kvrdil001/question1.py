#Dilan Koovarjee
#11 May 2014
#Std deviation program

file= input("Enter the marks filename:\n")
marks=[]
learner_marks= {}

filename= open(file, "r")
for line in filename:
    x= line.split(',')
    marks.append(x[1])
    learner_marks[x[1]]= x[0]
filename.close()

for i in marks:
    x[1]= x[1].replace("\n","")
    
sum_marks=0
for a in marks:
    sum_marks += eval(a)
print("The average is: {0:0.2f}".format(sum_marks/len(marks)))

y=0
for i in marks:
    y+= (eval(i)-(sum_marks/len(marks)))**2
std_deviation= (y/len(marks))**0.5
print("The std deviation is: {0:0.2f}".format(std_deviation))

cutoff= (sum_marks/len(marks))-std_deviation
print("List of students who need to see an advisor:")
for k in marks:
    if eval(k) < cutoff:
        print(learner_marks[k])