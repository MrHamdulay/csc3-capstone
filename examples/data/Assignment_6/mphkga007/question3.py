""" program that counts the number if votes of a party
kenneth mphele
231/04/2014"""
def party():
    print("Independent Electoral Commission")
    print("--------------------------------")
    
#input party names
    party_name=input("Enter the names of parties (terminated by DONE):\n")
    if party_name!="DONE":
        party_names=[]
        while not party_name=="DONE":
            party_names.append(party_name)
            party_name=input("")
        print()
        
    #sort out the parties names
        party_names.sort()
        print("Vote counts:")
       #counts the number of votes for each party 
        vote_party=[]
        for i in party_names:
            if i in vote_party:continue
            vote_party.append(i)
            count=party_names.count(i)
            results="{name:<10s} - {count:<10}"
            print(results.format(name=i, count=count))
    
    else: print("\nVote counts:")       
        
        
party()