import math
user = input("Enter the marks filename:\n")
f = open(user,"r")
s = f.readlines()
s[-1]+=("\n")
f.close()
count1 = 0
count2 = 0
SD = 0
for i in range(len(s)):
    s[i]=s[i][:-1]
    cPosition=s[i].find(",")
    count2 +=(eval(s[i][cPosition+1:]))
    count1 +=1
average = count2/count1
print("The average is:","%0.2f"%average)
for i in range(len(s)):
    cPosition=s[i].find(",")
    SD+=((eval(s[i][cPosition+1:])-average)**2)
SD=(math.sqrt(SD/count1))
print("The std deviation is:","%0.2f"%SD)   
x = []
for i in range(len(s)):
    cPosition=s[i].find(",")
    if(eval(s[i][cPosition+1:])<(average-SD)):
        x.append(s[i][:cPosition])
if(len(x)>=1):
    print("List of students who need to see an advisor:")
    for i in range(len(x)):
        cPosition=s[i].find(",")
        print(x[i])