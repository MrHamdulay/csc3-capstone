#a program to count the number of votes for each political party in an election
#Jenny Luo
#23 April 2014

def main():
    print("Independent Electoral Commission")
    print("--------------------------------")
    #add parties into a list
    parties=[]
    party=input("Enter the names of parties (terminated by DONE):\n")
    while party != "DONE":
        parties.append(party)
        party=input()
    
    #a dictionary to count the votes
    partiesvotes={}
    for i in parties:
        if i not in partiesvotes:
            partiesvotes[i]=1
        else:
            partiesvotes[i]+=1
    
    #print the list of votes in left justified format
    print()
    print("Vote counts:")
    for i in sorted(partiesvotes):
        print(i.ljust(10), "-", partiesvotes[i])
        
        
    
        
main()

