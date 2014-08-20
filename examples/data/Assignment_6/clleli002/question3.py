"""count the number of votes
Elizabeth Cilliers
20/04/2014"""

"""count number of votes
Elizabeth Cilliers
20/04/2014"""

def display():
    print("Independent Electoral Commission")
    print("--------------------------------")
    
def listOfparty():
    display()
    
    #create list/array
    list_of_parties=[]
    
    # get a list of names
    party = input ("Enter the names of parties (terminated by DONE):\n")
    # as long as user has not typed done
    while party != "DONE":
        # store name in array
        list_of_parties.append (party)
        # get next name
        party = input ("") 
    print()
    
    
      
    counter={}
    for party in list_of_parties:
        if party in counter:
            counter[party] +=1 #add 1 for every occurance of particular party
        else:
            counter[party] = 1
    
    print("Vote counts:")
    for party in sorted(counter.keys()): #sort parties in alphabetical order
        space=" "*(10-len(party))
        print(party,space," - ",counter[party],sep="")
        
listOfparty()