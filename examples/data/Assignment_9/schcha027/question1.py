#CHARLES SCHLEICH
#SCHCHA027
filename= input("Enter the marks filename:\n")
f = open(filename, 'r')
    
line=f.readline()
array=[]
while line!="":
    name=(line.split(","))
    line=f.readline() 
    array.append(name)
    
average=0

for i in range(len(array)):
    average+=eval(array[i][1])
average=average/len(array)    
#calculates the average, then round formats it
print("The average is: ","%0.2f" % average,sep="" )

std=0
for j in range(len(array)):
    std=std+((eval(array[j][1])-average)**2)

std=std/len(array)
#formats the print to have 2 decimal places Always
std=std**0.5
print("The std deviation is: ","%0.2f" % std,sep="" )

#only prints if there are students in trouble
def header_Text():
    print("List of students who need to see an advisor:")
    return 1
stop=0
#checks for students in trouble
for k in range(len(array)):
    if (eval(array[k][1])+std)<average:
        if stop==0:
            stop=header_Text()
        print(array[k][0])
        
