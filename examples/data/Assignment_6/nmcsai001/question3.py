"""Saijil Nemchund 
NMCSAI001
Question 3
Program that is used to tally votes """ 

print("Independent Electoral Commission")
print("--------------------------------")

votes=[] #creating an empty list
vote=input("Enter the names of parties (terminated by DONE):\n") #Asking user for input of vote types

while vote != "DONE":
    votes.append(vote)
    vote=input()
    
votes.sort()
found=[]
f="{0:<10}"
print()
print("Vote counts:")

for i in votes:
    if not i in found:
        v=votes.count(i)
        print(f.format(i),"-",v)
        found.append(i)
        



