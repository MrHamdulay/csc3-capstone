"""Dumisani Ngwenza
NGWDUM005
21/04/2014
Assignment 6 Question 3"""

#prints heading/title
print ("Independent Electoral Commission")
print ("--------------------------------")

#requiring input of votes
votes = input ("Enter the names of parties (terminated by DONE):\n")
list_of_votes= []

done = 'DONE'


#requiring input of votes until 'DONE' is typed
while votes != done:
    if votes == done: break
    list_of_votes.append(votes)
    votes = input("")


list_of_votes.sort() 
count_votes = {}


#print (x)
#counts number of occurences
for vote in list_of_votes:
    if not vote in count_votes:
        count_votes[vote] = 0 #creates a new entry with value equal to 0 when it isn't present
    count_votes[vote] += 1


#displays each vote and it's respective number of votes
print ()
print ("Vote counts:")
new_votes_list = []
for item in list_of_votes:
    if not item in new_votes_list:
        new_votes_list.append(item)
        
for item in new_votes_list:
    print (item, ' '*(10-len(item)-1), '-', count_votes[item])
#for i in count_votes:
    #print (i, ' '*(10-len(i)-1), "-", count_votes[i])
   