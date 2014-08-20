#question3
import random 
print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")
party=input().upper()
parties=[]
while party!="DONE":
    count=0
    
    parties.append(party.lower())
    party=input("")

r=[]
for i in parties:
    if i in r:
        continue
    r.append(i)
r=sorted(r)
print()
print("Vote counts:")
    
for j in r:
    print(j.ljust(10), "-", parties.count(j),)
