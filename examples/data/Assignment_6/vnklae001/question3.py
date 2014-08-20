# Assignment 6 - Question 3
# A program that counts the number of votes a political party gets
# Written by: Laene van Niekerk
# VNKLAE001

list = []

print("Independent Electoral Commission")
print("--------------------------------")
votes = input("Enter the names of parties (terminated by DONE):\n")

while votes != "DONE":  # Adds the names entered by the user to the list
    list.append(votes)
    votes = input("")   # Allows the user to enter more names

list.sort()    # Arranges the names in alphabetical order
counts = []
repeats = []
    
for i in list:  # Used to count the number of votes for each party
    x = list.count(i)   # Counts the number of occurances of the name in the list
    if not i in repeats:    # Proceeds if it has not already counted the number of votes for this party
        counts.append(x)    
        repeats.append(i)   # Ensures that it does not count the same party twice
        
names = []
repeated_names = []
for i in list:  # Creates a list of the names so that they can be matched to the count
    if not i in repeated_names: # Adds the name if it does not already appear in names
        names.append(i)
        repeated_names.append(i)
    
print()
print("Vote counts:")

pos = 0
for i in names: # Prints the party name followed by the vote count, right justified 
    number_of_votes = counts[pos]
    number_of_votes = str(number_of_votes)
    number_of_votes = "- " + number_of_votes
    form = "{:<10}{:>4}".format(i, number_of_votes)
    print(form)
    pos = pos+1
    