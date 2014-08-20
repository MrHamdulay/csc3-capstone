'''counting parties in a list
Frans Ledwaba
25 April 2014'''

print('Independent Electoral Commission')
print('--------------------------------')

#create list
parties = []

#create input for the list
x = input('Enter the names of parties (terminated by DONE):\n')
parties.append(x)

#set parameters
if x == 'DONE':
    print(' ')
    print('Vote counts:')
    
else:
    #craete empty string and loop input
    x = ''
    while x != 'DONE':
        x = input('')
        parties.append(x)
    
    #remove last loop and sort the list
    parties.remove('DONE')
    parties.sort()
    
    #vote counts
    print(' ')
    print('Vote counts:')
    #loop the counting process
    if parties.count(parties[0]) == len(parties):
            print(parties[0], ' '*(11 - len(parties[0])), '- ', len(parties), sep='')
    else:
        for i in range(len(parties)):
            if parties[i] != parties[i-1]:
                print(parties[i], ' '*(11 - len(parties[i])), '- ', parties.count(parties[i]), sep='')