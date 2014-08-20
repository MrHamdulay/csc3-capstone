#Author: NLXALE001
#Date:23 April 2014
#Assignment 6

print ("Independent Electoral Commission\n--------------------------------")
name = ""
names = []
print ("Enter the names of parties (terminated by DONE):\n")
while name != "DONE":
    name = input("")
    names.append(name)
vote = []
extravote = []
counter=0
del names[-1]
#add votes for each candidate into lists
for i in names:
    if i not in vote:
        vote.append(i)

    else:
        extravote.append(i)

#print votes
newvote = vote
newvote.sort()
print ("Vote counts:")
space = 0
for j in newvote:
    count = 1
    for m in range (0, len(extravote)):
        if extravote[m] == j:
            count += 1
        m += 1
    space = 9 - len(j)
    print(j, " "*space, "-", count)

