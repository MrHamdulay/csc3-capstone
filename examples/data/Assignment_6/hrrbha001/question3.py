print ("Independent Electoral Commission")
print ("--------------------------------")
print ("Enter the names of parties (terminated by DONE):")

votes = {}
name = ""
while name != 'DONE':
   name = input ("")
   if name != 'DONE':
      if not name in votes:
         votes[name] = 1
      else:
         votes[name] = votes[name] + 1

print ("\nVote counts:")
for name in sorted(votes.keys()):
   print ("{:<10} - {}".format (name, votes[name]))
  