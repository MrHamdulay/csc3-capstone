"""Assignment 6 Question 3 count number of votes for each party
joshua wort
19 april 2014"""

#print intro
print("Independent Electoral Commission")
print("--------------------------------")

#create list of parties
names=[]
name=input("Enter the names of parties (terminated by DONE):\n")
while name!="DONE":
    names.append(name)
    name=input("")

print()

print("Vote counts:")

counters={}

#get dictionary
for name in names:
    if not name in counters:
        counters[name]=0
    counters[name]+=1
    
#get vote counts and printing alphabetically
number_parties=len(counters)
while number_parties>0:
    name=min(counters)
    print(name," "*(10-len(name))," - ",counters[name],sep="")
    del(counters[name])
    number_parties-=1

    

    
    