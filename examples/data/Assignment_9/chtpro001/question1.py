
f=input("Enter the marks filename:\n")
f=open(f,"r")
lines=f.readlines()
Line=[]
marks=[]
names=[]
summ=0 
for line in lines:
    Line.append(line[:-1].split(","))
for i in range(len(Line)):
    marks.append(Line[i][1])
    names.append(Line[i][0])
    summ+=eval(marks[i])
   
mu=(summ/len(marks))
sse=0
for i in range (len(marks)):
    sse+=((eval(marks[i])-mu)**2)
    
sigma=((sse/len(marks))**0.5)
mu="{0:.2f}".format(mu)
sigma="{0:.2f}".format(sigma)

print("The average is:",mu)
print("The std deviation is:",sigma)
s=0
for i in range (len(Line)):
    if eval(Line[i][1]) < (eval(mu)-eval(sigma)):
        s+=1
    else:
        s+=0
        
if s!=0:
    print("List of students who need to see an advisor:")
    for i in range (len(Line)):
        if eval(Line[i][1]) < (eval(mu)-eval(sigma)):  
            print(Line[i][0])
    
    
    

