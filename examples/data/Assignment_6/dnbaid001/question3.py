#Assignment 6 - Question 3
#Vote counter
#Author: Aidan de Nobrega DNBAID001
#19/04/2014

print("Independent Electoral Commission")
print("--------------------------------")

parties = []

ballot = input("Enter the names of parties (terminated by DONE):\n")
while ballot != "DONE": #sentinel
    parties.append(ballot) #each vote adds party name to parties list
    ballot = input()

partiesdict = {} #to have key:value pairs

for party in parties:
    if not party in partiesdict: #adds key to dictionary from list
        partiesdict[party] = 0
    partiesdict[party] += 1 #increments value if key is in dictionary
    
print("\nVote counts:")

for key, value in sorted(partiesdict.items()): #sorted alphabetises keys
    diff = 10 - len(key) #alignment formatting
    print(str(key) + " "*diff + " - " + str(value)) #prints "key - value"
    

    
