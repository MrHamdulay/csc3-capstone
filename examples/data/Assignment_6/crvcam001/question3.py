# question3.py
# program to count number of votes for a party in a political election
# camilla craven
# 23 april 2014

print("Independent Electoral Commission")
print("--------------------------------")
party = input("Enter the names of parties (terminated by DONE):\n")

dictionary={}

while party != "DONE": # creating sentinel loop
    if party not in dictionary: 
        dictionary[party] = 1 # adds new party to dictionary
    else: dictionary[party] += 1 # if party in dictionary already, add 1 to key
    party = input()
    
List = []

# turns dictionary into list
for i in dictionary:
    List.append(i) 
    
List.sort() # sorts list alphabetically

print()
print("Vote counts:")

# prints names of parties alphabetically from list and prints related key from dictonary
for name in List: 
    print(name, " "*(12 - len(name) - len(str(dictionary[name]))), "- ", dictionary[name], sep = "")