#Done by Guy Green
#Counting votes from given input
#Assignment 6

#Creating empty list
votes=[]

print("Independent Electoral Commission")
print("--------------------------------")

#Getting Input from user
vote=input("Enter the names of parties (terminated by DONE):\n")

#Adding the vote to the list until the user stops it
while vote!="DONE":
    votes.append(vote)
    vote=input("")

votes.sort()
#Creating a Temporary String so that the loop will work fot the first part of the loop.
random=""

print("")
print("Vote counts:")
#Checking if the next word is the same word
#If it is, it will be skipped until it finds a new word
for vote in votes:
    if vote!=random:
        #Changing the temporary string into the new word
        random=vote
        print(vote, (9-len(vote))*" ", "-", votes.count(vote))