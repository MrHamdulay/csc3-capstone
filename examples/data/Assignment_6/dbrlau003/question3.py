#Lauren de Bruyn
#Program to count the number of votes for each political party in an election
#22 April 2014

#print heading
print("Independent Electoral Commission")
print("--------------------------------")

#get list of parties from user
listparties=[]
aparty=input("Enter the names of parties (terminated by DONE): \n")
while aparty != "DONE":
    listparties.append(aparty)
    aparty=input("")
    
#calculate how many votes each party receives
listparties.sort()
counter = {}
print("\nVote counts:")
for party in listparties:
    if not party in counter:
        counter[party] = 1
    else:
        counter[party] += 1
        
#print out list of each party and corresponding number of votes
for party in sorted(counter):
    a='{0:<10}'.format(party)    
    print (a,"-", counter[party])