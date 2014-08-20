"""Assignment 6 Question 3
21 April 2014
Jordan Kadish, Political Vote Counts"""


def VoteCount():
    VoteCounts={}
    print('Independent Electoral Commission\n--------------------------------')
    Votes=input('Enter the names of parties (terminated by DONE):\n')
    while Votes!='DONE':
        if Votes in VoteCounts.keys(): #Check to see if the vote has already been used before
            VoteCounts[Votes]+=1 #If it has been voted for before, add 1 to the value of that key
        else:
            VoteCounts[Votes]=1 #Else, create the new key
        Votes=input('')
    print()
    print('Vote counts:')
    for key in sorted(list(VoteCounts.keys())): #Sort the dictionary into alphabetical order of keys
        print(key.ljust(10),'-',VoteCounts[key])
if __name__=='__main__':
    VoteCount()