# program to count the number of votes for each political party in an election.
# Mulisa Badugela
# 20 April 2014

def box():
    parties=[]   # empty list for parties
    print("Independent Electoral Commission\n--------------------------------")
    
    # user inputs party names and add to list
    n=input("Enter the names of parties (terminated by DONE):\n")
    parties.append(n)
    while n!= 'DONE':
        n=input() # user continues to input parties until input is 'DONE'
        parties.append(n)
    
    done=len(parties) # legnth of list    
    # remove 'DONE' from the list by deleting the last index of the list
    del parties[done-1]
    
    #create dictionay of party votes
    votes={}
    for i in parties:
        if i in votes: # if parties is already in dictinary add 1 to count for parties
            votes[i]+=1
        else: # set count for parties to 1
            votes[i]=1
    
    names=list(votes.keys()) # return the party names
    names.sort() # sort list of party names in alphabetical order
    print()
    print("Vote counts:")
    for i in names: # create column
        width=10-1    # field width and subtract the removed 'DONE'     
        length=len(i)  # length of name
        column=width-length #column size by subtracting field width by lenghth of each name
        a=column*' '
        b=votes[i]
        print(i,a,'-',b)
            
        
    
box()