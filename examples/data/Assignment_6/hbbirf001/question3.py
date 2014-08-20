# Votes
# Irfan Habib
# 2014/04/24

def main():
    print('Independent Electoral Commission')
    print('--------------------------------')
    voted = []
    votes = []
    print('Enter the names of parties (terminated by DONE):')    
    i = input()
    while i != 'DONE':
        votes.append(i)#adds vote to entire vote list
        if i not in voted:
            voted.append(i)#adds vote to the candidate list 
        i = input()

    voted = sorted(voted)           
    print('\nVote counts:')
    for k in range(len(voted)):
        dif = 14-len(voted[k])
        print(voted[k]+('{0:>' + str(dif) +'}').format('- ' + str(votes.count(voted[k]))))

main()        
    