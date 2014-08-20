#Mbongeni Mazibuko
#MZBMBO002
#Assignment 6

def election():
    '''fuction to count the number of votes for each political party in an election'''
    print('''Independent Electoral Commission
--------------------------------
Enter the names of parties (terminated by DONE):''')
    lParty= []
    count= []
    party=' '
    
    while party!='DONE':
        #get political party names
        party= input()
        if party!='DONE':
            if party not in lParty:
                lParty.append(party)
                count.append(1)
            else:
                s=lParty.index(party)
                count[s]+=1
    print()
    print('Vote counts:')
    votes=[]
    for i in range(len(lParty)):
        votes.append('{0:<10}'.format(lParty[i])+' - '+str(count[i]))
    votes.sort()
    for i in range(len(votes)):
        print(votes[i])
        
if __name__=='__main__':
    election()