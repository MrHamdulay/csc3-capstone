'''program to count number of votes
question3, assignment6
Simangaliso ,Mlangeni
MLNSIM014
24 April 2014'''

#create function to calculate number of votes for each party
def votesCount():
    votes = {}#creates empty dictionary
    NumV = 0
    Party_Names = []
    
    print("Independent Electoral Commission")
    print("--------------------------------")
    n = input("Enter the names of parties (terminated by DONE):\n")
    
    while n != 'DONE':#loop to iterate until user prints done
            if n not in Party_Names:
                Party_Names.append(n)
            if n in votes:
                votes[n] += 1
            else:
                votes[n] = 1
                NumV += 1
            n = input("")
        #prompts user to input names
        
    Party_Names.sort()#sorts name of political parties in ascending order
    print()
    print("Vote counts:")
    for i in Party_Names:
        print(i," "*(9-len(i)),"-",votes[i])#prints name of party with number of votes it received
    
votesCount()