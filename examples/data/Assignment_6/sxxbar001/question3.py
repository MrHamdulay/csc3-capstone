#Assignment 6
#Question 3
#Barry Su
#23 April 2014
#Program to count the number of votes for each politcal party in an election

#print introduction line
print("Independent Electoral Commission")
print("--------------------------------")

#get the list of votes in terms of parties
voteparties=[]
votes = input("Enter the names of parties (terminated by DONE): \n")
while votes != "DONE":
    voteparties.append(votes)
    votes = input("")

#create a counter starting with 0
counter = {}
    
#count votes and add new parties as they are encountered
for party in voteparties:
    if not party in counter:
        counter[party] = 1
    else:
        counter[party] += 1

#print out vote counts for each party
print()
print("Vote counts:")
for party in sorted(counter):
    print ("{0:<11}{1}{2:2}".format(party, "-", counter[party]))