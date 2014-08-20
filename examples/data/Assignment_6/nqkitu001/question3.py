"""Assignment 6 question 3 
Itumeleng Nqoko
24 April 2014"""

#program to count votes
print("Independent Electoral Commission")
print("--------------------------------")
Dict={}
names=input("Enter the names of parties (terminated by DONE):\n")
while names!="DONE":
    if names not in Dict:
        Dict[names]=1
        names=input("")
    if names in Dict:
        Dict[names]+=1
        names=input("")
print("")
print("Vote counts:")
for names in sorted(Dict):  #sort party names into alphabetical order
    aligned="{0:<10}".format(names)
    print(aligned,"-",Dict[names])
