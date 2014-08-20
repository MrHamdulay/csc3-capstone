""" Counts the num,ber of votes for each political party
Divan Jagers
25 April 2014"""

print("Independent Electoral Commission")
print("--------------------------------")
list_parties=[] # creates a list of list_parties
partyname=input("Enter the names of parties (terminated by DONE):\n") #prompts the user to input the name of the party
list_parties.append(partyname)
while partyname!="DONE":
    partyname=input("")
    list_parties.append(partyname)

sep_parties=[]        # create a separate list with each party only appearing once
for party in list_parties:
    if party not in sep_parties:
        sep_parties.append(party)

print()
print("Vote counts:")
list_parties.sort()
sep_parties.sort()

# prints the respective party and their votes  
for j in range(1,len(sep_parties)):
    votes=list_parties.count(sep_parties[j])
    print("{0:10}".format(sep_parties[j]),"-",votes)

      
    
          



    
    