#Shaylan Lalloo
#counts votes

print('Independent Electoral Commission')
print('--------------------------------')
print('Enter the names of parties (terminated by DONE):\n')

myword = ''
#current input
totwords = {}
#THe votes
myparties = []
#stores parties

while True:
    myword = input()
    #gets vote
    if myword == "DONE":
        #if sentinel found
        break
    if myword in totwords:
        totwords[myword] += 1
        #increases vote
    else:
        totwords[myword] = 1
        #sets vote and adds to list
        myparties.append(myword)

print('Vote counts:')

myparties.sort()
#sorts in alphabetical order

for i in myparties:
    print(i + ' ' * (10 - len(i)), '-', totwords[i])
#outputs appropriately
