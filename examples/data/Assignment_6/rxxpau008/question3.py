#Description: Totals up the number of votes for each specific party in an election
#Name: Paul Roux - RXXPAU008
#Date: 22 April 2014

votes = []
candidates = []

print('Independent Electoral Commission','\n--------------------------------',)
entry = input("Enter the names of parties (terminated by DONE):\n")
while entry!= "DONE": #Captures strings, that represent the political parties, until "DONE" is entered
    votes.append(entry)
    entry = input()

print()

for i in votes:#Identifies the political parties that have been voted for
    if i not in candidates: candidates.append(i)
candidates.sort()

print('Vote counts:')    
for i in candidates: #Prints the total votes for each party as well as the party name
    print(i+' '*(10-len(i)),'-',votes.count(i))
    
    

    
        