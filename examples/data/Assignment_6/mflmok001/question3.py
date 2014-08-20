"""MOkoena Mafologele
elections program
22/04/2014"""
print("Independent Electoral Commission\n--------------------------------")
parties=[]
votes=[]
#put values into parties and votes arrays
party_names=input("Enter the names of parties (terminated by DONE):\n")
while party_names!="done" and party_names!="DONE":
    votes.append(party_names)
    if party_names in parties:
        x=1
    else:
        parties.append(party_names)
    party_names=input()
parties.sort() #sort parties in alphabitical order
print("\nVote counts:")
formater="{party:<10} - {vote}"
#dispaly votes on screen
for i in parties:
    print(formater.format(party=i,vote=votes.count(i)))
    
