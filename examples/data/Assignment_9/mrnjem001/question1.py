filename=input("Enter the marks filename:\n")

file=open(filename, "r")
test = file.readlines()
file.close()

test=("").join(test)
lines=test.split("\n")
persons=[]
for line in lines:
    persons.append(line.split(","))
    
sum=0
stdcore=0
for i in range(0,len(persons)-1):
    sum+=eval(persons[i][1])
mean=sum/(len(persons)-1)

for i in range(0,len(persons)-1):
    stdcore+=(eval(persons[i][1])-mean)**2
stddev=(stdcore/(len(persons)-1))**(0.5)
 
advisory=""
for i in range(0,len(persons)-1): 
    if (eval(persons[i][1])+stddev)<mean:
        advisory+=persons[i][0]+"\n"

print("The average is:", "{0:.2f}".format(mean))
print("The std deviation is:", "{0:.2f}".format(stddev))
if advisory!="":
    print("List of students who need to see an advisor:\n", advisory, sep="")