#CSC1015F 
#ASSIGNMENT 6
#QUESTION 3
#WHTBAS001
#23/04/2014

import collections
print("Independent Electoral Commission")
print("--------------------------------")
parties = list()
party = input('Enter the names of parties (terminated by DONE):\n') # initalize before the loop
while party != 'DONE':           # while NOT DONE
    parties.append(party) #adds the new string
    party = input('')  #resets loop
    
print()
print("Vote counts:")

def final(x):
    c = collections.Counter() #create new counter subdictionary
    for word in x:
        c[word]+=1 #word in list added to dictionary as key then +1 to value
    y = sorted(c) #sorts the dictionary into a list 
    for i in y:
        r = "{0:<11}".format(i) + "- " + str(c[i]) #generates string of output
        print(r)
        
final(parties)
