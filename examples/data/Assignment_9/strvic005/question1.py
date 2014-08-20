"""program to anaylse student marks read in from a file and determine which students need to see an advisor
vicky stark
13 may 2014"""

import math

filename=input("Enter the marks filename:\n")

#accessing file that the input enters
f=open(filename, "r")
lines=f.readlines()
f.close()

#create a list with the marks
list_=[]

for i in lines:
    x=i.split(",")
    list_.append(eval(x[1]))
    
#calc the average
total=0
for j in list_:
    total+=j

average=(total/ len(list_))
rounded_ave="{:.2f}".format(average)
print("The average is:", rounded_ave )

#calc the stnd dev
y=0
for k in list_:
    y+=(k-average)**2

stnd_dev= round((math.sqrt(y/len(list_))), 2)
formatted_stnd_dev="{:.2f}".format(stnd_dev)
print("The std deviation is:", formatted_stnd_dev)


#check who needs to see the advisor
list_to_advise=[]
for h in list_:
    if h< (average-stnd_dev):
        list_to_advise.append(h)


#make another list with the names and corresponding marks
list_2=[]
for c in lines:
    z=c.split(",")
    list_2.append(z)

list_to_advise2=[]
for g in list_to_advise:
    string=str(g)
     
     #match marks to names
    for d in range(len(list_2)):
        if string == list_2[d][1][:-1]:
            m=list_2[d][0]
            if m not in list_to_advise2:
                list_to_advise2.append(m)


        
if list_to_advise2 != []:
    print("List of students who need to see an advisor:")        
    for b in list_to_advise2:
        print(b)

      

        
    

