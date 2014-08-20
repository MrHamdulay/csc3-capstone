#Thea Sitek, STKTHE002
#18.05.2014
#Count votes


print('Independent Electoral Commission')
print('--------------------------------')

#store inputed votes
array = []
vote = input('Enter the names of parties (terminated by DONE): \n')
while vote != 'DONE':
    array.append(vote)
    vote = input()   

array.sort()
length = len(array)

#if any votes
if array:
    
    votes = [array[0]] #start value is first vote, alfabetic
    amount = [1] #first vote
    count = 0
    
    for i in range(1 , len(array)):
        #if vote not equal to one already counted, store name
        if array[i] != array[i-1]:
            votes.append(array[i])
            amount.append(1)
            count += 1    
        #if not give existing name one extra vote
        elif array[i] == array[i-1]:
            amount[count] += 1    
            
    
print('\nVote counts:')
    
if array:
    #format and print
    space = 8
    for i in range(len(votes)):
        space -= len(votes[i]) - 1 
        print(votes[i], ' '*space, '-', amount[i])
        space = 8

