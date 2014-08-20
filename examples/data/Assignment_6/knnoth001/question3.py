''' Program that counts the number of votes for each political party in an election 
Othniel KONAN
KNNOTH001
2014/04/19'''

#CREATION OF VARIABLES
vote_list=[]
list_participants=[]
nbrPerParticipants=[]
array=[]

#PRINT THE TOP
print('Independent Electoral Commission\n--------------------------------')

#ASK THE USER TO ENTER THE VOTES
lt = input('Enter the names of parties (terminated by DONE):\n')
while lt != 'DONE':
    vote_list.append(lt)                       
    if not lt in list_participants:            #Append to list_participants if the word was not already enterd
        list_participants.append(lt)
    lt = input()

list_participants.sort()   #Sort the list_participants
#COUNT THE NUMBER OF VOTE PER PARTICIPANT
for i in range(len(list_participants)):                    
    nbrPerParticipants.append(vote_list.count(list_participants[i]))

#CREATE A 2D ARRAY OF list_participants by 14
for i in range(len(list_participants)):
    array.append([' ']*14)

#ENTER THE VOTE IN THE ARRAY    
for i in range(len(list_participants)):
    for j in range(len(list_participants[i])):
        array[i][j]=list_participants[i][j]
    array[i][11] = '-'
    array[i][13] = nbrPerParticipants[i]

print('\nVote counts:')

#PRINT THE VOTE
for x in range(len(list_participants)):
    for y in range(14):
        print(array[x][y],end='')
    print()

