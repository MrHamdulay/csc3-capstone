#GPXSHI001
#Ass9
#Q1

import math

filename = input("Enter the marks filename:\n")

infile = open(filename, "r")


lstx = []

lines= infile.read()
lst = lines.split()
for line in lst:
    comma = line.find(",")
    number = line[comma + 1:]
    lstx.append(int(number))

total = 0  

for i in range(len(lstx)):
    total = total + (lstx[i])


avg = (round(total/len(lstx), 2))

y = "{0:.2f}".format(avg)

print("The average is:",y)

term_total = 0 

for i in range(len(lstx)):
    terms = (int(lstx[i]) - avg)**2
    term_total = term_total + terms

sd = round(math.sqrt(term_total/len(lstx)), 2)

x = "{0:.2f}".format(sd)

print("The std deviation is:",x)

lsty = []

for i in range(len(lstx)):
    if int(lstx[i]) < (avg - sd):
        lsty.append(lst[i])
 
lstr = [] 
    
for i in range(len(lsty)):
    lstz = lsty[i].split(",")
    lstr.append(lstz[0])

if len(lstr) >= 1:
    print("List of students who need to see an advisor:")

for i in range(len(lstr)):
    print(lstr[i])
    

infile.close()