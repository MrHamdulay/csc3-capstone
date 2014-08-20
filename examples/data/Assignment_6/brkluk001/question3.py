'''Program to count the number of votes for each political party in an election
23 April 2014
Luke Barker'''
from collections import Counter
list_votes =[]   #empty list
print("Independent Electoral Commission")
print('--------------------------------')
votes = input('Enter the names of parties (terminated by DONE): \n')
while not votes == 'DONE':    #keep adding input until DONE is entered
    list_votes.append(votes)  #adds vote to a list
    votes = input()
x = Counter(list_votes)     #counts number of occasions vote appear and adds to a dictionary
print()
print("Vote counts:")
for party,vote in sorted(x.items()):
    diff = 10 - len(party)      #to format
    print(str(party) + ' '* diff +' - ' + str(vote)) #printing party and vote count according to format



    
    