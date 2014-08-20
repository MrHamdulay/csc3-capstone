'''a program to count the number of votes for each party in an election.
Sfiso Mthembu MTHSFI005
22 April 2014'''
print('Independent Electoral Commission')
print('--------------------------------')

#create list of parties
party_list = []

#ask for votes
parties = input('Enter the names of parties (terminated by DONE):\n')

#add the votes on a list
while parties != "DONE":
    party_list.append(parties)
    parties=input('')
#sort the list 
party_list.sort()

#import the counting function
from collections import Counter

#convert list to dictionary
Dic = Counter(party_list)

#create new list of parties where each party will appear once
real =[]

#take keys in dictionary and append them to new list
for i in Dic:
    real.append(i)

#sort the new list
real.sort()

print()
print('Vote counts:')

#print the desired output
for i in real:
    print('{0:<10}'.format(i),"-",party_list.count(i))