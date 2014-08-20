#AMNTAS003  #Tashfia Amin #Due Date: 25 April 2014
#Question 3: Assignment 6   #Count the number of votes per party

#Create empty lists for the votes and parties
vote = []
party = []

#Enter data into the lists - both vote and party
print("Independent Electoral Commission")
print("--------------------------------")
votes=input("Enter the names of parties (terminated by DONE): \n")
while votes != "DONE":
    vote.append(votes)
    if vote.count(votes) == 1:    
        party.append(votes)
    votes = input("")
            
#Sort the list of parties and print the number of votes per party
party.sort()

print("\nVote counts:")
for i in party:
    print("{0:<10}".format(i), "-", vote.count(i))