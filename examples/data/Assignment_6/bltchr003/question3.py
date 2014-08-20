"""Voting system ; USer inputs names of parties, program then  counts up all the names and returns the amount of votes per party.
Chris Bolton"""

print ("Independent Electoral Commission")
print ("-"*32)
print ("Enter the names of parties (terminated by DONE):")

user_input = ""
parties = {}
sentinel = "DONE" #when suer inputs "DONE" the while loop will stop
while user_input != sentinel: #while loop to obtain data from user untill sentinal is entered
    user_input = input()
    if user_input not in parties:
        parties[user_input] = 1
    else:
        parties[user_input] = parties[user_input] + 1

del parties['DONE']

print ("\nVote counts:")

for i,j in sorted(parties.items()): #loop through and print out the counts of votes
    print (i.ljust(11) + "-", j )
