"""A program to count the number of votes for each political party in an election
Simlindile Mahlaba
23 April 2014"""

def elections():
    
    print("\nIndependent Electoral Commission")
    print("--------------------------------")
    
    list_names=[]
    names = input("Enter the names of parties (terminated by DONE):\n")
   
    while names != "DONE" and names != "done":
        list_names.append(names)
        names = input()
    
    print()
    parties={}
    for x in list_names:
        parties[x]=parties.get(x,0) + 1
    party_names = list(parties.keys())
    party_names.sort()
    
    print("Vote counts:")
    for i in party_names:
        print(i, ' '*(10-len(i)-1), '-', parties[i])
        
elections()
    
        