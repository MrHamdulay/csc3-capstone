"""Counting the votes for the 
rama raphalalani
23-04-2014"""

#Getting input of strings and also creating an empty list
print("Independent Electoral Commission\n--------------------------------")
parties = []
Names = input("Enter the names of parties (terminated by DONE):\n")

#creating a sentinel DONE. then using the sort function and creating an empty dictionary
while Names != "DONE": 
    parties.append(Names)    
    Names=input("") #prompting for inputs(prompt not seen)
parties.sort()
votes={} 

#runs to see if this vote has already been cast, if not it adds to the votees roll.
for Name in parties: 
    if Name not in votes: 
        votes[Name] = 1
    else:
        votes[Name] = votes[Name] + 1 
print("\nVote counts:")

#the funtion to print in the format required.
for Name in sorted(votes):
    print("{0:10}".format(Name),"-",votes[Name])
    
