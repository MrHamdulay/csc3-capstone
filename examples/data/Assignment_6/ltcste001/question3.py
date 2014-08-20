#stephanie latchmanan
#Assignment 6(Vote Counting)
#20 April 2014

#create an empty list
votes= []
parties = []

#append votes into list
names = input("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):\n")
while names != 'DONE':
        votes.append(names)
        if votes.count(names) == 1:     #create list of parties
                parties.append(names)
        names = input("")

#sort parties in list
parties.sort()

#print names of parties with votes
print("\nVote counts:")
for i in parties:
        print("{0:<10}".format(i), "-", votes.count(i))