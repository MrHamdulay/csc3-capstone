# Program to count the number of votes for each political party in an election.

# Names of parties need to be entered (terminated by the word DONE) and votes per party should be kept track of. 

# No pre-determined party list so the list must be created as party names are encountered. 

# Names of the parties and their vote counts to be printed out, with the parties listed in sorted order (the default order of the sorted function).


# Collecting Data
print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")


party = []
votes = ""


while votes.lower() != "done":
    votes = input()
    if votes.lower != "done":
        party.append(votes)

del party[len(party)-1]


# Printing out the output of counted votes per party
print("Vote counts:")

count = 0
for i in range (len(party)):
     
        if i == 0:
            number = 1
            count = i + 1
            
        elif sorted(party)[i-1] != sorted(party)[i]:
            number = 1
            count = i + 1
            
        else: 
            continue
                
        while count < len(party):
            
            if sorted(party)[count-1] != sorted(party)[count]:
                break
            
            elif sorted(party)[count-1] == sorted(party)[count]:
                number += 1
                count += 1
                
        print(sorted(party)[i]," " * (9-len(sorted(party)[i])), "-", number)
                