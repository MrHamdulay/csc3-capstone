'''Program which counts the number of votes for each political party during an election
HAMZA EBRAHIM
25/04/14.'''

# Assignment 6 - Question 3 

# print head banner 

print('Independent Electoral Commission')
print('--------------------------------')

# prompt user for names of parties

parties = input("Enter the names of parties (terminated by DONE):\n")

# initialize list (list_of_parties) & dictionary (counters)  

list_of_parties = []

counters = {}

# sentinel loop which appends names of parties to list

while parties != 'DONE':
    list_of_parties.append(parties)
    parties = input('')
    
# creates counter for party names

for party in list_of_parties:
    if not party in counters:
        counters[party] = 0
    counters[party] += 1    
        
# prints output
sorted(counters.keys())
print()
print('Vote counts:')   
for party in counters:
    
    print(party.ljust(10), "-", counters[party])

    

# program ends    