#Assignment 6
#Question 3
#Annie Ho
#23/04/2014
#Political election

print("Independent Electoral Commission\n"+"--------------------------------")

parties=[]
numVotes = input("Enter the names of parties (terminated by DONE): \n")
while numVotes != "DONE":
    parties.append(numVotes)
    numVotes = input("")
    
counter = {}
    

for party in parties:
    if not party in counter:
        counter[party] = 1
    else:
        counter[party] += 1

print()
print("Vote counts:")
for party in sorted(counter):
    print ("{0:<11}{1}{2:2}".format(party,"-",counter[party]))