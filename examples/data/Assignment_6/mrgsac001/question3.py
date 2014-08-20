"""Candidate Parties
Sachin Murugan
25/04/2014"""

print("Independent Electoral Commission")
print("--------------------------------")

candidates=[]
#enter the names 
name=input("Enter the names of parties (terminated by DONE):\n")
while name!="DONE":
    candidates.append(name)
    name=input("")

count = {}
    
#Count th3e number of votes
for word in candidates:
    if not word in count:
        count[word] = 1
    else:
        count[word] += 1
others = list()
for j in candidates:
   
    if j not in others:
        others.append(j)

others.sort()

print('\nVote counts:')


for i in others:
    z = 11-len(i)
    print ( i,' '*z+'- ',count[i],sep='')
    
    