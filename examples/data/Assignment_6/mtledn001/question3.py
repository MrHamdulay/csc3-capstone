'''the voting class
Ednecia MATLAPENG
19 April 2014'''

#Get the headline
print('Independent Electoral Commission\n--------------------------------')
#Getting the votes
vote = input('Enter the names of parties (terminated by DONE):\n')
voteList=[]
while vote.lower() != 'done':
    voteList.append(vote)
    vote= input('')
#Now all the votes are in, we must disinguish  using count
#Then load them into an array so that we can sort them
output = []
tracker=''
for i in (voteList):
    if tracker.find(' '+i+' ')<0:
        votes = voteList.count(i)
        #print(len(i))
        space =' '*(11-len(i))
        output.append(i+space+'- '+str(votes))
        tracker+= ' '+ i+' '
output.sort()
print('\nVote counts:')
for h in output:
    print(h)


    
    
    
