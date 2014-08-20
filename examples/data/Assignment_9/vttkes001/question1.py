"""Check student Advisory
Keshin Vittee
11 May 2014"""
"""
Alan,35
Siobhan,23
Mmberengeni,38
"""
import math

fname = input("Enter the marks filename:\n")
snos = []
marks = []
f = open(fname,"r")
count = 0
total = 0
for line in f:
    comma = line.find(",")
    snos.append(line[0:comma])
    marks.append(eval(line[comma+1:comma+3]))
    total += marks[count]
    count += 1
f.close()
avg = total/count
print("The average is: {:.2f}".format(round(avg,2)))
sumsqrt = 0
for mark in marks:
    sumsqrt += (mark-avg)**2
sd = math.sqrt(sumsqrt/count)

print("The std deviation is: {:.2f}".format(round(sd,2)))

advisor = []
for i in range(len(marks)):
    if marks[i] < (avg-sd):
        advisor.append(snos[i])

if len(advisor) != 0:
    print("List of students who need to see an advisor:")
    for a in advisor:
        print(a)


    

    
         

