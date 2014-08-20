'''
Prashanth Sridharan
SRDPRA001
Assignment 06
Question 03
'''
print ("Independent Electoral Commission")
print ("--------------------------------")
print ("Enter the names of parties (terminated by DONE):")

votes = {}
n = "" #inititalising the name of the party variable
while n != 'DONE':  #loop stage
   n = input ("")
   if n != 'DONE':  #if the person does not quit
      if not n in votes:
         votes[n] = 1
      else:
         votes[n] = votes[n] + 1

print ("\nVote counts:")
for n in sorted(votes.keys()):
   print ("{:<10} - {}".format (n, votes[n]))
  