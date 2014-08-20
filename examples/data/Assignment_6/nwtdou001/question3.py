'''NWTDOU001
question3.py
25 april 2014'''

# print a nice header
print ('Independent Electoral Commission')
print ('--------------------------------')

# set up an empty dictionary of parties - since we don't know the names yet
parties = {}

# prompt to enter party names, getting the first one so long
party_name = input('Enter the names of parties (terminated by DONE):\n')

# for each party name, either increment the dictionary value if the key is
# already in the dictionary, or create a new field with the party name, value 1
while party_name!='DONE':
    if party_name in parties:
        parties[party_name] += 1
    else: parties[party_name] = 1
    # get the next party name
    party_name = input('')

print('')

# print the results of the election alphabetically: each key with each value
print('Vote counts:')
for key in sorted(parties.keys()):
    print(key.ljust(10),' - ',parties[key],sep='')