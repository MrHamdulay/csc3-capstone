#SNGSOH004
#Assignment 6
#Question 1
#23rd April 2014

print("Independent Electoral Commission\n--------------------------------\nEnter the names of parties (terminated by DONE):") #Prompting input
dictionary = {} #creating an empty dictionary
parties=""

while parties!="DONE":
 parties = input()
 if parties!="DONE": #needed to be double checked since input was stored again after the first check, so possibility of "DONE" being entered.
  if parties not in dictionary:
   dictionary[parties] = 1 #adding the party to the dictionary if it was the first vote
  else:
   dictionary[parties] +=1 #increasing the vote if this party has been nominated before
   
print("\nVote counts:")
for parties in sorted(dictionary.keys()):
 print("{:<10} - {}".format(parties, dictionary[parties])) #printing the results in a sorted format