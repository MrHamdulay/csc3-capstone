"""Luvo Fokazi
22/04/2014"""
print("Independent Electoral Commission\n--------------------------------")
parties=[]
votes=[]
#populate votes and parties list
inpt=input("Enter the names of parties (terminated by DONE):\n")
while inpt!="done" and inpt!="DONE":
    votes.append(inpt)
    if inpt in parties:
        x=1
    else:
        parties.append(inpt)
    inpt=input()
parties.sort() #sort the parties alphabetically in the parties list
print("\nVote counts:")
formater="{party:<10} - {vote}"
#print the votes
for i in parties:
    print(formater.format(party=i,vote=votes.count(i)))
    