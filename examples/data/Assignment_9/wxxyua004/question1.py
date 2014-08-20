"""programe to calculate whether if students need an advisor or not
yuan-yow wu
12th may 2014"""


import math

def markadd(mark): #add the marks with recursion
    """add marks"""
    if len(mark) == 1:
        return eval(mark[0])
    else:
        return eval(mark[0]) + markadd(mark[1:])

def isolatemark(mark): #isolates the number i.e. the marks
    """isolate the marks"""
    mark1 = ""
    for i in mark:
        if i.isnumeric():
            mark1 += i
    return mark1
        
def sdnumerator(marks): 
    """adds all the square of the mark minus average"""
    if len(marks) == 1:
        return (eval(marks[0])-average)**2
    else:
        return (eval(marks[0])-average)**2 + sdnumerator(marks[1:])
    
def isolatename(s):
    name = ""
    for i in s:
        if i.isalpha():
            name += i
    return name



filename = input("Enter the marks filename:\n")

f = open(filename,"r")

lines = f.readlines()

names = []
for i in range (len(lines)): #creating list for names:
    names.append(isolatename(lines[i]))

#lines.split(",")

for i in range (len(lines)): #finding average mark
    lines[i] = isolatemark(lines[i])

average = markadd(lines)/len(lines)
#print(average)


"""Need to calculate standard deviation"""

# Square root of (ans - average)
sd = (math.sqrt(sdnumerator(lines)/len(lines)))
#print(sd)

'''Find all people who are more than one deviation less than the average'''
studentadvisor = ""
for i in range (len(lines)):
        
    if eval(lines[i]) < average - sd:
        studentadvisor += names[i] + "\n" 

#print (sdnumerator(lines))

f.close()

print("The average is:", "{0:.2f}".format(average))
print("The std deviation is:", "{0:.2f}".format(sd))
if len(studentadvisor) > 0:
    print("List of students who need to see an advisor:\n",studentadvisor,sep="")