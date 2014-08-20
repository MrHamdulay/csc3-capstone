#Program to count the number of votes for each political party in an election vote
#knnsad001
#question 3

print("Independent Electoral Commission")
print("--------------------------------")

# this will get the list

partys = []
party = input('Enter the names of parties (terminated by DONE):\n')


while party != 'DONE':       #this will use 'DONE' as a sentinel
    partys.append(party)
    party = input('')

print('')

partys2 = []               

partys.sort()           #this aranges the list in alphabetical order

print('Vote counts:')
for party in partys:
    if not party in partys2:    #this will check if item is in partys2
        partys2.append(party)    # will move item to partys2
        print((party),(partys.count(party)), sep='')

