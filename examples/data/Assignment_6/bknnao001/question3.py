#BKNNAO001
#NAME OF PARTIES
print ("Independent Electoral Commission")
print ("-"*32)
print ("Enter the names of parties (terminated by DONE):")
v= {}
name = ""
while name != "DONE":
   name = input ("")
   if name != "DONE":
      if not name in v:
         v[name] = 1
      else:
         v[name] = v[name] + 1

print ("\nVote counts:")
for name in sorted(v.keys()):
   print ("{:<10} - {}".format (name, v[name]))
  