print ("Independent Electoral Commission")
print ("-"*32)
print ("Enter the names of parties (terminated by DONE):")

inp = ""
parties = {}
sentinel = "DONE"
while inp != sentinel:
    inp = input()
    if inp not in parties:
        parties[inp] = 1
    else:
        parties[inp] = parties[inp] + 1

del parties['DONE']

print ("\nVote counts:")

for i,j in sorted(parties.items()):
    print (i.ljust(11) + "-", j )

