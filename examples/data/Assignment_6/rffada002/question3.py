parties = []
printed = []
print ("Independent Electoral Commission")
print ("--------------------------------")
print ("Enter the names of parties (terminated by DONE):")

while True:
     party = input("")
        
     if party == 'DONE':
          break
     
     parties.append(party)
     
parties.sort()

print ("")          
print ("Vote counts:")
for i in range(len(parties)):
     if parties[i] not in printed:
          count = parties.count(parties[i])
          print (parties[i].ljust(11)+("- "+str(count)))
          printed.append(parties[i])