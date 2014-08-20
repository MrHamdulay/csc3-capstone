"""Assignment 6, Question 3: Counting votes in an election
Duncan Saffy
20 April 2014"""
import math
intro="Independent Electoral Commission"
print(intro,"\n","-"*len(intro), sep="")
parties=input("Enter the names of parties (terminated by DONE):\n")
x=[]

while parties != "DONE":
    
    x.append(parties)
    parties=input("")

y=[]
print()
x=sorted(x)

print("Vote counts:")
for i in range(len(x)):
    while x[i] not in y:

        no = x.count(x[i])
        print(x[i]," "*(9-len(x[i])), "-", no)
        y.append(x[i])