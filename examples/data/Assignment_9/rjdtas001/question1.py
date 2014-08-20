import math
test = input("Enter the marks filename:\n")
infile = open(test, "r")
another = []

markstotal = 0
lines=0
advisor = []
nyoom = 0

for line in infile:
    
    person = line.split(",")
    markstotal += eval(person[1])
    another.append(eval(person[1]))
    lines += 1

mean = markstotal/lines

infile.close()
infile = open(test ,"r") 

for x in another :
    
    nyoom = nyoom + ((x - mean)**2)

deviation = math.sqrt(nyoom/lines)

for x in infile:
    person = x.split(",")
    if eval(person[1]) < (mean-deviation):
        advisor.append(person[0])

mean = "%.2f"%round(mean,2)
deviation = "%.2f"%round(deviation,2)
print ("The average is:", mean)
print ("The std deviation is:", deviation )

if not advisor:
    print("")
else:
    print("List of students who need to see an advisor:")
    for i in advisor:
        print(i)
