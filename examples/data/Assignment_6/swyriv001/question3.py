"""program that keeps a counter
 Rivoningo Seweya
 23 April 2014"""
#print top banner
print("Independent Electoral Commission")
print("--------------------------------")
#ask for parties
parties=[]
party=input("Enter the names of parties (terminated by DONE):\n")
#loop for party names
while party!="DONE":
    parties.append(party)
    party=input("")
print("")
#begin with an empty counter
votes={}
#add words into votes if its alredy there add to count
for i in parties:
    if not i in votes:
        votes[i]= 1
    else:
        votes[i] +=1
#print the results
print("Vote counts:")
for i in sorted(votes):
    print("{0:<10}".format(i),"-",votes[i])