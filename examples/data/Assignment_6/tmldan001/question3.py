'''Program to count the number of votes for each political party in an election
Daniel M. Tamale
2014-04-22'''

print ('Independent Electoral Commission')
print ('--------------------------------')

'''To get the different polls and store as a list'''
poll=input('Enter the names of parties (terminated by DONE):\n')
polls=[]
while True:
    if poll=='DONE':
        break
    polls.append(poll)
    poll=input('')
print('')

'''To get the vote counts per respective party'''
print('Vote counts:')  
from collections import Counter
votes=Counter(polls)
new=[]
for i in votes:
   new.append(i)

new.sort()     
"""To print vote counts per respective party"""
for i in new:
   print('{0:<10}'.format(i),'-',votes[i])