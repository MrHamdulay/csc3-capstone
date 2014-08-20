"""Assignment 9 Question 1
16 May 2014 Djavan Arrigone"""

import math
markd={}
markn=[]


FileName=input('Enter the marks filename:\n')
f = open(FileName, 'r') #Reading from input file.
lines = f.readlines() #Storing each line in list. 
f.close()

#At this point loop is used to remove new line characters from code (\n)
for i in range (len (lines)-1):
    lines[i] = lines[i][:-1]


#Here I am creating a dictionary of the list, the name of person being the key, and their mark the value
for i in range (len (lines)):
    entries = (lines[i].split (','))
    markd[entries[0]] = eval(entries[1])
for key in markd: #Appending marks to a new list
    markn.append(markd[key])

av = 0
dev = 0
for i in markn: # Determing the average mark
    av = av + i
av = av/len(markn)    

for i in markn: #Determining the standard deviation
    dev = dev + (i - av)**2
dev = math.sqrt(dev / len(markn) )


warning = av - dev   
#formatting answers to round of to two decimal places
av ="{:.2f}".format(av) 
dev ="{:.2f}".format(dev)


print('The average is:' , av)
print('The std deviation is:', dev)

#Determining if there are any students who need to see advisor. 
count = False
for i in markd.keys():
    if markd[i] < warning:
        count = True
if count == True:
    print("List of students who need to see an advisor:")

#prints out students who need to see student advisor.
for i in range(len(lines)):
    pos = lines[i].index(",")
    if eval(lines[i][pos+1:]) < warning:
        print(lines[i][:pos])          



