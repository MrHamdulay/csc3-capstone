#Ali Goldstein
#program to analyse student marks from a file and determine which students need to see a student advisor
#15 May 2014

import math
#open the file and read the contents of it
filename = input("Enter the marks filename:\n")
f =open(filename,"r")
text=f.readlines()
f.close()

#creating variables
ave=0.00
count=0.00
stand=0

#going through text and spliting by the comma into name and mark
for i in range(len(text)):
    s=text[i].split(",")
    name=s[0]
    mark=s[1]
    #each time going around the loop adding the mark to a counter
    ave=ave+eval(mark)
    count=count+1
ave= ave/count
ave=("%.2f"%ave)
print("The average is:", (ave))

for i in range(len(text)):
    s=text[i].split(",")
    mark=s[1]
    #each time in the loop it words out the standard deviation with the average and adds it to the counter 'stand'
    stand =stand+((eval(mark)-eval(ave))**2)
stand= round(math.sqrt(stand/count),2)
stand=("%.2f"%stand)
print("The std deviation is:", stand)

#creating a list for the people who need to see a student advisor
adv=[]
for i in range(len(text)):
    name,mark = text[i].split(",")
    #this is the condition to see a student advisor
    #if condition equals true, their name is added to the list
    if eval(mark)<(float(ave)-float(stand)):
        adv.append(name)
if len(adv)!=0:
    #printing the list
    print("List of students who need to see an advisor:")
    for i in range(len(adv)):
        print(adv[i])