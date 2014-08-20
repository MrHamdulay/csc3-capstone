"""Dzunisani Nyoni
23 April 2014
A program used for to count the number of votes"""

def iec():
    x="Independent Electoral Commission"
    print(x)
    print("-"*len(x))
    
    partylist=[]   
    counter={}
    
    party=input("Enter the names of parties (terminated by DONE):\n")

    while party != "DONE":
            
            partylist.append(party)
            party=input()
    
    for party in partylist:
    
        if not party in counter:    #Adds list into a dictionary (counter)
            counter[party]=1
    
        else:
            counter[party]+=1
    
    parties=list(counter.keys())    #creates a list called parties using the keys in the dictionary counter
    
    print("\nVote counts:")
    for party in sorted(parties):
        print("{0:<10}".format(party),'-',counter[party]) #prints party, and the number of votes it got, using formatting
        
if __name__=='__main__':
    
    iec()