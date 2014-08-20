'''program to count number of votes in election per party
nasreen hoosain
27/04/14'''

#get list of votes
Votes = []
vote = ''
print('Independent Electoral Commission\n--------------------------------')
print('Enter the names of parties (terminated by DONE):')
while not vote == 'DONE':
    vote = input()
    Votes.append(vote)
Votes = Votes[:-1] #remove 'DONE' from list
#count votes in dictionary
count_votes = {}
for name in Votes:
    if not name in count_votes: #if party name is not in dictionary of votes, add it
        count_votes[name] = 0
    count_votes[name] += 1 #else add 1 to party's votes
#sort votes
names = count_votes.keys()
list_of_names = [] #put party names in a list so they can be sorted
for party in names:
    list_of_names.append(party)
list_of_names.sort()

#print votes in format
a = '{0:<10}{1:^3}{2:<}'
print()
print('Vote counts:')
for name in list_of_names:
    print(a.format(name, '-', count_votes[name]))