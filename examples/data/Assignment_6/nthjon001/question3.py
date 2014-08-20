"""counts number of votes for each political party in an election and prints out the names of the parties and the number of votes each received
Jonathan Nathan
20 April 2014"""

# prints header
print('Independent Electoral Commission')
print('--------------------------------')

# creates an empty list, in which party names will be added
party_names_list = []

# gets party names from user
party_names_input = input("Enter the names of parties (terminated by DONE):\n")

# adds party names entered by user to list until the sentinel, 'DONE', is entered
while party_names_input != 'DONE':
    party_names_list.append(party_names_input)
    party_names_input = input('')
    
# prints next header    
print()
print("Vote counts:")

# creates a new list, which is an alphabetically sorted version of party_names_list
party_names_sorted_list = sorted(party_names_list)

# creates a variable i, which will terminate the following while loop, when it is no longer within the range of the list
i = 0
while i <= len(party_names_sorted_list)-1:
    # prints the vote counts, with formatting
    print('{0:11}'.format(party_names_sorted_list[i]), '- ', party_names_sorted_list.count(party_names_sorted_list[i]), sep='')
    # changes i to print the next unique party
    i += party_names_sorted_list.count(party_names_sorted_list[i])