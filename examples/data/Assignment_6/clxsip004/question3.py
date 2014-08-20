#Siphesihle Cele
#26 April 2014
#program that simulates a voting system.

#the usage of 2 array's is requireed.
#append all votes onto the first list
#adopt 1 element of each component onto the second array
#then calculate how many times it appeared in the first array.
#simple enough lol, JOKES.
print("Independent Electoral Commission")
print("--------------------------------")
parties =[]
print("Enter the names of parties (terminated by DONE):\n")
poll="0"
i=1
while (poll!="DONE"):
    poll=input()
    if(poll=="DONE"):
        break
    else:
        parties.append(poll)
filter = []
for i in parties:
    if i in filter:
        i = 0
    else:
        filter.append(i)
filter.sort()        
print("Vote counts:")
for i in filter:
   
    print("%-10s - %s" % (i, parties.count(i)))

